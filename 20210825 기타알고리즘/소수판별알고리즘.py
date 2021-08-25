
#소수 판별 함수(2이상의 자연수에 대하여)
import math


def newIs_prime_number(x): #시간복잡도가 N의 1/2승
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2,int(math.sqrt(x))+1):
        #x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False #소수가아님
        return True #소수임

def oldIs_prime_number(x): #시간복잡도가 N
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2,x):
        #x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False #소수가아님
        return True #소수임

print(newIs_prime_number(4)) #소수아님
print(newIs_prime_number(7)) #소수임