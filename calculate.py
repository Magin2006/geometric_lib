import circle
import square
import triangle
import rectangle

figs = ['circle', 'square', 'triangle', 'rectangle']
funcs = ['perimeter', 'area']
sizes = {
    'perimeter-circle': 1,
    'area-circle': 1,
    'perimeter-square': 1,
    'area-square': 1,
    'perimeter-rectangle': 2,
    'area-rectangle': 2,
    'perimeter-triangle': 3,
    'area-triangle': 3,
}

def calc(fig, func, size):
    if any(isinstance(s, str) for s in size):
        return

    elif all(int(s) > 0 for s in size):
        assert fig in figs
        assert func in funcs

        result = eval(f'{fig}.{func}(*{size})')
        return result
    else:
        print("Sizes must be > 0")


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

    result = calc(fig, func, size)
    print(result)
