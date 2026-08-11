class Pet:
    def __init__(self, name, species, age, breed="Unknown"):
        self.name = name          # Stores the pet's name
        self.species = species    # Stores the species (e.g., Dog, Cat)
        self.age = age            # Stores the pet's age in years
        self.breed = breed        # Stores the breed with a default value
    def display_profile(self):
        """Access and print object-specific information."""
        print(f"--- {self.name}'s Profile ---")
        print(f"Species: {self.species}")
        print(f"Breed:   {self.breed}")
        print(f"Age:     {self.age} years old\n")
pet1 = Pet(name="Buddy", species="Dog", age=3, breed="Golden Retriever")
pet2 = Pet(name="Whiskers", species="Cat", age=2)
pet1.display_profile()
pet2.display_profile()
