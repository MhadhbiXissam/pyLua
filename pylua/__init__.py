from .lua import python2lua
from .luaformat import prettyLua



def py2lua(pythoncode) : 
	luacode = python2lua(pythoncode)
	return prettyLua(luacode)