#analyzes tweets from text file and compares to keywords file and determines happiness value and assorts each tweet to a specific region.
#mshaik52 250959996

#import graphics from graphics
from graphics import GraphicsWindow

from happy_histogram import drawSimpleHistogram,drawHappyFace,drawSadFace

#create dictionary and arrays
keywords={}
sentimentTotal=[]
pacific=[]
mountain=[]
eastern=[]
central=[]

#define main function
def main():
    #call function to create dictionary of keywords
    keyFile()

    #exception to see if file input is valid
    try:
        #input file name and open file
        fileInput=input("Enter a file name")
        file=open(fileInput,"r",encoding="utf-8")
        #while loop is true keep reading lines
        flag=True
        while flag==True:
            total=0
            #read the line and split it into array
            line=file.readline()
            data=line.split()
            #if reach end of file set flag to false else keep looping through each line
            if line=="":
                flag=False
            else:
                #print(data)
                matches=0
                for i in range (len(data)):
                    lowerWord=data[i].lower()
                    lowerWord=lowerWord.strip(".,!?#:;'")
                    #print(lowerWord)
                    if lowerWord in keywords:
                        #print("sentiment for word",data[i],keywords[lowerWord])
                        total=total+keywords[lowerWord]
                        matches=matches+1
                #if the number of words matched is greater than 0 calculate sentiment and location using long and lat and add to specific array
                if matches>0:
                    #print("number of matches",matches)
                    avg=total/matches
                    #print(total,avg)
                    sentimentTotal.append(avg)

                    lat=float(data[0].strip("[],"))
                    long=float(data[1].strip("[],"))

                    #print(lat)
                    #print(long)
                    if (lat <= 49.189787 and lat >= 24.6606845 and long>=-87.518395 and long <=-67.444574):
                        #print("tweet is in eastern time zone")
                        eastern.append(avg)
                    elif (lat <=49.189787 and lat >= 24.6606845 and long >-101.998892 and long <-87.518395):
                        #print("tweet is in central time zone")
                        central.append(avg)
                    elif (lat<= 49.189787 and lat >= 24.6606845 and long>-115.236428 and long <=-101.998892):
                        #print("tweet is in Mountain time zone")
                        mountain.append(avg)
                    elif (lat <=49.189787 and lat >=24.6606845 and long>=-125.242264 and long<=-115.236428):
                        #print("tweet is in Pacific time zone")
                        pacific.append(avg)
                #if tweet has no matching words then do nothing
                else:
                    pass

        eHappiness=sum(eastern)/len(eastern)
        cHappiness=sum(central)/len(central)
        mHappiness=sum(central)/len(central)
        pHappiness=sum(central)/len(central)

        #final output, output the happiness score and total number of tweets for each location
        print("The Happiness score for each Eastern is:", round(sum(eastern)/len(eastern),2))
        print("The Happiness score for Central is:", round(sum(central)/len(central),2))
        print("The Happiness score for Mountain is:", round(sum(mountain)/len(mountain),2))
        print("The Happiness score for Pacific is:", round(sum(pacific)/len(pacific),2))
        print("\n\n")
        print("The total Eastern Tweets are", len(eastern ))
        print("The total Central Tweets are",len(central))
        print("The total Mountain Tweets are",len(mountain))
        print("The total Pacific Tweets are", len(pacific))
        print("\n\n")
        # print("The total Happiness score for Eastern is:",round(sum(eastern),2))
        # print("The total Happiness score for Central is: ", round(sum(central),2))
        # print("The total Happiness score for Mountain is:", round(sum(mountain),2))
        # print("The total Happiness score for Pacific is:", round(sum(pacific),2))

        #draw a histogram of the happiness value of each timezone
        drawSimpleHistogram(eHappiness,cHappiness,mHappiness,pHappiness)
        file.close()



    #exceptions for handling invalid file name and zero divison
    except IOError:
        print("Invalid file name")
    except ZeroDivisionError:
        print("Divided by zero")

#define method to create dictionary of keywords
def keyFile():
    try:
        i=0
        #take keywords file and append to dictionary keywords
        kInput=input("Enter the Keywords file name")
        key = open(kInput, "r")
        flag = True
        while flag == True:
            line = key.readline()
            data = line.split(",")
            if line == "":
                flag = False
            else:
                keywords[data[0]] = int(data[1])
    except IOError:
        print("invalid File Name")
        main()
    key.close()
#end of program
main()
