# import modules 
import os
import csv

# declare the list for two columns
month_list = []
profit_Losses_list = []

csvPath = os.path.join("..", "Resources", "02-Homework_03-Python_PyBank_Resources_budget_data.csv")
with open(csvPath, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip the header
    row = next(csvreader)
    
    # append column values to corresponding lists
    monthCount = 0
    for row in csvreader:
        month_list.append(row[0])
        profit_Losses_list.append(row[1])
        monthCount = monthCount + 1

    # geting total profit/loss value
    totalValue = 0 
    for i in profit_Losses_list:
        totalValue = totalValue + int(i)

    # using the same index number of two lists to access information
    maxIncrease = 0
    maxDecrease = 0
    # compare values via loop, till the max/min is found   
    for i in range(len(profit_Losses_list)):
        if int(profit_Losses_list[i]) > maxIncrease:
            maxIncrease = int(profit_Losses_list[i])
            greatestIncreaseMonth = month_list[i]
        if int(profit_Losses_list[i]) < maxDecrease:
             maxDecrease = int(profit_Losses_list[i])
             greatestDecreaseMonth = month_list[i]

    # get the average
    averageChange = round (totalValue / monthCount, 2)          
# print analysis table in the terminal 
print("-------------------------------------------------------------")
print("|Financial Analysis|")
print("|-------------------------------------------------------------")
print("|Total Months: " + str(monthCount)+"|") 
print("|Total:" +" $"+ str(totalValue)+"|")
print("|Average Change:" + " $"+ str(averageChange)+"|")
print("|Greatest Increase in Profits: " + str(greatestIncreaseMonth) + " ($" + str(maxIncrease) + ")"+"|")
print("|Greatest Decrease in Profits: " + str(greatestDecreaseMonth) + " ($" + str(maxDecrease) + ")"+"|")
print("-------------------------------------------------------------")

# pirnt out text table
textoutput = os.path.join('..', 'Analysis table', 'PyBank_final.txt')
with open (textoutput, 'w', newline='') as resultTable:
    write = csv.writer(resultTable)
    write.writerows([
        ["-------------------------------------------------------------"],
        ["|Financial Analysis|"],
        ["|-------------------------------------------------------------"],
        ["|Total Months: " + str(monthCount)+"|"], 
        ["|Total:" +" $"+ str(totalValue)+"|"],
        ["|Average Change:" + " $"+ str(averageChange)+"|"],
        ["|Greatest Increase in Profits: " + str(greatestIncreaseMonth) + " ($" + str(maxIncrease) + ")"+"|"],
        ["|Greatest Decrease in Profits: " + str(greatestDecreaseMonth) + " ($" + str(maxDecrease) + ")"+"|"],
        ["-------------------------------------------------------------"],
    ])    
