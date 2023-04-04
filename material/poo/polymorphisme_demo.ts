abstract class Shape {
  abstract get area(): number;
  showName() {
    console.log("shape");
  }
}

abstract class TwoDimensionShape extends Shape {
  // surchage (ou override) de showName
  showName() {
    console.log("TwoDimensionShape");
  }
}

class Rectangle extends TwoDimensionShape {
  constructor(readonly width: number, readonly height: number) {
    super();
  }

  get area() {
    return this.width * this.height;
  }

  showName() {
    console.log("Rectangle");
  }
}

class Line extends Shape {
  get area() {
    return 0;
  }

  showName() {
    console.log("Line");
  }
}

const s: Shape = new Rectangle(10, 100);
console.log(s.area);
s.showName();
