# Saturn is missing from the planet_list
# Insert it into the correct position

planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
saturn = ["Saturn"]
planet_list = planet_list[:5] + saturn + planet_list[5:]

print (planet_list)
