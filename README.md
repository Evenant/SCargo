# SCargo
SCargo is an extension of SCons that allows you to build Rust with SCons.

## Running Tests
After installing SCargo, go into the tests/ directory and run:
```sh
python test_suite.py
```

This will build the tests with SCons and then runs the tests.

## Quickstart
Install SCargo (locally or globally), create a `SConstruct` file, and see if you can import it.
```py
import SCargo
```

Run the following:
```sh
scons

# Alternatively
python -m SCons
```

If nothing bad happened, then we can start creating a program.
Add the following to that `SConstruct` file:
```py
import SCargo

env = Environment()
SCargo.init_SCargo(env)

env.RustProgram('main', ['main.rs'])
```

Now create a `main.rs` file and add the following:
```rs
fn main()
{
	println("Hello World!");
}
```

Now run:
```sh
scons

# Alternatively
python -m SCons
```

Now that we have built a program, run the executable:
Linux / MacOS:
```
./main
```

Windows:
```
main
```

## Advanced Usage
Use the `init_SCargo` function to initialize the builders.
```py
import SCargo
env = Environment()
SCargo.init_SCargo(env)
```

### Builders

Now the `env` variable contains 5 new builder functions, `RustProgram`, `RustShared`, `RustStatic`, `RustCShared`, `RustCStatic`.

`RustProgram` creates an executable. (`--crate-type bin`)

`RustShared` creates a Rust dynamic library. (`--crate-type dylib`)

`RustStatic` creates Rust static library (more commonly known as a "Crate"). (`--crate-type rlib`)

`RustCShared` creates a native shared library. (`--crate-type cdylib`)

`RustCStatic` creates a native static library. (`--crate-type staticlib`)

### Constrution Variables

`env` also has 4 new constrution variables, `RUSTCFG`, `RUSTEXTERNS`, `RUSTOPTIM`, `RUSTFLAGS`.

`RUSTCFG` is a list which contains values/key-value pairs that will be included in a `--cfg` flag.
```py
env.RustProgram('main', ['main.rs'], RUSTCFG=['foo', 'bar="baz"'])

# Outputs:
# rustc main.rs -o main --cfg foo --cfg bar=baz -g --crate-type bin
```

`RUSTEXTERNS` is a list which contains key-value pairs that will be included in an `--extern` flag.
```py
env.RustProgram('main', ['main.rs'], RUSTEXTERNS=['bar="baz"'])

# Outputs:
# rustc main.rs -o main --extern bar="baz" -g --crate-type bin
```

`RUSTOPTIM` specifies the optimization of the output, it may only be "release" to optimize the output, anything else is assumed to be "debug".
```py
env.RustProgram('main', ['main.rs'], RUSTOPTIM='release')

# Outputs:
# rustc main.rs -o main -O --crate-type bin
```

`RUSTFLAGS` is a list which contains a bunch extra flags that will be passed to the compiler, incase you want lower-level access to the compiler.
```py
env.RustProgram('main', ['main.rs'], RUSTFLAGS=['-L /path/to/lib','-l static=mylib'])

# Outputs:
# rustc main.rs -o main -L /path/to/lib -l static=mylib --crate-type bin
```