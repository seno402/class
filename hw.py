class dog:
    species="dog"
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
d1=dog("tom","husky")
d2=dog("rocky","golden retiver")
print(d1.name,d1.breed,dog.species)
print(d2.name,d2.breed,dog.species)