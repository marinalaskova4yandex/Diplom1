import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
            (INGREDIENT_TYPE_FILLING, "cutlet", 150.50),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 0.0),        # Граничное значение цены
            (INGREDIENT_TYPE_FILLING, "dinosaur meat", -10.0), # Проверка отрицательного значения
            ("UNKNOWN_TYPE", "exotic ingredient", 500)         # Невалидный тип даных
        ]
    )
    def test_ingredient_initialization_and_getters(self, ingredient_type, name, price):
        #Параметризованный тест для проверки данных
        # Создаем объект ингредиента с тестовыми данными
        ingredient = Ingredient(ingredient_type, name, price)
        
        # Проверяем, что геттеры возвращают именно те значения, которые были переданы в конструктор
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price