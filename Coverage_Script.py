
import pandas as pd
import numpy as np
import re
import argparse as ap

parser = ap.ArgumentParser(description = 'Checks coverage of all columns')
parser.add_argument('data', help = 'Excel file to check the coverage of')

args = parser.parse_args()
args = parser.parse_args(''.split(' '))

data = args.data

file = pd.read_excel(data)
nocbs = pd.read_excel(data)

cbs = pd.DataFrame()
samecb = pd.DataFrame()



#Make check_dict
counter = 0
checkboxes = []
for col in file.columns:
    if re.search('___97',col) != None or re.search('___98',col) != None or re.search('___99',col) != None or re.search('___100',col) != None:
        del file[col]
        del nocbs[col]
for col in file.columns:
    if re.search('___\d*',col) != None:
        checkboxes.append(col)
        del nocbs[col]
        cbs[col] = file[col]
    while counter < len(checkboxes):
        checkboxes[counter] = re.sub('___\d*','',checkboxes[counter])
        counter += 1
    counter = 0
check_dict = {i:checkboxes.count(i) for i in checkboxes}

#Remake checkboxes so they have correct digits
file = pd.read_excel('outfile.xlsx')
nocbs = pd.read_excel('outfile.xlsx')
cbs = pd.DataFrame()
checkboxes = []
for col in file.columns:
    if re.search('___97',col) != None or re.search('___98',col) != None or re.search('___99',col) != None or re.search('___100',col) != None:
        del file[col]
        del nocbs[col]
for col in file.columns:
    if re.search('___\d*',col) != None:
        checkboxes.append(col)
        del nocbs[col]
        cbs[col] = file[col]


#Make cbcovs
counter = 1
checkcount = 0
cbcovs = []
for k, v in check_dict.items():
    while counter <= v:
        dig = re.findall('\d*$',checkboxes[checkcount])
        digit = dig[0]
        samecb[str(k) + '___' + str(digit)] = file[str(k) + '___' + str(digit)]
        counter += 1
        checkcount += 1
    samecb = samecb.replace(0,np.nan)
    samecb = samecb.dropna(how='all')
    cbcovs.append(len(samecb))
    samecb = pd.DataFrame()
    counter = 1
    
allcounts = []    

#Record cb coverages
counter = 0
for k, v in check_dict.items():
    allcounts.append(str(k) + '  :  ' + str(int((cbcovs[counter] / 93) * 100)) + ' % coverage')
    counter += 1

#All you need for non-cb 
covcounts = []
for notnull in nocbs.count():
    covcounts.append(notnull) 
counter = 0
for col in nocbs:
    allcounts.append(str(col) + '  :  ' + str(int((covcounts[counter] / 93) * 100)) + ' % coverage')
    counter += 1

with open('All_Coverages.txt','w') as writeout:
    for cov in allcounts:
        writeout.write('%s\n' % cov)
        
