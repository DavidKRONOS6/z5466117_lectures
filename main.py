# This is a sample Python script.
from six import b


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def qan_tic():
    tic = "qan.tnnx"
    print(tic)
    return tic

print(tic)
qan_tic()


list0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]

def list1(lis):
    list1 = []
    for i in lis:
        if i % 2 == 0:
            list1.append(i)
    return list1
list1(list0)
print(list1(list0))



numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
a = list({i for i in  numbers if i % 2==0})
print(a)

def num(a, b):
    for a, b in num:
        a = 6
        b = 12
        return a+b
num(a, b)