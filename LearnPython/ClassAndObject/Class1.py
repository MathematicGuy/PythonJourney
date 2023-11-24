class John:

    def __init__(self, Trait, Height, First_name, Last_name, Catch_phrase):
        self.trait = Trait
        self.height = Height
        self.weight = 0  #  unregistered value also starts with 0
        self.first_name = First_name
        self.last_name = Last_name
        self.catch_phrase = Catch_phrase

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def surgeons(self, special_human):
        #  self (take values from __init__ dunder)
        #  special_human (take values from given argument)
        self.weight += 1
        special_human.weight += 5
        special_human.catch_phrase = "Suffer to hell"
        print('{}/{}'.format(self.weight, special_human.weight))

human_1 = John('courage', 150, 'Harvard', 'John', 'How you doing')
human_2 = John('coward', 175, 'Dank', 'Smith', 'Could cha doubt it')

for i in range(2):
    human_1.surgeons(human_2)

    # print(human_1.__repr__())
    # print(human_2.__repr__())
    print()

print(human_1.weight)


#  .text -> turn class value attribute to text
