def read_int(prompt, min, max):
    while True:
        value = input(prompt)    
        try:
            value = int(value)
            if value >= min and value <= max:
                return value
            else:
                print("The value is not within the permitted range, try again!")
        except ValueError:
            print("Error: wrong input")
            continue
            


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

