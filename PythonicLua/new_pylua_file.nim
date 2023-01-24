import nimpy
import os
let py = pyBuiltinsModule()
let c = paramCount()
var has_arg : bool  = false
if c > 0  :
    has_arg = true

var arg_path = paramStr(1)
var compile_files = "path = \"" & arg_path & "\"\n"
compile_files = compile_files & """
import os
path = path.strip()
cwd = os.getcwd()
new_file_path = "." + path + ".pylua"
default_code = ""
if path.endswith(".script") : 
    default_code = "def init(self) : \n\tpass\n\n\ndef final(self) : \n\tpass\n\n\ndef update(self, dt) : \n\tpass\n\n\ndef fixed_update(self, dt) : \n\tpass\n\n\ndef on_message(self, message_id, message, sender) : \n\tpass\n\n\ndef on_input(self, action_id, action) : \n\tpass\n\n\ndef on_reload(self) : \n\tpass\n"
if path.endswith(".lua") : 
    default_code = "M : local = {}\n\n# private\nmessage : local = \"Hello world!\"\n\ndef M.hello() : \n\tprint(message)\n\n\nreturn M"

if not os.path.exists(new_file_path) : 
    print(default_code, file = open(new_file_path,"w"))
else : 
    raise Exception("info : file already exists......")






"""
try:
    discard py.exec(compile_files)
except :
    let msg = getCurrentExceptionMsg()
    echo msg
