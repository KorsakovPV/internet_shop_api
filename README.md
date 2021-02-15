# internet_shop_api

Техническое задание

1. Используя фреймворк Django реализовать RESTful api.

2. Реализовать сущности:

- Товары,
- Категории,
- Товар-Категория.

3 Реализовать выдачу данных в формате json по RESTful:

- Создание товаров (у каждого товара может быть от 2х до 10 категорий),
- Редактирование товаров,
- Удаление товаров (товар помечается как удаленный),
- Создание категорий,
- Удаление категорий (вернуть ошибку если категория прикреплена к товару)
- Получение списка товаров:
  
    а. Имя / по совпадению с именем,

    b. id категории,

    c. Назначение категории / по совпадению с категорией,

    d. Цена от - до,

    e. Опубликованный да / нет,

    f. Не удаленные.

4. Добавить юнит тесты с использованием mock объектов для тестирования методов api (можно для одного метода)




