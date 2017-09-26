class Garden:
    def __init__(self):
        self.list_of_flowers = []
        self.list_of_trees = []
    
    def add_flower(self, flower):
        self.list_of_flowers.append(flower)

    
    def add_tree(self, tree):
        self.list_of_trees.append(tree)

    
    def watering(self, liter):
        print(self.list_of_flowers)
        for i in self.list_of_flowers:
            i.watering(liter)
            i.get_status()

        for j in self.list_of_trees:
            j.watering(liter)
            j.get_status()

        
class Flower(object):
    def __init__(self, f_color, liter):
        self.f_color = f_color
        self.liter = liter
    
    def watering(self, liter = 0):
        self.liter += liter

    def get_status(self):
        if self.liter > 65:
            print("The {} color flower doesn't need water.".format(self.f_color))
        else:
            print("The {} color flower needs water.".format(self.f_color))

class Tree(object):
    def __init__(self, t_color, liter):
        self.t_color = t_color
        self.liter = liter

    def watering(self, liter = 0):
        self.liter += liter

    def get_status(self):
        if self.liter > 65:
            print("The {} color tree doesn't need water.".format(self.t_color))
        else:
            print("The {} color tree needs water.".format(self.t_color))

    
my_garden = Garden()

flower01 = Flower("blue", 25)
my_garden.add_flower(flower01)
flower02 = Flower("yellow", 34)
my_garden.add_flower(flower02)
flower03 = Flower("red", 45)
my_garden.add_flower(flower03)
tree01 = Tree("brown", 56)
my_garden.add_tree(tree01)
tree02 = Tree("dark brown", 67)
my_garden.add_tree(tree02)
tree03 = Tree("black", 78)
my_garden.add_tree(tree03)

# my_garden.watering(10)
my_garden.watering(60)
