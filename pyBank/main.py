import os
import csv
import string


# Create the path of the file
csvpath=os.path.join('..','Resources','budget_data.csv')
csvpathwrite=os.path.join('..','Resources','budget_data_write.csv')
#Declare Varibled 
total=0
totalmonth=0
profitlist=[]
maxtotal=0
greatesChange=0.0
firstvalue=[]
difference=[0]
length=0
avg = 0
maxvalue=0
minvalue=0
dateValue=[]
maxDate=''
minDate=''
#Get the csv rows into the list

with open(csvpath,'r',newline='',encoding='utf8') as budgetfile:
     csvreader=csv.reader(budgetfile,delimiter=',')
     next(csvreader,None)
     for row in csvreader:
         total+=int(row[1])
         firstvalue.append(row[1])
         dateValue.append(row[0])
          
#Calculete differnce 
difference=[int(firstvalue[i]) - int(firstvalue[i-1]) for i in range(1, len(firstvalue))]
avg= sum(difference)/len(difference)+1

length=len(difference)
for j in range(1,length):
    if maxvalue < difference[j]:
        maxvalue=difference[j]
        maxDate=dateValue[j+1]
    if minvalue > difference[j]:
        minvalue=difference[j]
        minDate=dateValue[j+1]


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(dateValue)}")
print(f"Total: ${total}")
print(f"Average  Change: ${round(avg,2)}")
print(f"Greatest Increase in Profits: {maxDate}(${maxvalue})")
print(f"Greatest Decrease in Profits: {minDate}(${minvalue})")


with open(csvpathwrite,'w') as csvwriter:
    csvwrite=csv.writer(csvwriter,delimiter='\n')
    csvwrite.writerow("Financial Analysis")
    csvwrite.writerow("----------------------------")
    csvwrite.writerow(f"Total Months: {len(dateValue)}")
    csvwrite.writerow(f"Total: ${total}")
    csvwrite.writerow(f"Average  Change: ${round(avg,2)}")
    csvwrite.writerow(f"Greatest Increase in Profits: {maxDate}(${maxvalue})")
    csvwrite.writerow(f"Greatest Decrease in Profits: {minDate}(${minvalue})")





