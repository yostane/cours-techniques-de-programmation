class Watch {
  constructor(private hour: number, private minute: number) {}

  clone(): Watch {
    return new Watch(this.hour, this.minute);
  }

  // Avant d'une minute
  advance() {
    this.minute += 1;
    if (this.minute === 60) {
      this.hour += 1;
      this.minute = 0;
      if (this.hour === 24) {
        this.hour = 0;
      }
    }
  }

  getTimeString(): string {
    return `${this.hour}:${this.minute}`;
  }
}

class Person {
  constructor(readonly name: string, private watch: Watch | null) {}
  // wear:  porter (pour les vêtement)
  wear(watch: Watch) {
    if (this.watch === null) {
      this.watch = watch;
    }
  }
  remove() {
    this.watch = null;
  }
  requestTime(person: Person): string {
    if (person.watch !== null) {
      return `${person.name}: il est ${person.watch.getTimeString()}`;
    }
    // else pas nécessaire car de toute façon, le if fait un return
    return "";
  }
}

const w = new Watch(10, 59);
const w2 = w.clone();
w.advance();
console.log(w, w2);

const tintin = new Person("Tintin", null);
const dupond = new Person("Dupond", w2);

console.log(tintin);
tintin.wear(w);
console.log(tintin);
tintin.remove();
console.log(tintin);

const time = tintin.requestTime(dupond);
console.log(time);
