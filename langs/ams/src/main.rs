use std::env;
use std::process;
use std::string::String;
use std::fs;
use std::path;
use std::str;

fn usage() {
    //Print usage infos
    println!("");
    println!("Usage of AMS tool:");  
    println!("");
    println!("ams -h                        |  Show usage infos");
    println!("ams -s  {{AMS program file}}    |  Simulate the given AMS program");
    println!("ams -r  {{AMS byte code file}}  |  Execute the given AMS byte code");
    println!("ams -cb {{AMS program file}}    |  Compile the given AMS program to AMS byte code");
    println!("ams -cn {{AMS program file}}    |  Compile the given AMS program to native machine code");
    println!("ams -ca {{AMS program file}}    |  Compile the given AMS program to x86_64 assembly");
}

fn exit(code: u8) {
    //Halt process
    process::exit(code.into());
}

fn main() {
    // Get command line args
    let mut args: Vec<String> = env::args().collect::<Vec<String>>();
    args.remove(0);

    //List valid subcommands
    let subcmds: Vec<String> = vec![
        String::from("-v"),
        String::from("-h"), 
        String::from("-s"), 
        String::from("-r"), 
        String::from("-cb"), 
        String::from("-cn"), 
        String::from("-ca")];
    //Subcommands, that require a file
    let mut subcmds_rf = subcmds.clone();
    subcmds_rf.remove(0);
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

    
    //Check if subcommand is "-v"
    if subcmd == subcmds[0] {
        println!("AMS v2.0u0");
        exit(0);
    }


    //Check if subcommand is "-h"
    if subcmd == subcmds[1] {
        usage();
        exit(0);
    }

    //Check if subcommand is any other valid subcommand
    if !subcmds_rf.contains(&subcmd) {
        println!("Fatal exception: Unable to resolve subcommand:");
        println!("{}", subcmd);
        exit(1);
    }

    //Check if path is valid
    if !path::Path::new(&args[0]).exists() {
        println!("An error occured: Couldn't find file:");
        println!("{}", &args[0]);
        exit(1);
    }

    //Read file
    let prog = fs::read_to_string(&args[0]).expect("MAIN - L91 - Couldn't read file!");

    //Check if ascii
    if !str::is_ascii(&prog) {
        println!("An error occured: Detected non-ascii characters in program!");
        exit(1);
    }

    println!("{}", prog);
}
