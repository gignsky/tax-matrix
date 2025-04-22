#![allow(unused_imports)]
#![allow(dead_code)]

use std::fs;

use clap::Parser;
use serde::Deserialize;
use toml::Table;

mod toml_importer;

#[derive(Parser, Debug)]
#[clap(author = "Maxwell Rupp", version, about)]
/// Application configuration
struct Args {
    /// whether to be verbose
    #[arg(short = 'v')]
    verbose: bool,

    /// an optional name to greet
    #[arg()]
    name: Option<String>,
}

fn main() {
    let args = Args::parse();
    if args.verbose {
        println!("DEBUG {args:?}");
    }
    println!(
        "Hello {} (from tax-matrix)!",
        args.name.unwrap_or("world".to_string())
    );

    let rates_path = "src/rates";
    // let rates =
    toml_importer::import_rates_and_fees(rates_path);
}
