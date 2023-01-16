import json





class BuiltInLua : 
	def ilua(args,keywords) : 
		return json.loads(repr(args[0]))

	def irange(args,keywords) :
		if len(args) == 1  : 
			return "1," + repr(args[0]) + ",1" 
		if len(args) == 2  : 
			return repr(args[0])  + "," + repr(args[1])  + ",1"
		if len(args) == 3  : 
			return repr(args[0])  + "," + repr(args[1])  + "," + repr(args[2]) 

	def ilua(args,keywords) : 
		return json.loads(repr(args[0]))

	def ilen(args,keywords) : 
		return "#" + repr(args[0])

	def idict(args,keywords) : 
		return "{ "  + ",".join([repr(k) for k in keywords ])  + "}"

	def get_func(self,func) : 
		for i in dir(BuiltInLua) : 
			if i.startswith("i") : 
				if func == i  : 
					return i  
		return None