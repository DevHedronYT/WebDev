class Enemy {
    constructor(x, y, radius, color, vel) {
	this.x        = x;
	this.y        = y;
	this.radius   = radius;
	this.color    = color;
	this.velocity = vel; 
    }

    Update() {
	this.x += this.velocity.x;
	this.y += this.velocity.y;
    }
};

export default Enemy;
