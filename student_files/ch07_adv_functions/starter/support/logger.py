"""
            logger.py   -   Use this module to define a decorator that will be used to
                            decorate the methods of the main module (get_location())
                            to indicate when the methods are called.


    Instructions:
    ------------
    1. Define a logger below.  Include the following steps:
        a) import logging
        b) create a logger calling getLogger()
        c) set the default logging level invoking your logger's setLevel(logging.DEBUG)
        d) define a handler and formatter as follows:
            handler1 = logging.FileHandler('./logfile.log')
            formatter = logging.Formatter(fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M:%S')
            handler1.setFormatter(formatter)
            my_logger.addHandler(handler1)

    2. Create a function that will serve as the decorator.  Call it log().
       Within the decorator, add a function that will log calls to any function.
       Use the following format as a suggestion:
       def log(func):
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            <your_logger_name>.info('{0} called passing args: {1}'.format(func.__name__, ' '.join([str(arg) for arg in args[1:]])))
            return ret
        return wrapper


    3. Open the task7_1_starter.py module, import this (logger.py) module and add the decorator to
       all of the method within the the file.

    4. Run and test this solution.
"""

