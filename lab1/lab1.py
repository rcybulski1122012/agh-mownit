import numpy as np
from matplotlib import pyplot as plt


def f1(x):
    return x**8 - 8 * x**7 + 28 * x**6 - 56 * x**5 + 70 * x**4 - 56 * x**3 + 28 * x**2 - 8 * x + 1


def f2(x):
    return (((((((x - 8) * x + 28) * x - 56) * x + 70) * x - 56) * x + 28) * x - 8) * x + 1


def f3(x):
    return (x - 1)**8


# x != 1
def f4(x, dtype):
    return np.exp(8 * np.log(abs(x - 1), dtype=dtype
                             ), dtype=dtype)


X_float = np.linspace(0.99, 1.01, 101, dtype=np.single)
X_double = np.linspace(0.99, 1.01, 101, dtype=np.double)
X_longdouble = np.linspace(0.99, 1.01, 101, dtype=np.longdouble)

# f1

f1_Y_float = f1(X_float)
f1_Y_double = f1(X_double)
f1_Y_longdouble = f1(X_longdouble)

fig, axs = plt.subplots(2, 2, figsize=(9, 6))
fig.tight_layout(pad=2.5)
axs[0, 0].plot(X_float, f1_Y_float)
axs[0, 0].set_title("f1 float")

axs[0, 1].plot(X_double, f1_Y_double)
axs[0, 1].set_title("f1 double")

axs[1, 0].plot(X_longdouble, f1_Y_longdouble)
axs[1, 0].set_title("f1 long double")

axs[1, 1].plot(X_longdouble, f1_Y_float)
axs[1, 1].plot(X_longdouble, f1_Y_double)
axs[1, 1].plot(X_longdouble, f1_Y_longdouble)
axs[1, 1].set_title("f1 wszystkie")
axs[1, 1].legend(["float", "double", "long double"])

for ax in axs.flat:
    ax.set(xlabel='x', ylabel='y')


plt.show()


# f2

f2_Y_float = f2(X_float)
f2_Y_double = f2(X_double)
f2_Y_longdouble = f2(X_longdouble)

fig, axs = plt.subplots(2, 2, figsize=(9, 6))
fig.tight_layout(pad=2.5)
axs[0, 0].plot(X_float, f2_Y_float)
axs[0, 0].set_title("f2 float")

axs[0, 1].plot(X_double, f2_Y_double)
axs[0, 1].set_title("f2 double")

axs[1, 0].plot(X_longdouble, f2_Y_longdouble)
axs[1, 0].set_title("f2 long double")

axs[1, 1].plot(X_longdouble, f2_Y_float)
axs[1, 1].plot(X_longdouble, f2_Y_double)
axs[1, 1].plot(X_longdouble, f2_Y_longdouble)
axs[1, 1].set_title("f2 wszystkie")
axs[1, 1].legend(["float", "double", "long double"])

for ax in axs.flat:
    ax.set(xlabel='x', ylabel='y')


plt.show()



# f3

f3_Y_float = f3(X_float)
f3_Y_double = f3(X_double)
f3_Y_longdouble = f3(X_longdouble)

fig, axs = plt.subplots(2, 2, figsize=(9, 6))
fig.tight_layout(pad=2.5)
axs[0, 0].plot(X_float, f3_Y_float)
axs[0, 0].set_title("f3 float")

axs[0, 1].plot(X_double, f3_Y_double)
axs[0, 1].set_title("f3 double")

axs[1, 0].plot(X_longdouble, f3_Y_longdouble)
axs[1, 0].set_title("f3 long double")

axs[1, 1].plot(X_longdouble, f3_Y_float)
axs[1, 1].plot(X_longdouble, f3_Y_double)
axs[1, 1].plot(X_longdouble, f3_Y_longdouble)
axs[1, 1].set_title("f3 wszystkie")
axs[1, 1].legend(["float", "double", "long double"])

for ax in axs.flat:
    ax.set(xlabel='x', ylabel='y')

plt.show()



# f4

X_float_without_1 = X_float[X_float != 1]
X_double_without_1 = X_double[X_double != 1]
X_longdouble_without_1 = X_longdouble[X_longdouble != 1]

f4_Y_float = f4(X_float_without_1, dtype=np.longdouble)
f4_Y_double = f4(X_double_without_1, dtype=np.longdouble)
f4_Y_longdouble = f4(X_longdouble_without_1, dtype=np.longdouble)

fig, axs = plt.subplots(2, 2, figsize=(9, 6))
fig.tight_layout(pad=2.5)
axs[0, 0].plot(X_float_without_1, f4_Y_float)
axs[0, 0].set_title("f4 float")

axs[0, 1].plot(X_double_without_1, f4_Y_double)
axs[0, 1].set_title("f4 double")

axs[1, 0].plot(X_longdouble_without_1, f4_Y_longdouble)
axs[1, 0].set_title("f4 long double")

axs[1, 1].plot(X_longdouble_without_1, f4_Y_float)
axs[1, 1].plot(X_longdouble_without_1, f4_Y_double)
axs[1, 1].plot(X_longdouble_without_1, f4_Y_longdouble)
axs[1, 1].set_title("f4 wszystkie")
axs[1, 1].legend(["float", "double", "long double"])

for ax in axs.flat:
    ax.set(xlabel='x', ylabel='y')

plt.show()

plt.plot(X_longdouble, f2_Y_longdouble)
plt.plot(X_longdouble, f3_Y_longdouble)
plt.plot(X_longdouble_without_1, f4_Y_longdouble)

plt.xlabel("x")
plt.ylabel("x")
plt.legend(["f2", "f3", "f4"])
plt.title("f2, f3, f4 dla typu long double")

plt.show()


print("f1 roznice", max(abs(f1_Y_float - f1_Y_double)), max(abs(f1_Y_double - f1_Y_longdouble)))

print("f2 roznice", max(abs(f2_Y_float - f2_Y_double)), max(abs(f2_Y_double - f2_Y_longdouble)))

print("f3 roznice", max(abs(f3_Y_float - f3_Y_double)), max(abs(f3_Y_double - f3_Y_longdouble)))

print("f4 roznice", max(abs(f4_Y_float - f4_Y_double)), max(abs(f4_Y_double - f4_Y_longdouble)))