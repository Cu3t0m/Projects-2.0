use std::collections::HashMap;

struct Todo {
    // use HashMap to store key value pairs
    map: HashMap<String, bool>,
}



fn main() {
    // let action = std::env::args().nth(1).expect("Please specify action");
    // let item = std::env::args().nth(2).expect("Please specify item");
    let action = std::env::args().nth(1).expect("Please specify an action");
    let item = std::env::args().nth(2).expect("Please specify an item");
    println!("{:?}, {:?}", action, item)
}