#[link(name = "helloworld_c", kind = "static")]
extern "C"
{
	fn helloworld()->();
}

fn main()
{
	println!("My name is Rust, what is your name?");
	unsafe {helloworld()};
}