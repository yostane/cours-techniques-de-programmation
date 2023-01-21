const monsterName1 = "Lapinou";
const monsterHp1 = 100;

const monsterName2 = "Chatounet";
const monsterHp2 = 0;

function checkMonsterAlive(name: string, hp: number) {
  if (hp <= 0) {
    console.log(name, "est ko 💀");
  } else {
    console.log(name, "est va bien 👌");
  }
}

checkMonsterAlive(monsterName1, monsterHp1);
checkMonsterAlive(monsterName2, monsterHp2);

const monsters = [monsterName1, monsterHp1, monsterName2, monsterHp2];
checkMonsterAlive(monsters[0] as string, monsters[1] as number);
