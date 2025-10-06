# ====================================
# APP 03: TRABAJAR CON DATOS
# ====================================
# Conceptos: file uploader, pandas, dataframes, gráficos simples

# Importamos las bibliotecas necesarias:
# - streamlit: para crear la interfaz web
# - pandas: biblioteca principal para análisis de datos en Python
# - numpy: para operaciones numéricas avanzadas
import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Visualización de Datos")

# ====================================
# PARTE 1: CREAR Y MOSTRAR DATOS 
# ====================================

st.header("1. Crear un DataFrame")

# Crear datos de ejemplo (simulamos datos de ventas)
# Un DataFrame es como una tabla de Excel en Python.
# Lo creamos usando un diccionario donde las claves son los nombres de las columnas.
datos = {
    'Producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Auriculares'],
    'Precio': [899, 25, 79, 249, 159],
    'Cantidad': [15, 50, 30, 20, 35],
    'Categoría': ['Electrónica', 'Accesorios', 'Accesorios', 'Electrónica', 'Accesorios']
}

# Convertir a DataFrame de pandas
# pd.DataFrame() toma los datos y crea una estructura tabular.
df = pd.DataFrame(datos)

# Calcular una columna adicional
# Podemos crear nuevas columnas haciendo operaciones con las existentes.
df['Total'] = df['Precio'] * df['Cantidad']

# st.dataframe() - Mostrar tabla interactiva
# Muestra el DataFrame como una tabla que se puede ordenar y filtrar.
st.write("Tabla de productos:")
st.dataframe(df)
#st.table(df)  # Alternativa: tabla estática
#st.write(df)  # Alternativa: muestra básica
# ====================================
# PARTE 2: MÉTRICAS 
# ====================================

st.header("2. Métricas Importantes")

# st.metric() - Mostrar números destacados (KPIs)
# Las métricas son útiles para mostrar indicadores clave de rendimiento.
# st.columns() divide la página en columnas para organizar mejor el contenido.
col1, col2, col3 = st.columns(3)

with col1:
    total_productos = len(df)  # len() cuenta las filas del DataFrame
    st.metric("Total Productos", total_productos)

with col2:
    precio_promedio = df['Precio'].mean()  # .mean() calcula el promedio
    st.metric("Precio Promedio", f"€{precio_promedio:.2f}")

with col3:
    ventas_totales = df['Total'].sum()  # .sum() suma todos los valores
    st.metric("Ventas Totales", f"€{ventas_totales:,.0f}")

# ====================================
# PARTE 3: GRÁFICOS SIMPLES
# ====================================

st.header("3. Gráficos Básicos")

# Gráfico de barras - Precio por producto
# st.bar_chart() crea automáticamente un gráfico de barras.
# set_index() hace que 'Producto' sea el índice (etiquetas del eje X).
st.subheader("📊 Precio por Producto")
st.bar_chart(df.set_index('Producto')['Precio'])

# Gráfico de líneas - Cantidad por producto
# st.line_chart() crea un gráfico de líneas.
st.subheader("📈 Cantidad en Stock")
st.line_chart(df.set_index('Producto')['Cantidad'])

st.divider()

# ====================================
# PARTE 4: CARGAR ARCHIVOS CSV
# ====================================

st.header("4. Cargar tu Propio CSV")

# st.file_uploader() - Permite al usuario subir archivos
# Esto hace que la app sea más flexible, permitiendo datos personalizados.
archivo = st.file_uploader("Sube un archivo CSV", type=['csv'])

if archivo is not None:
    try:
        # Leer el archivo CSV
        # pd.read_csv() lee archivos CSV y los convierte en DataFrames.
        df_subido = pd.read_csv(archivo)
        
        st.success("✅ Archivo cargado correctamente")
        
        # Mostrar información básica
        # len(df) da el número de filas, len(df.columns) el número de columnas.
        st.write(f"**Filas:** {len(df_subido)} | **Columnas:** {len(df_subido.columns)}")
        
        # Mostrar primeras filas
        # .head() muestra las primeras 5 filas por defecto.
        st.write("Primeras 5 filas:")
        st.dataframe(df_subido.head())
        
        # Mostrar estadísticas si hay columnas numéricas
        # select_dtypes() filtra columnas por tipo de dato.
        columnas_numericas = df_subido.select_dtypes(include=[np.number]).columns
        
        if len(columnas_numericas) > 0:
            st.write("Estadísticas:")
            # .describe() calcula estadísticas básicas (media, desviación, etc.)
            st.dataframe(df_subido[columnas_numericas].describe())
            
            # Crear un gráfico simple con la primera columna numérica
            st.write("Gráfico de la primera columna numérica:")
            st.line_chart(df_subido[columnas_numericas[0]])
        
    except Exception as e:
        st.error(f"❌ Error al cargar el archivo: {str(e)}")
        st.info("💡 Asegúrate de que sea un archivo CSV válido")

else:
    st.info("👆 Sube un archivo CSV para comenzar")

# ====================================
# EJEMPLO DE CSV PARA PROBAR
# ====================================

st.divider()
st.header("💡 Consejo")
st.write("Si no tienes un CSV, puedes crear uno simple con estos datos:")

st.code("""
Nombre,Edad,Ciudad
Ana,25,Madrid
Luis,30,Barcelona
María,28,Valencia
Carlos,35,Sevilla
""", language="csv")

st.write("Copia esto en un archivo .txt, guárdalo como .csv y súbelo")
