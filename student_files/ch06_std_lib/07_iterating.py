class Something:
    def __init__(self, min=0, max=100):
        self.count = min
        self.max = 100

    def __next__(self):
        val = self.count
        self.count += 1
        if self.count > self.max:
            raise StopIteration
        return val

    def __iter__(self):
        return self

for i in Something():
    print(i)
