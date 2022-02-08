# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def bubbleSort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def g(t, x):
    return x[1] if t < x[0] else x[2]


def abc(times, a, b, c):
    result = []
    for i in range(len(times)):
        result.append([g(times[i], a), g(times[i], b), g(times[i], c)])
    return result


def f(abc):
    return abc[0] * abc[1] + abc[2];


def fs(parameters):
    result = []
    for i in range(len(parameters)):
        result.append(f(parameters[i]))
    return result

def notBefore(t0, t1, t2):
    if t0 <= t1:
        return t2-t1
    if t0 <= t2:
        return t2-t0
    return 0

def integral(t0, times, values):
    result = 0
    for i in range(len(values)):
        result += notBefore(t0, times[i],  times[i+1]) * values[i]
    return result


# (t0, [ta, a0, a1], [tb, b0, b1], [tc, c0, c1], t4)
def fees(t0, a, b, c, t4):
    times = [t0, a[0], b[0], c[0]]
    bubbleSort(times)
    parameters = abc(times, a, b, c)
    values = fs(parameters)
    total = integral(t0, [*times, t4], values)
    return total


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(fees(0, [20, 1, 2], [10, 3, 4], [30, 5, 6], 40))
    print_hi(fees(25, [20, 1, 2], [10, 3, 4], [30, 5, 6], 40))
    print_hi(fees(40, [20, 1, 2], [10, 3, 4], [30, 5, 6], 40))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
