var data;

const scale = (x, min, max) => (((max-min)*(x - 0) / (1 - 0)) + min);

function preload() {
  let cache = localStorage['data'];
   
  console.log(cache)

  if (!cache) {
    data = loadJSON('data');
    localStorage['data'] = Object.values(data);
  } else {
    data = cache;
  }
}

function setup() {
  console.log(data.length)
  createCanvas(550, 550);
  data = Object.values(data);
  console.log(data);
  window.data = data;
  strokeWeight(1);
  stroke(255);
  noFill();
  background(255);
  for (let i = 0; i < data.length; ++i) {
    let speed = data[i].speed / 60;
    stroke(
      scale(speed, 30, 240), // R
      scale((1-speed), 30, 90), // G
      scale((1-speed), 0, 150), // B
    );

    ellipse(data[i].x/60, data[i].y/60, 1, 1);
  }
}

function draw() {
}
