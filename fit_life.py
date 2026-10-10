"""Проект FitLife - MVP версия 1.0."""


def calculate_fit_metrics(weight, height):
    """Вычисления индекса массы тела и воды."""
    bmi = weight / (height ** 2)
    water_l = (weight * 30) / 1000
    return round(bmi, 1), round(water_l, 1)


print('Приветствую Вас! Давайте познакомимся.')

user_name = input('Как вас зовут? ')
user_age = int(input('Ваш возраст? '))
user_weight = float(input('Ваш вес в кг? '))
user_height = float(input('Ваш рост в м? '))

result_bmi, result_water = calculate_fit_metrics(user_weight, user_height)


print()
print(f'Отчёт для пользователя: {user_name} ({user_age} лет)')
print(f'Твой индекс массы тела: {result_bmi}')
print(f'Рекомендуемая норма воды: {result_water} л. в день')
print()
print('Расчёт окончен. Будьте здоровы!')
