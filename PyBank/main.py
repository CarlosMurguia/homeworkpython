# Modules
import os
import csv
import numpy
# Set path for file

months = []
revenue = []

csvpath = os.path.join(".", "raw_data", "budget_data_1.csv")
# This is the other data to work with:(Just erase the comment and put a comment in the up data)
# csvpath = os.path.join(".", "raw_data", "budget_data_2.csv") 
# Troubleshooting: My macbook doesnt read the files with ".." i must use "," just to clarify

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    next(csvreader, None)
    
    for row in csvreader:
      months.append(row[0])
      revenue.append(row[1])
      data = csvreader
    
    revenue  = [ int(x) for x in revenue ]
    max_reveneu = max(revenue)
    min_reveneu = min(revenue)

    print(min_reveneu)

    print(months)
     
    strMonths = "Total Months: " + str(len(months))
    max_revenue_month =  str(revenue.index(max_reveneu))
    min_revenue_month =  str(revenue.index(min_reveneu))

   

    strRevenue = "Total Reveneu: $" + str(sum(revenue))             
    strAverage = "Average Revenue Change: $" + str(numpy.mean(revenue))
    maxValue = ("Greatest Increase in Revenue: " + str(months[int(max_revenue_month)]) + " ($" + str(max(revenue)) + ")")
    minValue = ("Greatest Increase in Revenue: " + str(months[int(min_revenue_month)]) + " ($" + str(min(revenue)) + ")")
  
    print("```") 
    print("Financial Analysis") 
    print("----------------------------")    
    print(strMonths)
    print(strRevenue)
    print(strAverage)
    print(maxValue)
    print(minValue)
    
    print("```") 
        