import sys , ast , os 
from compiler import ast_globals

def getEXPORT_FILE(file) : 
	EXPORT_FILE = None
	with open(file) as pyfile : 
		for line in pyfile : 
			if line.startswith("###") :
				EXPORT_FILE = line.strip()[3:]
	return EXPORT_FILE



def transpile_code(file,export_file = None) : 
	code = ""
	with open(file) as buff :  code = ast.dump(ast.parse(buff.read()))
	code_generated = eval("repr(" + code + ")",ast_globals)
	code_generated = "		--lua code genrated from file : " + os.path.abspath(file) + "\n\n" + code_generated
	EXPORT_FILE = getEXPORT_FILE(file)
	if export_file != None : 
		EXPORT_FILE = export_file
	if EXPORT_FILE == None :
		print("generated code = \n" ,code_generated)
	else : 
		print(code_generated , file = open(EXPORT_FILE , "w"))
		print("generated file= \n" ,EXPORT_FILE)


if __name__ == '__main__':
	if len(sys.argv) > 1  : transpile_code(sys.argv[1],export_file = None)










