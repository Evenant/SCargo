import SCargo.utils as utils
import SCons.Builder as Builder
import SCons.Errors as SCerrors
import sys
from subprocess import Popen

def builder_func(target, source, env):
	command = utils.generic_command(target, source, env)
	command += " --crate-type bin"
	print(command)
	if Popen(args=command.split(' '), stdout=sys.stdout, stderr=sys.stderr).wait()!= 0:
		raise SCerrors.BuildError(errstr="rustc error.", filename=str(target), action=builder_func)

builder = Builder.Builder(action=builder_func,
	src_suffix=".rs"
)