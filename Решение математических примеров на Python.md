
# Задания на Python: решение математических примеров

## Часть 1. Базовые вычисления

Задание 1
> Вычислите значение выражения:
> $$y = \frac{3x^2 - 5x + 7}{2x + 1}$$
> для $x = 4$.

Задание 2
> Найдите корни квадратного уравнения $ax^2 + bx + c = 0$ через дискриминант, если $a=2, b=-7, c=3$.

Задание 3
> Вычислите сумму арифметической прогрессии:
> $$S_n = \frac{(a_1 + a_n) \cdot n}{2}$$
> где $a_1 = 3$, $d = 5$, $n = 20$.

Задание 4
> Вычислите факториал $n = 7$ без библиотеки `math` (через цикл).

Задание 5
> Вычислите значение функции:
> $$f(x) = \sin(x) \cdot e^{-x} + \ln(x+1)$$
> для $x = 2$.

---

## Часть 2. Циклы и списки

Задание 6
> Дан список `[12, 45, 3, 67, 23, 89, 5]`. Найдите среднее, максимум и минимум **без** `sum`, `max`, `min`.

Задание 7
> Проверьте, является ли число $n = 97$ простым.

Задание 12 (доп.)
> Дан список температур `[18, 21, 19, 25, 23, 17, 20]`. Найдите, сколько дней температура была выше среднего.

Задание 13 (доп.)
> Найдите все числа Фибоначчи, не превышающие $n = 100$.
---

## Решения

python

```python
import math

# ---------- Задание 1 ----------
x = 4
y = (3*x**2 - 5*x + 7) / (2*x + 1)
print("Задание 1: y =", y)

# ---------- Задание 2 ----------
a, b, c = 2, -7, 3
D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Задание 2: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x1 = -b / (2*a)
    print(f"Задание 2: x1 = x2 = {x1}")
else:
    print("Задание 2: действительных корней нет")

# ---------- Задание 3 ----------
a1, d, n = 3, 5, 20
an = a1 + (n - 1) * d
S_n = (a1 + an) * n / 2
print("Задание 3: S_n =", S_n)

# ---------- Задание 4 ----------
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Задание 4: 7! =", factorial(7))

# ---------- Задание 5 ----------
x = 2
f = math.sin(x) * math.exp(-x) + math.log(x + 1)
print("Задание 5: f(x) =", f)

# ---------- Задание 6 ----------
numbers = [12, 45, 3, 67, 23, 89, 5]

total = 0
for num in numbers:
    total += num
average = total / len(numbers)

maximum = numbers[0]
minimum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print(f"Задание 6: среднее = {average}, максимум = {maximum}, минимум = {minimum}")

# ---------- Задание 7 ----------
n = 97
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break

print(f"Задание 7: число {n} простое? {is_prime}")

# ---------- Задание 8: Персептрон ----------
def step_function(z):
    return 1 if z >= 0 else 0

x = [0.5, -0.2, 0.8]
w = [0.4, 0.3, -0.6]
b = 0.1

z = sum(xi * wi for xi, wi in zip(x, w)) + b
y = step_function(z)

print(f"Задание 8: взвешенная сумма z = {z}")
print(f"Задание 8: выход персептрона y = {y}")
```

python

```python
import math

# ---------- Задание 9 ----------
x = 3
y = math.sqrt(x**3 + 2*x) - math.cos(x)
print("Задание 9: y =", y)

# ---------- Задание 10 ----------
b1, q, n = 2, 3, 8
S_n = b1 * (q**n - 1) / (q - 1)
print("Задание 10: S_n =", S_n)

# ---------- Задание 11 ----------
a, b, c = 5, 6, 7
p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Задание 11: площадь треугольника S =", S)

# ---------- Задание 12 ----------
temps = [18, 21, 19, 25, 23, 17, 20]

total = 0
for t in temps:
    total += t
average = total / len(temps)

count_above = 0
for t in temps:
    if t > average:
        count_above += 1

print(f"Задание 12: среднее = {average}, дней выше среднего = {count_above}")

# ---------- Задание 13 ----------
n = 100
fib_list = [0, 1]
while True:
    next_fib = fib_list[-1] + fib_list[-2]
    if next_fib > n:
        break
    fib_list.append(next_fib)

print("Задание 13: числа Фибоначчи до", n, "=", fib_list)



