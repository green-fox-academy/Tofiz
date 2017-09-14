shop_items = ["Cupcake", 2, "Brownie", False]

# Accidentally we added "2" and "false" to the list. 
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)

shop_items.remove(2)
shop_items.remove(False)

shop_items.insert(1,"Croissant")
shop_items.insert(3,"Ice cream")

print(shop_items)