interface Product {
  id: number;
  name: string;
  price: number;
}

function getProduct(id: number): Product {
  return {
    id: id,
    name: `Awesome Gadget ${id}`,
    price: 99.5,
  };
}

const product = getProduct(1);
const showProduct = (name: string, price: number) => {
  console.log(`The product ${name} costs ${price}.`);
};

showProduct(product.name, product.price);
console.log("Hello".length);
console.log("Hello".toLocaleUpperCase());

// Types:
// string
// number
// boolean
// null
// undefined
// symbol

let count: number = 1;

let uname: string = "John";
let age: number = 25;
let active: boolean = true;

let names: string[] = ["John", "Jane", "Doe"];

let person: {
  name: string;
  age: number;
};

person = {
  name: "John",
  age: 25,
};

let greeting: (name: string) => string;

greeting = function (name: string) {
  return `Hi ${name}`;
};

// let counter: number = 0;

// function setCounter(max=100) {
//     return counter++;
// }

let items = [1, 2, 3, null];

// let items = [0, 1, null, 'Hi'];

let arr = [new Date(), new RegExp("d+")];

document.addEventListener("click", function (event) {
  console.log(event.button);
});

let price = 9.95;

let counter: number = 0;
let x: number = 100,
  y: number = 200;

let bin = 0b100;
let diffBin: number = 0b010;

console.log(bin);
console.log(diffBin);

let octal: number = 0o10;
let hexadec: number = 0xa;

let fName: string = "John";
let jobTitle: string = "Web Dev";

let desc = `This TS string can
span multiple
lines
of
text
`;

let profile: string = `I'm ${fName} and I'm a ${jobTitle}`;

console.log(profile);

let pend: boolean;
pend = true;
pend = false;
let employee: object;

employee = {
  fName: "John",
  lName: "Doe",
  age: 25,
  jobTitle: "Web Developer",
};

console.log(employee);

const double = (x: number) => x * 2;
console.log(double(2));

console.log("💀 ");
