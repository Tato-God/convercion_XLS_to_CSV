import pandas as pd

def getData():
    df = pd.read_excel(r'C:\Users\Don Tato\Desktop\Ejemplo Convercion XLS to CSV\excel\dataconvert.xlsx')

    df.to_csv(r'C:\Users\Don Tato\Desktop\Ejemplo Convercion XLS to CSV\csv\dataconvert.csv', index=None, header=True)

    # print(df)
    return df


getData()