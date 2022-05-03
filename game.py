"""The new game: 'Guess the number"""
import numpy as np
number=np.random.randint(1,5)# guessing the number
count = 0

while True:
    count+=1
    predict_number=int(input('Guess the number from 1 to 200'))
    if predict_number>number:
        print('Your nuber more than we need')
    elif predict_number<number:
        print('Your number is less than nessary')
    else:
        print (f'This is the number that we need! The number is {number}\
        you have {count} try.')
        break