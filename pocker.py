li = [i for i in range (0,13)]*4
li.append('a')
li.append('b')

import random
random.shuffle(li)
print(li[0:18])
trial_num = 1000000
count = 0
for t in range(1,trial_num+1):
    random.shuffle(li)
    for i in range (0, 13):
        if (li[0:18].count(i) == 4) :
            #print('{}炸1,{}'.format(i,t))
            count += 1
            break
        elif (li[18:36].count(i) == 4) :
            #print('{}炸2,{}'.format(i, t))
            count += 1
            break
        elif (li[36:54].count(i) == 4) :
            #print('{}炸3,{}'.format(i, t))
            count += 1
            break


print(count)
print(float(count/trial_num))
