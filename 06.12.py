# Задача о спящем парикмахере. У парикмахера есть одно рабочее место и приёмная с несколькими стульями. 
# Когда парикмахер заканчивает подстригать клиента, он отпускает клиента и затем идёт в приёмную, 
# чтобы посмотреть, есть ли там ожидающие клиенты. Если они есть, он приглашает одного из них и стрижёт его. 
# Если ждущих клиентов нет, он возвращается к своему креслу и спит в нём.
# Каждый приходящий клиент смотрит на то, что делает парикмахер. 
# Если парикмахер спит, то клиент будит его и садится в кресло. 
# Если парикмахер работает, то клиент идёт в приёмную. Если в приёмной есть свободный стул, 
# клиент садится и ждёт своей очереди. Если свободного стула нет, то клиент уходит. 
# Подсказка реализации: парикмахер и клиенты - объекты соответствующих классов, 
# стулья в приёмной - очередь, парикмахерская - рабочий процесс или объект с рабочим процессом, 
# пробуждение парикмахера - управление событием Event (пришёл клиент). Добавьте ситуацию,
# в которой если парикмахера никто не будит и он просыпается сам (например, по таймауту 20 секунд),
# он закрывает парикмахерскую (рабочий процесс завершается).

from multiprocessing import Process, Queue, Event, Lock
from time import sleep
from random import randint


class Customer:
    def __init__(self, name):
        self.name = name


class Barber:
    # actions = 'Sleep', 'Not sleep'
    def __init__(self):
        self.barberEvent = Event()
        # self.action = 'start'

    def sleeps(self):
        print('Barber is sleeping')
        return self.barberEvent.wait(timeout=10)

    def wakeUp(self):
        self.barberEvent.set()


    def cutHair(self, customer):  
        print('Barber take client {} for heardressing'.format(customer.name))

    def barber_work(self, client):
        self.barberEvent.clear()
        self.cutHair(client)
        sleep(2)
        print("Client {} is make".format(client.name))

        
        

class Barbershop:
    def __init__(self):
        self.queue = Queue(maxsize=3)
        self.process = Process(target=self.work)
        self.barber = Barber()
        self.lock = Lock()


    def open(self):
        print('Barbershop opens')
        self.process.start()
        

    def close(self):
        print('Hairdresser close barbershop as there are not clients')

    def work(self):
        while True:
            self.lock.acquire()
            if self.queue.empty():
                self.lock.release()
                if not self.barber.sleeps():
                # if self.barber.action == 'end':
                #     print('Barbershop closes')
                    self.close()
                    break
            else:
                self.lock.release()
                self.barber.barber_work(self.queue.get())

    def come_in(self, Customer):
        with self.lock:
            print('Client comes in barbershop')
            if self.queue.full():
                print('Client goes home')
            else:
                self.queue.put(Customer)
                self.barber.wakeUp()




if __name__ == '__main__':
    mutex = Lock()
    barbershop = Barbershop()
    clients = [Customer('bob'), Customer('rob'), Customer('bor'), Customer('orb') ]
    barbershop.open()
    for b in clients:
        barbershop.come_in(b)
        sleep(randint(1, 6))

