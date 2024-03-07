use std::env;
use std::process;
use std::string::String;

fn usage() {
    println!("Usage:");    
    println!("ams -h                        |  Show these informations");
    println!("ams -s  {{AMS program file}}    |  Simulate the given AMS program");
    println!("ams -r  {{AMS byte code file}}  |  Execute the given AMS byte code");
    println!("ams -cb {{AMS program file}}    |  Compile the given AMS program to AMS byte code");
    println!("ams -cn {{AMS program file}}    |  Compile the given AMS program to native machine code");
    println!("ams -ca {{AMS program file}}    |  Compile the given AMS program to x86_64 assembly");
}

fn exit(code: i32) {
    process::exit(code);
}

fn main() {
    // Get command line args
    let mut args: Vec<String> = env::args().collect::<Vec<String>>();
    args.remove(0);

    //List valid subcommands
    let subcmds: Vec<String> = vec![
        String::from("-h"), 
        String::from("-s"), 
        String::from("-r"), 
        String::from("-cb"), 
        String::from("-cn"), 
        String::from("-ca")];

    //Check if subcommand exists
    if args.len() < 1 {
        println!("An error occured: No subcommand!");
        usage();
        exit(1);
    }

    //Check if subcommand valid
    if !subcmds.contains(&args[0]) {
        println!("An error occured: Invalid subcommand:");
        println!("{}", &args[0]);
        usage();
        exit(1);
    }



    let subcmd = &args[0];

    if subcmd == &subcmds[0] {
        usage();
        exit(0);
    }
    exit(1);
}
