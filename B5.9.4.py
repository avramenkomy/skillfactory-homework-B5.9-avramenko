'''Реализация кода с использованием декоратора как объекта класса.'''

import time
class Secoondomer:
    # Конструктор класса
    # Принимаем количество запусков
    def __init__(self, num_runs=10):
        # Сохраняем количство запусков
        self.num_runs = num_runs
    
    # Метод, который отвечает за то, как ведет себя объект, когда мы используем его как функцию
    # В данном случае мы используем объект, как декоратор
    # Метод принимает на вход функцию, которую мы хотим обернуть (посчитать время выполнения)
    # Мы создаём функцию-обертку
    # В функции-обертке выполняем подсчёт среднего времени выполнения функции и выводим его в консоль
    # Потом возвращаем эту обертку
    def __call__(self, func):
        def wrapper():
            avg_time = 0
            # сохраняем начальное время
            # в цикле вызываем self.num_runs раз функицю func
            for i in range(self.num_runs):
                # Считаем разницу меджу текущим и начальным временем
                print("Запуск № ", i+1)
                t0 = time.time()
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
                print("Конец запуска № ", i+1)
                print("Время выполнения запуска № ", i+1, " заняло %.5f секунд" % (t1 - t0))
            avg_time /= self.num_runs
            # Выводим в консоль среднее время с помощью print
            print("Среднее время выполнения функции занимает %.5f секунд" % avg_time)
            return func
        return wrapper
 
# Теперь пример использования:
# Создаём объект класса Secoondomer и используем его в качестве декоратора
@Secoondomer(int(input("Введите количество запусков ")))
def f():
    print("Выполнение функции f")
    for j in range(1000000):
        pass
 
# Вызываем функцию
f()