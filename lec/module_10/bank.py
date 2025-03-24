import enum
from threading import Thread
from queue import Queue
import time

class PointEnum(str, enum.Enum):
    QUESTION = 'Вопрос'
    PRODUCT = 'Оформление продукта'
    
class ResponsibilityEnum(str, enum.Enum):
    CONSULTANT = 'Консультант'
    OFORDERING = 'Оформитель'


class Client:
    def __init__(self,  point: PointEnum, name: str = 'Undefined'):
        self.name = name  
        if isinstance(point, PointEnum):
            self.point = point
        
    def __str__(self):
        return f"Клиент {self.name} пришел с целью \"{self.point}\"."
    
    def __repr__(self):
        return f"Client[{self.name}]"


class BankWorker(Thread):
    def __init__(self, name: str, queue: Queue, responsibility: ResponsibilityEnum):
        Thread.__init__(self)
        self.name = name
        self.queue = queue
        if isinstance(responsibility, ResponsibilityEnum):
            self.responsibility = responsibility
    
    def run(self):
        print(f'Работник {self.name} начал работу.')
        while not self.queue.empty():
            print(f'[BankWOrker[{self.name}]]Текущая очередь: {self.queue.queue}')
            client: Client = self.queue.get()
            print(f'[BankWOrker[{self.name}]]Текущая очередь: {self.queue.queue}')
            if client.point == PointEnum.QUESTION and self.responsibility == ResponsibilityEnum.CONSULTANT:
                    print(f'Работник {self.name} начал обслуживание клиента {client.name}.')
                    print(str(client))
                    time.sleep(2)
                    print(f'Работник {self.name} закончил обслуживаение клиента {client.name}.')
            elif client.point == PointEnum.PRODUCT and self.responsibility == ResponsibilityEnum.OFORDERING:
                    print(f'Работник {self.name} начал обслуживание клиента {client.name}.')
                    print(str(client))
                    time.sleep(4)
                    print(f'Работник {self.name} закончил обслуживаение клиента {client.name}.')
            else:
                print(f'{client}Отправляем обратно в очередь так как, работник - {self.responsibility}.')
                self.queue.put(client)
        print(f'Работник {self.name} закончил работу.')
       
if __name__ == '__main__':      
    clients_queue = Queue()
    clients_queue.put( Client(name='Иван', point=PointEnum.QUESTION) )
    clients_queue.put( Client(name='Мария', point=PointEnum.PRODUCT) )
    clients_queue.put( Client(name='Игорь', point=PointEnum.QUESTION) )
    clients_queue.put( Client(name='Алексей', point=PointEnum.QUESTION) )
    clients_queue.put( Client(name='Аня', point=PointEnum.PRODUCT) )

    worker1 = BankWorker(name='Сергей', queue=clients_queue, responsibility=ResponsibilityEnum.CONSULTANT)
    worker2 = BankWorker(name='Андрей', queue=clients_queue, responsibility=ResponsibilityEnum.OFORDERING)

    worker1.start()
    worker2.start()

    worker1.join()
    worker2.join()

