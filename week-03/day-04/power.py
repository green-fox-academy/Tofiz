# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def to_the_n_power(base, n):
    if n == 0:
        return 1
    elif base == 0:
        return 0
    else:
        return base * to_the_n_power(base, n-1)

print(to_the_n_power(2, 5))