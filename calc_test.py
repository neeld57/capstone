import pytest
from calc import add, subtract, divide, multiply

def test_add_1():
    event = {}
    event["number1"] = -1
    event["number2"] = -1
    assert add(event) == -2

def test_add_2():
    event = {}
    event["number1"] = -30
    event["number2"] = 0
    assert add(event) == -30


def test_add_3():
    event = {}
    event["number1"] = -99
    event["number2"] = 5
    assert add(event) == -94


def test_add_4():
    event = {}
    event["number1"] = 0
    event["number2"] = -312
    assert add(event) == -312


def test_add_5():
    event = {}
    event["number1"] = 0
    event["number2"] = 0
    assert add(event) == 0


def test_add_6():
    event = {}
    event["number1"] = 0
    event["number2"] = 54
    assert add(event) == 54


def test_add_7():
    event = {}
    event["number1"] = 643
    event["number2"] = -2
    assert add(event) == 641


def test_add_8():
    event = {}
    event["number1"] = 79
    event["number2"] = 0
    assert add(event) == 79


def test_add_9():
    event = {}
    event["number1"] = 63
    event["number2"] = 84
    assert add(event) == 147

def test_subtract_1():
    event = {}
    event["number1"] = -56
    event["number2"] = -51
    assert subtract(event) == -5

def test_subtract_2():
    event = {}
    event["number1"] = -65
    event["number2"] = 0
    assert subtract(event) == -65

def test_subtract_3():
    event = {}
    event["number1"] = -268
    event["number2"] = 34
    assert subtract(event) == -302

def test_subtract_4():
    event = {}
    event["number1"] = 0
    event["number2"] = -314
    assert subtract(event) == 314

def test_subtract_5():
    event = {}
    event["number1"] = 0
    event["number2"] = 0
    assert subtract(event) == 0

def test_subtract_6():
    event = {}
    event["number1"] = 0
    event["number2"] = 228
    assert subtract(event) == -228

def test_subtract_7():
    event = {}
    event["number1"] = 445
    event["number2"] = -89
    assert subtract(event) == 534

def test_subtract_8():
    event = {}
    event["number1"] = 187
    event["number2"] = 0
    assert subtract(event) == 187

def test_subtract_9():
    event = {}
    event["number1"] = 170
    event["number2"] = 103
    assert subtract(event) == 67

def test_divide_1():
    event = {}
    event["number1"] = -164
    event["number2"] = -491
    assert round(divide(event), 3) == .334

def test_divide_2():
    event = {}
    event["number1"] = -212
    event["number2"] = 0
    try:
        divide(event)
    except ZeroDivisionError:
        assert True
    else:
        assert False

def test_divide_3():
    event = {}
    event["number1"] = -318
    event["number2"] = -494
    assert round(divide(event), 3) == .644

def test_divide_4():
    event = {}
    event["number1"] = 0
    event["number2"] = -307
    assert divide(event) == 0

def test_divide_5():
    event = {}
    event["number1"] = 0
    event["number2"] = 0
    try:
        divide(event)
    except ZeroDivisionError:
        assert True
    else:
        assert False

def test_divide_6():
    event = {}
    event["number1"] = 0
    event["number2"] = -438
    assert divide(event) == 0

def test_divide_7():
    event = {}
    event["number1"] = 23
    event["number2"] = -488
    assert round(divide(event), 3) == -0.047

def test_divide_8():
    event = {}
    event["number1"] = 357
    event["number2"] = 0
    try:
        divide(event)
    except ZeroDivisionError:
        assert True
    else:
        assert False

def test_divide_9():
    event = {}
    event["number1"] = 146
    event["number2"] = 278
    assert round(divide(event), 3) == 0.525

def test_multiply_1():
    event = {}
    event["number1"] = -163
    event["number2"] = -379
    assert multiply(event) == 61777

def test_multiply_2():
    event = {}
    event["number1"] = -43
    event["number2"] = 0
    assert multiply(event) == 0

def test_multiply_3():
    event = {}
    event["number1"] = -78
    event["number2"] = 233
    assert multiply(event) == -18174

def test_multiply_4():
    event = {}
    event["number1"] = 0
    event["number2"] = -59
    assert multiply(event) == 0

def test_multiply_5():
    event = {}
    event["number1"] = 0
    event["number2"] = 0
    assert multiply(event) == 0

def test_multiply_6():
    event = {}
    event["number1"] = 0
    event["number2"] = 6
    assert multiply(event) == 0

def test_multiply_7():
    event = {}
    event["number1"] = 471
    event["number2"] = -215
    assert multiply(event) == -101265

def test_multiply_8():
    event = {}
    event["number1"] = 43
    event["number2"] = 0
    assert multiply(event) == 0

def test_multiply_9():
    event = {}
    event["number1"] = 72
    event["number2"] = 403
    assert multiply(event) == 29016