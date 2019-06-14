import os
import csv
import string
# Create the path of the file
csvpathRead='election_data.csv'
csvpathWrite='election_data.txt'
csvpath=os.path.join(csvpathRead)
csvpathwrite=os.path.join(csvpathWrite)
#Declare Varibale 
candidateKhan=[]
candidateCorrey=[]
candidateLi=[]
candidateTooley=[]
candidateAll=[]
votepercentKhan=0.00
votepercentcorrey=0.0
votpercenteli=0.00
votepercentTooley=0.00
totalofall=0
resultlist=[]
winner=''
maxvotepercent=0.0



#Get the csv rows into the list

with open(csvpath,'r',newline='',encoding='utf8') as budgetfile:
     csvreader=csv.reader(budgetfile,delimiter=',')
     next(csvreader,None)
     for row in csvreader:
        if row[2]=="Khan":
            candidateKhan.append(row[0])
           
        if row[2]=="Correy":
            candidateCorrey.append(row[0])
        if row[2]=="Li":
            candidateLi.append(row[0])
        if row[2]=="O'Tooley":
            candidateTooley.append(row[0])
        candidateAll.append(row[0])
        
    


votepercentKhan=round(len(candidateKhan)/len(candidateAll) * 100,3)
votepercentcorrey=round(len(candidateCorrey)/len(candidateAll) * 100,3)
votpercenteli=round(len(candidateLi)/len(candidateAll)*100 ,3)
votepercentTooley=round(len(candidateTooley)/len(candidateAll) *100,3)


maxvotepercent=votepercentKhan
winner='Khan'

if maxvotepercent < votepercentcorrey:
    winner='correy'
    maxvotepercent=votepercentcorrey
elif maxvotepercent < votpercenteli:
        winner='Li'
        maxvotepercent=votpercenteli
elif maxvotepercent < votepercentTooley:
         winner="O'Tooley"
         maxvotepercent=votepercentTooley
            
#Output

print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(candidateAll)}")
print("-------------------------")
print(f"Khan: {votepercentKhan}% ({len(candidateKhan)})")
print(f"Correy: {votepercentcorrey}% ({len(candidateCorrey)})")
print(f"Li: {votpercenteli}% ({len(candidateLi)})")
print(f"O'Tooley: {votepercentTooley}% ({len(candidateTooley)})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")



with open(csvpathwrite,'w',newline='') as csvwriter:
    csvwrite=csv.writer(csvwriter,delimiter='\n')
    csvwrite.writerow("Election Results")
    csvwrite.writerow("-------------------------")
    csvwrite.writerow(f"Total Votes: {len(candidateAll)}")
    csvwrite.writerow("-------------------------")
    csvwrite.writerow(f"Khan: {votepercentKhan}% ({len(candidateKhan)})")
    csvwrite.writerow(f"Correy: {votepercentcorrey}% ({len(candidateCorrey)})")
    csvwrite.writerow(f"Li: {votpercenteli}% ({len(candidateLi)})")
    csvwrite.writerow(f"O'Tooley: {votepercentTooley}% ({len(candidateTooley)})")
    csvwrite.writerow("-------------------------")
    csvwrite.writerow(f"Winner: {winner}")
    csvwrite.writerow("-------------------------")















