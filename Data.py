import random 

def normalize(rain, clouds, wind):
    rain_n = rain / 100
    clouds_n = clouds / 100
    wind_n = wind / 100

    if wind_n > 1:
        wind_n = 1
    return [rain_n, clouds_n, wind_n]

def human_rule(x):
    score = 0.55 * x[0] + 0.30 * x[1] + 0.15 * x[2]
    return score

def make_example(count):
    random.seed(1)

    inputs = []
    answers = []
    while len(inputs) < count:
        rain = random.randint(0, 100)
        clouds = random.randint(0, 100)
        wind = random.randint(0, 100)
        x = normalize(rain, clouds, wind)
        score = human_rule(x)

        if abs(score - 0.5) < 0.05:
            continue
        inputs.append(x)
        if score > 0.5:
            answers.append(1)
        else:
            answers.append(0)
    return inputs, answers

def ask_number(question, low, hight):
    while True:
        text = input(question)
        if text == "q":
            return None
        try:
            number = float(text.replace(",", "."))
        except ValueError:
            print("Нужно ввести число, попробуй еще раз !")
            continue
        if number < low or number > hight:
            print(f"Число должно быть от - {low}, до {hight} - попробуй еще раз !")
            continue
        return number
        