from calculate import calc
import pytest
from math import pi as pi

@pytest.mark.parametrize('size, expected, is_correct', [
        ({2}, 4, True),
        ({3}, 9, True),
        ({4}, 16, True), 
        ({16}, 4, False)
        
    ])
def test_area_square(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('square', 'area', size)
    else:
        assert expected != calc('square', 'area', size)
    

@pytest.mark.parametrize('size, expected, is_correct', [
        ({3}, 12, True),
        ({6}, 12, False),
        ({3}, 12, True),
        ({52}, 666, False)
])
def test_perimeter_square(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('square', 'perimeter', size)
    else:
        assert expected != calc('square', 'perimeter', size)


@pytest.mark.parametrize('size, expected, is_correct', [
        ({3, 4, 5}, 6, True),
        ({10, 20, 30}, 6, False),
        ([52, 52, 52], 156, False),
        ({6, 8, 10}, 24, True)
])
def test_area_triangle(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('triangle', 'area', size)
    else:
        assert expected != calc('triangle', 'area', size)

@pytest.mark.parametrize('size, expected, is_correct', [
        ({2, 4, 10}, 16, True),
        ({28, 2, 1}, 32, False),
        ({100, 200, 300}, 600, True),
        ({4, 5, 6}, 15, True)
])

def test_perimeter_triangle(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('triangle', 'perimeter', size)
    else:
        assert expected != calc('triangle', 'perimeter', size)



@pytest.mark.parametrize('size, expected, is_correct', [
        ({2,6}, 16, True),
        ({7, 9}, 31, False),
        ({100, 200}, 600, True),
        ({52, 1488}, 228, False)
])

def test_perimeter_rectangle(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('rectangle', 'perimeter', size)
    else:
        assert expected != calc('rectangle', 'perimeter', size)


@pytest.mark.parametrize('size, expected, is_correct', [
        ({2,6}, 12, True),
        ({7, 9}, 64, False),
        ({100, 200}, 20000, True),
        ({52, 1488}, 1337, False)
])


def test_area_rectangle(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('rectangle', 'area', size)
    else:
        assert expected != calc('rectangle', 'area', size)


@pytest.mark.parametrize('size, expected, is_correct', [
        ({3}, 6*pi, True),
        ({4}, 88*pi, False),
        ({6}, 12*pi, True),
        ({10}, 10*pi, False)
])


def test_perimeter_circle(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('circle', 'perimeter', size)
    else:
        assert expected != calc('circle', 'perimeter', size)


@pytest.mark.parametrize('size, expected, is_correct', [
        ({2}, 4*pi, True),
        ({7}, 52, False),
        ({20}, 400*pi, True),
        ({30}, 228*pi, False)
])


def test_area_circle(size, expected, is_correct):
    if (is_correct):
        assert expected == calc('circle', 'area', size)
    else:
        assert expected != calc('circle', 'area', size)
