# import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
#Get current working directory
cwkdir = os.getcwd()
#Append file directory and make a complete file path
csvpath = os.path.join( cwkdir,'Resources','election_data.csv')

# Reading using CSV module
with open(csvpath, newline='') as election_data:
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
    #create empty list for votes for further append
    votes=[]
    # Read each row of data after the header
    for row in csvreader:
        row_count+=1
        if candidate[0]==row[2]:
            Khan+=1
        if candidate[1]==row[2]:
            Correy+=1
        if candidate[2]==row[2]:
            Li+=1
        if candidate[3]==row[2]:
            OTolley+=1
    votes.append(Khan)
    votes.append(Correy)
    votes.append(Li)
    votes.append(OTolley)
#     print(row_count)  
#     print(Khan)
#     print(Khan/row_count)
#     print(Correy)
#     print(Correy/row_count)
#     print(Li)
#     print(Li/row_count)    
#     print(OTolley)
#     print(OTolley/row_count)
    #find winner based on the index of max votes
    winner = candidate[votes.index(max(votes))]

    #print texts
    print("Election Results")
    print("------------------------")
    print("Total Votes:", row_count)
    print("------------------------")
    print(f'{candidate[0]}:{"%.3f%%" % (Khan/row_count*100)} ({Khan})')
    print(f'{candidate[1]}:{"%.3f%%" % (Correy/row_count*100)}({Correy})')
    print(f'{candidate[2]}:{"%.3f%%" % (Li/row_count*100)}({Li})')
    print(f'{candidate[3]}:{"%.3f%%" % (OTolley/row_count*100)}({OTolley})')
    print("------------------------")
    print("Winner:", winner)
