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

# a=tokens, b=apr, c=reserved
def fee(abc, acc):
    return (abc[0] - acc) * abc[1] * (1-abc[2]);


def fs(parameters, fun):
    result = []
    for i in range(len(parameters)):
        result.append(fun(parameters[i]))
    return result

def notBefore(t0, t1, t2):
    if t0 <= t1:
        return t2-t1
    if t0 <= t2:
        return t2-t0
    return 0

def integral(t0, times, parameters, fun):
    acc = 0
    for i in range(len(parameters)):
        value = fun(parameters[i], acc)
        acc += notBefore(t0, times[i],  times[i+1]) * value
    return acc


# (t0, [ta, a0, a1], [tb, b0, b1], [tc, c0, c1], t4)
def fees(t0, a, b, c, t4, fun):
    times = [t0, a[0], b[0], c[0]]
    bubbleSort(times)
    parameters = abc(times, a, b, c)
    return integral(t0, [*times, t4], parameters, fun)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # a=tokens, b=apr, c=reserved
    print_hi(fees(0, [0.5, 1000, 900], [0.5, 0.1, 0.2], [0.5, 0, 0.1], 1, fee))

