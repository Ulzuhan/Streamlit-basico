# ====================================
# APP 01: FUNDAMENTOS DE STREAMLIT
# ====================================
# Conceptos: importar, título, texto, botones, mensajes

# Streamlit es una biblioteca de Python que permite crear aplicaciones web interactivas
# de manera sencilla y rápida, sin necesidad de conocimientos avanzados de HTML, CSS o JavaScript.
# Es ideal para científicos de datos, analistas y desarrolladores que quieren compartir sus análisis
# o modelos de machine learning con una interfaz web amigable.

import streamlit as st

# ====================================
# PARTE 1: MOSTRAR TEXTO 
# ====================================

# st.title() - Título principal (el más grande)
# Esta función crea un encabezado grande y prominente en la página web.
# Es útil para el título principal de tu aplicación.
st.title("🎓 Mi Primera App con Streamlit")

# st.write() - La función más versátil
# Detecta automáticamente qué tipo de contenido es y lo muestra
# Puede mostrar texto, números, listas, dataframes de pandas, gráficos, etc.
# Es como la función "print" pero para la web.
st.write("¡Hola! Esta es mi primera aplicación con Streamlit")
st.write("Streamlit hace que crear apps web sea muy fácil")

# st.header() - Encabezado (un poco más pequeño que title)
# Similar a st.title() pero más pequeño. Útil para seccionar la página.
st.header("📝 Sobre mí")

# st.write() también entiende Markdown
# Markdown es un lenguaje de marcado simple para dar formato al texto.
# Puedes usar **negrita**, *cursiva*, listas, enlaces, etc.
st.write("Mi nombre es: **[Tu Nombre]**")
st.write("Estoy aprendiendo a crear apps web con Python")

# ====================================
# PARTE 2: MENSAJES DE COLORES 
# ====================================

st.header("💬 Mensajes Importantes")

# Cada tipo de mensaje tiene un color diferente
# Estos mensajes ayudan a comunicar diferentes tipos de información al usuario:
# - success: para confirmar acciones exitosas
# - info: para información general
# - warning: para alertas que requieren atención
# - error: para errores o problemas
st.success("✅ Este es un mensaje de éxito (verde)")
st.info("ℹ️ Este es un mensaje informativo (azul)")
st.warning("⚠️ Este es un mensaje de advertencia (amarillo)")
st.error("❌ Este es un mensaje de error (rojo)")

# st.divider() - Línea separadora
# Crea una línea horizontal que ayuda a separar secciones visualmente.
st.divider()

# ====================================
# PARTE 3: INTERACTIVIDAD BÁSICA
# ====================================

st.header("🎮 Botones Interactivos")

# st.button() - Crea un botón
# Devuelve True cuando se hace clic, False el resto del tiempo
# Los botones permiten al usuario interactuar con la aplicación.
if st.button("¡Haz clic aquí!"):
    st.write("¡Has hecho clic en el botón!")
    st.balloons()  # Animación de celebración
    # st.balloons() muestra una animación divertida de globos.
    # Es una función especial de Streamlit para hacer la app más amigable.

# st.checkbox() - Casilla de verificación
# Devuelve True si está marcada, False si no
# Las checkboxes permiten opciones de sí/no o activar/desactivar funciones.
mostrar_secreto = st.checkbox("¿Quieres ver un secreto?")

if mostrar_secreto:
    st.write("🎉 El secreto es: ¡Streamlit es genial!")

# ====================================
# PARTE 4: SELECCIÓN DE OPCIONES
# ====================================

st.header("🎯 Elige tus preferencias")

# st.radio() - Solo se puede elegir una opción
# Crea botones de radio donde el usuario puede seleccionar una opción de una lista.
# Es útil cuando hay múltiples opciones pero solo una puede ser elegida.
lenguaje = st.radio(
    "¿Cuál es tu lenguaje de programación favorito?",
    ["Python", "JavaScript", "Java", "Otro"]
)
st.write(f"Has elegido: {lenguaje}")

# st.selectbox() - Lista desplegable (dropdown)
# Crea una lista desplegable donde el usuario puede seleccionar una opción.
# Similar a st.radio() pero ocupa menos espacio cuando hay muchas opciones.
ciudad = st.selectbox(
    "¿En qué ciudad vives?",
    ["Madrid", "Barcelona", "Valencia", "Sevilla", "Otra"]
)
st.write(f"Vives en: {ciudad}")

# ====================================
# MINI EJERCICIO: TARJETA DE PRESENTACIÓN
# ====================================
# Los alumnos deben personalizar esta sección con su información
# Este es un ejemplo de cómo crear una sección personalizable en la app.

st.divider()
st.header("👤 Mi Tarjeta de Presentación")

st.write("**Nombre:** Tu Nombre Aquí")
st.write("**Ocupación:** Data Analyst / Developer / Estudiante")
st.write("**Intereses:** Data Science, IA, Programación")

# Checkbox para mostrar más información
# Aquí combinamos conceptos: usamos una checkbox para controlar qué contenido mostrar.
ver_mas = st.checkbox("Ver más información")
if ver_mas:
    st.info("📧 Email: tu.email@example.com")
    st.info("🔗 LinkedIn: linkedin.com/in/tu-perfil")
