
# %%
import shutil
import os
import datetime
import pandas as pd
import openpyxl




df=pd.read_excel("C:\\Users\\luis.lizana\\Downloads\\Reporte_644.xlsx")
df=df.loc[(df["ESTADO_PLAN"]=="p_guardado") & (df["USUARIO_EM"]=="GONZALO ALBERTO MONTES ACEVEDO")]
df=df.reset_index(drop=True)


df2=pd.DataFrame()
df2["Asunto"]="Formalizar EAF "+df["NUMERO_EAF"]+": "+df["NOMBRE_OBJETO"]
df2["Fecha de inicio"]=df["FECHA_REQ"]
df2["Fecha de vencimiento"]=df["FECHA_FINALIZACION_PLAN"]
df2["Prioridad"]=0
df2["% Completado"]=0
df2["Estado"]="No comenzada"
df2["Categoría"]="Categoría púrpura"
df2["Mensaje"]=df["REQ_ID"]
df2.to_excel("salida_indice_644_v1.xlsx", index=False)

# %%
