import SCargo.rust_shared as rust_shared
import SCargo.rust_static as rust_static
import SCargo.program as program
import SCargo.c_shared as c_shared
import SCargo.c_static as c_static

from SCons.Script import Builder

"""
SCargo is an extension of the SCons build tool meant for compiling Rust projects.


"""

def init_SCargo(env):
	env.Append(BUILDERS = {'RustProgram':program.rust_program_builder})
	env.Append(BUILDERS = {'RustStatic':rust_static.builder})
	env.Append(BUILDERS = {'RustShared':rust_shared.builder})
	env.Append(BUILDERS = {'RustCStatic':c_shared.builder})
	env.Append(BUILDERS = {'RustCShared':c_static.builder})



