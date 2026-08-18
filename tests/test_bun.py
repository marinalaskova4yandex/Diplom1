import pytest
from bun import Bun  

class TestBun:

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100.0),
            ("white bun", 200.50),
            ("red bun", 300.0),
            ("very long name for a burger bun text", 0.0),  # Граничные значения
            ("special bun", -50.0)                         # Проверка отрицательной цены
        ]
    )
    def test_bun_initialization_and_getters(self, name, price):
        # Создаем объект булочки с параметризованными данными
        bun = Bun(name, price)
        
        # Проверяем, что методы возвращают именно те значения, которые мы передали
        assert bun.get_name() == name
        assert bun.get_price() == price