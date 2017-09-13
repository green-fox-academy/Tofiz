# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string shouldf be a preverb
# The function appends every verb to the preverb and returns the list of the new verbs


verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"

# WITHOUT A FUNCTION
# new_verbs = ""
# for i in range(len(verbs)):
#     new_verbs += str(preverb + verbs[i]) + ", "
# print(new_verbs)



# WITH A FUNCTION

def create_new_verbs():
    new_verbs = ""
    for i in range(len(verbs)):
        new_verbs += str(preverb + verbs[i]) + ", "
    return new_verbs

print(create_new_verbs())

    