# lua-format : 
## Edit lua format config  : 
*	check (Style config file)[https://github.com/Koihik/LuaFormatter/blob/master/docs/Style-Config.md#style-config-file]



# How to use pylua : 
example : 
```python 
from  pylua import py2lua , python2lua

py = "print(123)"
# this will will use the formatter "LuaFormatter" , which will be reoved in the future versions  
print(py2lua(py))

# this will emit none formated code
print(python2lua(py))




```
