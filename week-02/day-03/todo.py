# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected outpt:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo


first_line = "My todo:"
secound_line = 0
third_line = " - Download games"
fourth_line = "     - Diablo"

todoText = str(first_line) + "\n" + " - Buy milk" + "\n"+ str(third_line) + "\n" + str(fourth_line)

print(todoText)
