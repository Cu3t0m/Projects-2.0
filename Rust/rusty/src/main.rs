use std::io::stdin;

fn main() {

    let mut name = String::new();
    stdin().read_line(&mut name).expect("failed to read line");

    println!("Hello, world!");
}
