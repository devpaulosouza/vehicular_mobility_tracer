var data;
var momentum = 0;
var finished = false;
var looop = true;
var drawCircle = false;

const s2Color = (x, min, max) => (((max-min)*(x - 0) / (1 - 0)) + min);

function preload() {
  let cache = localStorage['data'];
  if (!cache) {
    data = loadJSON('data/momentum');
  } else {
    data = cache;
  }
}

function setup() {
  document.getElementById('nyan').remove();
  console.log(data.length);
  createCanvas(600, 600);
  data = Object.values(data);
  //console.log(data);
  window.data = data;
  frameRate(20);
}

function draw() {
  background(255);
  textSize(32);
  fill(0,0,0);
  text(''+data[momentum].length,10,30);
  for (let i = 0; i < data[momentum].length; ++i) {
    let speed = (data[momentum][i].s < 60) ? data[momentum][i].s / 60 : 1;
    strokeWeight(1);
    stroke(
      s2Color(speed, 30, 240), // R
      s2Color((1-speed), 30, 90), // G
      s2Color((1-speed), 0, 150), // B
    );
    point(data[momentum][i].x/45, data[momentum][i].y/45);
  }  
  momentum++;
  if (drawCircle) {
    stroke(50,55,100);
    fill(50,55,100, 50);
    ellipse(mouseX, mouseY, 40, 40);
  }

  if (data.length === momentum) {
    noLoop();
    finished = true;
  }
  if (!looop) {
    noLoop();
  }
}


function mouseClicked() {
  console.log('foi');
  if (!finished) {
    looop = !looop;
    drawCircle = !looop;

    if (looop) {
      loop();
    }
  }
  
}
