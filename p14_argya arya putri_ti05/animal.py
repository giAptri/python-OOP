#Argya arya putri
#Ti_05
#0110222241
#tugas animal python



class Animal:
    def __init__(self, name, food, habitat, reproduction):
        self.name = name
        self.food = food
        self.habitat = habitat
        self.reproduction = reproduction
        
class Kucing(Animal):
    def __init__(self, name, food, habitat, reproduction, size):
        super().__init__(name, food, habitat, reproduction)
        self.size = size
        
    def display_characteristics(self):
        print(f"Nama: {self.name}")
        print(f"Makanan: {self.food}")
        print(f"Habitat: {self.habitat}")
        print(f"Cara berkembang biak: {self.reproduction}")
        print(f"Ukuran: {self.size}")
        
        
class Semut(Animal):
    def __init__(self, name, food, habitat, reproduction, size):
        super().__init__(name, food, habitat, reproduction)
        self.size = size
        
    def display_characteristics(self):
        print(f"Nama: {self.name}")
        print(f"Manakan: {self.food}")
        print(f"Habitat: {self.habitat}")
        print(f"Cara Berkembangbiak: {self.reproduction}")
        print(f"Ukuran: {self.size}")
        

class Marmut(Animal):
    def __init__(self, name, food, habitat, reproduction, size):
        super().__init__(name, food, habitat, reproduction)
        self.size = size
        
    def display_characteristics(self):
        print(f"Nama: {self.name}")
        print(f"Manakan: {self.food}")
        print(f"Habitat: {self.habitat}")
        print(f"Cara Berkembangbiak: {self.reproduction}")
        print(f"Ukuran: {self.size}")
        
        
class Burung(Animal):
    def __init__(self, name, food, habitat, reproduction, size):
        super().__init__(name, food, habitat, reproduction)
        self.size = size
        
    def display_characteristics(self):
        print(f"Nama: {self.name}")
        print(f"Manakan: {self.food}")
        print(f"Habitat: {self.habitat}")
        print(f"Cara Berkembangbiak: {self.reproduction}")
        print(f"Ukuran: {self.size}")
        
        
class Kepiting(Animal):
    def __init__(self, name, food, habitat, reproduction, size):
        super().__init__(name, food, habitat, reproduction)
        self.size = size
        
    def display_characteristics(self):
        print(f"Nama: {self.name}")
        print(f"Manakan: {self.food}")
        print(f"Habitat: {self.habitat}")
        print(f"Cara Berkembangbiak: {self.reproduction}")
        print(f"Ukuran: {self.size}")
        
        
kucing = Kucing("Kucing", "Karnivora", "Neutral", "Beranak", "sedang")
kucing.display_characteristics()
print('\n=====================')

semut = Semut("semut", "Omnivora", "Pepohonan, Tanah", "Bertelur", "kecil")
semut.display_characteristics()
print('\n=====================')

marmut = Marmut("marmut", "Herbivora", "pepohonan, peliharaan", "Beranak", "Kecil")
marmut.display_characteristics()
print('\n=====================')

kepiting = Kepiting("kepiting", "omnivora", "air", "Bertelur", "sedang")
kepiting.display_characteristics()
print('\n=====================')