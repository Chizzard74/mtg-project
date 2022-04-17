import unittest
from main import Library

        
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
        
    def test_validate_name(self):
        """Name validator should return true if a 
        card exists, and false otherwise.
        """
        lib = Library()
        self.assertEqual(True, lib.validate_name("The Wandering Emperor"))
        self.assertEqual(False, lib.validate_name("Bob"))
        self.assertEqual(True, lib.validate_name("Kaito Shizuki"))
        
    def test_add_one(self):
        """Add the first card into the dictionary.
        """
        lib = Library()
        lib.add("The Wandering Emperor")
        print(lib)
        self.assertEqual(True, "The Wandering Emperor" in lib.data)
        
    def test_size_after_add(self):
        """Size of library should be 1 after adding one card.
        """
        lib = Library()
        lib.add("The Wandering Emperor")
        self.assertEqual(1, lib.size)
        
    def test_add_two(self):
        """Adding two cards should increase their count.
        """
        lib = Library()
        lib.add("The Wandering Emperor")
        lib.add("The Wandering Emperor")
        self.assertEqual(2, lib.size)
        self.assertEqual(2, lib.data["The Wandering Emperor"])
        

if __name__ == '__main__':
    unittest.main()
   
#this tests an empty library
#lib = Library()
#print(lib)