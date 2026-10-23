import time, sys

indent = 0 # количество пробелов для отступа
indentIncreasing = True # увеличение или уменьшение отступа

try:
    while True: # главный цикл программы
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # пауза длительностью 1/10 секунды

        if indentIncreasing:
            # Увеличение количества пробелов
            indent = indent + 1
            if indent == 20:
                # Изменение направления
                indentIncreasing = False
        else:
            # Уменьшение количества пробелов
            indent = indent - 1
            if indent == 0:
                # Изменение направления
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()