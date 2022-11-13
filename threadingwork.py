from concurrent.futures import thread
import threading
import time


def tool():
    for i in range(5):
        print(" Itne Threading Work Ho Rahe Hai -> {} ".format(threading.active_count()))
        time.sleep(5)
        print("Now Will Be Ready")


another_thread = threading.Thread(target=tool)

begin_time = time.time()
another_thread.start()
print(time.time()-begin_time)