for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


for i in range(1, 101):
    if i % 4 == 0 and i % 6 == 0:
        print("FooBar")
    elif i % 4 == 0:
        print("Foo")
    elif i % 6 == 0:
        print("Bar")
    else:
        print(i)