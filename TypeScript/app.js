// let box;
// console.log(typeof (box));
//
// box = "Hello";
// console.log(typeof (box));
//
// box = 100;
// console.log(typeof (box));
function getProductId(id) {
    return {
        id: id,
        name: "Awesome Gadget ".concat(id),
        price: 99.5
    };
}
var product = getProductId(1);
console.log("The Product ".concat(product.name, " costs $").concat(product.price));
var showProduct = function (name, price) {
    console.log("The product ".concat(name, " costs ").concat(price, "$."));
};
showProduct(product.price, product.name);
