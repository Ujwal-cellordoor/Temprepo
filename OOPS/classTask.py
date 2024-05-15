class Animal:
    def __init__(self, animal_base):
        self.animal_base = animal_base

    def base(self):
        print(self.animal_base + " is a animal base.")


class Cat(Animal):

    def __init__(self, animal_type):
        self.animal_type = animal_type
        super().__init__(animal_type)

    def print(self):

        print("Print is a cat property")


cat_obj = Cat("tiger")
cat_obj.print()
cat_obj.base()
