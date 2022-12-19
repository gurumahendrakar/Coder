import threading
from threading import Thread,Event
from queue import Queue
import time
import csv
import datetime


#
# members_names = []
# room1 = []
# room2 = []
#
# timeing = time.time()
#
# class threading_(Thread):
#
#     def __init__(self):
#
#         self.room1_attendence = []
#         self.room2_attendence = []
#         self.lock = threading.Lock()
#         self.rlock = threading.RLock()
#         self.sempherone = threading.Semaphore(1)
#         self.Boundedsemaphore = threading.BoundedSemaphore(1)
#         self.event = Event()
#         self.queue = Queue()
#         self.condition = threading.Condition()
#         self.retunvalue = 0
#
#         #super(cls_name,clsobject).__init__()
#
#         super(threading_,self).__init__()
#
#
#     def method1(self,time_):
#
#         print('__Room__1 members Adding... ',room1)
#         for x in self.room1_attendence:
#             room1.append(x)
#
#         else:
#             self.retunvalue =  'Hey Man !!'
#
#     def method2(self,time_):
#         print('__Room__ 2 Members Adding ...',room2)
#         for x in self.room2_attendence:
#             room2.append(x)
#         else:
#             return  room1,room2
#
#     def _room1_attendence(self):
#         print(' Hello Sir !! ')
#         self.Boundedsemaphore.acquire()
#         def __room__2():
#             print('Handeling Me >> ',threading.current_thread().name)
#             for x in range(int(input('__Room__ 2 HOw Many Employes  >> '))):
#                 name = input('Enter The Name : > ')
#
#
#                 if name not in self.room2_attendence:
#                     print(f'__ Member Added __ : {name}')
#                     self.room2_attendence.append(name)
#
#                 else:
#                     print('Name is already registered Try One More time !!')
#
#                     try_more = input('Enter the name one more time ! ')
#
#                     if try_more not in self.room2_attendence:
#                         self.room2_attendence.append(try_more)
#
#                     else:
#                         print('Rules not followed U You can go brother \n'
#                               'I will Your Chance Another Member !!')
#
#             else:
#                 return (self.room1_attendence ,self.room2_attendence)
#
#
#         for x in range(int(input(' __Room__ 1  How Many Employes  >>'))):
#             name = input('Enter The Name : > ')
#
#             if name not in self.room2_attendence:
#                 print(f'__ Member Added __ : {name}')
#                 self.room1_attendence.append(name)
#
#                 print(self.room1_attendence)
#
#             else:
#                 print('Name is already registered Try One More time !!')
#
#                 try_more = input('Enter the name one more time ! ')
#
#                 if try_more not in self.room1_attendence:
#                     self.room1_attendence.append(name)
#
#                 else:
#                     print('Rules not followed U You can go brother \n'
#                           'I will Your Chance Another Member !!')
#         __room__2()
#
#         self.Boundedsemaphore.release()
#
# thread_ = threading_()
# thread2_ = threading_()
# thread3_ = threading_()
#
#
# thread_._target = thread_.method1
# thread2_._target = thread2_.method2
# thread3_._target = thread_._room1_attendence
#
# thread_.name = 'i_love_u'
# thread_._args = (1,)
#
# thread2_.name = 'i_love_u2'
# thread2_._args = (1,)
#
# thread3_.start()
# thread3_.join()
#
#
#
#
# print('---------------------------------thread-3 work completed brother-----------------------')
# print()
# print()
# print()
# print()
#
# if thread3_.is_alive()==False:
#     thread_.start()
#     thread2_.start()
#
#     thread2_.join()
#     thread_.join()
#
# print('room 1 members ',thread_.room1_attendence)
# print('room 2 members ',thread_.room2_attendence)
# print('Executed Seconds > ',time.time()-timeing)
#



# --------------------------------------------==Threading EVents==-----------------------------------------------------
# event = threading.Event()
#
# class thread_(threading.Thread):
#
#     def __Init__(self):
#         super().__init__()
#
#     def _Ordering_(self):
#         event.set()
#         for x in ['Dosa','Idli','Paratha']:
#             print(x)
#
#         time.sleep(0.4)
#         event.clear()
#
#         print(event.__dict__)
#
#
#     def Customer_service(self):
#
#         event.wait()
#         while event.is_set():
#             print('You Can Give Me 100 RS ')
#
#
# threed = thread_()
# threed2 = thread_()
#
# threed._target = threed._Ordering_
# threed2._target = threed.Customer_service
#
# threed.start()
# threed2.start()
#



#-----------------------------------------------threading Condition--------------------------------------------------

#
#
# class thread_(threading.Thread):
#
#     def __init__(self):
#         super().__init__()
#         self.conditon_event = threading.Condition()
#
#     def _Ordering_(self):
#
#         self.conditon_event.acquire()
#
#         for x in ['Dosa','Idli','Paratha']:
#             print(x)
#
#         self.conditon_event.notify()
#         self.conditon_event.release()
#
#     def Customer_service(self):
#
#         self.conditon_event.acquire()
#         self.conditon_event.wait(timeout=0.2)
#         print('You Can Give Me 100 RS ')
#         self.conditon_event.release()
#
#
# threed = thread_()
# threed2 = thread_()
#
# threed._target = threed._Ordering_
# threed2._target = threed.Customer_service
#
# threed.start()
# threed2.start()
#
# threed.join()
# threed2.join()


#--------------------------------------------threading Queue--------------------------------------------------------

#
#
# class thread_(threading.Thread):
#
#     def __init__(self):
#         super().__init__()
#         self.queue_event = Queue()
#         self.lock = threading.Lock()
#
#     def _Ordering_(self):
#
#         self.lock.acquire()
#         for x in ['Dosa','Idli','Paratha']:
#             print('takeing order-----------')
#             self.queue_event.put(x)
#
#         self.lock.release()
#
#
#     def Customer_service(self):
#
#         for x in range(3):
#             print(self.queue_event.get())
#
#
# threed = thread_()
# threed2 = thread_()
#
# threed._target = threed._Ordering_
# threed2._target = threed.Customer_service
#
# threed.start()
# threed2.start()
#
# threed.join()
# threed2.join()



#------------------------------------------------Demon - Thread ----------------------------------------------------------

def soO():
    print(threading.currentThread())
    def one_more():
        print('one more -- thread')
        for x in range(5):
            print(x,end=' ')

    thread2_ = threading.Thread(target=one_more)
    thread2_.start()
    print('Thread Kill Or not : ',thread2_.daemon)

print(threading.main_thread().is_alive())
thread_ = threading.Thread(target=soO)
thread_.start()

thread_.join()
print('____Main Thread___')

