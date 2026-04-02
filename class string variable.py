class reverse:
    def __init__(self, s=""):
        self.s = s

    def rev(self):
        return self.s[::-1]


# main program
word = input("Enter a word: ")
obj = reverse(word)
print("Reversed string:", obj.rev())
