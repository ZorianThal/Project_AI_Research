from Data import make_example, normalize, ask_number

name = ["дождь", "облачность", "ветер"]
inputs, answers = make_example(200)
print("Примеры обучения", len(inputs))

weights = [0.0, 0.0, 0.0]
bias = 0.0
speed = 0.1

def predict(x):
    total = bias 
    for i in range(3):
        total = total + weights[i] * x[i]
    if total > 0:
        return 1 
    return 0

print("начало обучения !")
for epoch in range(1, 1001):
    mistakes = 0 

    for n in range(len(inputs)):
        x = inputs[n]
        right_answer = answers[n]
        my_answer = predict(x)
        error = right_answer - my_answer

        if error != 0:
            for i in range(3):
                weights[i] = weights[i] + speed * error * x[i]
            bias = bias + speed * error
            mistakes += 1

    if epoch % 10 == 0 or mistakes == 0:
        print("Эпоха: ", epoch, "Ошибок: ", mistakes)
    if mistakes == 0:
        print("Обучение закончено !")
        break

# Что выучил нейрон
print("Правильные веса")
for i in range(3):
    print(" ", name[i], "=", round(weights[i], 2))
    print("Смещение", round(bias, 2))
    print("Тут сеть понимает что у нас вес дождя гараздо важнее")

correct = 0
for n in range(len(inputs)):
    if predict(inputs[n]) == answers[n]:
        correct += 1
print("Верных ответов на примерах = ", correct, "из", len(inputs))
#Менюшка для юзера
print("\nБрать ли нам зонт ?!")

while True:
    rain = ask_number("Вероятность дождя, %(0-100)", 0, 100)
    if rain is None:
        break
    clouds = ask_number("Облачность, %(0-100)", 0, 100)
    if clouds is None:
        break
    wind = ask_number("Скорость ветра, от 0 до 20 мс", 0, 20)
    if wind is None:
        break
    x = normalize(rain, clouds, wind)

    print("Что на это скажет нейросеть ?!?!?!?!?!?")
    total = bias
    for i in range(3):
        part = weights[i] * x[i]
        total = total + part
        print(" ", name[i]," Вклад", round(part, 2))
    print("  смещение: Вклад", round(bias, 2))
    print("     сумма = ", round(total, 2))
    if total > 0:
        print("Берите зонт")
    else:
        print("Все четко !")
