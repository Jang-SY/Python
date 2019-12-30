# binomial function
'''
x(array)의 값들이 확률이라고 했을 때, 
binomial distribution으로 1을 return
'''

import random   # random 함수를 import
import numpy    # array생성, 할당에 유용한 함수

def binomial_func(arr):
    arr2 = numpy.zeros(len(arr))        # numpy.zeros(크기)로 arr와 같은 크기의 배열을 생성(모든 항의 값 = 0)
    for i in range(len(arr)):
        if random.random() < arr[i]:    # random으로 나온 값이(0.0~1.0) arr확률보다 작으면
            arr2[i] = 1                 # arr2의 0값을 1로 바꿈
    return arr2


if __name__ == "__main__":              # main 문
    arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    result = binomial_func(arr)
    print(result)
