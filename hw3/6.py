#!/bin/python3

class FizzBuzzException(Exception):
    def __init__(self, message="no message"):
        self.message = message
        super().__init__(self.message)


def i_can_raise_exception():
    raise FizzBuzzException("<-- I am Fizz-Buzz Exception message -->")

def i_still_can_not_raise_exception():
    return i_can_raise_exception()

def i_can_not_raise_exception():
    return i_still_can_not_raise_exception()

def i_definetely_can_not_raise_exception():
    return i_can_not_raise_exception()

i_definetely_can_not_raise_exception()
