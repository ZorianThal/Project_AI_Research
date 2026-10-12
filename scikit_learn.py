from sklearn.linear_model import Perceptron
from Data import make_example, normalize, ask_number

name = ["дождь", "облачность", "ветер"]

inputs, answers = make_example(200)
print("Примеров для обучения: ", len(inputs))

#Начало обучения
model = Perceptron(max_iter=1000, tol=None, random_state=1)
model.fit(inputs, answers)
print("Обучение закончено !")

#Что выучила библиотека
for i in range(3):
    print(" ", name[i], "=", round(model.coef_[0][i], 2))
    print(" Смещение", "=", round(model.intercept_[0], 2))
    print("Жождь самый важный !")

accuracy = model.score(inputs, answers)
print("Верных ответов на примерах: ", round(accuracy * 100), "%")

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
    answer = model.predict([x])[0]
    if answer == 1:
        print("Берите зонтик")
    else:
        print("Зонтик не нужен")