import unittest
import time
from main import Library

class TestLibrary(unittest.TestCase):

    def test_startup():    
        print("testing")
        print("start")
        print("Completed")
        
    def test_initialize_library(self):
        """Check for a Library.
        """
        try:
            Library()
        except NameError:
            self.fail("Library Does Not Exist :(")
        
    def test_size(self):
        """Library should have 
        """

    if __name__ == '__main__':
        unittest.main()
   
#this tests an empty library
#lib = Library()
#print(lib)