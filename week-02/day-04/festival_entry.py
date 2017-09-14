watchlist = []

security_alcohol_loot = 0

they_can_enter = []

queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 0, 'guns': 0 }
]

# Queue of festivalgoers at entry
# no. of alcohol units 
# no. of guns

# Create a security_check function that returns a list of festivalgoers who can enter the festival
def security_check (in_queue):
    for empty_festivalgoers in in_queue:
        if empty_festivalgoers['alcohol'] == 0 and empty_festivalgoers['guns'] == 0:
        	they_can_enter.append(empty_festivalgoers['name'])
security_check(queue)
print("They can enter: " , they_can_enter)




# If guns are found, remove them and put them on the watchlist (only the names)
# If alcohol is found confiscate it (set it to zero and add it to security_alcohol_loot) and let them enter the festival