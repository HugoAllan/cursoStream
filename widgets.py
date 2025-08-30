import streamlit as st

st.set_page_config(
    page_title="Curso de Streamlit",
    layout="wide"
)

st.title("Widgets en Streamlit")

st.header("Botones")
if st.button("Presióname"):
    st.write("¡Botón presionado!")

st.header("Checkbox")
if st.checkbox("Acepto los términos y condiciones"):
    st.write("¡Checkbox seleccionado!")

st.header("Radio")
opcion = st.radio("Selecciona una opción", ("Opción 1", "Opción 2", "Opción 3"))
st.write(f"Has seleccionado: {opcion}")

st.header("Select")
opcion = st.selectbox("Selecciona una opción", ("Opción 1", "Opción 2", "Opción 3"))
st.write(f"Has seleccionado: {opcion}")

st.header("Slider")
valor = st.slider("Selecciona un valor", 0, 100, 50)
st.write(f"Has seleccionado: {valor}")

opcion_multiple = st.multiselect("Selecciona varias opciones", ("Opción 1", "Opción 2", "Opción 3"))
st.write(f"Has seleccionado: {opcion_multiple}")

# condicionales
var = 1
if var == 1:
    st.write("La variable es igual a 1")
else:
    st.write("La variable no es igual a 1")


# Toggle
st.header("Toggle")
opcion = st.toggle("Activar opción")
st.write(f"Has {'activado' if opcion else 'desactivado'} la opción")    

# Color Picker
st.header("Color Picker")
color = st.color_picker("Selecciona un color", "#00f900")
st.write(f"Has seleccionado el color: {color}")

