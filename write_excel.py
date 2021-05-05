import pandas as pd

class write_excel:

    # Метод для сохранения данных в data.xlsx
    def write_excel(list_product, list_features, list_money):
        # Запись в словарь,через функцию DataFrame
        book = pd.DataFrame({
            'Продукт': list_product,
            'Модели': list_features,
            'Цена (руб)': list_money,
        })

        # Записываем данные в data.xlsx
        writer = pd.ExcelWriter('data.xlsx')
        book.to_excel(writer)
        writer.save()
