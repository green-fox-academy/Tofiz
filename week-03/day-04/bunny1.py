
# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

def bunny_ear_counter(bunny):
    if bunny <= 0:
        return 0
    else:
        return (bunny_ear_counter(bunny -1)) + 2

print(bunny_ear_counter(99))