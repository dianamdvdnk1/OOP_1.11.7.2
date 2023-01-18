# N философов сидят вокруг круглого стола, перед каждым философом стоит тарелка риса. 
# По палочке для еды (chopstick) лежит на столе между каждой парой ближайших философов. 
# Каждый философ может либо есть, либо размышлять. 
# Приём пищи не ограничен количеством оставшейся еды — подразумевается бесконечный запас.
#  Тем не менее, философ может есть только тогда, когда держит две палочки — взятую справа и слева. 
#  Ест философ случайное время в указанном вами интервале (например, randint(1, 3)).
#   Каждый философ может взять ближайшую палочку (если она доступна) или положить — если он уже держит её. 
#   Взятие каждой палочки и возвращение её на стол являются раздельными действиями, которые должны выполняться одно за другим. 
#   Задача заключается в том, чтобы разработать модель поведения (параллельный алгоритм), 
#   при котором ни один из философов не будет голодать, то есть будет вечно чередовать приём пищи и размышления. 
#   Вывод действий в терминал должен быть подробным (философ №N начал есть, закончил есть, взял правую палочку,
#    взял левую палочку, начал размышлять, закончил размышлять - на каждое действие должен быть вывод).
#    Задача со звёздочкой - написать мониторинг голода философов. При выставленном таймауте голодания, 
#    если конкретный философ голодает уже больше времени таймаута, начиная с этого момента каждую секунду
#     выводить заметное сообщение о том, что философ X голодает уже N секунд. Звёздочка выдаётся по принципу 
#     "кто первый встал - того и тапки".

from multiprocessing import Process,Lock
from random import randint
import time

class Philosopher(Process):
    def __init__(self, name, right_chopstick, left_chopstick):
        super().__init__(name=name) #наследование атрибутов от род класса
        self.name = name
        self.right_chopstick = right_chopstick
        self.left_chopstick = left_chopstick
    def run(self):
        while True:
            if self.left_chopstick.acquire(timeout=1):
                print('Philosopher {} takes left_chopstick'.format(self.name))
                if self.right_chopstick.acquire(timeout=1):
                    print('Philosopher {} takes right_chopstick'.format(self.name))
                    print('Philosopher {} has repast'.format(self.name))
                    time.sleep(randint(1, 4))
                    self.left_chopstick.release()
                    self.right_chopstick.release()
                    print('Chopsticks is free and Philosopher {} is starting think'.format(self.name))
                else:
                    self.left_chopstick.release()
                    print('Philosopher {} Otpustil left_chopstick'.format(self.name))
            
if __name__ == '__main__':
    for num in range(6):
        Philosopher(str(num), Lock(), Lock()).start()