extern crate dependency;
use dependency::hello_world;
fn main()->()
{
	println!("I came from the Main crate!");
	hello_world();
}


