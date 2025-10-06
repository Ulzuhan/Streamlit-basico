# ====================================
# APP 06: DASHBOARD SIMPLIFICADO
# ====================================
# Proyecto final que integra todo lo aprendido

# Este es el proyecto final del curso básico de Streamlit.
# Integra todos los conceptos aprendidos: widgets, datos, layout, session state (implícito),
# y crea un dashboard funcional para análisis de ventas.

import streamlit as st
import pandas as pd
import numpy as np

# ====================================
# CONFIGURACIÓN DE LA PÁGINA
# ====================================

# st.set_page_config() debe ser la primera función de Streamlit llamada.
# Configura el título de la pestaña, el ícono y el layout de la página.
st.set_page_config(
    page_title="Dashboard de Ventas",  # Título que aparece en la pestaña del navegador
    page_icon="📊",  # Ícono que aparece en la pestaña
    layout="wide"  # Usa todo el ancho de la pantalla (en lugar de centrado)
)

# ====================================
# GENERAR DATOS DE EJEMPLO
# ====================================

# @st.cache_data es un decorador que guarda en caché el resultado de la función.
# Esto significa que los datos se generan solo una vez, no en cada recarga.
# Es útil para funciones costosas que no cambian frecuentemente.
@st.cache_data  # Esto hace que los datos se generen solo una vez
def generar_datos():
    """Genera datos de ventas simulados
    
    Esta función crea datos ficticios de ventas para demostrar el dashboard.
    En un caso real, estos datos vendrían de una base de datos o API.
    """
    np.random.seed(42)  # Para obtener siempre los mismos datos (reproducibilidad)
    
    # Crear 100 registros de ventas
    productos = ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Auriculares']
    regiones = ['Norte', 'Sur', 'Este', 'Oeste']
    
    datos = []
    for _ in range(100):
        # np.random.choice() selecciona aleatoriamente de una lista
        # np.random.randint() genera números enteros aleatorios
        datos.append({
            'Producto': np.random.choice(productos),
            'Región': np.random.choice(regiones),
            'Cantidad': np.random.randint(1, 20),
            'Precio': np.random.randint(20, 500)
        })
    
    df = pd.DataFrame(datos)
    df['Total'] = df['Cantidad'] * df['Precio']  # Calcular columna derivada
    
    return df

# Cargar datos
# Como está decorada con @st.cache_data, esto es muy eficiente
df = generar_datos()

# ====================================
# SIDEBAR - FILTROS
# ====================================

st.sidebar.title("⚙️ Filtros")

# Filtro por producto
# multiselect permite seleccionar múltiples opciones
productos_seleccionados = st.sidebar.multiselect(
    "Selecciona productos:",
    options=df['Producto'].unique(),  # .unique() obtiene valores únicos
    default=df['Producto'].unique()  # Todos seleccionados por defecto
)

# Filtro por región
regiones_seleccionadas = st.sidebar.multiselect(
    "Selecciona regiones:",
    options=df['Región'].unique(),
    default=df['Región'].unique()
)

# Aplicar filtros
# Usamos operadores booleanos para filtrar el DataFrame
# .isin() verifica si los valores están en la lista seleccionada
df_filtrado = df[
    (df['Producto'].isin(productos_seleccionados)) &
    (df['Región'].isin(regiones_seleccionadas))
]

# ====================================
# HEADER
# ====================================

st.title("📊 Dashboard de Ventas")
st.markdown("### Panel de análisis de ventas por producto y región")
st.divider()

# ====================================
# KPIS PRINCIPALES
# ====================================

st.header("📈 Indicadores Clave")

# Calcular métricas
# Estas son las métricas clave (KPIs) que resumen el rendimiento
total_ventas = df_filtrado['Total'].sum()
total_productos = len(df_filtrado)
ticket_promedio = total_ventas / total_productos if total_productos > 0 else 0

# Mostrar en 3 columnas
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Ventas Totales",
        f"€{total_ventas:,.0f}"  # Formato con separador de miles
    )

with col2:
    st.metric(
        "🛒 Número de Ventas",
        f"{total_productos}"
    )

with col3:
    st.metric(
        "💳 Ticket Promedio",
        f"€{ticket_promedio:.2f}"  # Dos decimales
    )

st.divider()

# ====================================
# GRÁFICOS
# ====================================

st.header("📊 Visualizaciones")

# Crear dos columnas para los gráficos
col_izq, col_der = st.columns(2)

with col_izq:
    st.subheader("Ventas por Producto")
    
    # Agrupar por producto y sumar ventas
    # groupby() agrupa los datos, sum() suma los valores
    ventas_por_producto = df_filtrado.groupby('Producto')['Total'].sum()
    st.bar_chart(ventas_por_producto)

with col_der:
    st.subheader("Ventas por Región")
    
    # Agrupar por región y sumar ventas
    ventas_por_region = df_filtrado.groupby('Región')['Total'].sum()
    st.bar_chart(ventas_por_region)

st.divider()

# ====================================
# TABLA DE DATOS
# ====================================

st.header("📋 Datos Detallados")

# Checkbox para mostrar/ocultar tabla
# Esto permite al usuario controlar qué contenido ver
mostrar_datos = st.checkbox("Mostrar datos completos", value=True)

if mostrar_datos:
    st.write(f"Mostrando {len(df_filtrado)} registros:")
    
    # Ordenar por ventas totales (de mayor a menor)
    # sort_values() ordena el DataFrame por una columna
    df_ordenado = df_filtrado.sort_values('Total', ascending=False)
    
    # Mostrar tabla
    st.dataframe(
        df_ordenado,
        use_container_width=True,  # Usa todo el ancho disponible
        hide_index=True  # Oculta la columna de índices
    )
    
    # Estadísticas rápidas
    # expander crea una sección plegable
    with st.expander("Ver estadísticas"):
        # .describe() calcula estadísticas descriptivas
        st.write(df_filtrado[['Cantidad', 'Precio', 'Total']].describe())

st.divider()

# ====================================
# ANÁLISIS ADICIONAL
# ====================================

st.header("🎯 Análisis")

# tabs organizan contenido relacionado en pestañas
tab1, tab2 = st.tabs(["Top Productos", "Top Regiones"])

with tab1:
    st.subheader("Top 5 Productos por Ventas")
    
    # groupby + sum + sort_values + head = análisis típico
    top_productos = df_filtrado.groupby('Producto')['Total'].sum().sort_values(ascending=False).head()
    
    for i, (producto, ventas) in enumerate(top_productos.items(), 1):
        st.write(f"**{i}. {producto}:** €{ventas:,.0f}")

with tab2:
    st.subheader("Top 3 Regiones por Ventas")
    
    top_regiones = df_filtrado.groupby('Región')['Total'].sum().sort_values(ascending=False).head(3)
    
    for i, (region, ventas) in enumerate(top_regiones.items(), 1):
        st.write(f"**{i}. {region}:** €{ventas:,.0f}")

# ====================================
# FOOTER
# ====================================

st.divider()
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Dashboard creado con Streamlit | Bootcamp Data & IA 2025</p>
</div>
""", unsafe_allow_html=True)
