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
        
    def test_size_of_library(self):
        """Library should have a size of
        1 plus the amount of cards contained
        in the collection. 
        """
        lib = Library()
        self.assertEqual(0, lib.size)
        
    def test_init_of_data(self):
        """Library should have dictionary as
        data structure for holding names
        and counts.
        """
        lib = Library()
        self.assertEqual(type({}), type(lib.data))        
    
    def test_is_empty(self):
        """Library should return True if it is
        empty and False if it has at least one card.
        """
        lib = Library()
        self.assertEqual(True, lib.is_empty())
        

if __name__ == '__main__':
    unittest.main()
   
#this tests an empty library
#lib = Library()
#print(lib)