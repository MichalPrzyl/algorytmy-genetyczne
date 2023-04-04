from person import Person
from globals import MAX_WIDTH


class Population:
    count: int
    people = []

    
    def __init__(self, count):
        self.count = count   

        for _ in range(count):
            p = Person()
            self.people.append(p)

    def delete_left_half(self):
        for person in self.people:
            if person.position_x < MAX_WIDTH/2:
                self.people.remove(person)

    def delete_popualtion(self):
        self.people.clear()
        
