class John:

    def __init__(self, Trait, Height, First_name, Last_name, Catch_phrase):
        self.trait = Trait
        self.height = Height
        self.weight = 0  # unregistered value also starts with 0
        self.first_name = First_name
        self.last_name = Last_name
        self.catch_phrase = Catch_phrase

    def __repr__(self):
        ''' Return all John's class Keys ( __class__ ) and Values ( __dict__ ) '''
        return "%s(%r)" % (self.__class__, self.__dict__)

    def increase_weight(self):
        ''' Outputs a message with the name of the person '''
        self.weight += 1


human_1 = John('courage', 150, 'Harvard', 'John', 'How you doing')

help(human_1.increase_weight)  # function with no parentheses
