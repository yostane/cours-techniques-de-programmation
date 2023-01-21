class Monster {
  constructor(readonly name: string, readonly hp: number) {}

  checkAlive() {
    if (this.hp <= 0) {
      console.log(this.name, "est ko 💀");
    } else {
      console.log(this.name, "est va bien 👌");
    }
  }
}

const monster1 = new Monster("Lapinou", 100);
const monster2 = new Monster("Chatounet", 0);

monster1.checkAlive();
monster2.checkAlive();

const monsters = [monster1, monster2];
monsters[0].checkAlive();
