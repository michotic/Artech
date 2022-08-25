class Clicker {
  constructor(x, y, radius) {
    this.position = createVector(x, y);
    this.radius = radius;
    this.perClick = 1;
    this.sizeMulti = 1;
  }
  
  render() { // sizemulti logic is new
    fill(0);
    ellipse(this.position.x, this.position.y, this.radius * 1.1 * this.sizeMulti, this.radius * 1.1 * this.sizeMulti);
    image(cookieImage, this.position.x, this.position.y, this.radius * this.sizeMulti, this.radius * this.sizeMulti);
    if (this.sizeMulti > 1) {
      this.sizeMulti -= 1 / 60;
    }
  }
  
  addCookies(currentCookies, toAdd) {
    this.sizeMulti = 1.3;
    return (currentCookies + toAdd)
  }
}
