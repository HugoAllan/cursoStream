import streamlit as st

pagina = st.set_page_config(
    page_title="Callbacks",
    layout="wide"
)

st.title("Nivel 6: Calculadora con Historial")

# Inicializar session state
if 'resultado' not in st.session_state:
    st.session_state.resultado = 0
if 'historial' not in st.session_state:
    st.session_state.historial = []
if 'numero_actual' not in st.session_state:
    st.session_state.numero_actual = ""

# Funciones de la calculadora
def agregar_numero(num):
    st.session_state.numero_actual += str(num)

def calcular(operacion):
    if st.session_state.numero_actual:
        numero = float(st.session_state.numero_actual)
        if operacion == "sumar":
            nuevo_resultado = st.session_state.resultado + numero
        elif operacion == "restar":
            nuevo_resultado = st.session_state.resultado - numero
        elif operacion == "multiplicar":
            nuevo_resultado = st.session_state.resultado * numero
        elif operacion == "dividir":
            if numero != 0:
                nuevo_resultado = st.session_state.resultado / numero
            else:
                st.error("No se puede dividir por cero")
                return
        
        # Agregar al historial
        operacion_texto = f"{st.session_state.resultado} {operacion} {numero} = {nuevo_resultado}"
        st.session_state.historial.append(operacion_texto)
        
        st.session_state.resultado = nuevo_resultado
        st.session_state.numero_actual = ""

def limpiar():
    st.session_state.resultado = 0
    st.session_state.numero_actual = ""

def limpiar_historial():
    st.session_state.historial = []

# Interfaz
col1, col2 = st.columns([2, 1])

with col1:
    st.write(f"Resultado actual: **{st.session_state.resultado}**")
    st.write(f"Número a ingresar: **{st.session_state.numero_actual}**")
    
    # Teclado numérico
    col_num1, col_num2, col_num3 = st.columns(3)
    
    with col_num1:
        st.button("1", on_click=agregar_numero, args=(1,))
        st.button("4", on_click=agregar_numero, args=(4,))
        st.button("7", on_click=agregar_numero, args=(7,))
    
    with col_num2:
        st.button("2", on_click=agregar_numero, args=(2,))
        st.button("5", on_click=agregar_numero, args=(5,))
        st.button("8", on_click=agregar_numero, args=(8,))
    
    with col_num3:
        st.button("3", on_click=agregar_numero, args=(3,))
        st.button("6", on_click=agregar_numero, args=(6,))
        st.button("9", on_click=agregar_numero, args=(9,))
    
    st.button("0", on_click=agregar_numero, args=(0,))
    
    # Operaciones
    col_op1, col_op2, col_op3, col_op4 = st.columns(4)
    
    with col_op1:
        st.button("➕", on_click=calcular, args=("sumar",))
    
    with col_op2:
        st.button("➖", on_click=calcular, args=("restar",))
    
    with col_op3:
        st.button("✖️", on_click=calcular, args=("multiplicar",))
    
    with col_op4:
        st.button("➗", on_click=calcular, args=("dividir",))
    
    # Botones de control
    col_ctrl1, col_ctrl2 = st.columns(2)
    with col_ctrl1:
        st.button("🔄 Limpiar", on_click=limpiar)
    with col_ctrl2:
        st.button("🗑️ Limpiar Historial", on_click=limpiar_historial)

with col2:
    st.write("**Historial:**")
    if st.session_state.historial:
        for operacion in st.session_state.historial[-5:]:  # Mostrar últimas 5
            st.write(f"• {operacion}")
    else:
        st.write("No hay operaciones")


# Inicializar estado
if 'toggle_estado' not in st.session_state:
    st.session_state.toggle_estado = True

def toggle():
    st.session_state.toggle_estado = not st.session_state.toggle_estado

# Botón que cambia su texto según el estado
texto_boton = "🔴 Apagar" if st.session_state.toggle_estado else "🟢 Encender"
st.button(texto_boton, on_click=toggle)

# Mostrar estado
if st.session_state.toggle_estado:
    st.success("✅ Sistema ENCENDIDO")
    st.balloons()
else:
    st.error("❌ Sistema APAGADO")
    
st.divider()


print("🔥 1. INICIO - Esto se ejecuta SIEMPRE")

# 🔥 2. Esto se ejecuta ANTES de cualquier botón
if 'contador' not in st.session_state:
    st.session_state.contador = 0
    print("✨ 2. Inicializando contador = 0")

print(f"🔥 3. Valor actual del contador: {st.session_state.contador}")

# 🔥 4. Esto también se ejecuta antes de la interacción
def incrementar():
    print("🎯 CALLBACK: Incrementando...")
    st.session_state.contador += 1

# 🔥 5. El botón se "dibuja" pero aún no se ha presionado
if st.button("Incrementar"):
    print("🚨 Este print NO aparece hasta que se presione")

print("🔥 6. FIN - Esto también se ejecuta SIEMPRE")