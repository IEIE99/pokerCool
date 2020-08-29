NUMBER_of_INSTANCES = 10

class test(object):
    pass

def add_instance(cls,i):
    def instance(self):
        print (str(i**3))
    instance.__doc__ = "docstring for instance%d" % i
    instance.__name__ = "instance%d" % i
    setattr(cls,instance.__name__,instance)

d = test()
for i in range(NUMBER_of_INSTANCES):
    add_instance(test, i)        
    a = str('d.instance'+str(i)+'()')
    exec(a)




add_instance(test,3)

exec(a)

#class deck(object):
 #   pass

#def add_instance(cls,i):
 #   def instance(self):


class SomeObject():
    defined_name = u""

    def __init__(self, def_name=None):
        if def_name == None:
            def_name = u"%s" % (<INSTANCE NAME>)
        self.defined_name = def_name

ThisObject = SomeObject()
print ThisObject.defined_name   # Should print "ThisObject"
