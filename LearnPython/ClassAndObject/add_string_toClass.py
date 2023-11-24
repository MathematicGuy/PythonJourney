class car:
    def __init__(self):
        self.car_type = 'Lambo'
        self.color = 'red'

    def __str__(self):
        return 'It a {} {} '.format(self.color, self.car_type)

a = car()
print(a)