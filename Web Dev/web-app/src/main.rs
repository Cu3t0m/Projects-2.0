extern crate reqwest;

fn main() {
    let result = fetch_text("https://www.rust_lang.org");
    let count = result.unwrap().chars.count();

    println!("{}", count);
}

fn fetch_text(url: &str) -> Result<(String), reqwest::Error> {
    let body = reqwest::get(url).text()?;

    Ok(body)
}
