from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from credentials import email, password, discord_pass
import time
import os



class Automate:

    def google_login():
        global driver

        driver = webdriver.Chrome()
        driver.get('https://www.google.com')

        sign_in_button = driver.find_element_by_xpath('//*[@id="gb_70"]')
        sign_in_button.click()


        enter_email = driver.find_element_by_xpath('//*[@id="identifierId"]')
        enter_email.send_keys(email)

        submit_email = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
        submit_email.click()

        driver.implicitly_wait(2)

        enter_password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        enter_password.send_keys(password)

        submit_password = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
        submit_password.click()

        driver.implicitly_wait(3)

        search_bar = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search_bar.send_keys('Hello, World!')

    def discord_login():
        driver = webdriver.Chrome()
        driver.get('https://discord.com/channels/728968069678104597/729327896740495500')

        driver.implicitly_wait(5)

        enter_email = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input')
        enter_email.click()
        enter_email.send_keys(email)

        enter_password = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
        enter_password.click()
        enter_password.send_keys(discord_pass)

        submit = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
        submit.click()

        driver.implicitly_wait(5)

        while True:
            text = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div/main/form/div/div/div/div/textarea')

    def open_google_apps(link, new):

        if new == 'y':
            open_doc = input('Do you want to open a new document?')

        elif new == 'n':
            pass

        Automate.google_login()

        google_apps = driver.find_element_by_xpath('//*[@id="gbwa"]/div/a')
        google_apps.click()

        driver.get(link)

        new_doc = driver.find_element_by_xpath('//*[@id=":1g"]/div[1]/img')

        if open_doc == 'yes' or open_doc == 'Yes' or  open_doc == 'y' or  open_doc == 'Y':
            new_doc.click()

        elif open_doc == 'no' or open_doc == 'No' or open_doc == 'n' or open_doc == 'N':
            pass


    def google_app(do_input, name_lower, name_upper, link, type):

        if do_input == 'open ' + name_lower or do == 'Open ' + name_upper:

            Automate.open_google_apps(link, type)


use = input('Entertainment or School Work? (Enter e or E for Entertainment otherwise SW or sw for school work) ')
time.sleep(0.15)
os.system('clear')

if use == "e" or use == "E":
    do = input('What do you want to open/do, Search, Sign In, Open Gmail, Open Drive (Google Drive), Open Drawings (Google Drawings), Open Sites (Google Sites), Open Collections (Google Collections), Open Images (Google Images), Open Arts and Culture (Google Arts and Culture), Open Earth (Google Earth), Open Maps (Google Maps), Open YouTube, Open Reddit, Open Discord or Open Account Settings:  ')

elif use == "SW" or use == "sw":
    do = input('What do you want to open/do, Search, Sign In, Open Gmail, Open Drive (Google Drive), Open Docs (Google Docs), Open Sheets (Google Sheets), Open Slides (Google Slides), Open Drawings (Google Drawings), Open Scholar (Google Scholar), Open Classroom (Google Classroom), Open Meets (Google Meets), Open Calendar (Google Calendar), Open Translate (Google Translate), Open Books (Google Books), Open Keep (Google Keep), Open Jamboard (Google Jamboard), Open Collections (Google Collections), Open Images (Google Images) or Open Account Settings:  ')

if do == "search" or do == "Search":

    search = input('What do you want to search? ')

    driver = webdriver.Chrome()
    driver.get('https://www.google.com')

    search_bar = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    search_bar.send_keys(search)

    go_search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
    go_search.click()


elif do == "sign in" or do == "Sign in":
    Automate.google_login()

elif do == "open discord" or do == "Open Discord":
    Automate.discord_login()


Automate.google_app(do, "drive", "Drive", "https://drive.google.com/?authuser=0", "n")
Automate.google_app(do, "docs", "Docs", "https://docs.google.com/document/?usp=docs_alc&authuser=0", "y")
Automate.google_app(do, "sheets", "Sheets", "https://docs.google.com/spreadsheets/u/0/", "y")
Automate.google_app(do, "slides", "Slides", "https://docs.google.com/presentation/?usp=slides_alc&authuser=0", "y")
Automate.google_app(do, "drawings", "Drawings", "https://docs.google.com/drawings/", "n")
Automate.google_app(do, "sites", "Sites", "https://sites.google.com/new", "n")
Automate.google_app(do, "scholar", "Scholar", "https://scholar.google.com/", "n")
Automate.google_app(do, "classroom", "Classroom", "https://classroom.google.com/u/0/h", "n")
Automate.google_app(do, "meets", "Meets", "https://meet.google.com/", "n")
Automate.google_app(do, "calendar", "Calendar", "https://calendar.google.com/calendar/r", "n")
Automate.google_app(do, "translate", "Translate", "https://translate.google.co.za/?hl=en&tab=wT&authuser=0", "n")
Automate.google_app(do, "books", "Books", "https://books.google.com/", "n")
Automate.google_app(do, "keep", "Keep", "https://keep.google.com/u/0/", "n")
Automate.google_app(do, "jamboard", "Jamboard", "https://jamboard.google.com/", "n")
Automate.google_app(do, "arts and culture", "Arts And Culture", "https://artsandculture.google.com/", "n")
Automate.google_app(do, "collections", "Collections", "https://www.google.co.za/save?authuser=0", "n")
Automate.google_app(do, "images", "Images", "https://images.google.com/", "n")
Automate.google_app(do, "earth", "Earth", "https://earth.google.com/web/@0,0,0a,22251752.77375655d,35y,0h,0t,0r", "n")
Automate.google_app(do, "maps", "Maps", "https://www.google.com/maps/@-39.773756,3.2370054,3z", "n")
Automate.google_app(do, "youtube", "Youtube", "https://www.youtube.com/", "n")
Automate.google_app(do, "reddit", "Reddit", "https://reddit.com", "n")
Automate.google_app(do, "account settings", "Account Settings", "https://myaccount.google.com/", "n")
Automate.google_app(do, "gmail", "Gmail", "https://mail.google.com/mail/u/0/?tab=wm#inbox", "n")
