import streamlit as st

page = st.set_page_config(
    page_title="Tareas",
    layout="wide"
)

st.title("Nivel 6: Tareas")

# Inicializar session state
def inicializar():
    """Inicializa todas las variables de session state"""
    defaults = {
        'tareas': [],
        'tarea_actual': '',
        'tareas_completadas': [],
        'historial': []
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

inicializar()

tarea = st.text_input("Nueva tarea", st.session_state.tarea_actual)

if st.button("Agregar tarea"):
    if tarea:
        st.session_state.tareas.append(tarea)
        st.session_state.historial.append(tarea)
        st.session_state.tarea_actual = ''
    else:
        st.warning("Por favor, ingresa una tarea.")

col_tarea, col_boton = st.columns([3, 1])
with col_tarea:
    st.write("### Tareas pendientes:")
    for i, tarea in enumerate(st.session_state.tareas):
        st.write(f"{i + 1}. {tarea}")

with col_boton:
    st.write("### Acciones:")
    for i, tarea in enumerate(st.session_state.tareas):
        if st.toggle(f"Completar {i + 1}"):
            st.session_state.tareas_completadas.append(tarea)
            st.session_state.tareas.remove(tarea)
            st.success(f"Tarea '{tarea}' completada.")
            break



st.write("### Historial de tareas:")
for i, tarea in enumerate(st.session_state.historial):
    st.write(f"{i + 1}. {tarea}")


