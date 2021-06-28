import Player from './Modules/Player.js';
import Projectile from './Modules/Projectile.js';
import DrawFuncs from './Modules/Draw.js';
import Enemy from './Modules/Enemy.js';

// HTML Document Setup
const canvas = document.querySelector('canvas');
canvas.width = innerWidth;
canvas.height = innerHeight;

const ctx = canvas.getContext('2d');

console.log(canvas);
console.log(ctx);

const drawer = new DrawFuncs();

// Game Objs
const player = new Player(canvas.width * 0.5, canvas.height * 0.5, 30, 'blue');
const projectiles = [];
const enemies = [];

function SpawnEnemies() {
    setInterval(() => {
	const enemy = new Enemy(
	    100,
	    100,
	    30, 
	    'green',
	    {
		x: 1,
		y: 1
	    }
	);

	enemies.push(enemy);
	console.log(enemies);
    }, 4000);
}

function Loop() {
    requestAnimationFrame(Loop);
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    SpawnEnemies();

    drawer.DrawCircle(player, ctx);
    projectiles.forEach(projectile => {	
	projectile.Update();
	drawer.DrawCircle(projectile, ctx);
    })

    enemies.forEach(enemy => {
	enemy.Update();
	drawer.DrawCircle(enemy, ctx);
    })
};

addEventListener('click', (event) => {
    const angle = Math.atan2(event.clientY - player.y, event.clientX - player.x);

    const xvel = Math.cos(angle) * 2;
    const yvel = Math.sin(angle) * 2;

    const projectile = new Projectile(
	player.x,
	player.y,
	2,
	'red',
	{
	    x: xvel,
	    y: yvel
	}
    ); 
    projectiles.push(projectile);
});

Loop();

// Handle Event
// Update
// Draw
