import SCargo.rust_shared as rust_shared
import SCargo.rust_static as rust_static
import SCargo.program as program
import SCargo.c_shared as c_shared
import SCargo.c_static as c_static

"""
SCargo is an extension of the SCons build tool meant for compiling Rust projects.


"""

def init_SCargo(env):
	env["RUSTCFG"] = []
	env['RUSTEXTERNS'] = []
	env['RUSTOPTIM'] = 'debug'
	env['RUSTFLAGS'] = []
	env.Append(BUILDERS = {'RustProgram':program.builder})
	env.Append(BUILDERS = {'RustStatic':rust_static.builder})
	env.Append(BUILDERS = {'RustShared':rust_shared.builder})
	env.Append(BUILDERS = {'RustCStatic':c_shared.builder})
	env.Append(BUILDERS = {'RustCShared':c_static.builder})



