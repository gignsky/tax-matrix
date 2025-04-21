use clap::Parser;
use toml::Table;

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

    let rates_path = "../rates/";
    let rates = import_rates(rates_path);
}

fn import_rates(path: str) {
    let mut rates = Vec::new();
}
struct State {
    name: String,
    abbrevation: String,
    counties: Vec<County>,
}

struct County {
    name: String,
    rate: f32,
    state: State,
    districts: Vec<District>,
    cities_towns: Vec<CityTown>,
    fees: Vec<Fee>,
}

struct District {
    name: String,
    rate: f32,
    county: County,
}

struct CityTown {
    name: String,
    rate: f32,
    county: County,
}

struct Fee {
    name: String,
    rate: f32,
    county: County,
}
