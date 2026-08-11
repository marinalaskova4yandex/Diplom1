import pytest
from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    @pytest.fixture(autouse=True)
    def setup_database(self):
        #Фикстура для инициализации базы данных перед каждым тестом
        self.db = Database()

    def test_database_initialization_buns_count(self):
        #Проверка, что при старте бд создается ровно 3 булки
        buns = self.db.available_buns()
        assert len(buns) == 3

    def test_database_initialization_ingredients_count(self):
        #Проверка, что при старте бд создается ровно 6 ингредиентов
        ingredients = self.db.available_ingredients()
        assert len(ingredients) == 6

    @pytest.mark.parametrize(
        "index, expected_name, expected_price",
        [
            (0, "black bun", 100),
            (1, "white bun", 200),
            (2, "red bun", 300)
        ]
    )
    def test_available_buns_returns_correct_data(self, index, expected_name, expected_price):
        #Параметризованный тест для проверки правильности данных каждой булки
        buns = self.db.available_buns()
        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price

    @pytest.mark.parametrize(
        "index, expected_type, expected_name, expected_price",
        [
            (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (5, INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]
    )
    def test_available_ingredients_returns_correct_data(self, index, expected_type, expected_name, expected_price):
        #Параметризованный тест для проверки всех ингредиентов (соусов и начинок)
        ingredients = self.db.available_ingredients()
        assert ingredients[index].get_type() == expected_type
        assert ingredients[index].get_name() == expected_name
        assert ingredients[index].get_price() == expected_price