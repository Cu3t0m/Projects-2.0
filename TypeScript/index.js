#!/usr/bin/env node
function getProduct(id) {
    return {
        id: id,
        name: "Awesome Gadget ".concat(id),
        price: 99.5
    };
}
// console.log(`The product ${product.name} costs $${product.price}`);
var product = getProduct(1);
var showProduct = function (name, price) {
    console.log("The product ".concat(name, " costs ").concat(price, "."));
};
showProduct(product.name, product.price);
console.log('Hello'.length);
console.log('Hello'.toLocaleUpperCase());
// Types:
// string
// number
// boolean
// null
// undefined
// symbol
// const heading = document.querySelector('h1');
// Type annotations
// let count: number;
// count = 'Hello';
var count = 1;
var uname = 'John';
var age = 25;
var active = true;
var names = ['John', 'Jane', 'Doe'];
var person;
person = {
    name: 'John',
    age: 25
};
var greeting;
greeting = function (name) {
    return "Hi ".concat(name);
};
var counter = 0;
function setCounter(max) {
    if (max === void 0) { max = 100; }
    return counter++;
}
var items = [1, 2, 3, null];
// let items = [0, 1, null, 'Hi'];
var arr = [new Date(), new RegExp('\d+')];
document.addEventListener('click', function (event) {
    console.log(event.button);
});
// document.addEventListener('scroll', function (event) {
//     console.log(event.button);
// })

// =>