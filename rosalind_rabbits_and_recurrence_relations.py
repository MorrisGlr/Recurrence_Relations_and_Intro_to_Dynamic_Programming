global months
months = 33
upperlimit = months + 1
ReproRate = 5
timeline = []
totalpopulation = 0
thesavana = {}                              #this dictionary will act as the ledger that tracks how many rabit pairs there are
while 0 < months < upperlimit:              #this loop runs until the number of months hits zero.
    months = months - 1                     #each time the loop runs it subtracts 1 from the value of months and reassigns a value until it hits 0
    timeline.append(months)                 #each time the loop runs it adds the new value into an unpopualted list that I designated as 'timeline' which represents months
timeline = timeline[::-1]                  #I reversed the order so that the numbers in the list are in ascending order within thesavana
for i in timeline:                          #loops through every list item
    timeline[i] += 1                        #technically unnecessary but starts the timeline at 1 instead of 0 and shifts the other numbers by one
for i in timeline:
    thesavana[i] = {'immature': 0,
                    'mature': 0}            #this is the template for the embeded dictionaries that reprsent the generations by months in thesavana dict.
thesavana[1]['immature'] = 1                #this indicates that thesavana begins with 1 pair of wabbits
for i in timeline:                          #this is the begginning of the number crunching on a per month basis
    if i > 1:
        k = i - 1                           #k represents the previous generation/month population and I am transfering data between generations
        thesavana[i]['mature'] = thesavana[k]['immature'] + thesavana[k]['mature']      #transfer the immature from a previous generation to the newlymature category for the next generation
        thesavana[i]['immature'] = thesavana[k]['mature']*ReproRate                     #last month's mature pool will multiply by the ReproRate and will be the CURRENT month's immature population
        totalpopulation = thesavana[i]['immature'] + thesavana[i]['mature']             #caluates the total each month but the value will ultimately land on the last month.
print(totalpopulation)
