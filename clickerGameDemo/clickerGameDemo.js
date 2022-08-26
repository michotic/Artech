let mainButton; // Variable for main clicker/button object
let cookieCount = 0; // Cookies start at 0
let cps = 0; // Cookies/second
let priceMultiplier = 1.07; // Multiplier for store prices after buying an upgrade

// Load game assets
function preload() {
  cookieImage = loadImage("cookieButton.png");
  buyButton = loadImage("buyButton.png") 
  storeBackground = loadImage("storeBackground.png"); 
  font = loadFont("font.ttf"); 
  goldCookie = loadImage("goldCookie.png"); // new ----------------------------------------
  saveImage = loadImage("save.png");
  loadImg = loadImage("load.png");
}

// Runs once at game start
function setup() {
  textFont(font); 
  imageMode(CENTER);
  createCanvas(800, 600);
  mainButton = new Clicker(width / 4.6, 300, 150);
  store = new Store(createVector(width / 2, 50)); 
  
  goldCookies = [];
  ellipseMode(CENTER);
  
  saveButton = new createVector(40, height - 60);
  rectMode(CENTER);
}

function draw() {
  background(0, 176, 255);
  mainButton.render();
  fill(255);
  stroke(0);
  strokeWeight(4);
  textSize(40);
  push();
  textAlign(CENTER);
  text(float(cookieCount).toFixed(1) + " Cookies", mainButton.position.x, 50); //add str 
  text(float(cps).toFixed(1) + "/second", mainButton.position.x, 100); //add str
  pop();
  cookieCount += cps / 60;
  store.render(); 
  
  // new
  fill(255);
  let milkHeight = constrain((cps / 1000), 0, height / 2);
  rect(width / 4 - 25,height - (milkHeight / 2), width / 2 - 50, milkHeight);
  
  //new-----------------------
  if (random(1) < 0.001) {
    goldCookies.push(new GoldCookie(createVector(random(width / 2), random(height))));
  }
  for (let i=0; i < goldCookies.length; i++) {
    goldCookies[i].render(); 
    if (goldCookies[i].duration < 0.01) {
      goldCookies.splice(i, 1);
    }
  }
  
  let saveSize = 50
  fill(0);
  rect(saveButton.x, saveButton.y, saveSize * 1.2, saveSize * 1.2);
  image(saveImage, saveButton.x, saveButton.y, saveSize, saveSize);
  rect(saveButton.x + saveSize + 25, saveButton.y, saveSize * 1.2, saveSize * 1.2);
  image(loadImg, saveButton.x + saveSize + 25, saveButton.y, saveSize, saveSize);
}

function mousePressed() {
  if (dist(mouseX, mouseY, mainButton.position.x, mainButton.position.y) < mainButton.radius / 2) {
    cookieCount = mainButton.addCookies(cookieCount, mainButton.perClick);
  }
  
  for (let i = 0; i < store.buttons.length; i++) {
    let bX = store.buttons[i].x;
    let bY = store.buttons[i].y;
    if (dist(mouseX, mouseY, bX, bY) < store.buttonSize / 2) {
      if (cookieCount >= store.items[i]["price"]) {
        cps += store.items[i]["cps"];
        cookieCount -= store.items[i]["price"];
        store.items[i]["price"] *= priceMultiplier;
        store.items[i]["price"] = int(store.items[i]["price"]);
      }
    }
  }
  
  // new --------------------------------------------
  for (let i = 0; i < goldCookies.length; i++) {
    let goldenCookie = goldCookies[i];
    if (dist(mouseX, mouseY, goldenCookie.position.x, goldenCookie.position.y) < goldenCookie.radius / 2) {
      cookieCount += goldCookies[i].reward;
      goldenCookie.duration=0;
    }
  }
  
  if (dist(mouseX, mouseY, saveButton.x, saveButton.y) < 30) {
    let saveInfo = [int(cookieCount), int(cps)];
    for (let i=0; i < store.items.length; i++) {
      saveInfo.push(store.items[i]["price"]);
    }
    print(saveInfo);
    saveStrings(saveInfo, 'save.txt');
  }
  if (dist(mouseX, mouseY, saveButton.x + 75, saveButton.y) < 30) {
    loadStrings('save.txt', loadGame);
  }
}

function loadGame(data) {
  cookieCount = float(data[0]);
  cps = float(data[1]);
  for (let i = 0; i < store.items.length; i++) {
    store.items[i]["price"] = float(data[i+2]);
    print(store.items[i]["name"]);
  }
}
