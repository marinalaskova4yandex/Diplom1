import pytest
from unittest.mock import Mock
from burger import Burger


class TestBurger:

    def test_set_buns_sets_bun_correctly(self):
        #Проверка установки булочки в бургер
        burger = Burger()
        mock_bun = Mock()  # Создаем мок булочки
        
        burger.set_buns(mock_bun)
        
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_to_list(self):
        #Проверка добавления ингредиента в список бургера
        burger = Burger()
        mock_ingredient = Mock()  # Создаем мок ингредиента
        
        burger.add_ingredient(mock_ingredient)
        
        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_removes_by_index(self):
        #Проверка удаления ингредиента из списка по индексу
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        
        burger.remove_ingredient(0)
        
        assert len(burger.ingredients) == 0

    def test_move_ingredient_changes_elements_order(self):
        #Проверка перемещения ингредиента на другую позицию
        burger = Burger()
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        
        # Меняем их местами
        burger.move_ingredient(0, 1)
        
        assert burger.ingredients[0] == mock_ing2
        assert burger.ingredients[1] == mock_ing1

    def test_get_price_calculates_total_cost_correctly(self):
        #Проверка расчета итоговой стоимости бургера 
        burger = Burger()
        
        # Настраиваем мок булочки, чтобы get_price() возвращал 100.0
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100.0
        
        # Настраиваем моки ингредиентов
        mock_ing1 = Mock()
        mock_ing1.get_price.return_value = 50.0
        
        mock_ing2 = Mock()
        mock_ing2.get_price.return_value = 30.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)

        # Ожидаемая цена: (цена булки * 2) + цена всех ингредиентов
        expected_price = (100.0 * 2) + 50.0 + 30.0
        
        assert burger.get_price() == expected_price

    def test_get_receipt_returns_correct_format(self):
        #Проверка генерации текстового чека 
        burger = Burger()
        
        # Мок булочки возвращает имя и цену
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100.0
        
        # Мок ингредиента возвращает тип, имя и цену
        mock_ing = Mock()
        mock_ing.get_type.return_value = "SAUCE"
        mock_ing.get_name.return_value = "hot sauce"
        mock_ing.get_price.return_value = 50.0

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing)

        receipt = burger.get_receipt()
        
        # Проверяем наличие всех ключевых строк в чеке
        assert "(==== black bun ====)" in receipt
        assert "= sauce hot sauce =" in receipt  
        assert "Price: 250.0" in receipt


# Параметризация для чека 
@pytest.mark.parametrize(
    "ingredient_type, ingredient_name, expected_line",
    [
        ("SAUCE", "chili sauce", "= sauce chili sauce ="),
        ("FILLING", "cutlet", "= filling cutlet =")
    ]
)
def test_get_receipt_formats_different_ingredient_types(ingredient_type, ingredient_name, expected_line):
    #Параметризованный тест для проверки разных типов ингредиентов в чеке
    burger = Burger()
    
    mock_bun = Mock()
    mock_bun.get_name.return_value = "white bun"
    mock_bun.get_price.return_value = 0.0
    
    mock_ing = Mock()
    mock_ing.get_type.return_value = ingredient_type
    mock_ing.get_name.return_value = ingredient_name
    mock_ing.get_price.return_value = 0.0

    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ing)
    
    receipt = burger.get_receipt()
    assert expected_line in receipt