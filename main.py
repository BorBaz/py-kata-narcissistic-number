# My case
def narcissistic(value):
    return sum(item ** len(str(value)) for item in map(int, str(value))) == value


# Best case
narcissistic_bc = lambda n: sum([int(d) ** len(str(n)) for d in list(str(n))]) == n

print(narcissistic(153))
