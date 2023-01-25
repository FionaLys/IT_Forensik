import pandas as pd
#import graphen
from Darstellung import graphen

dict = {'input': [-3,0,2,-1,-2,3,1], 'output': [-1,+1,-1,+1,-1,-1,+1]}
df = pd.DataFrame.from_dict(dict)
df['ii'] = df['input']**2
df['ii'] = df['input']**3


def weight_vector(df):
    geschafft = 1
    i = 0
    w_vector = (1,0,0)
    while geschafft<8:
        w0 = w_vector[0]
        w1 = w_vector[1]
        w2 = w_vector[2]
        x0 = 1
        x1 = list(df['input'].values)[i]
        x2 = list(df['input'].values)[i] **2
        output = list(df['output'].values)[i]
        # klassifizierung wird ausgerechnet
        result = w0 * x0 + w1 * x1 +w2 * x2
        print(result)
        if result >= 0:
            value = +1
        else:
            value = -1
        # mit echten werten vergleichen und möglicherweise gewichtsvektor anpassen
        if value==output:
            geschafft+=1
        else:
            geschafft = 1
            w_vector = (w_vector[0]+(value*x0),w_vector[1]+(value*x1),w_vector[2]+(value*x2))
        if i>=6:
            i=0
        else:
            i+=1
    print(w_vector)

#weight_vector(df)

def classifier(value):
    pass


print(graphen.plotting(df, 'value'))