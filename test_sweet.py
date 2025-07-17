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

def test_search_sweets_by_category():
    shop = SweetShop()
    shop.add_sweet(1, "Rasgulla", "Milk-based", 20.0, 10)
    shop.add_sweet(2, "Ladoo", "Gram-based", 15.0, 5)
    shop.add_sweet(3, "Barfi", "Milk-based", 25.0, 7)

    results = shop.search_sweets_by_category("Milk-based")
    
    assert len(results) == 2
    assert results[0]['name'] == "Rasgulla"
    assert results[1]['name'] == "Barfi"

def test_search_sweets_by_price_range():
    shop = SweetShop()
    shop.add_sweet(1, "Rasgulla", "Milk-based", 20.0, 10)
    shop.add_sweet(2, "Ladoo", "Gram-based", 15.0, 5)
    shop.add_sweet(3, "Barfi", "Milk-based", 25.0, 7)
    shop.add_sweet(4, "Jalebi", "Sugar-based", 30.0, 4)

    results = shop.search_sweets_by_price_range(15.0, 25.0)
    
    assert len(results) == 3
    assert results[0]['name'] == "Rasgulla"
    assert results[1]['name'] == "Ladoo"
    assert results[2]['name'] == "Barfi"

def test_sort_sweets_by_price():
    shop = SweetShop()
    shop.add_sweet(1, "Rasgulla", "Milk-based", 25.0, 15)
    shop.add_sweet(2, "Ladoo", "Gram-based", 15.0, 10)
    shop.add_sweet(3, "Barfi", "Milk-based", 20.0, 20)

    sorted_sweets = shop.sort_sweets_by_price()
    prices = [sweet['price'] for sweet in sorted_sweets]

    assert prices == sorted(prices)

def test_sort_sweets_by_quantity():
    shop = SweetShop()
    shop.add_sweet(1, "Rasgulla", "Milk-based", 25.0, 15)
    shop.add_sweet(2, "Ladoo", "Gram-based", 15.0, 10)
    shop.add_sweet(3, "Barfi", "Milk-based", 20.0, 20)

    sorted_sweets = shop.sort_sweets_by_quantity()
    quantities = [sweet['qty'] for sweet in sorted_sweets]

    assert quantities == sorted(quantities)

def test_purchase_sweet_success():
    shop = SweetShop()
    shop.add_sweet(1, "Rasgulla", "Milk-based", 25.0, 15)

    shop.purchase_sweet(1, 5)
    sweets = shop.get_all_sweets()

    assert sweets[0]['qty'] == 10


def test_purchase_sweet_insufficient_stock():
    shop = SweetShop()
    shop.add_sweet(2, "Ladoo", "Gram-based", 15.0, 5)

    with pytest.raises(ValueError, match="Not enough stock for sweet ID: 2"):
        shop.purchase_sweet(2, 10)

def test_restock_sweet():
    shop = SweetShop()
    shop.add_sweet(1, "Barfi", "Milk-based", 25.0, 5)

    shop.restock_sweet(1, 10)
    sweets = shop.get_all_sweets()

    assert sweets[0]['qty'] == 15

def test_add_sweet_duplicate_id():
    shop = SweetShop()
    shop.add_sweet(1001, "Kaju Katli", "Nut-based", 20.0, 30)
    with pytest.raises(ValueError, match="Sweet ID 1001 already exists."):
        shop.add_sweet(1001, "Duplicate", "Error-based", 10.0, 10)

