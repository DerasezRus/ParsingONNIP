class write_txt:

    # Метод, для добавления информации в data.txt
    def write_txt(list_product, list_features, list_money, count, ready_dictionary):
        # Открываем файл
        with open('data.txt', 'a') as f:
            # Цикл для записи в словарь данных
            for i in range(count):
                # Запись в словарь
                ready_dictionary = ({
                    'Продукст - ': list_product[i],
                    'Модель - ': list_features[i],
                    'Цена (руб) - ': int(list_money[i]),
                })
                # Запись в файл data.txt
                f.write(f'{ready_dictionary}''\n')