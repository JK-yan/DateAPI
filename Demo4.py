import datetime
import random
import time



date = '2016-12-%s' % random.randint(1, 32)+' %s' % random.randint(0, 24) + ':%s' % random.randint(0, 61) + ':%s' % random.randint(0, 61)

start = time.clock()
# time.sleep(5)
end = time.clock()
print("The function run time is : %.03f seconds" %(end-start))
print(date)
ip = '%s.%s.%s.%s' % (random.randint(1, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# ip = '%s.'% random.randint(1, 255)+'%s.'% random.randint(1, 255)+'%s.'% random.randint(1, 255)+'%s' % random.randint(0, 255)
print(random.randint(1, 2))
print(ip)
ww = '%s%s%s'%('sda',1,'sda')
print(ww)