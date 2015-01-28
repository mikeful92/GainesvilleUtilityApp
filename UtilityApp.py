"""
Created by mikeful92
Date: 01/28/2015

This program access a comma separated value file called 'GRU_Customer_Electric_Consumption.csv'

It then used an adress stored in addr 
(Format: Address should be in all uppercase and exclude city, state, and zip code)

It parses through the file using a module called csv and finds all instances of addr.

Next it uses a function to organize the data for addr. 
It adds up all three years and makes a list of monthly averages
It also makes a list of all 2014 comsumption at addr. 

Last it uses a module called prettytable to organize the data into a table and output it.
"""

#Two modules needed
#'csv' to parse through the csv file
import csv
# PrettyTable function inside of prettytable module to visualy setup data for output
from prettytable import PrettyTable

#This function opens the file, loads it with csv and returns the 'data'
def Load():
    #Opens file into 'f', first argument is the name of the file, second argument('r') means read only
    f = open('GRU_Customer_Electric_Consumption.csv', 'r')
    print 'File open'

    #Uses the function DictReader inside of module csv to read the file.
    #This will create a dictionary that can be access by giving an index with the column name
    #We will iterate through data in the next function
    data = csv.DictReader(f)
    print 'File read'
    #Now we just return it. 
    return data
    
#This function will iterate through data and find every entry that we are looking for.
#It will take in the addr you are looking for and the data from the load() function 
def Parse(addr, data):
    #Conumption_list will be a list of list with every entry for addr
    consumption_list = []

    #This will go through every line in the data. Each line will be called row.
    for row in data:
        #Now that we pick a specific line (row), we can access a specific field by name.
        #'ServiceAddress' is the name of the column in the csv file.
        #So row['ServiceAdress'] will give us the address of the row we are looking at.
        #The following line assings that addrress to a string variable called row_addr
        row_addr = row['ServiceAddress']
        #Next line we see if the row's adress(row_addr) matches the address(addr) we are looking for    
        if row_addr == addr:
            #Now we append the a list of the row that matches the address to the consumption list
            #We ask for only 'Month', 'Year', and integer of 'KWH Consumption'
            consumption_list.append([row['Month'], row['Year'], int(row['KWH Consumption'])])

    #Return the list of compsumption for addr
    return consumption_list


#Organize() will set up the data into two list that we need: average and 2014
def Organize(consumption_list):
    #months two dimensional list will be used to find the sum of three years for each month
    months = [['January',0],['February',0],['March',0],['April',0],['May',0],['June',0],['July',0],['August',0],['September',0],['October',0],['November',0],['December',0]]
    #month_list will be assigned the name of the months, this will be used by the table to create the left most column
    month_list = []
    #We will loop through the months list and find the three year average of each
    average_list = []
    #list_2014 will hold the monthly consumption for only 2014
    list_2014 = []

    #First we iterate through each monthly entry in consumption_list
    for entry in consumption_list:
        #In the parse function we appended each entry by month, year and consumption
        #Now we will access the second index in entry to get the year
        #Then compare the year to '2014' to find all 2014 entries
        if entry[1] == '2014':
            #For entries that are in '2014' we append the consumption to a 2014 list
            list_2014.append(entry[2])

        for month in months:
            #Now we go through the list of months and see if the entry's month matches.
            if month[0] == entry[0]:
                #If it does match, we add it to the total consumption of that month
                month[1] += entry[2]

    # Monthly average
    for month in months:
        #We divide the total consumption of each month by 3
        month[1] /= 3

        #Append the month to the month_list to have the left column
        #Append the average to the average_list
        month_list.append(month[0])
        average_list.append(month[1])

    return month_list, average_list, list_2014

def Table(month_list, average_list, list_2014):
    #Creates a PrettyTable object under the name 'table'
    table = PrettyTable()

    #Adds each column based on the given column lable and the matching list
    table.add_column('Month', month_list)
    table.add_column('Average', average_list)
    
    #There is a bug with the data, there might not be an entry for each month
    #I will try to fix this as soon as possible
    #To fix this we make sure than len(list_2014) is 12

    if len(list_2014) < 12:
        #Appned 0 if not complete (size of 12)
        for x in range(12-len(list_2014)):
            list_2014.append(0)
    table.add_column('2014', list_2014)

    return table


def Main():        
    #The address you are looking for
    addr = '521 NE 6TH ST'

    #Load data
    data = Load()

    #Parse data
    consumption_list = Parse(addr, data)

    #Organize data
    month_list, average_list, list_2014 = Organize(consumption_list)

    #create table
    table = Table(month_list, average_list, list_2014)

    ## Output data
    print 'Consumption data at', addr
    print table


#This is just a standard procedue which makes sure to execute the complete code if it is executed as its own program
if __name__ == '__main__':
    Main()

