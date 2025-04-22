use std::fs;

use serde::Deserialize;
use toml::Table;

pub fn import_rates_and_fees(path: &str) {
    // let mut states = Vec::new();
    println!("Importing rates and fees from {}", path);

    // Get the list of folders in the rates directory
    let county_folders = match easy_paths::get_paths_in_dir(&path) {
        Ok(vec_result) => vec_result,
        Err(err) => panic!("{}", err,),
    };

    // Iterate over each folder
    for county_folder in county_folders {
        println!("Found folder: {}", county_folder.clone());

        // Get the list of files in the folder
        let files = match easy_paths::get_paths_in_dir(&county_folder) {
            Ok(vec_result) => vec_result,
            Err(err) => panic!("{}", err,),
        };

        // Iterate over each file
        for file in files {
            println!("Found file: {}", file.clone());

            // Read the file contents
            let contents = fs::read_to_string(&file).unwrap_or("".to_string());

            println!("File contents: {}", contents.clone());

            let county: Table = toml::from_str(&contents).unwrap();

            dbg!("Parsed county: {:?}", county);

            // Initialize the County structs
        }
    }
}

fn county_importer(county: Table) -> County {}

enum State {
    NC,
    SC,
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
