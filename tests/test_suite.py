import os
from subprocess import Popen
from termcolor import colored

def run_test_in_dir(dir)->bool:
	rootdir = os.getcwd()
	os.chdir(dir)
	ret = False
	if Popen(args="./main".split(" ")).wait() != 0:
		ret = True
	os.chdir(rootdir)
	return ret

print(colored('Building tests with command: `python -m SCons -j4`.','yellow'))
if Popen(args="python -m SCons -j4".split(" ")).wait() != 0:
	raise Exception(colored("Something went wrong when building.",'red'))
print(colored('Succesfully built tests.\n','green'))

try:
	print(colored("Test 1 (Simple Program)",'blue'))
	if run_test_in_dir("simple_program"):
		raise Exception(colored("Test 1 Failed!", 'red'))
	print(colored("Test 1 Successful!\n",'green'))
	

	print(colored("Test 2 (Binary with external Crate)", 'blue'))
	if run_test_in_dir("ext_crate"):
		raise Exception(colored("Test 2 Failed!"),'red')
	print(colored("Test 2 Successful!\n",'green'))

	print(colored("Test 3 (C in Rust)", 'blue'))
	if run_test_in_dir("c_in_rust"):
		raise Exception(colored("Test 3 Failed!"),'red')
	print(colored("Test 3 Successful!\n", 'green'))

	print(colored("Test 4 (Rust in C)", 'blue'))
	if run_test_in_dir("rust_in_c"):
		raise Exception(colored("Test 4 Failed!"),'red')
	print(colored("Test 4 Successful!\n", 'green'))
	
	print(colored("Test 5 (Cargo in SCargo)", 'blue'))
	if run_test_in_dir("cargo_interop"):
		raise Exception(colored("Test 5 Failed!"),'red')
	print(colored("Test 5 Successful!\n", 'green'))
except:
	print(colored("TESTS UNSUCCESSFUL", 'red'))
else:
	print(colored("TESTS SUCCESSFUL", 'green'))

