import matplotlib.pyplot as plt
import math


def f(x):
    return x**2 + 5 * math.sin(x)


def f_prime(x):
    return 2*x + 5 * math.cos(x)


# Chọn ngẫu nhiên giá trị ban đầu của x.
x = 20
# Chọn alpha.
alpha = 0.01
# Lặp 10000 lần.
for _ in range(10000):
    x -= alpha * f_prime(x)
print('Gia tri cua x : ', x)
print('Gia tri cua f(x) : ', f(x))

xs = [x / 100.0 for x in range(-400, 200)]
ys = [f(x) for x in xs]
plt.plot(xs, ys)
plt.show()
