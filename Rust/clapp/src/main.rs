use clap::Parser;

#[derive(Parser, Debug)]
#[clap(about, version, author)]
struct Args {
    // name of person
    #[clap(short, long)]
    name: String,

    // Number of times to greet
    #[clap(short, long, default_value_t = 1)]
    count: u8,
}

struct Args {
    // url
    #[clap(short, long)]
    url: String,

    // Output file
    #[clap(short, long)]
    output: String,
}

fn main() {
    let args = Args::parse();

    println!("Url: {}", args.url);
    println!("Output: {}", args.output)
}