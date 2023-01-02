/*
- New Project
    $ cargo new MyProj
    (--bin will make it a program and not a library)
- Build
    $ cd MyProj
    $ cargo build
    #> in ./target/debug/ you will find .exe file
- Run
    #> instead of using build command every time:
    $ cargo run
    #> this will compiles and runs and is also faster
- Check for errors without compiling
    $ cargo check
- Format code
    $ rustfmt myfile.rs 


- Syntax:
    Comments:    // and /* */ 
    Variables:
        (All variables in rust are immutable)
        let x = 5;
        let mut x = 5;  // "mut" keyword makes it mutable
        let x: u32 = 5;
            INTS:   signed,unsigned (i/u)(8,16,32,64), isize, usize
            FLOATS: f32,f64
            %: Mod
            bool
            'a': char
            Tuple:
                let t:(i32,f64,char) = (42,6.12,'h');
                let (x,y,z) = t;  // unpacking
                let (_,_,x) = t;  // just get char
                t.0  // getting items with using indexes
                functions that don't return anything, return empty tuple (called unit)
            Array:
                let a = [1,2,3,4,5];
                let a:[5,i32] = ... 
                a[0]  // indexing
                a.len()
                mem::size_of_val(&a)
                slicing:  &a[2..4]
            string:
                "mystring" is not equal to String::from("mystring")
                    // use .to_string() to make it string
                slicing works as same as arrays
                you can use "+" operator (second arg gets reference of a variable)
    println!("Hello {}",x)
    println!("this is my tuple:  {:?}",mytpl)
                                #debug flag (tuples have debug tray)
                                :#? would pretty print it
*/

fn main() {
    println!("Hello, world!");
}
