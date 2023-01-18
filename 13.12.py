# Решить с помощью потоков задачу читателей и писателей. 
# Задача состоит в следующем - существует ряд писателей и читателей,
#  которые обращаются к одному и тому же источнику (представим себе его как книгу). 
#  Все они читают и пишут одну и ту же книгу. Писать может одновременно только один писатель, 
#  остальные ожидают своей очереди. Процесс написания состоит в добавлении случайной буквы раз в timeout времени. 
#  когда писатель заканчивает писать все свои буквы, он уходит отдыхать. 
#  После отдыха он вёрнется и снова будет ждать своей очереди писать. 
#  Следующий писатель стирает книгу и пишет её заново. 
#  Читатели видят весь этот процесс и могут читать книгу в реальном времени.
#   Читатель и писатель должны быть отдельными классами. 
#   Программа должна работать бесконечно.

from threading import Thread, Condition, Lock
from time import sleep
from random import randint, choice

spisok_of_pictures = ['sunflowers', 'starry sky', 'pink rose']
spisok_1 = ''

class Artist(Thread):
    def __init__(self, name):
        super().__init__(name=name)
        self.name = name
    def run(self):
        global spisok_1
        while True:
            with lock:
                random_picture = choice(spisok_of_pictures)
                for i in random_picture:
                    spisok_1 += i
                    print('Artist {} is painting: {}'.format(self.name, spisok_1))
                    with condition:
                        condition.notify_all()
                    sleep(randint(1, 2))
                print('Artist {} finished paint'.format(self.name))
                print('Artist {} is выгорел и дает свободу для творчества другому'.format(self.name))
                spisok_1 = ''
            sleep(randint(1,4))

class Visitor(Thread):
    def __init__(self, name):
        super().__init__(name=name)
        self.name = name
    def run(self):
        global condition
        while True:
            with condition:
                condition.wait()
                print('Visitor {} is watching: {}'.format(self.name, spisok_1))

            
if __name__ == '__main__':

    condition = Condition()
    lock = Lock()
    for gfdhjk in range(4):
        Artist(str(gfdhjk)).start()
    for ghjlus in range(6):
        Visitor(str(ghjlus)).start()
        


