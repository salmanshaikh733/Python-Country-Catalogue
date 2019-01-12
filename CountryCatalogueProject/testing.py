from catalogue import *
from country import *

def testFindCountry(countryCatalog,test):
    x = 0
    cntryObj = countryCatalog.findCountry("Canada")
    if cntryObj.getName() == "Canada":
        x = 4
    cntryObj = countryCatalog.findCountry("NoName") # should return None
    if cntryObj is None:
        x = x + 1
    if x == 0:
        print("*** Test "+str(test)+" failed.")
    elif x == 1:
        print("*** Test "+str(test)+" partially succeeded.")
    else:
        print("*** Test "+str(test)+" passed.")
    return x

def testSetPopulationOfCountry(countryCatalog,test):
    # Assumes that FindCountry works
    x = 0
    # Use Canada for testing: original value = 34,207,000
    cPop = 34207999
    itemFound = countryCatalog.setPopulationOfCountry("Canada",cPop)
    if itemFound:
       cntryObj = countryCatalog.findCountry("Canada")
       if cntryObj.getPopulation() == cPop:
           x = 1.0
           print("*** Test "+str(test)+" setting population of existing country passed.")
       else:
           x = 0.2 # did return True, but changing population failed
           print("*** Test "+str(test)+" setting population of existing partially succeeded.")
    cPop = 1
    itemFound = countryCatalog.setAreaOfCountry("NoName",cPop)
    if not itemFound:
        x = x + 1.0
        print("*** Test "+str(test)+" for setting population of non-existing country passed.")
    else:
        print("*** Test "+str(test)+" for setting population of non-existing country failed.")
    return x

def testSetAreaOfCountry(countryCatalog,test):
    # Assumes that FindCountry works
    x = 0
    # Use Canada for testing: original value = 9,975,140
    cSz = 9976200.0
    itemFound = countryCatalog.setAreaOfCountry("Canada",cSz)
    if itemFound:
       cntryObj = countryCatalog.findCountry("Canada")
       if (float(cntryObj.getArea()) < cSz+2) and (float(cntryObj.getArea()) > cSz-2):
           x = 1.0
           print("*** Test "+str(test)+" for setting area of existing country passed.")
       else:
           x = 0.2 # did return True, but changing area failed
           print("*** Test "+str(test)+" for setting area existing country partially succeeded.")
    cSz = 0
    itemFound = countryCatalog.setAreaOfCountry("NoName",cSz)
    if not itemFound:
        x = x + 1.0
        print("*** Test "+str(test)+" for setting area of non-existing country passed.")
    else:
        print("*** Test "+str(test)+" for setting area non-existing country failed.")
    return x

def testAddCountry(countryCatalog,test):
    # Assumes that FindCountry works
    x = 0
    # try adding a country
    cntry = "Sweden"
    cPop = 65668129.0
    cSz = 641656.0
    theCont = "Europe"
    itemFound = countryCatalog.addCountry(cntry,cPop,cSz,theCont)
    if itemFound: # country doesn't exist - was it added correctly?
       cntryObj = countryCatalog.findCountry(cntry)
       if cntryObj.getPopulation() == cPop and cntryObj.getArea() == cSz and cntryObj.getContinent() == theCont:
           x = 2.0
           print("*** Test "+str(test)+" adding country passed.")
       else:
           x = 0.0 # returned false - didn't add?
           print("*** Test "+str(test)+" adding country failed.")
    # Now .. try adding existing country
    cntry = "France"
    cPop = 11111111
    cSz = 123455678
    theCont = "Europe"
    itemFound = countryCatalog.addCountry(cntry,cPop,cSz,theCont)
    if not itemFound:
        # return value indicates country already exists - good - but check to see if no change - just check Pop
       cntryObj = countryCatalog.findCountry(cntry)
       if cntryObj.getPopulation() != cPop:
           x = x + 2.0
           print("*** Test "+str(test)+" adding existing country passed.")
       else:
           # looks like a change happened
           x = x + 0.2
           # returned "exisitng" flag, but some change happened
           print("*** Test "+str(test)+" adding existing country partially succeeded.")
    else:  # uh-oh - flag indicates country was added
        # return value indicates country already exists - good - but check to see if no change - just check Pop
       cntryObj = countryCatalog.findCountry(cntry)
       if cntryObj.getPopulation() == cPop:
           print("*** Test "+str(test)+" adding existing country failed - country added.")
       else:
           # maybe just wrong flag
           x = x + 0.2 # returned "not exisitng" flag, but no change happened
           print("*** Test "+str(test)+" adding existing country partially succeeded.")
    return x

def testDeleteCountry(countryCatalog,test):
    # Assumes that FindCountry works
    x = 0
    # try adding a country
    cntry = "China"
    countryCatalog.deleteCountry(cntry)
    cntryObj = countryCatalog.findCountry(cntry)
    if cntryObj is None:  # shouldn't find Egypt
        x = 2.0
        print("*** Test "+str(test)+" deleting existing country passed.")
    else:
        x = 0.0 # Egypt was found ... didn't delete
        print("*** Test "+str(test)+" deleting existing country failed.")
    # Now .. try deleting a non-existing country
    cntry = "NoName"
    countryCatalog.deleteCountry(cntry)
    cntryObj = countryCatalog.findCountry(cntry)
    if cntryObj is None:  # shouldn't find NoName
        x = x + 2.0
        print("*** Test "+str(test)+" deleting non-existing country passed.")
    else:
        # Not sure what was found ... didn't delete
        print("*** Test "+str(test)+" deleting existing country failed.")
    return x

def testGetCountriesByContinent(countryCatalog,test):
    # checks to see if France and Italy are in Europe
    lst = countryCatalog.getCountriesByContinent("Europe")
    nameList = [lst[0].getName(),lst[1].getName()]
    if len(lst) > 0:
        if "France" in nameList and "Italy" in nameList:
            x = 4.0
            print("*** Test "+str(test)+" for countries from continent passed.")
        else:
            x = 0.2 # returned a list, but not correct
            print("*** Test "+str(test)+" for countries from continent partially passed.")
    else:
        x = 0
        print("*** Test "+str(test)+" for countries from continent failed.")
    return x

def testGetCountriesByArea(countryCatalog,test):
    # checks entire list
    # checks Canada, China and Brazil - should be in positions 1,3,4 ... expecting list to be sorted
    lst = countryCatalog.getCountriesByArea("")
    # returns a list of pairs - hopefully
    if len(lst) > 0:
        if isinstance(lst[0][0], Country):
            if "Canada" == lst[0][0].getName() and "China" == lst[2][0].getName() and "Brazil" == lst[3][0].getName():
                x = 3.0
                print("*** Test " + str(test) + " for countries by area passed.")
            else:
                x = 1.0  # returned a list, give some marks
                print("*** Test " + str(test) + " for countries by area partially passed.")
        else:
            if "Canada" == lst[0][0] and "China" == lst[2][0] and "Brazil" == lst[3][0]:
                x = 3.0
                print("*** Test "+str(test)+" for countries by area passed.")
            else:
                x = 1.0 # returned a list, give some marks
                print("*** Test "+str(test)+" for countries by area partially passed.")
    else:
        x = 0.0
        print("*** Test "+str(test)+" for countries by area failed.")
    # now check list on continent - uses Europe
    # checks France and Italy - should be in positions 1,2 ... expecting list to be sorted
    lst = countryCatalog.getCountriesByArea("Europe")
    # returns a list of pairs - hopefully
    if len(lst) > 0:
        if isinstance(lst[0][0], Country):
            if "France" == lst[0][0].getName() and "Italy" == lst[1][0].getName():
                x = x + 3.0
                print("*** Test " + str(test) + " for countries in Europe by area passed.")
            else:
                x = x + 1.0  # returned a list, give some marks
                print("*** Test " + str(test) + " for countries in Europe by area partially passed.")
        else:
            if "France" == lst[0][0] and "Italy" == lst[1][0]:
                x = x + 3.0
                print("*** Test "+str(test)+" for countries in Europe by area passed.")
            else:
                x = x + 1.0 # returned a list, give some marks
                print("*** Test "+str(test)+" for countries in Europe by area partially passed.")
    else:
        print("*** Test "+str(test)+" for countries in Europe by area failed.")
    return x

def testGetCountriesByPopulation(countryCatalog,test):
    # checks on entire list first
    # checks China, Brazil and Japan - should be in positions 1,4,7 ... expecting list to be sorted
    lst = countryCatalog.getCountriesByPopulation("")
    # returns a list of pairs - hopefully
    if len(lst) > 0:
        if isinstance(lst[0][0], Country):
            if "China" == lst[0][0].getName() and "Brazil" == lst[3][0].getName() and "Japan" == lst[6][0].getName():
                x = 3.0
                print("*** Test " + str(test) + " for countries by population passed.")
            else:
                x = 1.0  # returned a list, give some marks
                print("*** Test " + str(test) + " for countries by population partially passed.")
        else:
            if "China" == lst[0][0] and "Brazil" == lst[3][0] and "Japan" == lst[6][0]:
                x = 3.0
                print("*** Test "+str(test)+" for countries by population passed.")
            else:
                x = 1.0 # returned a list, give some marks
                print("*** Test "+str(test)+" for countries by population partially passed.")
    else:
        x = 0
        print("*** Test "+str(test)+" for countries by population failed.")
    # checks on list from Africa
    # checks Nigeria and Egypt - should be in positions 1,2 ... expecting list to be sorted
    lst = countryCatalog.getCountriesByPopulation("Africa")
    # returns a list of pairs - hopefully
    if len(lst) > 0:
        if isinstance(lst[0][0], Country):
            if "Nigeria" == lst[0][0].getName() and "Egypt" == lst[1][0].getName():
                x = x + 3.0
                print("*** Test " + str(test) + " for countries in Africa by population passed.")
            else:
                x = x + 1.0  # returned a list, give some marks
                print("*** Test " + str(test) + " for countries in Africa by population partially passed.")
        else:
            if "Nigeria" == lst[0][0] and "Egypt" == lst[1][0]:
                x = x + 3.0
                print("*** Test "+str(test)+" for countries in Africa by population passed.")
            else:
                x = x + 1.0 # returned a list, give some marks
                print("*** Test "+str(test)+" for countries in Africa by population partially passed.")
    else:
        print("*** Test "+str(test)+" for countries in Africa by population failed.")
    return x

def testFindMostPopulousContinent(countryCatalog,test):
    rslt = countryCatalog.findMostPopulousContinent()
    if len(rslt) > 0:
        if "Asia" == rslt[0]:
            x = 4.0
            print("*** Test "+str(test)+" for most populous continent passed.")
        else:
            x = 0.2 # returned a tuple, give some marks
            print("*** Test "+str(test)+" for most populous continent partially passed.")
    else:
        x = 0
        print("*** Test "+str(test)+" for most populous continent failed.")
    return x

def testFilterCountriesByPopDensity(countryCatalog,test):
    # checks on entire list - lower bound of 0 and upper bound of 30 - should be Canada and Brazil with
    #   densities of 3.4 and 22.7, approximately.
    x = 0.0
    rlst = countryCatalog.filterCountriesByPopDensity(0,30)
    if len(rlst) == 0:
        print("*** Test "+str(test)+" for population density look up failed.")
    else:
        brazilTest = "Brazil" == rlst[0][0] and rlst[0][1] < 25.0 and rlst[0][1] > 20.0
        canadaTest = "Canada" == rlst[1][0] and rlst[1][1] < 5.0 and rlst[1][1] > 2.0
        if brazilTest and canadaTest:
            x = 4.0
            print("*** Test "+str(test)+" for population density passed.")
        else:
            x = 0.2 # returned a list, give some marks
    return x

def testGetCountriesByContinent2(countryCatalog,test):
    # after adding Sweden, checks to see if Sweden, France and Italy are in Europe
    lst = countryCatalog.getCountriesByContinent("Europe")
    nameList = [lst[0].getName(),lst[1].getName(), lst[2].getName()]
    if len(lst) > 0:
        if "France" in nameList and "Italy" in nameList and "Sweden" in nameList:
            x = 4.0
            print("*** Test "+str(test)+" (post-updates) for countries from continent passed.")
        else:
            x = 0.2 # returned a list, but not correct
            print("*** Test "+str(test)+" (post-updates) for countries from continent partially passed.")
    else:
        x = 0
        print("*** Test "+str(test)+" (post-updates) for countries from continent failed.")
    return x

def testGetCountriesByArea2(countryCatalog,test):
    # checks entire list
    # with China removed, checks Canada, Brazil - should be in positions 1,3 ... expecting list to be sorted
    lst = countryCatalog.getCountriesByArea("")
    # returns a list of pairs - hopefully
    if len(lst) > 0:
        if isinstance(lst[0][0], Country):
            if "Canada" == lst[0][0].getName() and "Brazil" == lst[2][0].getName():
                x = 3.0
                print("*** Test "+str(test)+" (post-updates) for countries by area passed.")
            else:
                x = 1.0 # returned a list, give some marks
                print("*** Test "+str(test)+" (post-updates) for countries by area partially passed.")
        else:
            if "Canada" == lst[0][0] and "Brazil" == lst[2][0]:
                x = 3.0
                print("*** Test " + str(test) + " (post-updates) for countries by area passed.")
            else:
                x = 1.0  # returned a list, give some marks
                print("*** Test " + str(test) + " (post-updates) for countries by area partially passed.")
    else:
        x = 0.0
        print("*** Test "+str(test)+" (post-updates) for countries by area failed.")
    # now check list on continent - uses Europe
    # Sweden was added to be largest ... should be in position 1 ... expecting list to be sorted
    lst = countryCatalog.getCountriesByArea("Europe")
    # returns a list of pairs - hopefully
    if len(lst) > 0:
        if isinstance(lst[0][0], Country):
            if "Sweden" == lst[0][0].getName():
                x = x + 3.0
                print("*** Test "+str(test)+" (post-updates) for countries in Europe by area passed.")
            else:
                x = x + 1.0 # returned a list, give some marks
                print("*** Test "+str(test)+" (post-updates) for countries in Europe by area partially passed.")
        else:
            if "Sweden" == lst[0][0]:
                x = x + 3.0
                print("*** Test " + str(test) + " (post-updates) for countries in Europe by area passed.")
            else:
                x = x + 1.0  # returned a list, give some marks
                print("*** Test " + str(test) + " (post-updates) for countries in Europe by area partially passed.")
    else:
        print("*** Test "+str(test)+" (post-updates) for countries in Europe by area failed.")
    return x

def testGetCountriesByPopulation2(countryCatalog,test):
    # checks on entire list
    # China should have been removed, so Brazil and Nigeria should be in positions 3,4 ... expecting list to be sorted
    lst = countryCatalog.getCountriesByPopulation("")
    # returns a list of pairs - hopefully
    if len(lst) > 0:
        if isinstance(lst[0][0], Country):
            if "Brazil" == lst[2][0].getName() and "Nigeria" == lst[3][0].getName():
                x = 3.0
                print("*** Test " + str(test) + " (post-updates) for countries by population passed.")
            else:
                x = 1.0  # returned a list, give some marks
                print("*** Test " + str(test) + " (post-updates) for countries by population partially passed.")
        else:
            if "Brazil" == lst[2][0] and "Nigeria" == lst[3][0]:
                x = 3.0
                print("*** Test "+str(test)+" (post-updates) for countries by population passed.")
            else:
                x = 1.0 # returned a list, give some marks
                print("*** Test "+str(test)+" (post-updates) for countries by population partially passed.")
    else:
        x = 0
        print("*** Test "+str(test)+" (post-updates) for countries by population failed.")
    # checks on list from Europe
    # after adding Sweden, Sweden should be #1 in Europe ... expecting list to be sorted
    lst = countryCatalog.getCountriesByPopulation("Europe")
    # returns a list of pairs - hopefully
    if len(lst) > 0:
        if isinstance(lst[0][0], Country):
            if "Sweden" == lst[0][0].getName():
                x = x + 3.0
                print("*** Test " + str(test) + " (post-updates) for countries in Europe by population passed.")
            else:
                x = x + 1.0  # returned a list, give some marks
                print(
                    "*** Test " + str(test) + " (post-updates) for countries in Europe by population partially passed.")
        else:
            if "Sweden" == lst[0][0]:
                x = x + 3.0
                print("*** Test "+str(test)+" (post-updates) for countries in Europe by population passed.")
            else:
                x = x + 1.0 # returned a list, give some marks
                print("*** Test "+str(test)+" (post-updates) for countries in Europe by population partially passed.")
    else:
        print("*** Test "+str(test)+" (post-updates) for countries in Europe by population failed.")
    return x

def testFindMostPopulousContinent2(countryCatalog,test):
    rslt = countryCatalog.findMostPopulousContinent()
    if len(rslt) > 0:
        if "North America" == rslt[0]:
            x = 4.0
            print("*** Test "+str(test)+" (post-updates) for most populous continent passed.")
        else:
            x = 0.2 # returned a tuple, give some marks
            print("*** Test "+str(test)+" (post-updates) for most populous continent partially passed.")
    else:
        x = 0
        print("*** Test "+str(test)+" (post-updates) for most populous continent passed.")
    return x

def testSaveCatalog(countryCatalog,fname,test):
    try:
        nitems = countryCatalog.saveCountryCatalogue(fname)
        if nitems == 14:
            x = 4.0 # wrote the correct number
        elif nitems > 0:
            x = 1.0 # wrote something successfully to a file
        else:
            x = 0.0
        # do second part of test ... if there was something written
        # now ... we'll try to read the first couple of lines and check
        if nitems > 0:
            line1 = "Brazil|South America|193364000|8511965.00|22.72"
            line2 = "Canada|North America|34207999|9976200.00|3.43"
            testf = open(fname,"r")
            tline1 = testf.readline().strip()
            tline2 = testf.readline().strip()
            if line1 == tline1 and line2 == tline2:
                x = x + 6.0
            else:
                x = x + 2.0
            if x > 8.0:
                print("*** Test "+str(test)+" saving catalog passed.")
            else:
                print("*** Test "+str(test)+" saving catalog partially passed.")
        return x
    except:
        x = 0
        print("*** Test "+str(test)+" saving catalog failed.")
        return x

def main():
    score = 0.0
    points = 0.0
    print()
    print("Program Testing")
    print("---------------")
    print()

    # +++++++++++++++++ Initial Test - manual - but critical
    # if this test fails, then not clear how remaining tests will fare ...
    # test #1 - manual
    # read files and print catalog
    print("Test #1 - Manual - Review output from initial catalog; Critical.")
    cc = CountryCatalogue('data.txt', 'continent.txt')
    # print initial catalogue
    cc.printCountryCatalogue()
    print()
    chk = input("Enter Y if OK, N otherwise: ")
    points = 2.0
    if chk == "Y":
        score = 2.0

    # +++++++++++++++++ Phase 2 Test - look up country
    # test #2 - look up country - 5 points
    # really critical that this method works
    points = points + 5.0
    x = testFindCountry(cc,2)
    score = score + x

    # +++++++++++++++++ Phase 3 Tests - check collection information before any changes
    # test #3 - countries by continent - Europe is test
    points = points + 4.0
    x = testGetCountriesByContinent(cc,3)
    score = score + x

    # test #4 - countries by area
    points = points + 6.0
    x = testGetCountriesByArea(cc,4)
    score = score + x

    # test #5 - countries by population
    points = points + 6.0
    x = testGetCountriesByPopulation(cc,5)
    score = score + x

    # test #6 - countries by population density
    points = points + 4.0
    x = testFilterCountriesByPopDensity(cc,6)
    score = score + x

    # test #7 - find most populous country
    points = points + 4.0
    x = testFindMostPopulousContinent(cc,7)
    score = score + x

    # +++++++++++++++++ Phase 4 Tests - make changes to catalogue
    # test #8 - set area 2 point
    points = points + 2.0
    x = testSetAreaOfCountry(cc,8)
    score = score + x

    # test #9 - set population 2 point
    points = points + 2.0
    x = testSetPopulationOfCountry(cc,9)
    score = score + x

    # test #10 - add a country - 4 points
    points = points + 4.0
    x = testAddCountry(cc,10)
    score = score + x

    # test #11 - delete a country - 4 points
    points = points + 4.0
    x = testDeleteCountry(cc,11)
    score = score + x


    # +++++++++++++++++ Phase 5 Tests - check catalog information after changes
    # test 12 - countries by continent - Europe is test
    points = points + 4.0
    x = testGetCountriesByContinent2(cc,12)
    score = score + x

    # test #13 - countries by area
    points = points + 6.0
    x = testGetCountriesByArea2(cc,13)
    score = score + x

    # test #14 - countries by population
    points = points + 6.0
    x = testGetCountriesByPopulation2(cc,14)
    score = score + x

    # test #15 - countries by population density
    points = points + 4.0
    x = testFindMostPopulousContinent2(cc,15)
    score = score + x

    # +++++++++++++++++ Phase 6 Tests - final check of catalog information from file
    # test 16 - save catalog to a file
    points = points + 10.0
    #cc.printCountryCatalogue()
    x = testSaveCatalog(cc,"cattest.txt",16)
    score = score + x

    print()
    print("+++++++ Scores +++++++")
    print(str(score)+" out of a maximum of "+str(points))
    print("+++++++       +++++++")
    print("TEST COMPLETED")

main()
