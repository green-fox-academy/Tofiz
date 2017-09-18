# Create a method that decrypts the duplicated-chars.txt

file_name = "my_file.txt"
def decrypt(fn):
    try:
        file = open(fn, "r")
        text = ""
        decrypt_copy_inside = open("decrypt_copy_inside.txt", "w")
        lines_list = file.readlines()
        for line in lines_list:
            for i in range(0, len(line), 3):
                text += line[i]
        decrypt_copy_inside.write(text)
        file.close()
        decrypt_copy_inside.close()
    except IOError:
        pass
decrypt(file_name)