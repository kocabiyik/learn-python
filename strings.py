class String:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return self.string[::-1]

    def string_list_reversed(self):
        return list(reversed(self.string))

s = String("quick fox jumps over the lazy dog")

print('Reversed:', s.reverse())
print('Reversed in list:', s.string_list_reversed())
