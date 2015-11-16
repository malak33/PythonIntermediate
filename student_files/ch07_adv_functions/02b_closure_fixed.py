def outer_function():
    x = [3]
    
    def my_closure():
        x[0] += 1
        print(x[0])
    
    my_closure()


outer_function()
