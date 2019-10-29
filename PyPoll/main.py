# import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvfile ='C:/Users/hxl08/OneDrive/Desktop/WUSTL-STL-DATA-PT-10-2019-U-C/03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv'
# Reading using CSV module
with open(csvfile, newline='') as election_data:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(election_data, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)    
    #set the initial value for row_count,Khan,Correy,Li,OTolley
    row_count=0
    Khan=0
    Correy=0
    Li=0
    OTolley=0
    #create list for candidate
    candidate=["Khan","Correy","Li","O'Tooley"]
    # Read each row of data after the header
    for row in csvreader:
        row_count+=1
        if candidate[0]==row[2]:
            Khan+=1
        elif candidate[1]==row[2]:
            Correy+=1
        elif candidate[2]==row[2]:
            Li+=1
        elif candidate[3]==row[2]:
            OTolley+=1
#     print(row_count)  
#     print(Khan)
#     print(Khan/row_count)
#     print(Correy)
#     print(Correy/row_count)
#     print(Li)
#     print(Li/row_count)    
#     print(OTolley)
#     print(OTolley/row_count)
    
    #print texts
    print("Election Results")
    print("------------------------")
    print("Total Votes:", row_count)
    print("------------------------")
    print(candidate[0],":","%.3f%%" % (Khan/row_count*100), "(",Khan,")")
    print(candidate[1],":","%.3f%%" % (Correy/row_count*100), "(",Correy,")")
    print(candidate[2],":","%.3f%%" % (Li/row_count*100), "(",Li,")")
    print(candidate[3],":","%.3f%%" % (OTolley/row_count*100), "(",OTolley,")")
    print("------------------------")
    print("Winner:", candidate[0])
