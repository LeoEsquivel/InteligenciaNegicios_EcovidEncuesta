import pandas as pd
from pandas.core import indexing

def leerCSV():
    print("Leyendo csv")
    return pd.read_csv('data/datos2020.csv', encoding='latin-1')

def ExportarCSV(dataFrame, nombre):
    dataFrame.to_csv(nombre, index=False, encoding='latin-1')

#Pregunta 1.1
def nivelEducativo(df):
    #Nivel Educativo
    return df["NIVEL_ACADEMICO"].dropna()

#Pregunta 1.2
def SexoYNivelEducativo(df):
    #Filtro por sexo y nivel educativo no sea vacio
    filterH = df[df.SEXO.isin(['Hombre']) & df.NIVEL_ACADEMICO.notnull()]
    filterM = df[df.SEXO.isin(['Mujer']) & df.NIVEL_ACADEMICO.notnull()]
    return (nivelEducativo(filterH), nivelEducativo(filterM))

#Pregunta 2.1
def InscritosCicloEscolar2019_2020(df):
    
    return df["INSCRITO_CICLO_PASADO"].dropna()

def InscritosCicloEscolar2019_2020_por_Sexo(df):
    filterH = df[df.SEXO.isin(['Hombre']) & df.EDAD.notnull()]
    filterM = df[df.SEXO.isin(['Mujer']) & df.EDAD.notnull()]

def Main():
    df = leerCSV()
    sexo_nivel_edu = SexoYNivelEducativo(df)
    #ExportarCSV(sexo_nivel_edu[0], "Nivel_Edu_Hombres.csv")



if __name__ == "__main__":
    Main()

