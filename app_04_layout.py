# ====================================
# APP 04: LAYOUT Y ORGANIZACIÓN
# ====================================
# Conceptos: columnas, sidebar, tabs básico

# El layout se refiere a cómo organizamos visualmente los elementos en la página.
# Un buen layout hace que la aplicación sea más fácil de usar y entender.
# Streamlit ofrece herramientas como columnas, sidebar y tabs para organizar el contenido.

import streamlit as st
import pandas as pd
import numpy as np

st.title("🎨 Layout y Organización")

# ====================================
# PARTE 1: COLUMNAS 
# ====================================

st.header("1. Columnas")

st.write("Las columnas permiten organizar contenido lado a lado:")

# Crear 3 columnas de igual ancho
# st.columns() divide la página horizontalmente en secciones.
# El número indica cuántas columnas crear (todas del mismo ancho).
col1, col2, col3 = st.columns(3)

# Agregar contenido a cada columna
# Usamos 'with' para especificar qué va en cada columna.
with col1:
    st.subheader("Columna 1")
    st.write("Contenido de la primera columna")
    st.button("Botón 1")

with col2:
    st.subheader("Columna 2")
    st.write("Contenido de la segunda columna")
    st.button("Botón 2")

with col3:
    st.subheader("Columna 3")
    st.write("Contenido de la tercera columna")
    st.button("Botón 3")

# Columnas con anchos diferentes
st.write("También puedes hacer columnas de diferentes anchos:")

# Pasando una lista con proporciones relativas
col_izq, col_der = st.columns([2, 1])  # La izquierda es el doble de ancha

with col_izq:
    st.write("Esta columna es más ancha (2/3 del espacio)")
    np.random.seed(42)  # Fijar semilla para reproducibilidad
    # Crear datos aleatorios para el gráfico
    # np.random.randn() genera números aleatorios con distribución normal.
    datos = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    st.line_chart(datos)

with col_der:
    st.write("Esta columna es más estrecha (1/3 del espacio)")
    st.metric("Métrica 1", "100")
    st.metric("Métrica 2", "200")

st.divider()

# ====================================
# PARTE 2: SIDEBAR (10 min)
# ====================================

st.header("2. Sidebar (Barra Lateral)")

st.write("El sidebar aparece a la izquierda 👈 y es ideal para controles")

# Todo lo que pongas con st.sidebar aparecerá en la barra lateral
# El sidebar es útil para controles que afectan toda la aplicación,
# como filtros, configuraciones o navegación.
st.sidebar.title("⚙️ Panel de Control")
st.sidebar.write("Este es el sidebar")

# Agregar widgets al sidebar
# Los widgets en el sidebar funcionan igual que en el contenido principal.
nombre_sidebar = st.sidebar.text_input("Tu nombre:")
if nombre_sidebar:
    st.sidebar.success(f"¡Hola {nombre_sidebar}!")

edad_sidebar = st.sidebar.slider("Tu edad:", 0, 100, 25)
st.sidebar.write(f"Tienes {edad_sidebar} años")

# Radio buttons en el sidebar
# Los radio buttons permiten navegación entre secciones.
pagina = st.sidebar.radio(
    "Navega a:",
    ["Inicio", "Datos", "Configuración"]
)

# Mostrar contenido diferente según la selección
# Esto demuestra cómo el sidebar puede controlar el contenido principal.
st.info(f"Estás en la página: **{pagina}**")

st.divider()

# ====================================
# PARTE 3: TABS
# ====================================

st.header("3. Tabs (Pestañas)")

st.write("Las tabs organizan contenido en pestañas:")

# Crear 3 pestañas
# st.tabs() crea pestañas que permiten organizar contenido relacionado
# sin sobrecargar una sola página.
tab1, tab2, tab3 = st.tabs(["📊 Gráficos", "📋 Datos", "ℹ️ Info"])

# Contenido de cada tab
# Cada tab puede tener su propio contenido independiente.
with tab1:
    st.subheader("Gráfico de Ejemplo")
    
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Serie A', 'Serie B', 'Serie C']
    )
    st.line_chart(chart_data)

with tab2:
    st.subheader("Tabla de Datos")
    
    datos_tabla = pd.DataFrame({
        'Producto': ['A', 'B', 'C', 'D'],
        'Ventas': [100, 200, 150, 300],
        'Stock': [50, 30, 40, 20]
    })
    st.dataframe(datos_tabla)

with tab3:
    st.subheader("Información")
    st.write("Esta es una app de demostración de Streamlit")
    st.write("Creada en el Bootcamp de Data & IA")
    st.success("✅ Las tabs ayudan a organizar mucha información")

st.divider()

# ====================================
# EJEMPLO COMPLETO: TODO JUNTO
# ====================================

st.header("4. Ejemplo Completo")

st.write("Combinando sidebar + columnas + contenido:")

# Filtro en el sidebar
st.sidebar.divider()
st.sidebar.subheader("Filtros")
cantidad_datos = st.sidebar.slider("Cantidad de datos a mostrar:", 5, 50, 20)

# Generar datos según el slider
# Los datos se regeneran cada vez que cambia el slider.
datos_random = pd.DataFrame(
    np.random.randn(cantidad_datos, 2),
    columns=['X', 'Y']
)

# Mostrar en columnas
col_a, col_b = st.columns([2, 1])

with col_a:
    st.subheader("Gráfico")
    st.line_chart(datos_random)

with col_b:
    st.subheader("Estadísticas")
    st.write(f"Mostrando {cantidad_datos} puntos")
    st.metric("Media X", f"{datos_random['X'].mean():.2f}")
    st.metric("Media Y", f"{datos_random['Y'].mean():.2f}")

st.info("💡 Cambia el slider en el sidebar para ver cómo se actualiza todo")
