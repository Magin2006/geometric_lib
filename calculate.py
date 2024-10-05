import circle  # Импортирует модуль для работы с окружностями
import square  # Импортирует модуль для работы с квадратами

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
    """Вычисляет и выводит результат функции для заданной фигуры."""
    assert fig in figs  # Проверка допустимости фигуры
    assert func in funcs  # Проверка допустимости функции

    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    # Получение допустимого имени фигуры
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    # Получение допустимого имени функции
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    # Получение размеров фигуры
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

    calc(fig, func, size)
