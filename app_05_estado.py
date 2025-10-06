# ====================================
# APP 05: SESSION STATE
# ====================================
# Conceptos: mantener estado entre interacciones

# Session State es una de las características más importantes de Streamlit.
# Permite mantener datos entre diferentes interacciones del usuario,
# ya que por defecto Streamlit ejecuta todo el script desde cero cada vez.

import streamlit as st

st.title("💾 Session State - Mantener Estado")

# ====================================
# EXPLICACIÓN DEL PROBLEMA
# ====================================

st.header("🤔 ¿Por qué necesitamos Session State?")

st.write("""
**El problema:** Streamlit vuelve a ejecutar TODO el script cada vez que 
interactúas con la app (cada clic, cada cambio en un widget).

**La consecuencia:** Las variables normales se "olvidan" entre clicks.

**La solución:** Session State permite guardar variables entre ejecuciones.
""")

st.divider()

# ====================================
# EJEMPLO 1: CONTADOR SIMPLE
# ====================================

st.header("🔢 Ejemplo: Contador")

st.write("Vamos a crear un contador que recuerde su valor:")

# PASO 1: Inicializar el contador si no existe
# 'contador' not in st.session_state verifica si la variable ya existe
# Esto es importante porque el script se ejecuta múltiples veces.
if 'contador' not in st.session_state:
    st.session_state.contador = 0  # Crear la variable con valor 0

# PASO 2: Mostrar el valor actual
# Accedemos al valor guardado en session_state
st.subheader(f"Valor actual: {st.session_state.contador}")

# PASO 3: Botones para modificar el contador
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ Incrementar"):
        # Modificar el valor guardado en session_state
        # Esto cambia el valor que persiste entre ejecuciones
        st.session_state.contador += 1
        st.rerun()  # Forzar recarga para mostrar el nuevo valor

with col2:
    if st.button("➖ Decrementar"):
        st.session_state.contador -= 1
        st.rerun()

with col3:
    if st.button("🔄 Resetear"):
        st.session_state.contador = 0
        st.rerun()

# Mostrar el historial (ejemplo avanzado)
# Podemos usar condicionales para crear lógica basada en el estado
if st.session_state.contador > 10:
    st.success("🎉 ¡Has llegado a más de 10!")
elif st.session_state.contador < -10:
    st.warning("⚠️ ¡Estás muy abajo!")

st.divider()

# ====================================
# EJEMPLO 2: LISTA DE TAREAS 
# ====================================

st.header("📝 Ejemplo: Lista de Tareas Simple")

# Inicializar lista de tareas
# Las listas también se pueden guardar en session_state
if 'tareas' not in st.session_state:
    st.session_state.tareas = []

# Input para nueva tarea
nueva_tarea = st.text_input("Escribe una tarea:")

# Botón para agregar
if st.button("➕ Agregar tarea") and nueva_tarea:
    # Agregar la tarea a la lista
    # .append() añade elementos a la lista guardada en session_state
    st.session_state.tareas.append(nueva_tarea)
    st.rerun()

# Mostrar todas las tareas
if st.session_state.tareas:
    st.write("**Tus tareas:**")
    # enumerate() nos da el índice y el valor de cada elemento
    for i, tarea in enumerate(st.session_state.tareas, 1):
        st.write(f"{i}. {tarea}")
    
    # Botón para limpiar todas
    if st.button("🗑️ Limpiar todas"):
        st.session_state.tareas = []
        st.rerun()
else:
    st.info("No tienes tareas. ¡Agrega una!")

st.divider()

# ====================================
# RESUMEN
# ====================================

st.header("📚 Resumen")

st.write("""
**Pasos para usar Session State:**

1. Inicializar la variable (solo la primera vez):
   ```python
   if 'mi_variable' not in st.session_state:
       st.session_state.mi_variable = valor_inicial
   ```

2. Usar la variable:
   ```python
   st.write(st.session_state.mi_variable)
   ```

3. Modificar la variable:
   ```python
   st.session_state.mi_variable = nuevo_valor
   ```

4. Forzar recarga si es necesario:
   ```python
   st.rerun()
   ```
""")

st.info("💡 Session State es perfecto para: contadores, listas, formularios multi-paso, y cualquier dato que deba persistir")
