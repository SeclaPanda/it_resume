class Counter:
    value = 0
    def __init__(self):
        type(self).value = 0
    @classmethod
    def inc(cls):
        cls.value += 1
        return cls.value
    
    @classmethod
    def dec(cls):
        cls.value -= 1
        return cls.value

class NonDecreasingCounter(Counter):
    def __init__(self):
        super().__init__()
    @classmethod
    def dec(cls):
        return cls.value

cntr = NonDecreasingCounter()
print(cntr.inc())
print(cntr.inc())
print(cntr.dec())