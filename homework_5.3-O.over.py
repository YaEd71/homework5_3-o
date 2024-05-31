class Building:

    def __init__(self, numberOfFoors):
        self.numberOfFoors = numberOfFoors

    def __str__(self, buildingType):
        self.buildingType = buildingType

    def __eg__(self, other):
        return self.numberOfFoors == other.numberOfFoors and self.buildingType == other.buildingType

numberOfFoors = 25
buildingType = 'build'

print(numberOfFoors)
print(buildingType)
print(numberOfFoors == numberOfFoors and buildingType == buildingType)

numberOfFoors = Building
buildingType = Building