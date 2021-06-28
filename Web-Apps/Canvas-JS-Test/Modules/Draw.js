
class DrawFuncs {
    constructor() {
	
    }

    DrawCircle(circle, ctx) {
	ctx.beginPath();
	ctx.arc(circle.x, circle.y, circle.radius, 0, Math.PI * 2, false);
	ctx.fillStyle = circle.color;
	ctx.fill();
    }
}

export default DrawFuncs;
