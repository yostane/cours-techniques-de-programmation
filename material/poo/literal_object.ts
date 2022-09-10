const ship1 = {
  price: 20000,
  name: "The decennial Eagle",
  shootPower: 6,
  shoot() {
    console.log("pew pew");
  },
};

ship1.shoot();

interface Shooter {
  readonly shootPower: number;
  shoot(): void;
}
function checkPower(shooter: Shooter) {
  console.log("The shooter has power of", shooter.shootPower);
}

checkPower(ship1);

const serpent = {
  shootPower: 1,
  shoot() {
    console.log("pew pew");
  },
};

checkPower(serpent);

const cat = {
  name: "chat-pardeur",
};

// checkPower(cat); // fails
