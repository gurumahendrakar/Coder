from concurrent.futures import thread
import threading
import time

import collections

a = collections.Counter({1:2,3:4})

print(a.items())