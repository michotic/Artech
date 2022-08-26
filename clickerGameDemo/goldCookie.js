class GoldCookie {
  constructor(position) {
    this.position = position;
    this.radius = 50;
    this.duration = 60 * 5;
    this.reward = (cps + 1) * random(10, 100);
  }
  
  render() {
    fill(0);
    ellipse(this.position.x, this.position.y, this.radius * 1.2, this.radius * 1.2);
    image(goldCookie, this.position.x, this.position.y, this.radius, this.radius);
    this.duration -= 1;
  }
}
