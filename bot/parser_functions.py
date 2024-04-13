import sympy as sp


def parse_number(user_input):
    try:
        return sp.nsimplify(user_input)
        # parsed_number = float(user_input)
        # if parsed_number.is_integer():
        #     parsed_number = int(parsed_number)
        # return parsed_number
    except ValueError:
        raise ValueError(f"Некорректный ввод ({user_input}). Пожалуйста, введи число.")


def parse_number_list(inp):
    try:
        return list(map(parse_number, inp.split()))
    except:
        raise ValueError(f"Не смог распарсить список чисел:\n{inp}")


def parse_function(inp):
    try:
        sym_expr = sp.parse_expr(inp, evaluate=False)
        return sym_expr
    except Exception as e:
        raise ValueError(f"Не смог распарсить функцию:\n{inp}\n{e}")
