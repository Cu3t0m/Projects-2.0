use std::io;

fn main() {
    
    // Variables and constants

    // let mut x = 5; // mutable variable
    // println!("Value of x: {}", x);
    // x = 6;
    // println!("Value of x: {}", x);
    // let y = 6; // immutable variable
    
    // const NAME_OF_CONST: Type = Value
    // const Z: i32 = 69; // Constant, value can't be mutated, unlike with the "let" keyword
    // println!("z = {}", Z);

    // IO
    let mut fname = String::new();
    io::stdin().read_line(&mut fname).expect("Invalid");
    println!("Your name is: {}", fname);

    // let a = x + y; // Addition
    // println!("{} + {} = {}", x, y, a);
    // let b = x - y; // Subtraction
    // println!("{} - {} = {}", x, y, b);
    // let c = x * y; // Multiplication
    // println!("{} * {} = {}", x, y, c);
    // let d = x / y; // Division
    // println!("{} / {} = {}", x, y, d);
    // let e = x % y; // Modulus
    // println!("{} MOD {} = {}", x, y, e);
    // let f = x;
    // let g = u32::pow(x, y); // Multiply to power
    // println!("{}^{} = {}", x, y, g);

    // Data types
    let _signed_8: i8 = 127;
    let _unsigned_8: u8 = 255;
    let _signed_16: i16 = 32767;
    let _unsinged_16: u16 = 65367;
    
}