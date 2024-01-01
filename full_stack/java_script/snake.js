function keyDownEventHandler() {

    if (event.keyCode == 40)
        direction = "down";
    if (event.keyCode == 38)
        direction = "up";
    if (event.keyCode == 37)
        direction = "left";
    if (event.keyCode == 39)
        direction = "right";
    if (event.keyCode == 32)
        direction = "stop";

}


function TimeEventHandler() {
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, 400, 400);

    x1 = tail[tail.length - 1].x;
    y1 = tail[tail.length - 1].y;

    if (direction == "right") {
        for (i = tail.length - 1; i > 0; i--) {

            tail[i].x = tail[i - 1].x
            tail[i].y = tail[i - 1].y
        }
        tail[0].x += steps;
    }

    else if (direction == "left") {
        for (i = tail.length - 1; i > 0; i--) {

            tail[i].x = tail[i - 1].x
            tail[i].y = tail[i - 1].y
        }
        tail[0].x -= steps;
    }
    else if (direction == "up") {
        for (i = tail.length - 1; i > 0; i--) {

            tail[i].x = tail[i - 1].x
            tail[i].y = tail[i - 1].y
        }
        tail[0].y -= steps;
    }
    else if (direction == "down") {
        for (i = tail.length - 1; i > 0; i--) {

            tail[i].x = tail[i - 1].x
            tail[i].y = tail[i - 1].y
        }
        tail[0].y += steps;
    }


    if (tail[0].x == applex && tail[0].y == appley) {
        applex = Math.floor(Math.random() * 19) * 20;
        appley = Math.floor(Math.random() * 19) * 20;
        tail.push({ x: x1, y: y1 })
    }

    ctx.fillStyle = "black";
    ctx.fillRect(applex, appley, width, highet);
    console.log(tail.length);



    for (i = 0; i < tail.length; i++) {

        ctx.fillStyle = "green";
        ctx.fillRect(tail[i].x, tail[i].y, width, highet);
    }



}


ctx = document.getElementById('myCanvas').getContext('2d');


var x = 40;
var y = 80;


var x1, y1;
// for creating a tail
var tail = new Array({ x: 40, y: 80 }, { x: 20, y: 80 })

//define number of pixels of progres
steps = 10;

//define wideth and highet of the ctx
var width = 20;
var highet = 20;
//previosly define the apple destination
var applex = 60;
var appley = 120;
var count = 0;

var direction = "right"

var random;

var clear = [x, y]






document.onkeydown = keyDownEventHandler;

setInterval(TimeEventHandler, 150);