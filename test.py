i = 0
while i <= 99:
    i += 1
    if i % 15 == 0:
        print("Fizz")
        continue
    if i % 3 == 0:
        print("Buzz")
        continue

    if i % 5 == 0:
        print("FizzBuzz")
        continue

    print(i)
