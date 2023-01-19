# PythonicLua
Transpiler from python to lua 
# INSTALATION : 
```bash
cd $HOME ; git clone "https://github.com/MhadhbiXissam/pythonicLua.git" ; cp $HOME/pythonicLua/pythonicLua/PythonicLua.sublime-syntax $HOME/.config/sublime-text/Packages/User/cp $HOME/pythonicLua/pythonicLua/pythonicLua.sublime-build $HOME/.config/sublime-text/Packages/User/
```

# How to use  : 
## with sublime text : 
*	make the python file with *.pylua extension  
*	choose Build system to "pythonicLua"


# Example  : 

## Python 

```python
x = false
x = {}
x = {"a" : nil , "b" : 6 , "c" : "text"}
x = {a : nil , b : 6 , c : "text"}
x = idict(a = nil , b = 6 , c = "text")
y : local  = 6
for k , v in x : 
	print(k , " = " , v)

i : local = x.a
i = x["a"]

for i in irange(ilen(x)) : 
	print(x[i])

if x >= 2 : 
	if y != false and 1 <= x < 6 : 
		print("-")
	elif y == 2  : 
		print("+")
	else : 
		print(0)
else : 
	print("oops")

def print(x,i) : 
	return x + 1 

def print(x,i) ->local : 
	return x + 1 

def print(x,i) ->lvar : 
	return x + 1 

def print(x,i) ->gvar : 
	return x + 1 


if not x : 
	print("not x ")


v : local  = 1 if w > 3 else 0

import m.x
import m.r.t.v as mm

ilua("""
local v = (((w > 3)) and 1 or  0 )
""")

```


```lua
x = false
x = {}
x = {"a" = nil,"b" = 6,"c" = "text"}
x = {a = nil,b = 6,c = "text"}
x = { a = nil,b = 6,c = "text"}
local y = 6
for k , v in pairs(x) do
    print(k," = ",v)
end 
local i = x.a
i = x["a"]
for i = 1,#x,1 do
    print(x[i])
end 
if (x >= 2) then 
    if ( (y ~= false) and ( (1 <= x) and ( x < 6  ) ) ) then 
        print("-")
    elseif (y == 2) then 
        print("+")
    else 
       print(0)
   end
else 
   print("oops")
end
function print(x,i)
    return x + 1
end
local function print(x,i)
    return x + 1
end
local print = function (x,i)
    return x + 1
end
print = function (x,i)
    return x + 1
end
if (not x) then 
    print("not x ")
end
local v = (((w > 3)) and 1 or  0 )
require "m.x"
local mm  = require("m.r.t.v")

local v = (((w > 3)) and 1 or  0 )
```


