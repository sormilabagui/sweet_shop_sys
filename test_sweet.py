import pytest
from sweet_shop import SweetShop

def test_add_sweet():
    shop = SweetShop()
    shop.add_sweet(1,"Rasgulla", "Milk-based", 20.0,20)
    shop.add_sweet(2,"Ladoo", "Gram-based", 15.0,15)
    
    sweets = shop.get_all_sweets()
    
    assert len(sweets) == 2
    
    
def test_delete_sweet_valid_id():
    shop = SweetShop()
    shop.add_sweet(1, "Rasgulla", "Milk-based", 20.0, 10)
    shop.add_sweet(2, "Ladoo", "Gram-based", 15.0, 15)

    shop.delete_sweet(1)
    sweets = shop.get_all_sweets()

    assert len(sweets) == 1
    assert sweets[0]['name'] == "Ladoo"

def test_delete_sweet_invalid_id():
    shop = SweetShop()
    shop.add_sweet(1, "Rasgulla", "Milk-based", 20.0, 10)

    with pytest.raises(ValueError, match="No sweet found with ID: 99"):
        shop.delete_sweet(99)

    
