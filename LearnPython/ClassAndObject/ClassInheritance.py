class LandAnimal:
	def __init__(self):
		self.num_eyes = 2
		self.feather = True

	def breathe(self):
		print('Inhale, Exhale')

class carnivore(LandAnimal):
	def __init__(self):
		self.foodSource = 'meat'
		super().__init__()


class Lion(carnivore):
	def __init__(self):
		super().__init__()

	def roar(self):
		super().breathe()
		print('Grahahahahhahaha')

lion = Lion()

# print(lion.roar())

print(carnivore().foodSource)