import pandas as pd
import numpy as np



def find_mean_age(Sex,Typ):
    return temp.loc[(temp['Sex']==Sex)&(temp['Typ']==Typ),'Age']

if __name__ =='__main__':
    df = pd.DataFrame({'Id':[1,2,3,4,5,6],
                   'Sex':['male','male','female','male','female','female'],
                   'Age':[21,float('NAN'),float('NAN'),23,56,32],
                   'Typ':['A','A','V','V','V','V']})
    print(df)

    temp = df.loc[(df['Age'].notnull())&(df['Age'] < 65 ),
                ['Age','Sex','Typ']].groupby(['Sex','Typ'],as_index=False).mean()

    df.loc[df['Age'].isnull(), ['Age']] = df.apply(lambda row: find_mean_age(row['Sex'], row['Typ'][0]),
                                                   axis=1)
qqssssssssssssssssssssssss
    print(df)