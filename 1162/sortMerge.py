import time

MAX = 25010
train = [ None for i in range(MAX) ]
memo = [ None for i in range(MAX) ]


def merge(izq, der):
    result = []
    i, j, count = 0, 0, 0
    while (i < len(izq) and j < len(der)):
        if (izq[i] <= der[j]):
            count = count + j
            result.append(izq[i])
            i = i + 1
        else:
            result.append(der[j])
            j = j + 1
    count = count + j*(len(izq)-i) #Factor de multiplicacion de cantidad de cambios durante la mezcla del merge
    result = result + izq[i:]
    result = result + der[j:]
    return count, result

def mergeSort(list):
    if (len(list) <= 1):
        return 0, list
    mid = len(list)//2
    a, izq = mergeSort(list[:mid])
    b, der = mergeSort(list[mid:])
    c, ans = merge(izq, der)
    tot = a + b + c
    return tot, ans
    
def solve(n):
  global train,memo,countcls
  count = mergeSort(train[:n])
  return count[0]

def main():
  global train
  t0=time.time()
  arr = [27,28,8,16,35,18,30,10,37,21,12,39,17,24,20,13,11,25,23,22,5,31,1,6,4,7,32,26,34,29,40,2,14,33,19,38,9,15,36,3,41]
  print('Optimal train swapping takes {0} swaps.'.format(mergeSort(arr)[0]))
  arr = [4,1,6,2,7,5,3]
  print('Optimal train swapping takes {0} swaps.'.format(mergeSort(arr)[0]))
  arr = [50,36,6,23,10,3,43,48,29,31,25,39,11,15,21,1,5,18,2,22,26,28,7,44,27,8,38,19,17,35,14,37,46,30,47,16,40,12,32,34,4,49,42,13,20,33,41,9,24,45]
  print('Optimal train swapping takes {0} swaps.'.format(mergeSort(arr)[0]))
  t1=time.time()
  print("time",t1-t0)
main()