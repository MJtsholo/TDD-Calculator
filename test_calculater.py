from calculater import adding, multiply
import pytest


def test_adding_two_numbers():
	result = adding(0,0)
	assert result == 0

	result = adding(1,3)
	assert result == 4

def test_negative_numbers():
	result = adding(-1,-1)
	assert result == -2

def test_adding_more_than_two():
	result = adding(1,5,9)
	assert result == 15

	result = adding(10,5,20,4)
	assert result == 39

def test_multiplying_numbers():
	result = multiply(4,2)
	assert result == 8

	result = multiply(5,8)
	assert result == 40

def test_multiplying_more_than_two():
	result = multiply(4,2,2)
	assert result == 16

	result = multiply(4,2,3,1)
	assert result == 24