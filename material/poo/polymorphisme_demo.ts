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

const shapes: Shape[] = [new Line(), new Rectangle(40, 80), new Line()];
// Si TS n'était pas polymorphe
for (const shape of shapes) {
  if (shape instanceof Line) {
    // casting: changer le type
    (shape as Line).showName();
  } else if (shape instanceof Rectangle) {
    (shape as Rectangle).showName();
  }
}

// mais comme TS est polymorhpe
for (const shape of shapes) {
  shape.showName();
}
