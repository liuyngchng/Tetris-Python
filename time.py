import time

start = time.process_time()

for i in range(10000):

    print(i)

end = time.process_time()

print('different is %6.3f' % (end - start))

