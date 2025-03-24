from multiprocessing import Process, Pipe
from multiprocessing.connection import PipeConnection

def worker(conn: PipeConnection):
    data = conn.recv() # получаем данные из канала
    print(f'Process received: {data}')
    conn.send('Hello from worker')
    
if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=worker, args=(child_conn, ))
    p.start()
    
    parent_conn.send('Hello from main process')
    print(parent_conn.recv()) # получаем ответ от процесса
    p.join()
