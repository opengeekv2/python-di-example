from inspect import getfullargspec, ismethod, isawaitable

def createContainer():
    def container(contents: dict={}, memory: dict={}):
        if not contents:
            contents = memory
        else:
            memory.update(contents)
        
        def dec_inject(func):
            
            def wrapper(*args, **kwargs):
                to_inject = func
                if ismethod(func):
                    to_inject = func.__func__
                argspec = getfullargspec(to_inject).args
                if len(argspec) == len(args):
                    return func(*args, **kwargs)
                arglist = list(args)
                for arg in argspec:
                    parameter_to_inject = contents.get(arg, None)
                    if parameter_to_inject:
                        arglist.append(parameter_to_inject)
                if isawaitable(func):
                    
                    async def tmp():
                        return (await func(*(arglist), **kwargs))
                    
                    return tmp()
                
                return func(*(arglist), **kwargs)
            
            return wrapper
        
        return dec_inject
    return container

if not 'container' in locals():
    container = createContainer()
inject = container()
