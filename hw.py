class dog:
    species="dog"

    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
        
    def display(self):
        print("Name:",self.name)
        print("Breed:",self.breed)
        print("Species:",dog.species)


dog1=dog("tom","Labrador")
dog2=dog("lisa","Poodle")

print("Details of dog 1")
dog1.display()

print("\nDetails of dog 2")
dog2.display() 