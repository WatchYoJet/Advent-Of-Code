use std::fs::File;
use std::io::{BufRead, BufReader};




//IM NOT PROUD OF THIS CODE, I WAS IN A HURRY
fn part1() {
    let file = File::open("./input2.txt").unwrap();
    let reader = BufReader::new(file);
    let mut x = 0;
    let mut y = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        let split = line.split(" ");
        let mut counter = 0;
        let mut _state = "";
        for content in split {
            if counter == 0{
                _state = content;
            }else {
                let increment = content.parse::<i32>().unwrap();
                match _state {
                    "down" => y += increment,
                    "up" => y -= increment,
                    "forward" => x += increment,
                    _ => println!("BRRR"),
                };
            }
            counter += 1;
        }
    }
    println!("A1:{}", x * y);
}


fn part2() {
    let file = File::open("./input2.txt").unwrap();
    let reader = BufReader::new(file);
    let mut x = 0;
    let mut y = 0;
    let mut aim = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        let split = line.split(" ");
        let mut counter = 0;
        let mut _state = "";
        for content in split {
            if counter == 0{
                _state = content;
            }else {
                let increment = content.parse::<i32>().unwrap();
                match _state {
                    "down" => aim += increment,
                    "up" => aim -= increment,
                    "forward" =>{
                        x += increment;
                        y += aim * increment;
                    },
                    _ => println!("BRRR"),
                };
            }
            counter += 1;
        }
    }
    println!("A2:{}", x * y);
}

fn main() {
    part1();
    part2();
}
