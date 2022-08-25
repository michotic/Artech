let mainButton;
let cookieCount = 0;
let cookieImage;
let cps = 0; // new -------------------------------------------------------------
let priceMultiplier = 1.2; // new -----------------------------------------------------------

function preload() {
  cookieImage = loadImage("cookieButton.png");
  
  buyButton = loadImage("buyButton.png") // new------------------------------------------
  storeBackground = loadImage("storeBackground.png"); // new----------------------------------
  font = loadFont("font.ttf"); // new
  
  goldCookie = loadImage("goldCookie.png"); // new ----------------------------------------
}

function setup() {
  textFont(font); // new ---------------------------------------------------------------
  
  imageMode(CENTER);
  createCanvas(800, 600);
  mainButton = new Clicker(170, 300, 150);
  store = new Store(createVector(width / 2, 50)); // add param-----------------------
  goldenCookie = new GoldCookie(createVector(-100, -100));
}

function draw() {
  background(0, 176, 255);
  mainButton.render();
  fill(255);
  textSize(40);
  text(cookieCount.toFixed(1) + " Cookies", 125, 50); // new --------------------------------
  
  cookieCount += cps / 60; // new----------------------------------------------------
  text(cps.toFixed(1) + "/second", 125, 100); // new---------------------------------------------------
  store.render(); // new-----------------------------------------------------
  
  // new -------------------------------------------------------------
  if (random(1) < 0.001) {
    goldenCookie.position.x = random(width / 2);
    goldenCookie.position.y = random(height);
    goldenCookie.remaining = goldenCookie.duration;
    goldenCookie.reward = random(100, 50000);
  }
  goldenCookie.render();
}

function mousePressed() {
  if (dist(mouseX, mouseY, mainButton.position.x, mainButton.position.y) < mainButton.radius) {
    cookieCount = mainButton.addCookies(cookieCount, mainButton.perClick);
  }
  
  // new ------------------------------------------------------------------------------------------------------------
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
  
  if (dist(mouseX, mouseY, goldenCookie.position.x, goldenCookie.position.y) < goldenCookie.radius / 2) {
    cookieCount += goldenCookie.reward;
    goldenCookie.position.x = -100;
  }
}
