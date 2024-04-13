from typing import Callable, Any
from dataclasses import dataclass

from .parser_functions import parse_number, parse_number_list, parse_function


@dataclass
class InputType:
    example_format: str
    format_comment: str
    parser_function: Callable[[str], Any]

    def get_format(self):
        return f'{self.example_format} //{self.format_comment}'

    def parse(self, user_input: str):
        return self.parser_function(user_input)

    def __call__(self, user_input: str):
        return self.parse(user_input)

    def __str__(self):
        return self.get_format()


@dataclass
class ArgumentInput(InputType):
    description: str

    def __init__(self, input_type: InputType, description):
        self.example_format = input_type.example_format
        self.format_comment = input_type.format_comment
        self.parser_function = input_type.parser_function
        self.description = description

    def get_format(self):
        return super().get_format() + f'; {self.description}'


NUMBER_LIST = InputType('1 2.2 3 -4 -5.1', 'числа через пробел', parse_number_list)
SINGLE_NUMBER = InputType('2', 'одно число', parse_number)
FUNCTION = InputType('x**3 + 6 * x**2 + 9 * x + 1', ' функция одной переменной x', parse_function)
