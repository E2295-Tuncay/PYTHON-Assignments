fibonacci_list = [1,1]
toplam = 0
for i in range(100):
    toplam = fibonacci_list[i] + fibonacci_list[i + 1]
    fibonacci_list.append(toplam)
    if toplam == 55:
        break
print("Fibonacci numbers from 1 to 55 are : ", fibonacci_list)