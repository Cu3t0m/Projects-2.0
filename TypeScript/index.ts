#!/usr/bin/env node

// let message: string = "Hello, World!";
let message: string = "Hello, this is TypeScript!";
console.log(message);

// Create new h1
let heading = document.createElement('h1');
heading.textContent = message;

// Append the heading
document.body.appendChild(heading);

// JS Scheiße
// let box;
// console.log(typeof (box));

// box = "Hello";
// console.log(typeof (box));

// box = 100;
// console.log(typeof (box));

// function getProductId(id: any) {
//   return {
//     id: id,
//     name: `Awesome Gadget ${id}`,
//     price: 99.5,
//   }
// }

// const product = getProductId(1);
// console.log(`The Product ${product.name} costs $${product.price}`)
//
// const showProduct = (name: any, price: any) => {
//   console.log(`The product ${name} costs ${price}$.`)
// }

// showProduct(product.price, product.name)