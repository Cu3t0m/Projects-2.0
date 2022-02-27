class Human {
  constructor(public name) {}

  sayHi() {
    return `Hello ${this.name}`;
  }
}

const patrick = new Human("Patrick Mullot");

console.log(patrick.sayHi());

class SuperHuman extends Human {
  heroName;

  constructor(name) {
    super(name);
    this.heroName = `Hero ${name}`
  }

  superPower() {
      return `${this.heroName} will kys`
  }
}

const abdul = new SuperHuman('Abdul Mujeeb')
console.log( abdul.sayHi() )