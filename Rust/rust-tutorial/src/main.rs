// Imports
use std::io;

fn main() {
    println!("Hello, world!");

    println!("enter your name");
    let mut name = String::new();

    io::stdin().read_line(&mut name).expect("Nice name!");

    println!("Your name is {}", name);
    println!("That's a nice name!");
}
