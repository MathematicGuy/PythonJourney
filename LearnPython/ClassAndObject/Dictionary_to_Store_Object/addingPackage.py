class Repository:
    def __init__(self):
        self.packages = {'coca': 22}

    def add_package(self, package, size):
        self.packages.update({package : size})
    def total_size(self):
        result = 0
        for package in self.packages.values():
            print(package)
            result += package
        return result

a = Repository()
a.add_package('Box', 10)
print(a.total_size())
