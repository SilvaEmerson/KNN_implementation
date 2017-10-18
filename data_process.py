import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

descrip = {1:'ID',
         2:'Clump Thickness',
         3:'Uniformity of Cell Size',
         4:'Uniformity of Cell',
         5:'Marginal Adhesion',
         6:'Single Epithelial Cell Size',
         7:'Bare Nuclei',
         8:'Bland Chromatin',
         9:'Normal Nucleoli',
         10:'Mitoses',
         11:'Class'
         }

data = pd.read_csv('data/data.txt')

#columns = [list(range(1,12))]

#data.columns = columns
columns = []

for i in descrip.keys():
    name = descrip[i].split()
    name = [j[0] for j in name]
    name = ''.join(name)
    columns.append(name.upper())

data.columns = columns
data.drop('I', axis=1, inplace=True)

#print(len([i for i in data.BN i]))


#verify the index of missing values
tratable_columns = []
for i in range(len(data.dtypes)):
    if data.dtypes[i] == 'object':
        tratable_columns.append(columns[i+1])

# print(tratable_columns)



# #adicionar regex aqui
# #print(data[tratable_columns].values.tolist())
# print(data.BN.values.tolist().count('?'))
cleanData = data.copy()
for i in range(len(data.BN)):
    if( data.BN[i] == '?'):
        cleanData.drop(i, axis = 0, inplace=True)

# print(data.shape)
# print(cleanData.shape)
cleanData.BN = cleanData.BN.astype('int64')
cleanData = cleanData.values.tolist()

print(cleanData[0])
