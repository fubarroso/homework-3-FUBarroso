import os
import csv
#set csv path
csvpath = os.path.join('..','Data','budget_data.csv')
#open csv
with open(csvpath, newline='') as csvfile:
    #read csv
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #reset counters set lists
    numberOfMonths=0    
    totalAmountProfitLoss=0
    prevProfit=0
    revenueChanges = []
    dates= []
    increaseMax=0
    decreaseMax=0
    #print output header
    print("---------------------")
    print("Financial Analysis")
    print("---------------------")
    #cycle through rows count number of months,sum all profits
    for row in csvreader:
        numberOfMonths=numberOfMonths+1
        totalAmountProfitLoss=totalAmountProfitLoss+int(row[1])
        #create a list of profit changes from month to month
        revenueChanges.append(int(row[1])-prevProfit)
        prevProfit=int(row[1])
        #create a list of the dates
        dates.append(row[0])
        
    #output number of months and total Profits/Loss
    print(f"Total Months: {numberOfMonths}")
    print(f"Total: ${totalAmountProfitLoss}")
    #Eliminate first item of changes list. Can not calculate a change from month before Jan 2010
    revenueChanges.pop(0)
    #Add all profit changes , calculate and print average rounding to 2 decimals
    totalRevenueChanges=sum(revenueChanges)
    averageMonthlyChange=totalRevenueChanges/(numberOfMonths-1)
    averageMonthlyChangeTwoDecimal=round(averageMonthlyChange,2)
    print(f"Average Change: ${averageMonthlyChangeTwoDecimal}")
    #go through changes to find min and max. Record index
    for change in range(len(revenueChanges)):
        if revenueChanges[change]>increaseMax:
            increaseMax=revenueChanges[change]
            maxIndex=change
        if revenueChanges[change]<decreaseMax:
            decreaseMax=revenueChanges[change]
            minIndex=change
    #Print biggest increase and biggest decrease in profit. Use index print dates from dates list.
    print(f"Greatest Increase in Profits: {dates[maxIndex+1]} (${increaseMax})")
    print(f"Greatest Decrease in Profits: {dates[minIndex+1]} (${decreaseMax})")
    
f= open("report.txt","w+")
f.write("---------------------\nFinancial Analysis\n---------------------\n")
f.write(f"Total Months: {numberOfMonths}\n")
f.write(f"Total: ${totalAmountProfitLoss}\n")
f.write(f"Average Change: ${averageMonthlyChangeTwoDecimal}\n")
f.write(f"Greatest Increase in Profits: {dates[maxIndex+1]} (${increaseMax})\n")
f.write(f"Greatest Decrease in Profits: {dates[minIndex+1]} (${decreaseMax})\n")
f.close() 