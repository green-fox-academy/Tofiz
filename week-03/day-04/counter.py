# Write a recursive function that takes one parameter: n and counts down from n.

def counts_down(n):
    if n <= 0: #base case
        return 1
    else:
        return counts_down(n-1)

print('Counts down from n', counts_down(5))
