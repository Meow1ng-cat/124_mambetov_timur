import random
import time


class Animal:
    defaut = "Unknown"
    species_list = ("Mammal", "Bird", "Reptile")
    gender_list = ("Male", "Female")
    color_list = ("White", "Black", "Red", "Blue", "Green", "Yellow")

    def __init__(self, name, age, species, gender):
        if name:
            self.name = str(name)
        else:
            self.name = self.defaut
        if isinstance(age, int):
            self.age = age
        else:
            self.age = self.defaut
        if species and species in self.species_list:
            self.species = species
        else:
            self.species = self.defaut
        if gender and gender in self.gender_list:
            self.gender = gender
        else:
            self.gender = self.defaut

    def display_info(self):
        print("Name: {}. Age: {}. Species: {}. Gender: {}".format(self.name, self.age, self.species, self.gender))

    def age_is_define(self):
        if isinstance(self.age, int):
            return True
        else:
            return False

    def is_young(self):
        if self.age_is_define():
            if self.age < 2:
                return True
            else:
                return False

    @staticmethod
    def eat():
        print("Хрум-Хрум")

    @staticmethod
    def sleep():
        print("Zzzzzzzzzzzzzz")

    @staticmethod
    def make_sound():
        print("*Animal sounds*")


class Mammal(Animal):

    def __init__(self, name, age, species, gender, fur_color, number_of_legs):
        super().__init__(name, age, species, gender)
        if fur_color and fur_color in self.color_list:
            self.fur_color = fur_color
        else:
            self.fur_color = self.defaut
        if isinstance(number_of_legs, int):
            self.number_of_legs = number_of_legs
        else:
            self.number_of_legs = self.defaut

    def display_info(self):
        super().display_info()
        print("Fur color is {} and this mammul has {} legs".format(self.fur_color, self.number_of_legs))

    def give_birth(self, male_mammal):
        if self.age_is_define() and male_mammal.age_is_define():
            if self.is_young() or male_mammal.is_young():
                print("Too young!")
            else:
                if not self.gender == male_mammal.gender and self.gender == "Female":
                    fur_color_variation = [self.fur_color, male_mammal.fur_color,
                                           self.fur_color + "-and-" + male_mammal.fur_color,
                                           male_mammal.fur_color + "-and-" + self.fur_color]
                    childe_fur_color = random.choice(fur_color_variation)
                    childe_gender = random.choice(self.gender_list)
                    childe_mammal = Mammal("", 0, self.species, childe_gender, childe_fur_color, self.number_of_legs)
                    print("New mammal is born! Here is its description: ")
                    childe_mammal.display_info()
                    return childe_mammal
                else:
                    print("No homo")

    def nurse_young(self, young_mammal):
        if self.age_is_define():
            if self.is_young():
                print("Too young!")
            else:
                self.age += 1
                young_mammal.age += 1


class Reptile(Animal):
    venom_type_list = ("Heamotoxic", "Neurotoxic", "Myotoxic", "Haemorrhaginstoxins", "Haemolysinstoxins",
                       "Nephrotoxins", "Cardiotoxins", "Necrotoxins")

    def __init__(self, name, age, species, gender, scale_color, venom_type):
        super().__init__(name, age, species, gender)
        if scale_color and scale_color in self.color_list:
            self.scale_color = scale_color
        else:
            self.scale_color = self.defaut
        if venom_type and venom_type in self.venom_type_list:
            self.venom_type = venom_type
        else:
            self.venom_type = self.defaut

    def display_info(self):
        super().display_info()
        print("Scale color is {} and this reptile has {} venom".format(self.scale_color, self.venom_type))

    def lay_eggs(self, male_reptile):
        if self.age_is_define() and male_reptile.age_is_define():
            if self.is_young() or male_reptile.is_young():
                print("Too young!")
            else:
                if not self.gender == male_reptile.gender and self.gender == "Female":
                    scale_color_variation = [self.scale_color, male_reptile.scale_color,
                                             self.scale_color + "-and-" + male_reptile.scale_color,
                                             male_reptile.scale_color + "-and-" + self.scale_color]
                    venom_type_variation = [self.venom_type, male_reptile.venom_type]
                    childe_scale_color = random.choice(scale_color_variation)
                    childe_venom_type = random.choice(venom_type_variation)
                    childe_gender = random.choice(self.gender_list)
                    print("Eggs layed! Wait...")
                    time.sleep(3)
                    childe_reptile = Reptile("", 0, self.species, childe_gender, childe_scale_color, childe_venom_type)
                    print("New reptiole is born! Here is its description: ")
                    childe_reptile.display_info()
                    return childe_reptile
                else:
                    print("No homo")

    def shed_skin(self):
        new_color = random.choice(self.color_list)
        self.scale_color = new_color


class Bird(Animal):

    def __init__(self, name, age, species, gender, wing_span, beak_lenght):
        super().__init__(name, age, species, gender)
        if isinstance(wing_span, int):
            self.wing_span = wing_span
        if isinstance(beak_lenght, int):
            self.beak_lenght = beak_lenght

    def display_info(self):
        super().display_info()
        print("Wing span is {} and this bird has {} beaks lenght".format(self.wing_span, self.beak_lenght))

    @staticmethod
    def fly():
        print("Flip-Flop")

    @staticmethod
    def build_nest():
        print("Nest building noise")


tom = Mammal("Tom", 3, "Mammal", "Male", "red", 4)
meg = Mammal("Meg", 3, "Mammal", "Female", "white", 4)
tom.display_info()
mammal_childe = meg.give_birth(tom)
gans = Reptile("Gans", 4, "Reptile", "Male", "green", "Neurotoxic")
gans.display_info()
gena = Reptile("Gena", 3, "Reptile", "Female", "blue", "Myotoxic")
gena.display_info()
reptile_childe = gena.lay_eggs(gans)
gans.shed_skin()
gans.display_info()
clark = Bird("Clark", 2, "Bird", "Male", 3, 5)
clark.display_info()

