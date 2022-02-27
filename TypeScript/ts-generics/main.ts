// TS Generics

const println = (str: string) => console.log(str)
println('Hello World')

// function identity(arg: number): number {
//     return arg;
// }

function identity<Type> (arg: Type): Type {
    return arg;
}

let stdout = identity<string>("Stringaling");
let intout = identity<number>(5);