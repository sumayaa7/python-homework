# map bilan: barcha sonlarni kvadrat qilish
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)   # [1, 4, 9, 16, 25]

# filter bilan: faqat juft sonlarni olish
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)     # [2, 4]

#is_prime (n)
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

print(is_prime(4))  # False
print(is_prime(7))  # True

#sum key(k)
def digit_sum(k):
    return sum(map(int, str(k)))

print(digit_sum(24))   # 6
print(digit_sum(502))  # 7

#ikki sonning darajalari
def powers_of_two(N):
    p = 1
    res = []
    while (p := p * 2) <= N:
        res.append(p)
    return res

print(powers_of_two(10))  # [2, 4, 8]
