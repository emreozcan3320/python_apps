#Ptyhon Examples
#-----------------
class animal:
    def __init__(self,sound,life_span,eating_habit):
        self.cell_structure = "selective tin"
        self.habitat = []
        self.sound = sound
        self.life_span = life_span 
        self.eating_habit = eating_habit
    def add_habitat(self,*args):
        for i in args:
            self.habitat.append(i)
            
Dog = animal("hav hav", 10 , "mixed")
print(Dog.sound)
Dog.add_habitat("runing","walking","playing","biting")
print(Dog.habitat)

Cat = animal("miyav rr", 7 , "mixed")
print(Cat.sound)
Cat.add_habitat("climbing","jumping","scracing","playing")
print(Cat.habitat)

#Inheritance and super keyword usage
#------------------------------------
class dog(animal):
    def __init__(self,sound,life_span,eating_habit,color):
        super().__init__(sound,life_span,eating_habit)
        self.color = color
    
bulldog = dog("hav hav", 5, "meat","grey")
print(bulldog.color)
        
