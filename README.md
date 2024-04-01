# Точная интерполяция

## Интерполяция в лоб -- решение СЛАУ с определителем Ван дер Монда

См. функцию `naive_interpolation` в [accurate_interpolation.py](src/accurate_interpolation.py).

## Интерполяция Лагранжа

См. функцию `lagrange_interpolation` в [accurate_interpolation.py](src/accurate_interpolation.py).

## Интерполяция Ньютона (sympy)

См. функцию `newton_interpolation` в [accurate_interpolation.py](src/accurate_interpolation.py).

# Приближенная интерполяция
## Метод наименьших квадратов

См. функцию `mnk_interpolate` в [approx_interpolation.py](src/approx_interpolation.py).

[//]: # (Имеется некоторая функция, у которой мы знаем только набор значений функции. )

[//]: # ()
[//]: # (В ДЗ требуется для вычислений выбрать значения в концах отрезка и всех целых точек внутри него.)

# Одномерная оптимизация без использования производной

## Метод деления отрезка _(почти)_ пополам

Полагаем a1 = a, b1 = b.  

Выбираем две точки u1 = (a + b - delta) / 2 и u2 = (a + b + delta) / 2. 

Если f(u1) <= f(u2), тогда полагаем a2 = a1, b2 = u2. 

Иначе, если f(u1) > f(u2), тогда считаем, что a2 = u1, b2 = b1.

Аналогично на каждой следующей итерации. 

В дз необходимо выбрать минимум, а также точку минимума. 

См. функцию `bisect` в [extremum.py](src/extremum.py).

## Метод золотого сечения

Полагаем u1 = a + 0.382 * (b - a), u2 = a + 0.618 * (b - a). 

Если f(u1) <= f(u2), тогда a2 = a1, b2 = u2, bar_u2 = u1.

Инааче, если f(u1) > f(u2), тогда a2 = u1, b2 = b1, bar_u2 = u2.

Аналогично на каждой следующей итерации.

См. функцию `golden_cut` в [extremum.py](src/extremum.py). 

## Метод парабол 

Полагаем u[0] = x0, u[1] = u[0] + h. 

Если точка u[1] принадлежит [a, b]. Тогда вычисляем значение в ней. 

Если f(u[1]) <= f(u[0]), то вычисляем u[i] = u[0] + 2 ** (i - 1) * h, i >= 2.

Если ui принадлежит отрезку, то вычисляем значение в ней. 

Проверяем, образуют ли u[i - 2], u[i - 1], u[i] выпуклую тройку для f(x). 

Если не образуют, то берем следующую точку. Когда выпуклая тройка найдена, то проводим параболу ветвями вверх и ищем вершину параболы w. 

Если u[i] не принадлежит отрезку, а выпуклая тройка так и не найдена, тогда полагаем точкой минимума w = b. 

Если f(u[1]) > f(u[0]) или u[1] принадлежит отрезку, тогда изменим направление поиска. Переобозначим u[0] = u[1], u[i] = u[0] - 2 ** (i - 1) * h, i >=1.

Если тройка найдена, w - вершина параболы, если нет w = a. 

Далее f(bar_u) = min(f(w), f(u0), ..., f(un)).

См. функцию `parabola` в [extremum.py](src/extremum.py).

## Метод ломанных 

(пустая функция)

См. функцию `method_lomannih` в [extremum.py](src/extremum.py). 

# Одномерная оптимизация с использованием производных

## Метод средней точки

См. функцию `method_srednei_tochki` в [extremum_with_derivative.py](src/extremum_with_derivative.py).

## Метод хорд _(метод секущих)_

См. функцию `chordal_method` в [extremum_with_derivative.py](src/extremum_with_derivative.py).

## Метод Ньютона _(метод касательных)_

См. функцию `newton_method` в [extremum_with_two_derivatives.py](src/extremum_with_two_derivatives.py).

# Многомерная оптимизация 

## Градиентный метод дробления шага

См. функцию `grad_method_step_division` в [multidim_optimization_with_grad.py](src/multidim_optimization_with_grad.py).

## Градиентный метод скорейшего спуска

См. функцию `grad_method_of_fastest_fall` в [multidim_optimization_with_grad.py](src/multidim_optimization_with_grad.py).

## Метод сопряженных направлений

(нет)