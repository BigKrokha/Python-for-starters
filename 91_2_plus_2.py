
class two(int):
    def __add__(self, a):
        return super().__add__(a+1)

sec = two(2)
print(sec+2)

#5