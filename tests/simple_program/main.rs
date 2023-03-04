mod sub;

fn main()->Result<(),()>
{
	println!("Hello World!");
	sub::helloworld();
	bro();
	return Ok(());
}

fn bro()
{
	println!("Hello World! From bro() function.");
}