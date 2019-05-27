#This program will read the amount of rain for each month from a .dat file.
#It will then ask the user the range of months that would like to diplay.
#The final output will be stats about the range selected and total data for the entire year.
#
#Nico Busatto 04/22/2019

from operator import itemgetter
import os
import time

def main():

    rainfall = []                                                #Create rainfall list
    try:
        #Create list 
        with open('rainfall.dat', 'r') as f:
            rainfall = f.read().splitlines()                         #Read and add data to list from .dat file
    except FileNotFoundError:
        print("File not found")
        print("Program ending, have a good one!")
        time.sleep(4)
        os._exit(1)
           
    for x in range(0, len(rainfall)): 
        rainfall[x] = float(rainfall[x])                         #Convert to list of floats from list of strings

    startMonth, endMonth, months = selectMonthRange(rainfall)    #Call selectMonthRange() method
    totRangeRainfall, avg, minMonth, maxMonth, final, totals = calcs(startMonth, endMonth, months, rainfall)   #Call calcs() method
    displayRainfall(startMonth, endMonth, months, totRangeRainfall, avg, minMonth, maxMonth, rainfall, final, totals)      #Call displayRainfall() method

def selectMonthRange(rainfall):

    ok = True
    
    while ok:                                                      #Validate user input
        try:
            startMonth = int(input("Enter starting month number: "))
            endMonth = int(input("Enter ending month number: "))
            ok = False
        except ValueError:
            print("Only numbers from 1 to 12")
                                                                  #Create list with months names                 
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
              "October", "November", "December"]

    return startMonth, endMonth, months

def calcs(start, end, months, rainfall):

    totRangeRainfall = 0
    avg = 0
    minIn = 0
    maxIn = 0
    totals = ()    #  <---- TUPLETUPLETUPLETUPLE  :)
    final = []
                                                             
    for x in range(start - 1, end):                                 #Add all values for final total
         totRangeRainfall += round((rainfall[x]), 2)

    totals = totals + (totRangeRainfall,)                           #Add final total to a Tuple as data storage
    
    avg = totRangeRainfall / ((end - start) + 1)                      #Calc average
    totals = totals + (avg,)                                        #Add avg to TUPLE

    minIn = min(enumerate(rainfall), key=itemgetter(1))[0]          #Obtain index of lowest and highest rainfall list values
    maxIn = max(enumerate(rainfall), key=itemgetter(1))[0]

    minMonth = months[minIn]                                        #Obtain month name of highest and lowest values
    maxMonth = months[maxIn]

    totals = totals + (minMonth, maxMonth,)                          #Add min and max month names to TUPLE

    for x in range(12):                                              #Create a unique list for month names and rainfall values
        final.append((months[x], rainfall[x]))

    return totRangeRainfall, avg, minMonth, maxMonth, final, totals

def displayRainfall(start, end, months, totRange, avg, min, max, rainfall, final, tots):

    print("")
    print("Starting month selected:", months[start - 1])            #Format and output all final results
    print("Ending month selected:", months[end - 1])
    print("The rainfall for the selected months is:", str(rainfall[start - 1:end:1]))
    print("The total average rainfall for the selected range is", str("{:.2f}".format(tots[1])), "inches")
    print("The total rainfall for the range of months selected is:", str("{:.2f}".format(tots[0])), "inches")
    print("The lowest amount of rain was is", tots[2])
    print("The highest amount of rain was in", tots[3])
    print("")
    print("List of months from highest to lowest rainfall:")
    print("")

    final = (sorted(final, key = lambda x: float(x[1]), reverse = True))              #Sort unique list by numeric values indexes
    for v in range(len(final)):
        print(final[v])                                                 #Print sorted final list
       
    print("")

main()