class IOString():
    def __init__(self):
        self.str1 = ''

    def get(self):
        self.str1 = input('Enter string: ')

    def upper(self):
        print(f'The result is: {self.str1.upper()}')


str1 = IOString()
str1.get()
str1.upper()
