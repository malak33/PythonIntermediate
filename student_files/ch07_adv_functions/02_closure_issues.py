def outer_function():
    x = 3
    
    def my_closure():
        x += 1
        print(x)
    
    my_closure()


outer_function()
