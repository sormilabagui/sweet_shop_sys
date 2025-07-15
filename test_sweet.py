import pytest
from sweet_shop import SweetShop

def test_add_sweet():
    shop = SweetShop()
    shop.add_sweet("Rasgulla", "Milk-based", 20.0)
    
    sweets = shop.get_all_sweets()
    
    assert len(sweets) == 1
    assert sweets[0]['name'] == "Rasgulla"
    assert sweets[0]['category'] == "Milk-based"
    assert sweets[0]['price'] == 20.0
