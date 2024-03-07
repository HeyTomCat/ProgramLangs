use std::env;
use std::process;
use std::string::String;
use std::fs;

fn usage() {
    println!("");
    println!("Usage of AMS tool:");  
    println!("");
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
    //Subcommands, that require a file
    let mut subcmds_rf = subcmds.clone();
    subcmds_rf.remove(0);

    //Check if subcommand exists
    if args.len() < 1 {
        println!("An error occured: No subcommand!");
        usage();
        exit(1);
    }


    //Get subcommand
    let subcmd = args.remove(0);

    //Check if subcommand valid
    if !subcmds.contains(&subcmd) {
        println!("An error occured: Invalid subcommand:");
        println!("{}", subcmd);
        usage();
        exit(1);
    }

    //Check if subcommand has required args
    if subcmds_rf.contains(&subcmd) && args.len() < 1{
        println!("An error occured: No File given!");
        usage();
        exit(1);
    }



    

    //Check if subcommand is "-h"
    if subcmd == subcmds[0] {
        usage();
        exit(0);
    }

    //Check if subcommand is any other valid subcommand
    if !subcmds_rf.contains(&subcmd) {
        println!("Fatal exception: Unable to resolve subcommand:");
        println!("{}", subcmd);
    }

    //Read file
    let prog: String = fs::read_to_string(&args[0]).expect("~");

    //Check for error while reading file
    if prog == String::from("~") {
        println!("An Error Occured: Could not read file:");
        println!("{}", &args[0]);
        exit(1);
    }

    println!("{}", prog);
}
