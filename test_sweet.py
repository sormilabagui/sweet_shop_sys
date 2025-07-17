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

    
def test_get_all_sweets():
    shop = SweetShop()
    shop.add_sweet(1, "Rasgulla", "Milk-based", 20.0, 10)
    shop.add_sweet(2, "Ladoo", "Gram-based", 15.0, 15)

    sweets = shop.get_all_sweets()

    expected = [
        {'id': 1, 'name': 'Rasgulla', 'category': 'Milk-based', 'price': 20.0, 'qty': 10},
        {'id': 2, 'name': 'Ladoo', 'category': 'Gram-based', 'price': 15.0, 'qty': 15}
    ]

    assert sweets == expected

def test_search_sweets_by_name():
    shop = SweetShop()
    shop.add_sweet(1, "Rasgulla", "Milk-based", 20.0, 10)
    shop.add_sweet(2, "Ladoo", "Gram-based", 15.0, 15)

    result = shop.search_sweets_by_name("Rasgulla")
    
    assert len(result) == 1
    assert result[0]['name'] == "Rasgulla"

def test_search_sweet_by_id():
    shop = SweetShop()
    shop.add_sweet(1, "Rasgulla", "Milk-based", 20.0, 10)
    shop.add_sweet(2, "Ladoo", "Gram-based", 15.0, 15)

    result = shop.search_sweet_by_id(2)

    assert result['name'] == "Ladoo"
    assert result['category'] == "Gram-based"
    assert result['price'] == 15.0
    assert result['qty'] == 15
