#1
import math

radius = int(input("Введіть радіус круга: "))
area = math.pi * radius ** 2
print("Площа круга:", round(area, 2))

a = int(input("Введіть перший катет: "))
b = int(input("Введіть другий катет: "))
hypotenuza = math.sqrt(a ** 2 + b ** 2)
print("Гіпотенуза:", round(hypotenuza, 2))
c = int(input("Введіть кількість предметів: "))
d = int(input("Введіть кількість предметів в одній упаковці: "))
packages = math.ceil(c / d)
print("Потрібно упаковок:", packages)

#2
import random
import statistics
a = int(input("Введіть кількість оцінок: "))

if a <= 0:
    print("Кількість оцінок повинна бути додатною")
else:
    grades = []
    for i in range(a):
        grades.append(random.randint(1, 12))
    high = 0
    for grade in grades:
        if grade >= 10:
            high += 1

print("Оцінки:", grades)
print("Мінімальна оцінка:", min(grades))
print("Максимальна оцінка:", max(grades))
print("Середнє арифметичне:", round(statistics.mean(grades), 2))
print("Медіана:", statistics.median(grades))
print("Кількість оцінок 10–12:", high)

#3
from datetime import date

year = int(input("Введіть рік події: "))
month = int(input("Введіть місяць події: "))
day = int(input("Введіть день події: "))

event = date(year, month, day)
today = date.today()

if event > today:
    difference = event - today
    print("До події залишилося днів:", difference.days)
elif event < today:
    difference = today - event
    print("Від події минуло днів:", difference.days)
else:
    print("Подія відбувається сьогодні!")

#4
import random
import statistics
import tkinter as tk
import student
students = ["Анна", "Іван", "Ольга", "Максим"]

def generate_grades(count):
    return [random.randint(1, 12) for i in range(count)]
def average_grade(grades):
    return statistics.mean(grades)
def get_level(average):
    if average >= 10:
        return "високий"
    elif average >= 7:
        return "достатній"
    elif average >= 4:
        return "середній"
    return "початковий"
def generate_report():
    report = ""

    for name in students:
        grades = student.generate_grades(5)
        average = student.average_grade(grades)
        level = student.get_level(average)
        report += f"{name}: {grades}\n"
        report += f"Середній бал: {average:.2f}\n"
        report += f"Рівень: {level}\n\n"
    print(report)
    result.delete("1.0", tk.END)
    result.insert(tk.END, report)

window = tk.Tk()
window.title("Звіт успішності")
window.geometry("450x400")

tk.Button(window, text="Створити звіт", command=generate_report).pack(pady=10)

result = tk.Text(window, width=50, height=20)
result.pack()

window.mainloop()