abstract class Shape {
  abstract get area(): number;
  get name(): string {
    return "shape";
  }
}

abstract class TwoDimensionShape extends Shape {
  get name(): string {
    return "TwoDimensionShape";
  }
}

class Rectangle extends TwoDimensionShape {
  constructor(readonly width: number, readonly height: number) {
    super();
  }

  get area() {
    return this.width * this.height;
  }

  get name(): string {
    return "Rectangle";
  }
}

class Line extends Shape {
  get area() {
    return 0;
  }

  get name(): string {
    return "Line";
  }
}

const s: Shape = new Rectangle(10, 100);
console.log(s.name, s.area);
