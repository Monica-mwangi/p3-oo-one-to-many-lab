class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_instances = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type in self.PET_TYPES:
            self.name = name
            self.pet_type = pet_type
            self.owner = owner
            self.__class__.all_instances.append(self)
        else:
            raise Exception("Invalid pet type")

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all_instances if isinstance(pet.owner, Owner) and pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Invalid pet type")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda x: x.name)
    Pet.all_instances.clear()


    

    