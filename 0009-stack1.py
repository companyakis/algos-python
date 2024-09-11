# stack => First In Last Out or Last In First Out

from queue import LifoQueue

lq = LifoQueue()

lq.put(100)
lq.put(500)
lq.put(700)
lq.put(900)

print("Our stack info: ", lq) # Our stack info:  <queue.LifoQueue object at 0x000001FC3672C550>

# our stack => 900, 700, 500, 100

lq_first_item = lq.get() # 900

print("First item of lq: ", lq_first_item) # First item of lq:  900

lq_second_item = lq.get() # 700

print("Second item of lq: ", lq_second_item) # Second item of lq:  700

# try a list:)
l = []
l.append(100)
l.append(500)
l.append(700)
l.append(900)

print("Our list: ", l) # Our list:  [100, 500, 700, 900]
print("Our list first item: ", l[0]) # Our list first item:  100
