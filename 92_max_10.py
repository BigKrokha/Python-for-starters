
class Max10(list):
    def __init__(self, a):
        if len(a) > 10:
            print('>10 нельзя')
        else:
            super().__init__(a)

    def append(self,a):
        if len(self) == 10:
            print('>10 нельзя')
        else:
            super().append(a)


out = Max10([0,1,2,3,4,5,6,7,8,9])
print(out)

out.append(10)
print(out)
