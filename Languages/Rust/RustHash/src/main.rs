// extern crate crypto;
extern crate cipher_crypt;

use cipher_crypt::{Cipher, Railfence};


fn main() {
    use std::time::Instant;
    let now = Instant::now();

 
 
    let input = "abcdef";
    let mut i = 100;
    while i < 5000000 {
        let c = Railfence::new(2);
        let x = &c.encrypt(&i.to_string()).unwrap();
        // print!("{x}");
        // assert_eq!(m2, c.decrypt(&c.encrypt(m2).unwrap()).unwrap());

        i = i + 1;
        // break;
    }



    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);

}



//> MD5
/* 
use crypto::md5::Md5;
        let digest = md5::compute(input);
        println!("md5({:?}) = {:?}", input, digest);
*/

//> SHA1
/*
use crypto::digest::Digest;
use self::crypto::sha1::Sha1;

        let mut hasher = Sha1::new();
        hasher.input_str(input);
        let hex = hasher.result_str();
        // println!("sha1({:?}) = {:?}", input, hex);
*/

//> SHA256
/*
use self::crypto::digest::Digest;
use self::crypto::sha2::Sha256;
        let mut hasher = Sha256::new();
        hasher.input_str(input);
        let hex = hasher.result_str();
        // println!("{hex}");
*/
