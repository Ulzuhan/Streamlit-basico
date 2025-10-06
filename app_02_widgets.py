# ====================================
# APP 02: WIDGETS Y CALCULADORA
# ====================================
# Conceptos: inputs de texto, números, slider, calculadora funcional

# Los widgets en Streamlit son elementos interactivos que permiten al usuario
# introducir datos o hacer selecciones. Son la forma principal de hacer que
# tu aplicación sea interactiva y responda a las acciones del usuario.

import streamlit as st

st.title("🎮 Widgets y Entrada de Datos")

# ====================================
# PARTE 1: ENTRADA DE TEXTO
# ====================================

st.header("✍️ Entrada de Texto")

# st.text_input() - Campo de texto de una línea
# Crea un campo donde el usuario puede escribir texto.
# Es útil para nombres, emails, búsquedas, etc.
# El parámetro 'placeholder' muestra un texto de ejemplo cuando el campo está vacío.
nombre = st.text_input("¿Cómo te llamas?", placeholder="Escribe tu nombre aquí")

# Solo muestra el saludo si el usuario escribió algo
# Esto evita mostrar mensajes vacíos cuando el campo está en blanco.
if nombre:
    st.write(f"¡Hola, {nombre}! 👋")

# ====================================
# PARTE 2: ENTRADA DE NÚMEROS
# ====================================

st.header("🔢 Entrada de Números")

# st.number_input() - Campo numérico con botones +/-
# Similar a text_input pero solo acepta números.
# Tiene parámetros para controlar el rango permitido y el paso de incremento.
edad = st.number_input(
    "¿Cuántos años tienes?",
    min_value=0,      # Mínimo permitido
    max_value=120,    # Máximo permitido
    value=25,         # Valor por defecto
    step=1            # Cuánto aumenta/disminuye con cada clic
)

st.write(f"Tienes {edad} años")

# ====================================
# PARTE 3: SLIDER 
# ====================================

st.header("🎚️ Slider (Deslizador)")

# st.slider() - Control deslizante para elegir valores
# Ideal para seleccionar valores numéricos en un rango continuo.
# Es más intuitivo que escribir números cuando hay un rango amplio.
temperatura = st.slider(
    "Temperatura preferida (°C)",
    min_value=-10,
    max_value=40,
    value=20
)

st.write(f"Tu temperatura preferida es: {temperatura}°C")

# Mensaje personalizado según la temperatura
# Aquí vemos cómo usar condicionales para crear lógica basada en la entrada del usuario.
if temperatura < 10:
    st.info("🥶 ¡Hace mucho frío!")
elif temperatura > 30:
    st.warning("🥵 ¡Hace mucho calor!")
else:
    st.success("😊 ¡Temperatura perfecta!")

st.divider()

# ====================================
# EJERCICIO: CALCULADORA SIMPLE
# ====================================
# Vamos a construir una calculadora paso a paso
# Este ejercicio combina varios widgets para crear una aplicación funcional.

st.header("🧮 Calculadora Interactiva")

# Paso 1: Crear dos campos numéricos
# Usamos number_input con formato decimal para permitir números con decimales.
num1 = st.number_input("Primer número", value=0.0, format="%.2f")
num2 = st.number_input("Segundo número", value=0.0, format="%.2f")

# Paso 2: Selector de operación
# selectbox permite elegir una opción de una lista desplegable.
operacion = st.selectbox(
    "Elige una operación",
    ["➕ Suma", "➖ Resta", "✖️ Multiplicación", "➗ División"]
)

# Paso 3: Botón para calcular
# El botón con type="primary" se ve más destacado.
# Solo calcula cuando el usuario hace clic.
if st.button("Calcular", type="primary"):
    # Realizamos el cálculo según la operación elegida
    # Usamos if-elif para manejar diferentes casos.
    
    if operacion == "➕ Suma":
        resultado = num1 + num2
        st.success(f"Resultado: {num1} + {num2} = {resultado}")
    
    elif operacion == "➖ Resta":
        resultado = num1 - num2
        st.success(f"Resultado: {num1} - {num2} = {resultado}")
    
    elif operacion == "✖️ Multiplicación":
        resultado = num1 * num2
        st.success(f"Resultado: {num1} × {num2} = {resultado}")
    
    elif operacion == "➗ División":
        # Importante: verificar división por cero
        # La división por cero causa un error, así que debemos prevenirlo.
        if num2 == 0:
            st.error("❌ Error: No se puede dividir entre cero")
        else:
            resultado = num1 / num2
            st.success(f"Resultado: {num1} ÷ {num2} = {resultado:.2f}")

# ====================================
# EXTRA: MÁS WIDGETS ÚTILES
# ====================================

st.divider()
st.header("🎯 Otros Widgets Útiles")

# st.multiselect() - Selección múltiple
# Permite seleccionar múltiples opciones de una lista.
# Útil cuando el usuario puede tener varios intereses o preferencias.
hobbies = st.multiselect(
    "¿Cuáles son tus hobbies?",
    ["Programación", "Videojuegos", "Lectura", "Deporte", "Música", "Viajar"],
    default=["Programación"]  # Valor por defecto
)

if hobbies:
    st.write(f"Tienes {len(hobbies)} hobbies seleccionados:")
    for hobby in hobbies:
        st.write(f"- {hobby}")
