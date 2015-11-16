def outer_function():
    x = 3

    def my_closure():
        print(x)

    my_closure()

outer_function()

# these aren't valid
my_closure()
outer_function.myClosure()
