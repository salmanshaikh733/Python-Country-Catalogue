# this file creates the country object with the instance variables and also represents the object, it also has the get and set methods for each instance variable
# mshaik52, student number 250959996
# make a country class to make country objects
class Country:
    # declare constructor to construct country variables
    def __init__(self, name, population, area, continent):
        self.name = name
        self.population = population
        self.area = area
        self.continent = continent

    def getName(self):
        return self.name

    def getPop(self):
        return self.population

    def getArea(self):
        return self.area

    def getContinent(self):
        return self.continent

    def setPopulation(self, pop):
        self.population = pop

    def setArea(self, area):
        self.area = area

    def setContinent(self, cont):
        self.continent = cont

    def getPopDensity(self):
        density = float(self.population) / float(self.area)
        return density

    def __repr__(self):
        return self.name + " (population:" + str(self.population) + ", size:" + str(self.area).replace("\n",
                                                                                                       "") + ") in " + self.continent + "\n"
