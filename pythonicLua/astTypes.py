import json , ast 


def Store() : 
	return "Store"

def Load() : 
	return "Load"



class Module : 
	def __init__(self,body = list() , type_ignores  = [] ) : 
		self.body = body
		self.type_ignores = type_ignores

class Name : 
	def __init__(self , id,ctx) : 
		self.id = id 
		self.ctx = ctx 


class Assign : 
	def __init__(self , targets ,value ,  type_comment=None  ) : 
		self.targets = targets
		self.value = value
		self.type_comment = type_comment





class Constant : 
	def __init__(self , value, kind = None) : 
		self.value = value
		self.kind = kind



class arg  : 
	def __init__(self,arg, annotation=None, type_comment=None) : 
		self.arg = arg
		self.annotation = annotation
		self.type_comment = type_comment



class arguments : 
	def __init__(self,posonlyargs=[] , args = [] , vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults = [] ) : 
		self.posonlyargs = posonlyargs
		self.args = args
		self.vararg = vararg
		self.kwonlyargs = kwonlyargs
		self.kw_defaults = kw_defaults
		self.kwarg = kwarg
		self.defaults = defaults


class Return : 
	def __init__(self,value) : 
		self.value = value





class FunctionDef : 
	def __init__(self,name , args = [] ,  body = [] , decorator_list=[], returns=None, type_comment=None) : 
		self.name = name
		self.args = args
		self.body = body
		self.decorator_list = decorator_list
		self.returns = returns
		self.type_comment = type_comment



class Eq : 
	def __init__(self) : 
		pass

class NotEq :
	def __init__(self) : 
		pass


class Add : 
	def __init__(self) : 
		pass

class Mult : 
	def __init__(self) : 
		pass

class Sub : 
	def __init__(self) : 
		pass


class BinOp : 
	def __init__(self,left , op, right) : 
		self.left = left
		self.op = op
		self.right = right



class Call : 
	def __init__(self,func , args , keywords) : 
		self.func = func
		self.args = args
		self.keywords = keywords



class Expr : 
	def __init__(self,value) : 
		self.value = value

class Dict : 
	def __init__(self,keys ,values  ) : 
		self.keys = keys
		self.values = values


class GtE : 
	def __init__(self) : 
		pass


class LtE : 
	def __init__(self) : 
		pass


class Lt : 
	def __init__(self) : 
		pass


class Gt : 
	def __init__(self) : 
		pass



class Compare : 
	def __init__(self , left, ops, comparators ) : 
		self.left = left
		self.ops = ops
		self.comparators = comparators



class If : 
	def __init__(self,test,body , orelse) : 
		self.test = test
		self.body = body
		self.orelse = orelse





class And : 
	def __init__(self) : 
		pass	

class Or : 
	def __init__(self) : 
		pass



class Not : 
	def __init__(self) : 
		pass


class Break  : 
	def __init__(self) : 
		pass


class BoolOp : 
	def __init__(self,op, values = []) : 
		self.op = op
		self.values = values


class IfExp : 
	def __init__(self,test,body,orelse) : 
		self.test = test
		self.body = body
		self.orelse = orelse


class Attribute : 
	def __init__(self,value, attr , ctx ) : 
		self.value = value
		self.attr = attr
		self.ctx = ctx

class AnnAssign : 
	def __init__(self , target ,annotation , value = None ,  simple  = 1  ) : 
		self.target = target
		self.annotation = annotation
		self.value = value
		self.simple = simple



class keyword : 
	def __init__(self,arg,value) : 
		self.arg = arg
		self.value = value


class For : 
	def __init__(self,target,iter,body , orelse=[], type_comment=None) : 
		self.target = target
		self.iter = iter
		self.body = body
		self.orelse = orelse
		self.type_comment = type_comment



class Lambda : 
	def __init__(self,args,body) : 
		self.args = args
		self.body = body

class Tuple : 
	def __init__(self,elts,ctx) : 
		self.elts = elts
		self.ctx = ctx


class Set : 
	def __init__(self,elts) : 
		self.elts = elts

class Dict : 
	def __init__(self,keys,values) : 
		self.keys = keys
		self.values = values

class List : 
	def __init__(self,elts,ctx) : 
		assert(len(elts) == 1 )
		self.elts = elts
		self.ctx = ctx




class Pass : 
	def __init__(self)  : 
		pass

class UnaryOp : 
	def __init__(self,op,operand)  : 
		self.op = op 
		self.operand = operand


class AugAssign : 
	def __init__(self,target,op,value)  : 
		self.target = target 
		self.op = op
		self.value = value



class Subscript : 
	def __init__(self,value,slice,ctx)  : 
		self.value = value 
		self.slice = slice
		self.ctx = ctx

class Index : 
	def __init__(self,value)  : 
		self.value = value 
		self.slice = slice



class Import : 
	def __init__(self,names) : 
		self.names = names

class alias : 
	def __init__(self,name,asname = None) : 
		self.name = name
		self.asname = asname


class IfExp : 
	def __init__(self,test,body,orelse) : 
		self.test = test
		self.body = body
		self.orelse = orelse


