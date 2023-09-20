import sys
sys.path.append("./..")
from  pylua import py2lua

code = '''
import m.x
import m.r.t.v as mm
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



ilua("""
local v = (((w > 3)) and 1 or  0 )
""")

'''

if __name__ == '__main__':
	x = py2lua(code)
	print(x)
