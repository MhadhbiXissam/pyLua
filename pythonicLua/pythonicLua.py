import sys , ast , os , traceback
from compiler import ast_globals

def getEXPORT_FILE(file) : 
	EXPORT_FILE = None
	with open(file) as pyfile : 
		for line in pyfile : 
			if line.startswith("###") :
				EXPORT_FILE = line.strip()[3:]
				EXPORT_FILE = EXPORT_FILE.strip()
	return EXPORT_FILE



def transpile_code(file,export_file = None,log = True) : 
	code = ""
	with open(file) as buff :  code = ast.dump(ast.parse(buff.read()))
	code_generated  = "--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n"
	code_generated += "--python file\t:\t" + os.path.abspath(file) +"\n" 
	code_generated += "--python ast\t:\t" + code + "\n"
	code_generated += "--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n"
	has_error = False
	try : 
		code_generated += eval("repr(" + code + ")",ast_globals)
	except Exception as e  : 
		print("BAD PYTHON SYTHAXE :",traceback.print_exc())
		print(code)
		has_error = True
	code_generated += "\n--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
	if log and not has_error : print(code_generated)
	EXPORT_FILE = getEXPORT_FILE(file)
	if export_file != None : 
		EXPORT_FILE = export_file
	if EXPORT_FILE == None :
		defaul_EXPORT_FILE = os.path.abspath(file)[:-len(".pylua")] 
		print(code_generated , file = open(defaul_EXPORT_FILE , "w"))
	else : 
		print(code_generated , file = open(EXPORT_FILE , "w"))
	return code


if __name__ == '__main__':
	if len(sys.argv) > 1  : 
		code = transpile_code(sys.argv[1],export_file = None)
		print(sys.argv)
		print("debug:" , code)










