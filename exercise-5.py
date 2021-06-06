# exercise-05 Fibonacci sequence for first 50 terms

for num in range(50):
    if num == 0:
        print(f'term: {num} / number: 0')
    elif num == 1:
        print(f'term: {num} / number: 1')
    else:
        f_num = ((1.618034 ** num) - (1 - 1.618034 ** num))/(5 ** 0.5)
        f_num = int(f_num)
        print(f'term: {num} / number: {f_num}')
   

