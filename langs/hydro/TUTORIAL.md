# Tutorial for HYDRO-LANG
## Contents of this tutorial
### [Creating your first project](#creating-your-first-project-1)
#### [Installing HYDRO-LANG](#installing-hydro-lang-1)
#### [Setting up your project](#setting-up-your-project-1)
#### [Basic program structure](#basic-program-structure-1)

## Creating your first project
### Installing HYDRO-LANG
1. For installation of the HYDRO compiler, it has to be compiled by the [Rust](https://www.rust-lang.org/) programming language. To install rust first [download Visual Studio](https://visualstudio.microsoft.com/en/downloads/) and install it.
2. Now download and install the [RUST-LANG](https://www.rust-lang.org/tools/install).
3. In your terminal navigate to this directory and run `cargo build --release` to build the compiler to the `target/release` directory.
4. It's recomended to add the `target/release` directory to the system PATH variable. How this is done depends on the OS.
### Setting up your project
1. Navigate to a directory of your choice in your terminal.
2. Run `hydro -init [NAME]`, where `[NAME]` will be the name of your project.
3. A directory with your chosen name should have been created. It should contain a `hydro.json` file and a `src` directory, containing your code. In here the file `main.hd` should have been created, being the entry point of your program.
### Basic program structure
