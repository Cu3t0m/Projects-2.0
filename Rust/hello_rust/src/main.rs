// This code was formatted with the Prettier VSCode Extension

// * Imports
use std::io;

// * Rust tutorial code
fn main() {
    //Insert code here
    println!("Hello!");
    let name = "Kishore";
    let sname = "Satheeskumar";
    println!("My first name is {}, my last name is {}", name, sname);
    println!("What's yours?");
    let mut uname = String::new();

    io::stdin().read_line(&mut uname).expect("Nice name!");

    println!("Your name is {}", uname);
    println!("That's a great name!");

    // Gathers user input
    let mut userinput = String::new();
    println!("Please enter a string, and this program will print it out for you");
    io::stdin().read_line(&mut userinput).expect("Poggers!");

    println!("You entered {}", userinput);

}
