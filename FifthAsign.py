def max_of_three():
    a = int(input("Enter The Frist Number"))
    b = int(input("Enter The second Number"))
    c = int(input("Enter The third Number"))
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
resuit = max_of_three()
print("The Largest Number is :" , resuit)


def max_of_three(a, b, c):
    
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Enter the value of your number in this functuin
print(max_of_three(10, 20, 30))  