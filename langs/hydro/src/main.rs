use std::env;
use std::process;

fn exit(code: i32) {
    process::exit(code);
}



fn usage() {
    // Outputs usage information
    println!("");
    println!("Usage of the HYDRO-TOOL:");
    println!("");
    println!("hydro  -help         Show list of commands");
    println!("hydro  -init [NAME]  Initializes a HYDRO project in current directory");
    println!("hydro  -sim          Interprets the project in the current directory");
    println!("hydro  -com          Compiles the project in the current directory");
    println!("");
}



fn handle_init(name: &str) {
    println!("Error: Initializing is not yet implemented!");
    exit(1);    
}



fn main() {
    // Get args
    let mut args: Vec<String> = env::args().collect();
    args.remove(0);

    // Check for cmd
    if args.len() == 0 {
        println!("Error: No arguments given!");
        usage();
        exit(1);
    }

    // Get cmd
    let cmd_string = args.remove(0);
    let cmd = cmd_string.as_str();

    // Check for "-help"
    if cmd == "-help" {
        usage();
        exit(0);
    }

    // Check for "-init"
    if cmd == "-init" {
        // Check for name
        if args.len() == 0 {
            println!("Error: The project should be given a name!");
            exit(1);
        }

        // Get name
        let name_string = args.remove(0);
        let name = name_string.as_str();

        // Handle initialization
        handle_init(name);
    }

    // Check for "-sim"
    if cmd == "-sim" {
        println!("Error: Simulating is not yet implemented!");
        exit(1);
    }

    // Check for "-com"
    if cmd == "-com" {
        println!("Error: Compiling is not yet implemented!");
        exit(1);
    }

    // Handling of invalid cmd
    println!("Error: \"{}\" is not a valid command!", cmd);
    usage();
    exit(1);
}