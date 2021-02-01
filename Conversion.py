
'''
fieldmap : {
        k : {
        k2 : {k3 : v3},
        k2 : {k3 : v3}
        },
        etc.
        }
Where k is the newcolname, k2 is the desired value, k3 is the col name with current info and v3 is the old value
k, k3 must be strings
k2 must be string or int
v3 must be string, int, or list of strings or ints

      
  
colnames : {
        newcolname : type,
        etc.
        }
Where type = 'checkbox','radio','yesno', or the oldcolname if it's a text field
newcolname and type must both be strings 

'''


import argparse as ap
import pandas as pd

parser = ap.ArgumentParser(description = 'Converts column names and values')
parser.add_argument('data', help = 'Excel file to be converted')
parser.add_argument('dicts', help = 'File containing your dictionaries')
parser.add_argument('fieldmap', help = 'Dictionary containing values')
parser.add_argument('colnames', help = 'Dictionary containing column names')
parser.add_argument('outfile', help = 'Desired name for converted file')

args = parser.parse_args()
args = parser.parse_args(''.split(' '))
    
data = args.data
dicts = args.dicts
fieldmap = args.fieldmap
colnames = args.colnames
outfile = args.outfile

file = pd.read_excel(data)

#Check that all old colnames are correct
missing = []
for k, v in fieldmap.items():
    for k2, v2 in v.items():
        for k3, v3 in v2.items():
            if k3 not in file.columns:
                missing.append(k3)
for k, v in colnames.items():
    if v != 'checkbox' and v != 'yesno' and v != 'radio':
        if v not in file.columns:
            missing.append(v)
if missing != []:
    print('The following columns are not in your data file: ' + str(missing))

check_dict = {k:v for k, v in fieldmap.items() if dict.get(colnames, k) == 'checkbox'}
ynr_dict = {k:v for k, v in fieldmap.items() if dict.get(colnames, k) == 'yesno' or dict.get(colnames, k) == 'radio'}
text_dict = {k:v for k, v in colnames.items() if dict.get(colnames,k) != 'checkbox' and dict.get(colnames,k) != 'yesno' and dict.get(colnames,k) != 'radio'}
kl = []

if missing == []:

#   TEXT
    for k, v in text_dict.items():
        file[k] = file[v]
        kl.append(k)

#   YESNO RADIO
    for k, v in ynr_dict.items():
        for k2, v2 in v.items():
            for k3, v3 in v2.items():
                if isinstance(v3,int) or isinstance(v3,str):
                    file.loc[file[k3] == v3, k] = k2
                    kl.append(k)                    
                if isinstance(v3,list):
                    for v4 in v3:
                        file.loc[file[k3] == v4, k] = k2
                        
#   CHECKBOX
    for k, v in check_dict.items():
        for k2, v2 in v.items():
            for k3, v3 in v2.items():
                if isinstance(v3,int) or isinstance(v3,str):
                    file.loc[file[k3] == v3, k+'___'+str(k2)] = '1'
                    kl.append(k+'___'+str(k2))
                if isinstance(v3,list):
                    for v4 in v3:
                        file.loc[file[k3] == v4, k+'___'+str(k2)] = '1'
                        kl.append(k+'___'+str(k2))

#   REMOVE ALL THE OLD COLUMNS
    for k, v in colnames.items():
        kl.append(k)
    for col in file:
        if col not in kl:
            file = file.drop(columns = col)
        
    file.to_csv('outfile.csv', index = False)
