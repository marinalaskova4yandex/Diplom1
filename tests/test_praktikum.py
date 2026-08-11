import io
import sys
import runpy  
from praktikum import main


def test_main_execution_and_output(capsys):
    #Тест проверяет полную сборку бургера и вывод чека.

    # Запускаем главную функцию 
    main()

    # Перехватываем всё, что функция вывела в консоль через print()
    captured = capsys.readouterr()

    # Проверяем, что в итоговом чеке присутствуют правильные ингредиенты и цена
    assert "(==== black bun ====)" in captured.out
    assert "Price: 700" in captured.out  
    assert "= sauce sour cream =" in captured.out
    assert "= filling dinosaur =" in captured.out


def test_script_execution_block(capsys):    
    runpy.run_module("praktikum", run_name="__main__")
    
    captured = capsys.readouterr()
    assert "Price: 700" in captured.out