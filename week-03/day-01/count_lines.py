# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.



def number_of_lines ():
    num_lines = sum(1 for line in open('my_file.txt'))
    print(num_lines)
number_of_lines ()
