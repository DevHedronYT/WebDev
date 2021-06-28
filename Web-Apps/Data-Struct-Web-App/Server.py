from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from flask import Flask, request, jsonify
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy

from LinkedList import LinkedList
from HashTable import HashTable
from BST import BST
from CustomQueue import Queue
from Stack import Stack

import random


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0


@event.listens_for(Engine, "connect") 
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

db = SQLAlchemy(app)
now = datetime.now()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost", cascade = "all, delete")


class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
   
@app.route("/user", methods = ["POST"])
def create_user():
    data = request.get_json()
    new_user = User(
        name = data["name"],
        email = data["email"],
        address = data["address"],
        phone = data["phone"],
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message" : "User Created"}), 200

@app.route("/user/descending_id", methods = ["GET"])
def get_all_users_descending():
    users = User.query.all()
    allUsers = LinkedList()

    for user in users:
        allUsers.InsertBeginning({
            "id" : user.id,
            "name" : user.name, 
            "email" : user.email,
            "address" : user.address,
            "phone" : user.phone
        }) 

    return jsonify(allUsers.ToArray()), 200

@app.route("/user/ascending_id", methods = ["GET"])
def get_all_users_ascending():
    users = User.query.all()
    allUsers = LinkedList()

    for user in users:
        allUsers.InsertEnd({
            "id" : user.id,
            "name" : user.name, 
            "email" : user.email,
            "address" : user.address,
            "phone" : user.phone
        }) 

    return jsonify(allUsers.ToArray()), 200

@app.route("/user/<user_id>", methods = ["GET"])
def get_one_user(user_id):
    users = User.query.all()
    allUsers = LinkedList()

    for user in users:
        allUsers.InsertBeginning({
            "id" : user.id,
            "name" : user.name, 
            "email" : user.email,
            "address" : user.address,
            "phone" : user.phone
        }) 

    user = allUsers.GetUserByID(user_id)
    return jsonify(user), 200


@app.route("/user/<user_id>", methods = ["DELETE"])
def delete_user(user_id):
    user = User.query.filter_by(id = user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({}), 200

@app.route("/blog_post/<user_id>", methods = ["POST"])
def create_blog_post(user_id):
    data = request.get_json()
    user = User.query.filter_by(id = user_id).first()

    if not user:
        return jsonify({"message" : "user does not exist!"}), 400

    ht = HashTable(10)
    ht.AddKeyVal("title", data["title"])
    ht.AddKeyVal("body", data["body"])
    ht.AddKeyVal("date", now)
    ht.AddKeyVal("user_id", user_id)

    newBPost = BlogPost(
        title = ht.GetVal("title"),
        body = ht.GetVal("body"),
        date = ht.GetVal("date"),
        user_id = ht.GetVal("user_id")
    )

    return jsonify({"message" : "post created"}),  200

@app.route("/blog_post/<blog_post_id>", methods = ["GET"])
def get_one_blog_post(blog_post_id):
    blogPosts = BlogPost.query.all()
    random.shuffle(blogPosts)
    
    bst = BST()

    for post in blogPosts:
        bst.Insert({
            "id"    : post.id,
            "title" : post.title,
            "body"  : post.body,
            "user"  : post.user_id
        })

    post = bst.Search(blog_post_id)

    if not post:
        return jsonify({"message" : "post not found"})

    return jsonify(post) 

@app.route("/blog_post/numeric_body", methods = ["GET"])
def get_numeric_post_bodies():
    blogPosts = BlogPost.query.all()
    
    q = Queue()

    for post in blogPosts:
        q.Enqueue(post)

    returnList = []

    for _ in range(len(blogPosts)):
        post = q.Dequeue()
        numericBody = 0
        for char in post.data.body:
            numericBody += ord(char)

        post.data.body = numericBody

        returnList.append({
            "id"      : post.data.id,
            "title"   : post.data.title,
            "body"    : post.data.body,
            "user_id" : post.data.user_id 
        })

    return jsonify(returnList)

@app.route("/blog_post/delete_last_10", methods = ["DELETE"])
def delete_last_10():
    blogPosts = BlogPost.query.all()

    s = Stack()

    for post in blogPosts:
        s.Push(post)

    for _ in range(10):
        postToDel = s.Pop()
        db.session.delete(postToDel.data)
        db.session.commit()

    return jsonify({"message" : "successfully deleted the last 10 blog posts"}), 200

if __name__ == "__main__":
    app.run(debug = True)




