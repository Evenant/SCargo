
import SCons.Builder
import SCons.Errors as SCerror
import shutil
from SCons.Node.FS import File

class Crate(str):
	""" A Crate that has been built
	"""

def lib_prefix_suffix(env, out):
	if out.startswith(env.get('LIBPREFIX', None)):
		out = env['LIBPREFIX'] + out
	if out.endswith(env.get('LIBSUFFIX', None)):
		out = out + env['LIBSUFFIX']
	return out
def shlib_prefix_suffix(env, out):
	if out.startswith(env.get('SHLIBPREFIX', None)):
		out = env['SHLIBPREFIX'] + out
	if out.endswith(env.get('SHLIBSUFFIX', None)):
		out = out + env['SHLIBSUFFIX']
	return out

def rustc_get_cfg(env)->str:
	ret = ""
	for i in env.get("RUSTCFG", []):
		ret += f" --cfg {i}"
	return ret

def rustc_extern_crates(env, crates=[])->str:
	ret = ""
	if env.get('RUSTEXTERNS', None) != None:
		for crate in env['RUSTEXTERNS']:
			ret += f" --extern {crate}"
	for crate in crates:
		ret += f" --extern {crate}"
	return ret
def rustc_get_libs(env) -> str:
	ret = ""

	for libpath in env.get("LIBPATH", []):
		ret += f" -L {libpath}"
	
	for libname in env.get("LIBS", []):
		ret += f" -l {libname}"

	return ret

def  rustc_lib(env, lib)->str:
	ret = ""

	if "/" in lib:
		while lib[-1]:
			lib = lib[:-1]
	return ret

def rustc_optimizations(env)->str:
	ret = " "
	if env.get("RUSTTARGET","") == "release":
		ret += "-O"
	else:
		ret += "-g"
	return ret



def generic_command(target, source, env):
	rustc = shutil.which("rustc")
	if rustc is None:
		SCerror.BuildError(errstr="Rust compiler ( rustc ) not found.")
	
	command = f"{str(rustc)}"
	
	command += f" {str(source[0])}"
	command +=  f" -o {str(target[0])}"

	command += f" {env.get('RUSTFLAGS','')}"
	
	command +=  rustc_extern_crates(env)
	command += rustc_get_libs(env)
	command += rustc_get_cfg(env)
	command += rustc_optimizations(env)
	while "  " in command:
		command = command.replace("  ", " ")

	return command


