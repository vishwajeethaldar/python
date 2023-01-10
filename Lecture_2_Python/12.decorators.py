# Pyhton Decoratoors 

# in python we an passs one function into another function as parameter 


def announce (f):
    def wrapper():
        print("Function is about to run")
        f()
        print("Function is Completed running")
    return wrapper


@announce
def hello():
    print("Hellow")

hello()