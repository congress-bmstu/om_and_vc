import sympy as sp


def parse_number(user_input):
    try:
        res = sp.nsimplify(user_input)
        assert res.is_number
        return res
        # parsed_number = float(user_input)
        # if parsed_number.is_integer():
        #     parsed_number = int(parsed_number)
        # return parsed_number
    except:
        raise ValueError(f"Некорректный ввод `{user_input}`. Пожалуйста, введи число.")


def parse_number_list(inp):
    try:
        return list(map(parse_number, inp.split()))
    except Exception as e:
        raise ValueError(f"Не смог распарсить список чисел:\n{inp}\n{e}")


def parse_function(inp):
    try:
        sym_expr = sp.parse_expr(inp, evaluate=False)
        return sym_expr
    except Exception as e:
        raise ValueError(f"Не смог распарсить функцию:\n{inp}\n{e}")


def parse_variable(inp):
    try:
        sym_expr = sp.parse_expr(inp, evaluate=False)
        assert type(sym_expr) is sp.Symbol
        return sym_expr
    except Exception as e:
        raise ValueError(f"Не смог распарсить переменную:\n{inp}\n{e}")


def parse_variable_list(inp):
    try:
        sym_expr = sp.parse_expr(inp, evaluate=False)
        assert type(sym_expr) in [tuple, sp.Symbol]
        if type(sym_expr) is tuple:
            return list(sym_expr)
        return [sym_expr]
    except Exception as e:
        raise ValueError(f"Не смог распарсить список переменных:\n{inp}\n{e}")
