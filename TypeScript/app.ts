interface Product {
  id: number,
  name: string,
  price: number,
}

function getProduct(id: number): Product {
  return {
    id: id,
    name: `Awesome Gadget ${id}`,
    price: 99.5,
  }
}

// console.log(`The product ${product.name} costs $${product.price}`);

const product = getProduct(1);
const showProduct = (name: string, price: number) => {
  console.log(`The product ${name} costs ${price}.`);
}

showProduct(product.name, product.price)
