const { log, clear, table } = console;

interface Person {
  name: string;
  age: number;
  likesFood: boolean;
}

let John: Person = { name: "John", age: 25, likesFood: true };
let Alex: Person = { name: "Alex", age: 24, likesFood: false };
let people: any[] = [John, Alex]

log("Hello, World!");

table(people)
