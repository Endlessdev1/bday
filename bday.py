import time
from random import randint

for i in range(1,85):
    print('')

space = ''

for i in range(1,1000):
    count = randint(1, 100)
    while(count > 0):
        space += ' '
        count -= 1
    if(i%10==0):
        print(space + 'πHappy Birthdayπ!')
    elif(i%9 == 0):
        print(space + "πππ")
    elif(i%10==0):
        print(space + "πΊHappy Birthday!π₯π₯π₯")
    elif(i%8==0):
        print(space +"πππ₯ππ")
    elif(i%9==0):
	    print(space + "π")
    elif(i%6==0):
        print(space + "πΈ")
    elif(i%6==0):
        print(space + "ππ₯πΈπ")
    elif(i%10==0):
        print(space + 'πHappy Birthdayπ!')
    elif(i%9 == 0):
        print(space + "πΈπ«")
    elif(i%6==0):
        print(space + "πΊHappy Birthday!π₯π₯π₯")
    else:
        print(space + "πΈ")
    space = ''
    time.sleep(0.2)
