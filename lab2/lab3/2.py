class StringManipulator:
    def getString(self):
        self.input_string = input("Введите строку: ")

    def printString(self):
        print(self.input_string.upper())

if __name__ == "__main__":
    sm = StringManipulator()
    sm.getString()
    sm.printString()
