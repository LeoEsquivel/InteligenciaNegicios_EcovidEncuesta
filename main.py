import pandas as pd

def leerCSV():
    return pd.read_csv('data/datos2020.csv', encoding='cp1252')

def ExportarCSV(dataFrame, nombre):
    dataFrame.to_csv("CSVExportados/"+nombre+".csv", index=False, encoding='cp1252')

#Pregunta 1.1 
def nivelEducativo(df):
    ExportarCSV(df["NIVEL_ACADEMICO"].dropna(), "001_NivelAcademico")


#Pregunta 1.2
def SexoYNivelEducativo(df):
    ExportarCSV(df.loc[:,['SEXO', 'NIVEL_ACADEMICO']], "002_NivelEducativoSexo")


#Pregunta 2.1
def InscritosCicloEscolar2019_2020(df):
    ExportarCSV(df["INSCRITO_CICLO_PASADO"].dropna(), "003_InscritosCicloEscolar2019_2020")


def InscritosCicloEscolar2019_2020_por_Sexo(df):
    dfFiltrado = df[df.INSCRITO_CICLO_PASADO.isin(['Si'])]
    ExportarCSV(dfFiltrado.loc[:, ['SEXO', 'EDAD']], "004_Inscritos_Ciclo_Escolar_2019_2020_por_Sexo")


#Pregunta 3.1
def dispositivoElectronicoMasUsado(df):
    dfFiltrado = df[df.INSCRITO_CICLO_PASADO.isin(['Si']) & df.DISPOSITIVO_PRINCIPAL_PARA_CLASES.notnull()]
    ExportarCSV(dfFiltrado.loc[:,['EDAD','NIVEL_ACADEMICO', 'DISPOSITIVO_PRINCIPAL_PARA_CLASES']], "005_dispositivo_Electronico_mas_Usado")


#Pregunta 4.1
def exclusividadDispositivosElectronicosCiclo_19_20(df):
    dfFiltradoExclusividadDispositivosUsados = df[df.NIVEL_ACADEMICO.notnull() & df.CALIDAD_DE_DISPOSITIVO.notnull()]
    ExportarCSV(dfFiltradoExclusividadDispositivosUsados.loc[:, ['NIVEL_ACADEMICO', 'CALIDAD_DE_DISPOSITIVO']], "006_Exclusividad_Dispositivos_Electronicos_Ciclo_19_20")
    

#Pregunta 5.1
def tipoEscuela(df):
    dFiltradoTipoEscuela = df[df.ESC_PRIVADA_O_PUBLICA.notnull()]
    ExportarCSV(dFiltradoTipoEscuela.loc[:,['NIVEL_ACADEMICO', 'ESC_PRIVADA_O_PUBLICA']], "007_Tipo_de_Escuela")


#Pregunta 6.1
def conclusionEscolarPorTipoDeEscuela(df):
    dFiltradoconclusionTipoEscuela = df[df.ESC_PRIVADA_O_PUBLICA.notnull() & df.TERMINO_CICLO_19_20.notnull()]
    ExportarCSV(dFiltradoconclusionTipoEscuela.loc[:,['SEXO', 'ESC_PRIVADA_O_PUBLICA', 'TERMINO_CICLO_19_20']], "008_Conclusion_Escolar_por_Tipo_de_Escuela")


#Pregunta 7.1
def razonPrincipalRelacionadaCovid(df):
    ExportarCSV(df['RAZON_NO_CONCLUSION_RELACIONADO_COVID'].dropna(), "009_Razon_Principal_No_Conclusion_Ciclo_Escolar_Relacionada_Covid")


#Pregunta 8.1
def motivoPrincipalNoInscribirseCiclo20_21(df):
    ExportarCSV(df['RAZON_PRINCIPAL_NO_CONCLUSION'].dropna(), "010_Razon_Principal_No_Inscribirse_Ciclo_20_21")

#Pregunta 9.1
def contactoConProfesores(df):
    dfFiltrado = df[df.MANTUVO_CONTACTO_PROFESORES.notnull() & df.ESC_PRIVADA_O_PUBLICA.notnull()]
    ExportarCSV(dfFiltrado.loc[:,['SEXO', 'ESC_PRIVADA_O_PUBLICA']], "011_Contacto_con_Profesores_Tipo_de_Escuela")


#Pregunta 10.1
def tiempoDeEstudio(df):
    ExportarCSV(df['HORAS_DEDICADAS_ESTUDIO'].dropna(), "012_Horas_Dedicadas_Estudio")


#Pregunta 11.1
def tiempoEstudioPorNivelEducativo(df):
    dFiltrado = df[df.HORAS_DEDICADAS_ESTUDIO.notnull() & df.NIVEL_ACADEMICO.notnull()]
    ExportarCSV(dFiltrado.loc[:,['HORAS_DEDICADAS_ESTUDIO', 'NIVEL_ACADEMICO']], "013_Tiempo_Estudio_por_Nivel_Educativo")


#Pregunta 12.1
def aceptacionVolverAClasesPresenciales(df):
    ExportarCSV(df['DISPONIBILIDAD_PRESENCIAL'].dropna(), "014_Aceptacion_Volver_a_Clases_Presenciales")


def Main():
    df = leerCSV()
    nivelEducativo(df)
    SexoYNivelEducativo(df)
    InscritosCicloEscolar2019_2020(df)
    InscritosCicloEscolar2019_2020_por_Sexo(df)
    dispositivoElectronicoMasUsado(df)
    exclusividadDispositivosElectronicosCiclo_19_20(df)
    tipoEscuela(df)
    conclusionEscolarPorTipoDeEscuela(df)
    razonPrincipalRelacionadaCovid(df)
    motivoPrincipalNoInscribirseCiclo20_21(df)
    contactoConProfesores(df)
    tiempoDeEstudio(df)
    tiempoEstudioPorNivelEducativo(df)
    aceptacionVolverAClasesPresenciales(df)


if __name__ == "__main__":
    Main()

