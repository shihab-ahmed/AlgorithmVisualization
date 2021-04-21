# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = None
  def setName(self,name):
      self.lastname = name
  def printname(self):
    print(self.firstname, self.lastname)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def some(x):
    x.printname()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = Person("John", "Doe")
    x.lastname="sss"
    x.printname()
    some(x)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
