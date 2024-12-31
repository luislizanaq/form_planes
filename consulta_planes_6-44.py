
# %%
import pandas as pd
import openpyxl
import streamlit as st


st.title("📄 Índice de Planes de Acción SEC V1.0")
file = st.file_uploader("Sube el reporte general Planes de Accion plataforma SEC (.xlsx)", type=("xlsx"))


if file is not None and file.name.startswith("ReporteGeneralFuncionarioEmpresa"):

  df=pd.read_excel(file)
  columns=df.loc[0]
  columns=columns.reset_index(drop=True)
  df=df.rename(columns=dict(zip(df.columns, columns)))
  df=df.drop(df.index[:1])
  df=df.reset_index(drop=True)
  option = st.selectbox("Selecciona al ingeniero/a DAOP",
    ("GONZALO ALBERTO MONTES ACEVEDO", "JONATHAN ANDRÉS MARABOLÍ BALTIERRA", "DIEGO JOAQUIN ORELLANA LINEROS", "PABLO ANTONIO PALMA VILLAGRÁN", "JUAN PABLO ANDRÉS CASTILLO MIRANDA", "JORGE LUIS GALLEGOS MELLADO"), )
  df=df.loc[(df["ESTADO_PLAN"]=="p_guardado") & (df["USUARIO_EM"]==option)]
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
  st.dataframe(df2)

# %%
