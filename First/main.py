"""
def main():
    my_name = input("Name:")
    print("Az sam", my_name)


def display(x):
    print(x)

    def test_condition():
        var = input("Number:")
        if (var == "5"):
            int(var)
            print("fire")
        elif (var == "7"):
            print("ne raboti")
        else:
            print("lalal")

    if __name__ == "__main__":
        test_condition()


def add(a, b):
    return a+b


def main():
    a = input("vavedi edno chislo:")
    b = input("vavedi o6te edno 4islo:")
    a = int(a)
    b = int(b)
    # add(a,b)
    result = add(a, b)
    print(result)


def izv(x, y):
    return x-y
def umn(x, y):
    return x*y

def main():
    x = input("X:")
    y = input("Y:")
    x = int(x)
    y = int(y)
    result1= izv(x, y)
    result2= umn(x, y)
    print(result1, result2)

if __name__ == "__main__":
    main()

"""




def calc():
    a = input("A")
    b = input("B")
    a = int(a)
    b = int(b)
    op = input("Operation:")
    result = ""

    def add(a, b):
        return a+b
    def subs(a, b):
        return a-b
    def col(a, b):
        return a*b
    def di(a, b):
        return a/b


    if op == "+":
        result= add(a,b)

    elif op == "-":
        result= subs(a,b)

    elif op == "*":
        result= subs(a,b)

    elif op == "/":
        result= di(a,b)

    print(result)

if __name__ == "__main__":
    calc()


