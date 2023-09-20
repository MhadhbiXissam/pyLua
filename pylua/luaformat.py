import sys , subprocess , tempfile , os 

print()






	




def prettyLua(luacode) : 
	result = luacode
	# Create a temporary file
	temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False) 
	# Write data to the temporary file
	temp_file.write(luacode)
	temp_file.flush()
	temp_file_path = temp_file.name
	luaformatter_binary = os.path.join(os.path.split(__file__)[0],"lua-format")
	luaformatter_binary_config = os.path.join(os.path.split(__file__)[0],"lua-format.config")
	cmd = [luaformatter_binary,temp_file_path,"-c" , luaformatter_binary_config ]
	process = subprocess.Popen(
			cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
	)
	output = bytes.decode(process.stdout.read())
	error = bytes.decode(process.stderr.read())
	if error == "": 
		print(error)
		result = output

	temp_file.close()
	return result



