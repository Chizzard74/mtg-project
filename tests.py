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
        
    # def test_size_of_library(self):
    #     """Library should have a size of
    #     1 plus the amount of cards contained
    #     in the collection. 
    #     """
    #     lib = Library()
    #     self.assertEqual(0, lib.size)
        
    # def test_init_of_data(self):
    #     """Library should have dictionary as
    #     data structure for holding names
    #     and counts.
    #     """
    #     lib = Library()
    #     self.assertEqual(type({}), type(lib.data))        
    
    # def test_is_empty(self):
    #     """Library should return True if it is
    #     empty and False if it has at least one card.
    #     """
    #     lib = Library()
    #     self.assertEqual(True, lib.is_empty())
        
    # def test_validate_name(self):
    #     """Name validator should return true if a 
    #     card exists, and false otherwise.
    #     """
    #     lib = Library()
    #     self.assertEqual(True, lib.validate_name("The Wandering Emperor"))
    #     self.assertEqual(False, lib.validate_name("Bob"))
    #     self.assertEqual(True, lib.validate_name("Kaito Shizuki"))
        
    # def test_add_one(self):
    #     """Add the first card into the dictionary.
    #     """
    #     lib = Library()
    #     lib.add("The Wandering Emperor")
    #     print(lib)
    #     self.assertEqual(True, "The Wandering Emperor" in lib.data)
        
    # def test_size_after_add(self):
    #     """Size of library should be 1 after adding one card.
    #     """
    #     lib = Library()
    #     lib.add("The Wandering Emperor")
    #     self.assertEqual(1, lib.size)
        
    # def test_add_two(self):
    #     """Adding two cards should increase their count.
    #     """
    #     lib = Library()
    #     lib.add("The Wandering Emperor")
    #     lib.add("The Wandering Emperor")        
    #     self.assertEqual(2, lib.size)
    #     self.assertEqual(2, lib.data["The Wandering Emperor"])
        
    # def test_size_after_two(self):
    #     """size of library should be two when two cards are added.
    #     """
    #     card = "The wandering emperor"
    #     lib = Library()
    #     lib.add(card)
    #     self.assertEqual(1, lib.size)
    #     lib.add(card)
    #     self.assertEqual(2, lib.size)
    
    # def test_random_kami(self):
    #     """Random Kami function should return
    #     a valid card name in the set.
    #     """
    #     lib = Library()
    #     name = lib.get_random_kami()
    #     self.assertEqual(True, lib.validate_name(name))
        
    # def test_show_library(self):
    #     """Show library should show the output of
    #     the data.
    #     """
    #     lib = Library()
    #     for _ in range (5):
    #         lib.add(lib.get_random_kami())        
    #     self.assertEqual(True, lib.show_library())
    
    # def test_clear(self):
    #     """Clear function should set size back to 0
    #     and remove all items from the dict.
    #     """
    #     lib = Library()
    #     lib.add("The Wandering Emperor")
    #     self.assertEqual(1, lib.size)
    #     lib.add("Kaito Shizuki")
    #     self.assertEqual(2, lib.size)
    #     lib.clear()
    #     self.assertEqual(0, lib.size)
        
    # def test_get_name(self):
    #     """Retrieve a card from the database should
    #     return the card name, or false.
    #     """
    #     lib = Library()
    #     lib.add("The Wandering Emperor")
    #     chioce = lib.get_name()
    #     self.assertEqual("The Wandering Emperor", chioce)
    #     self.assertEqual(True, "BOB" != chioce)
    
    def test_remove_one(self):
        """Removing one card from the 
        database. Size should be zero and 
        Library should be empty.
        """
        lib = Library()
        name = "Kaito Shizuki"
        lib.add(name)
        self. assertEqual(1, lib.size)
        lib.remove(name)
        self.assertEqual(0, lib.size)
    
    

        
if __name__ == '__main__':
    unittest.main()
   
#this tests an empty library
#lib = Library()
#print(lib)