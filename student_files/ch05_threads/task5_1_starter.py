"""
        task5_1_starter.py  -   Multi-threaded Pinger

        The multi-threaded pinger should be a class that inherits from Thread,
        passes an address to ping into its constructor.
        The run method within the Pinger class then ping's the URL at the operating system level using a subprocess.

        Helpful hints:
        1. Create a class that inherits from Thread (don't forget to import threading).

        2. Create a constructor that accepts an address to ping.  Save the address as
           a class attribute (self.address = address)

        3. Create the run method and use the subprocess code presented on the slide
           in the materials

        That's it--your solution should work!
"""




addresses = 'www.google.com', 'www.yahoo.com', 'www.im_a_fake_address.com'
for addr in addresses:
    Pinger(addr).start()
