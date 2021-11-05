import pandas as pd
from pandas.core import indexing

def leerCSV():
    print("Leyendo csv")
    return pd.read_csv('data/datos2020.csv', encoding='latin-1')

def ExportarCSV(dataFrame, nombre):
    dataFrame.to_csv(nombre, index=False, encoding='latin-1')

#Pregunta 1.1 #Nivel Educativo
def nivelEducativo(df):
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


#Pregunta 3.1
def dispositivoElectronicoMasUsado(df):
    dfFiltrado = df[df.INSCRITO_CICLO_PASADO.isin(['Si']) & df.DISPOSITIVO_PRINCIPAL_PARA_CLASES.notnull()]
    return dfFiltrado.loc[:,['EDAD','NIVEL_ACADEMICO', 'DISPOSITIVO_PRINCIPAL_PARA_CLASES']]


#Pregunta 4.1
def exclusividadDispositivosElectronicosCiclo_19_20(df):
    dfFiltradoExclusividadDispositivosUsados = df[df.NIVEL_ACADEMICO.notnull() & df.CALIDAD_DE_DISPOSITIVO.notnull()]
    return dfFiltradoExclusividadDispositivosUsados.loc[:, ['NIVEL_ACADEMICO', 'CALIDAD_DE_DISPOSITIVO']]
    

#Pregunta 5.1
def tipoEscuela(df):
    dFiltradoTipoEscuela = df[df.ESC_PRIVADA_O_PUBLICA.notnull()]
    return dFiltradoTipoEscuela.loc[:,['NIVEL_ACADEMICO', 'ESC_PRIVADA_O_PUBLICA']]


#Pregunta 6.1
def conclusionEscolarPorTipoDeEscuela(df):
    dFiltradoconclusionTipoEscuela = df[df.ESC_PRIVADA_O_PUBLICA.notnull() & df.TERMINO_CICLO_19_20.notnull()]
    return dFiltradoconclusionTipoEscuela.loc[:,['SEXO', 'ESC_PRIVADA_O_PUBLICA', 'TERMINO_CICLO_19_20']]


#Pregunta 7.1
def razonPrincipalRelacionadaCovid(df):
    return df['RAZON_NO_CONCLUSION_RELACIONADO_COVID'].dropna()


#Pregunta 8.1
def motivoPrincipalNoInscribirseCiclo20_21(df):
    return df['RAZON_PRINCIPAL_NO_CONCLUSION'].dropna()

#Pregunta 9.1
def contactoConProfesores(df):
    dfFiltrado = df[df.MANTUVO_CONTACTO_PROFESORES.notnull & df.ESC_PRIVADA_O_PUBLICA.notnull()]
    return dfFiltrado.loc[:,['SEXO', 'ESC_PRIVADA_O_PUBLICA']]


#Pregunta 10.1
def tiempoDeEstudio(df):
    return df['HORAS_DEDICADAS_ESTUDIO'].dropna()


#Pregunta 11.1
def tiempoEstudioPorNivelEducativo(df):
    dFiltrado = df[df.HORAS_DEDICADAS_ESTUDIO.notnull & df.NIVEL_ACADEMICO.notnull()]
    return dFiltrado.loc[:,['HORAS_DEDICADAS_ESTUDIO', 'NIVEL_ACADEMICO']]


#Pregunta 12.1
def aceptacionVolverAClasesPresenciales(df):
    return df['DISPONIBILIDAD_PRESENCIAL'].dropna()


def Main():
    df = leerCSV()
    #sexo_nivel_edu = SexoYNivelEducativo(df)
    #ExportarCSV(sexo_nivel_edu[0], "Nivel_Edu_Hombres.csv")
    print(conclusionEscolarPorTipoDeEscuela(df))



if __name__ == "__main__":
    Main()

