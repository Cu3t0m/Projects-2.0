// Imports
use std::io;
use rand::Rng;

fn main() {
    println!("Hello, world!");

    println!("enter your name");
    let mut name = String::new();

   io::stdin().read_line(&mut name).expect("Nice name!");

    println!("Your name is {}", name);
    println!("That's a nice name!");

    // Random number generated and user has to guess
    let num = rand::thread_rng().gen_range(0..5);
    println!("Enter a guess for a number between 1 and 5");
    let mut uinput = int::new();

    io::stdin().read_line(&mut uinput).expect("Invalid");

    if let uinput =  {
        
    }
}
