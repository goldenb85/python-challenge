# import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
#Get current working directory
cwkdir = os.getcwd()
#Append file directory and make a complete file path
csvpath = os.path.join( cwkdir,'Resources','budget_data.csv')

# Reading using CSV module

with open(csvpath, newline='') as budget_data:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_data, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)    
        
    #set the initial value for total and row_count
    total=0
    row_count=0
    #create list for profit_loss and date
    profit_loss=[]
    date=[]
    
    # Read each row of data after the header
    for row in csvreader:
        
        total+=int(row[1])
        row_count+=1
        profit_loss.append(int(row[1]))
        date.append(row[0])
#     print(total)
#     print(row_count)  
    #create list for change and avg_change
    change=[]
    avg_change=[]
    #for loop to calculate change between two consecutive rows and average change
    for i in range(1,len(profit_loss)):
        change.append(profit_loss[i]-profit_loss[i-1])
        avg_change=sum(change)/len(change)
        #find the max change and min change
        change_max=max(change)
        change_min=min(change)
        #use index function to find the dates of max change and min change
        max_date=date[change.index(max(change))+1]
        min_date=date[change.index(min(change))+1]
#     print(avg_change)
#     print(change_max)
#     print(change_min)
#     print(max_date)
#     print(min_date)
    #print texts
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", row_count)
    print("Total: $", total)
    print("Avereage Change: $", round(avg_change,2))
    print("Greatest Increase in Profits:", max_date,"($", change_max,")")
    print("Greatest Decrease in Profits:", min_date,"($", change_min,")")
