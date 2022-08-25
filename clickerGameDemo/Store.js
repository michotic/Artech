class Store {
  constructor(position) { // param new
    this.items = [];
    this.numItems = 0;
    
    this.position = position; // new
    this.buttonSize = 50; // new
    this.buttons = []; // new
    
    this.addItem("Cursor", 15, 0.1);
    this.addItem("Grandma", 100, 1);
    this.addItem("Farm", 1100, 8);
    this.addItem("Mine", 12000, 47);
    this.addItem("Factory", 130000, 260);
    this.addItem("Bank", 1400000, 1400);
    this.addItem("Temple", 20000000, 7800);
    print(this.items);
  }
  
  addItem(name, price, cps) {
    this.items[this.numItems] = {"name":name, "price":price, "cps":cps}; // REVISE
    this.numItems += 1;
    
    // all new below
    let buttonX = this.position.x;
    let buttonY = this.position.y + this.numItems * this.buttonSize * 1.3;
    this.buttons.push(createVector(buttonX, buttonY));
  }
  
  render() { // new
    push();
    imageMode(CORNER);
    image(storeBackground, this.position.x - 50, 0, width / 2 + 50, height);
    pop();
    
    fill(255);
    text("Store", this.position.x, this.position.y);
    for (let i = 0; i < this.buttons.length; i++) {
      image(buyButton, this.buttons[i].x, this.buttons[i].y, this.buttonSize, this.buttonSize);
      let info = this.items[i]["name"] + " | " + this.items[i]["price"] + " Cookies | +" + this.items[i]["cps"] + "CPS";
      text(info, this.buttons[i].x + 30, this.buttons[i].y + 12)
    }
  }
}
