import streamlit as st

st.title("🔥 Callbacks en Streamlit: Todas las Formas")

# =============================================================================
# INICIALIZACIÓN
# =============================================================================
def inicializar():
    """Inicializa todas las variables de session state"""
    defaults = {
        'contador_boton': 0,
        'contador_slider': 50,
        'nombre': '',
        'activo': False,
        'archivo_subido': None,
        'color_favorito': 'Rojo',
        'fecha_seleccionada': None,
        'historial': []
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

inicializar()

st.divider()

# =============================================================================
# 1. BOTONES
# =============================================================================
st.subheader("1️⃣ Botones con Callbacks")

def callback_boton_simple():
    st.session_state.contador_boton += 1
    st.session_state.historial.append(f"Botón presionado - Contador: {st.session_state.contador_boton}")

def callback_boton_con_params(incremento, mensaje):
    st.session_state.contador_boton += incremento
    st.session_state.historial.append(f"{mensaje} - Incremento: {incremento}")

def reset_contador():
    st.session_state.contador_boton = 0
    st.session_state.historial.append("Contador reseteado")

col1, col2, col3, col4 = st.columns(4)

with col1:
    # Callback sin parámetros
    st.button("➕ +1", on_click=callback_boton_simple)

with col2:
    # Callback con parámetros
    st.button("➕ +5", on_click=callback_boton_con_params, args=(5, "Incremento grande"))

with col3:
    # Callback con parámetros nombrados
    st.button("➖ -3", on_click=callback_boton_con_params, 
              args=(-3,), kwargs={'mensaje': 'Decremento'})

with col4:
    # Callback para reset
    st.button("🔄 Reset", on_click=reset_contador)

st.write(f"**Contador actual**: {st.session_state.contador_boton}")

st.divider()

# =============================================================================
# 2. SLIDERS
# =============================================================================
st.subheader("2️⃣ Sliders con Callbacks")

def callback_slider(nuevo_valor):
    diferencia = nuevo_valor - st.session_state.get('slider_anterior', 50)
    st.session_state.slider_anterior = nuevo_valor
    st.session_state.historial.append(f"Slider cambió a {nuevo_valor} (Δ{diferencia:+d})")

# Slider con callback en cambio
st.slider(
    "Selecciona un valor:", 
    min_value=0, 
    max_value=100, 
    value=st.session_state.contador_slider,
    key="slider_callback",
    on_change=callback_slider,
    args=(st.session_state.get("slider_callback", 50),)  # Pasa el valor actual
)

st.write(f"**Valor del slider**: {st.session_state.get('slider_callback', 50)}")

st.divider()

# =============================================================================
# 3. INPUT DE TEXTO
# =============================================================================
st.subheader("3️⃣ Text Input con Callbacks")

def callback_texto():
    nuevo_nombre = st.session_state.input_nombre
    if nuevo_nombre != st.session_state.nombre:
        st.session_state.nombre = nuevo_nombre
        st.session_state.historial.append(f"Nombre cambiado a: '{nuevo_nombre}'")

st.text_input(
    "Tu nombre:",
    value=st.session_state.nombre,
    key="input_nombre",
    on_change=callback_texto
)

if st.session_state.nombre:
    st.write(f"¡Hola **{st.session_state.nombre}**! 👋")

st.divider()

# =============================================================================
# 4. CHECKBOX
# =============================================================================
st.subheader("4️⃣ Checkbox con Callbacks")

def callback_checkbox():
    estado = st.session_state.checkbox_activo
    mensaje = "Sistema ACTIVADO ✅" if estado else "Sistema DESACTIVADO ❌"
    st.session_state.historial.append(mensaje)

st.checkbox(
    "Sistema activo",
    value=st.session_state.activo,
    key="checkbox_activo",
    on_change=callback_checkbox
)

if st.session_state.get('checkbox_activo', False):
    st.success("🟢 Sistema funcionando correctamente")
else:
    st.error("🔴 Sistema desactivado")

st.divider()

# =============================================================================
# 5. SELECT BOX
# =============================================================================
st.subheader("5️⃣ Select Box con Callbacks")

def callback_selectbox():
    color = st.session_state.select_color
    st.session_state.color_favorito = color
    st.session_state.historial.append(f"Color favorito cambiado a: {color}")

opciones_color = ['Rojo', 'Verde', 'Azul', 'Amarillo', 'Morado']

st.selectbox(
    "Elige tu color favorito:",
    options=opciones_color,
    index=opciones_color.index(st.session_state.color_favorito),
    key="select_color",
    on_change=callback_selectbox
)

# Mostrar el color con estilo
colores_css = {
    'Rojo': '#FF0000',
    'Verde': '#00FF00', 
    'Azul': '#0000FF',
    'Amarillo': '#FFFF00',
    'Morado': '#800080'
}

color_elegido = st.session_state.get('select_color', 'Rojo')
st.markdown(f"""
<div style="background-color: {colores_css[color_elegido]}; 
            padding: 10px; border-radius: 5px; text-align: center;">
    <h3 style="color: white; text-shadow: 1px 1px 2px black;">
        Tu color: {color_elegido}
    </h3>
</div>
""", unsafe_allow_html=True)

st.divider()

# =============================================================================
# 6. FILE UPLOADER
# =============================================================================
st.subheader("6️⃣ File Uploader con Callbacks")

def callback_archivo():
    archivo = st.session_state.uploader_archivo
    if archivo is not None:
        st.session_state.archivo_subido = archivo
        st.session_state.historial.append(f"Archivo subido: {archivo.name} ({archivo.size} bytes)")
    else:
        st.session_state.archivo_subido = None
        st.session_state.historial.append("Archivo eliminado")

uploaded_file = st.file_uploader(
    "Sube un archivo:",
    key="uploader_archivo",
    on_change=callback_archivo
)

if st.session_state.archivo_subido:
    st.success(f"✅ Archivo: **{st.session_state.archivo_subido.name}**")
    st.write(f"Tamaño: {st.session_state.archivo_subido.size} bytes")
    st.write(f"Tipo: {st.session_state.archivo_subido.type}")

st.divider()

# =============================================================================
# 7. DATE INPUT
# =============================================================================
st.subheader("7️⃣ Date Input con Callbacks")

def callback_fecha():
    fecha = st.session_state.input_fecha
    st.session_state.fecha_seleccionada = fecha
    st.session_state.historial.append(f"Fecha seleccionada: {fecha.strftime('%d/%m/%Y')}")

import datetime

st.date_input(
    "Selecciona una fecha:",
    value=st.session_state.fecha_seleccionada or datetime.date.today(),
    key="input_fecha",
    on_change=callback_fecha
)

if st.session_state.fecha_seleccionada:
    dias_diferencia = (st.session_state.fecha_seleccionada - datetime.date.today()).days
    if dias_diferencia > 0:
        st.info(f"📅 Fecha seleccionada: en {dias_diferencia} días")
    elif dias_diferencia < 0:
        st.info(f"📅 Fecha seleccionada: hace {abs(dias_diferencia)} días")
    else:
        st.info("📅 Fecha seleccionada: ¡Hoy!")

st.divider()

# =============================================================================
# 8. CALLBACKS COMPLEJOS
# =============================================================================
st.subheader("8️⃣ Callbacks Complejos")

def callback_complejo():
    """Callback que realiza múltiples acciones"""
    # Validar datos
    if not st.session_state.nombre:
        st.session_state.historial.append("❌ Error: Nombre vacío")
        return
    
    # Calcular puntaje basado en diferentes factores
    puntaje = 0
    puntaje += len(st.session_state.nombre) * 2  # Puntos por longitud del nombre
    puntaje += st.session_state.contador_slider    # Puntos del slider
    
    if st.session_state.get('checkbox_activo', False):
        puntaje *= 2  # Doble puntos si está activo
    
    # Bonus por color favorito
    bonus_colores = {'Rojo': 10, 'Verde': 15, 'Azul': 12, 'Amarillo': 8, 'Morado': 20}
    puntaje += bonus_colores.get(st.session_state.color_favorito, 0)
    
    # Guardar en historial con información detallada
    st.session_state.historial.append(f"🎯 Puntaje calculado: {puntaje} puntos para {st.session_state.nombre}")

st.button("🎯 Calcular Puntaje Final", on_click=callback_complejo, type="primary")

st.divider()

# =============================================================================
# 9. HISTORIAL DE ACCIONES
# =============================================================================
st.subheader("9️⃣ Historial de Acciones")

col1, col2 = st.columns([3, 1])

with col1:
    st.write("**Últimas 10 acciones:**")
    if st.session_state.historial:
        for i, accion in enumerate(reversed(st.session_state.historial[-10:]), 1):
            st.write(f"{i}. {accion}")
    else:
        st.write("No hay acciones registradas")

with col2:
    def limpiar_historial():
        st.session_state.historial = []
    
    st.button("🗑️ Limpiar Historial", on_click=limpiar_historial)
    st.write(f"Total acciones: **{len(st.session_state.historial)}**")

st.divider()

# =============================================================================
# 10. COMPARACIÓN: CON Y SIN CALLBACKS
# =============================================================================
st.subheader("🔀 Comparación: Con vs Sin Callbacks")

col1, col2 = st.columns(2)

with col1:
    st.write("**❌ SIN Callbacks (Manual):**")
    
    # Sin callback - detección manual
    if st.button("Método Manual"):
        st.session_state.contador_boton += 1
        st.session_state.historial.append("Método manual usado")
        st.write("✅ Acción ejecutada manualmente")

with col2:
    st.write("**✅ CON Callbacks (Automático):**")
    
    def callback_automatico():
        st.session_state.contador_boton += 1
        st.session_state.historial.append("Método automático usado")
    
    # Con callback - automático
    st.button("Método Automático", on_click=callback_automatico)

st.divider()

# =============================================================================
# INFORMACIÓN TÉCNICA
# =============================================================================
with st.expander("🔧 Información Técnica"):
    st.write("**Widgets que soportan callbacks:**")
    widgets_con_callbacks = [
        "st.button() - on_click",
        "st.slider() - on_change", 
        "st.text_input() - on_change",
        "st.number_input() - on_change",
        "st.text_area() - on_change",
        "st.checkbox() - on_change",
        "st.radio() - on_change",
        "st.selectbox() - on_change",
        "st.multiselect() - on_change",
        "st.file_uploader() - on_change",
        "st.date_input() - on_change",
        "st.time_input() - on_change",
        "st.color_picker() - on_change"
    ]
    
    for widget in widgets_con_callbacks:
        st.write(f"• {widget}")
    
    st.write("**Ventajas de los callbacks:**")
    st.write("• Código más limpio y organizado")
    st.write("• Separación de lógica y UI")  
    st.write("• Mejor rendimiento")
    st.write("• Ejecución automática")
    st.write("• Menos propenso a errores")

# =============================================================================
# ESTADO ACTUAL
# =============================================================================
with st.expander("📊 Estado Actual de la Aplicación"):
    st.json({
        "contador_boton": st.session_state.contador_boton,
        "contador_slider": st.session_state.get('slider_callback', 50),
        "nombre": st.session_state.nombre,
        "activo": st.session_state.get('checkbox_activo', False),
        "color_favorito": st.session_state.get('select_color', 'Rojo'),
        "tiene_archivo": st.session_state.archivo_subido is not None,
        "fecha_seleccionada": str(st.session_state.fecha_seleccionada) if st.session_state.fecha_seleccionada else None,
        "total_acciones": len(st.session_state.historial)
    })