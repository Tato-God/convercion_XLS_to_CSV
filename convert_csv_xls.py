import pandas as pd

# VERSION ANTIGUA
def getData():
    df = pd.read_csv(r'C:\Users\Don Tato\Desktop\Ejemplo Convercion XLS to CSV\csv\emails.csv')
    df2 = pd.ExcelWriter(r'C:\Users\Don Tato\Desktop\Ejemplo Convercion XLS to CSV\excel\emails.xlsx')

    df.to_excel(df2, index=False)

    df2.close()
    
    msm = "Se convirtio el archivo CSV a XLSX"
    return msm




getData()