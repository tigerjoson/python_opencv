
# ref :https://stackoverflow.com/questions/625083/what-do-init-and-self-do-in-python

#####self
#the self variable represents the instance of the object itself.
#Most object-oriented languages pass this as a hidden parameter to the methods defined on an object;
#Python does not. You have to declare it explicitly.
#When you create an instance of the A class and call its methods, it will be passed automatically,


##########___init__
#constructor.
# The _init__ method is roughly what represents a constructor in Python.
# When you call A() Python creates an object for you, and passes it as the first parameter to the __init__ method.
# Any additional parameters (e.g., A(24, 'Hello')) will also get passed as arguments--in this case causing an exception to be raised, since the constructor isn't expecting them

class classa:
    def __init__(self):
        self.path = 'default constructor'

    def methoda(self, path):
        self.path = path;
        print(path);
    

A = classa();
A.methoda("c");

 
