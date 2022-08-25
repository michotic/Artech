class GoldCookie {
  constructor(position) {
    this.position = position;
    this.radius = 50;
    this.duration = 60 * 5;
    this.remaining = 0;
    this.reward = 0;
  }
  
  render() {
    image(goldCookie, this.position.x, this.position.y, this.radius, this.radius);
    this.remaining -= 1;
    if (this.remaining < 1) {
      this.position.x = -100;
    }
  }
}
