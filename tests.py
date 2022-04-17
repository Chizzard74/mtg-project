import unittest
import time
from main import Library

def test_startup():    
        print("testing")
        print("start")
        print("Completed")
        
class TestLibrary(unittest.TestCase):    
        
    def test_initialize_library(self):
        """Check for a Library.
        """
        try:
            Library()
        except NameError:
            self.fail("Library Does Not Exist :(")
        
    ## def test_size_of_library(self):
    #     """Library should have a size of
    #     1 plus the amount of cards contained
    #     in the collection. 
    #     """
    #     lib = Library()
    #     self.assertEqual(0, lib.size)
        

if __name__ == '__main__':
    unittest.main()
   
#this tests an empty library
#lib = Library()
#print(lib)