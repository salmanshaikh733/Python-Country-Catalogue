# This class creates a country object and also has the list of required methods for that specific object
# This class also stores the object into a another object called the catalogue.
# mshaik52, student number 250959996
########################################################################################################################
# impor the Country class from country
from country import Country


# declare the class countryCatalogue
class CountryCatalogue:
    # intialize catologue and fill it with countries
    def __init__(self, Continent, Data):
        self.countryCat = []
        self.cDictionary = {}
        self.countryName = {}
        # open the files
        dataFile = open(Data, "r")
        contFile = open(Continent, "r")
        # skip the headers of the files
        dataFile.readline()
        contFile.readline()

        # read through a continent file and make a dictionary where the key is the country name and it returns the continent value, create a dictionary of continents that returns a continent when country name is sent to it
        endOFLine = True

        while endOFLine == True:
            cLine = contFile.readline()
            cData = cLine.split(",")
            if cLine == "":
                endOFLine = False
            else:
                self.cDictionary[cData[0]] = cData[1].strip("\n")

        # read through data file and make a list of country with area name and population and add to catalogue from each line
        flag = True
        while flag == True:
            line = dataFile.readline()
            data = line.split("|")
            if line == "":
                flag = False
            # if not end of file create the new country object
            else:
                # create a dictionary for keeping the country names,
                self.countryName[data[0]] = data[0]
                population = data[1].replace(",", "")
                area = data[2].replace(",", "")
                name = data[0].strip("\n")
                newCountry = Country(data[0], population, area, self.cDictionary[data[0]])
                # add object to new catalogue collection of countries
                self.countryCat.append(newCountry)

    # method to find country and return its object
    def findCountry(self, c):

        for i in range(len(self.countryCat)):
            # if Country.getName(self.countryCat[i])==c:
            if self.countryCat[i].getName() == c:
                return self.countryCat[i]
            else:
                None
        else:
            return False

    # method to find country and set its population
    def setPopulationOfCountry(self, c, p):
        # loop through each object
        flag = False
        for i in range(len(self.countryCat)):
            # if the name matches the country named passed(c) then do this
            if c == (self.countryCat[i].getName()):
                self.countryCat[i].setPopulation(p)
                flag = True
                return flag

    # method to find country and set its area
    def setAreaOfCountry(self, c, a):
        # find the country
        flag = False
        for i in range(len(self.countryCat)):
            # if the name passed is equal to the name in loop
            if c == (self.countryCat[i].getName()):
                # mutate the countries area
                self.countryCat[i].setArea(a)
                flag = True
                return flag

    # add new country
    def addCountry(self, country, population, area, continent):
        # make new country object
        newCountry1 = Country(country, population, area, continent)
        # define dictionary of country names
        countryNameList = {}
        # create a dictionary of country names
        for i in range(len(self.countryCat)):
            countryNameList[self.countryCat[i].getName()] = self.countryCat[i].getName()
        # if country already exists
        if country in countryNameList:
            return False

        # else do this
        else:
            self.countryCat.append(newCountry1)
            self.cDictionary[country] = [continent]
            return True

    # delete country object from catalogue
    def deleteCountry(self, country):
        # loop the country objects
        for i in range(len(self.countryCat)):
            # if the country name passed equals the name in loop
            if country == (self.countryCat[i].getName()):
                self.countryCat.remove(self.countryCat[i])
                del self.cDictionary[country]
                return
            else:
                pass

    # print out the catalogue
    def printCountryCatalogue(self):
        # print out catalogue in the format given
        print((self.countryCat))

    # get countries by population
    def getCountriesByContinent(self, continent):
        # define list for countries with same continent
        listCont = []

        # loop through all country objects
        for i in range(len(self.countryCat)):
            # if the countryobjects in loop is equal to the continent then do this
            if continent == self.countryCat[i].getContinent():
                # add that country object to the list
                listCont.append(self.countryCat[i])

        return listCont

    # gets countries by population and sort them
    def getCountriesByPopulation(self, a):
        # define the stuff
        popList = []
        contList = []
        MasterList = []

        # if no continent value is passed make a list of populations
        if a == "":
            for i in range(len(self.countryCat)):
                popList.append(int(self.countryCat[i].getPop()))

        else:
            for i in range(len(self.countryCat)):
                if a == self.countryCat[i].getContinent():
                    popList.append(int(self.countryCat[i].getPop()))

        # sort the population lists
        sortedPopulationList = sorted(popList, reverse=True)
        # match the population with the correct country
        for i in range(len(sortedPopulationList)):
            for j in range(len(self.countryCat)):

                # if the population matches add the country to a list contList and move to next population
                if int(sortedPopulationList[i]) == int(self.countryCat[j].getPop()):
                    contList.append(self.countryCat[j].getName())
                    # make a tuple with population,name
                    a = sortedPopulationList[i], self.countryCat[j].getName()
                    # add tuple to master list
                    MasterList.append(a)
                else:
                    pass
        return (MasterList)

    # get country by area and sort them
    def getCountriesByArea(self, a):
        # define the stuff
        popList = []
        contList = []
        MasterList = []

        # if no continent value is passed make a list of populations
        if a == "":
            for i in range(len(self.countryCat)):
                popList.append(float(self.countryCat[i].getArea()))

        elif a in self.cDictionary:
            for i in range(len(self.countryCat)):
                if a == self.countryCat[i].getContinent():
                    popList.append(float(self.countryCat[i].getArea()))

        # sort the population lists
        sortedPopulationList = sorted(popList, reverse=False)
        # match the population with the correct country
        for i in range(len(sortedPopulationList)):
            for j in range(len(self.countryCat)):
                # if the population matches add the country to a list contList and move to next population
                if float(sortedPopulationList[i]) == float(self.countryCat[j].getArea()):
                    contList.append(self.countryCat[j].getName())
                    a = sortedPopulationList[i], self.countryCat[j].getName()
                    MasterList.append(a)
                else:
                    pass
        return (MasterList)

    # find the most popolous continent
    def findMostPopulousContinent(self):
        # get list of continents
        maxPop = 0
        set1 = set()
        name = ""
        tempList = []
        tempNameList = []
        tempNameSet = set(tempNameList)
        MasterList = []
        # make a set of continents
        for country in self.countryCat:
            set1.add(country.getContinent())

        # now add populations, loop through set
        for continent in set1:
            contPop = 0
            for i in range(len(self.countryCat)):

                if self.countryCat[i].getContinent() == continent:
                    contPop = contPop + int(self.countryCat[i].getPop())
                    tempNameSet.add(self.countryCat[i].getContinent())
                    # tempNameList.append(self.countryCat.getContinent())
            tempList.append(contPop)
            # turn set back into list
            tempNameList = list(tempNameSet)

        # find max value in tempList
        maxPop = max(tempList)
        # find index
        index = tempList.index(maxPop)
        # name of max pop continent
        maxName = tempNameList[index]

        # print(tempList,tempNameList)
        maxCont = (maxName, maxPop)
        return maxCont

    # filter countries by population density
    def filterCountriesByPopDensity(self, LBound, upBound):
        denseList = []
        contList = []
        MasterList = []

        for i in range(len(self.countryCat)):
            if float(self.countryCat[i].getPopDensity()) < float(upBound) and float(
                    self.countryCat[i].getPopDensity()) > float(LBound):
                # add to dense list and sort it
                denseList.append(self.countryCat[i].getPopDensity())
        # sort the list
        sortedDenseList = sorted(denseList, reverse=True)
        for i in range(len(sortedDenseList)):
            for j in range(len(self.countryCat)):
                # if the population matches add the country to a list contList and move to next population
                if float(sortedDenseList[i]) == float(self.countryCat[j].getPopDensity()):
                    contList.append(self.countryCat[j].getName())
                    #instead of converting to string it was supposed to be left without any conversion
                    a = self.countryCat[j].getName(), (sortedDenseList[i])
                    MasterList.append(a)

        return (MasterList)

    # save the catalogue to a file and sort it alphabetically
    def saveCountryCatalogue(self, fileName):
        # open the file if not create else overwrite
        wFile = open(fileName, "w")
        # counter to see how many countries were written to
        numWritten = 0
        contList = []

        # make a alphabetically sorted country name list
        for i in range(len(self.countryCat)):
            contList.append(self.countryCat[i].getName())
        sortedContList = sorted(contList)
        # alphabetically write to file
        for i in range(len(self.countryCat)):
            for j in range(len(sortedContList)):
                if self.countryCat[j].getName() == sortedContList[i]:
                    wFile.write(
                        str(self.countryCat[j].getName()) + "|" + str(self.countryCat[j].getContinent()) + "|" + str(
                            self.countryCat[j].getPop()) + "|" + str(self.countryCat[j].getArea()).strip(
                            "\n") + "|" + '%.2f' % (self.countryCat[j].getPopDensity()) + "\n")
                    numWritten = numWritten + 1

        # close file we are done editing it
        wFile.close()
        # check to see how many files were written to it
        if numWritten == len(self.countryCat):
            return numWritten
        # else just return the number -1
        else:
            return -1
