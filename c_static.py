import SCargo.utils as utils
import SCons.Builder as Builder
import SCons.Errors as SCerrors
import sys
import os
from subprocess import Popen

def builder_action(target, source, env):
	command = utils.generic_command(target, source, env)
	command += " --crate-type staticlib"
	
	print(command)
	if Popen(args=command.split(" "), stdout=sys.stdout, stderr=sys.stderr).wait() != 0:
		raise SCerrors.BuildError(errstr="rustc error.", filename=str(source[0]), action=builder_action)

def builder_emitter(target, source, env):
	target[0] = env.get('LIBPREFIX','') + str(target[0]) + env.get('LIBSUFFIX','')
	env.Append(RUSTFLAGS=f"-L\"{os.getcwd()}\"")

	return target, source

builder = Builder.Builder(action=builder_action,
	src_suffix=".rs",
	emitter=builder_emitter
)