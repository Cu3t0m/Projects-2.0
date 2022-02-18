// I'm committing to this, probably

// const alertamente = document.getElementById("alertamente")

// Not allowed, but also allowed. Basically the same as 'var'
// name = 'Jack';

// Explicitly stating 'var'
// var name = "~";

// Using let, the norm in modern JS
// let age = 27;

// Constants
const DATE = "Friday 13th October 2022"

let bool = true;

// Template literals
var namee = 'John'
var agee = 25
var colour = 'purple'
var job = "Software Developer"
var msg = `Hey, my name is ${namee} and I am ${agee} years old. My favourite colour is purple and I work as a ${job}`
console.log(msg)

// Arrow functions
function TimesTwo(params) { return params * 2}function TimesTwo(params) {
    return params * 2
}

console.log(TimesTwo(4))

let timesTwo = params => params * 2
console.log(timesTwo(4))

// With empty parentheses for no params
let NoParas = () => 42
let otherNoParas = _ => 42
console.table(NoParas + otherNoParas)

let optional = (x) => 42
console.log(optional())

let multiParams = (x, y) => 42
console.log(multiParams())

let feedMyCat = (cat) => {
    if (cat === 'hungry') {
        return 'Feed your damn cat';
    } else {
        return 'Do not feed the cat';
    }
}

let cat = 'hungry'

console.log(feedMyCat(cat))

// const employee = {
//     id: 007,
//     name: 'James',
//     surname: 'Bond',
//     dept: 'Spy'
// }

// const { id, name } = employee;

// console.log(`Name: ${name}, id: ${id}`)

const employee = {
    id: 007,
    name: 'James',
    dept: {
      id: 'D001',
      name: 'Spy',
      address: {
        street: '30 Wellington Square',
        city: 'Chelsea'  
      }
    }  
}

// const address = employee.dept.address;
// const street = employee.dept.address.street;
// console.log(address)

const { dept: { address: { street } } } = employee;
console.log(street)


const {name, dept, message = `${name} is ${dept}`} = employee;
console.log(message);

// Async Await (Watch Fireship stupid)