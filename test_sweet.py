import pytest
from sweet_shop import SweetShop

def test_add_sweet():
    shop = SweetShop()
    shop.add_sweet(1,"Rasgulla", "Milk-based", 20.0,20)
    shop.add_sweet(2,"Laddo", "Gram-based", 15.0,15)
    
    sweets = shop.get_all_sweets()
    
    assert len(sweets) == 1
    assert sweets[0]['name'] == "Ladoo"
    
