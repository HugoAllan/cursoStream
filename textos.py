import streamlit as st

st.set_page_config(
    page_title="Curso de Streamlit",
    layout="wide"
)

st.title("Curso de Streamlit")
st.header("Soy un header")
st.subheader("Soy un subheader")
st.caption("Soy una caption muy chido")
st.text("Soy un texto muy chido")
st.markdown("**Soy un markdown**")
st.code("print('Hola mundo')")
st.text_area("Soy un text area", "Hola mundo")
st.text_input("Soy un text input", "Hola mundo")


# Concatenacion

st.subheader("Segunda leccion de textos. Concatenacion")
nombre = "Alan"
edad = "34"
st.text("Hola mi nombre es " + nombre)
st.text("Hola mi nombre es {}".format(nombre))
st.text(f"Hola mi nombre es {nombre}")
st.text(f"Hola mi nombre es {nombre} y tengo {edad} años")

# MARKDOWN
st.subheader("Leccion 3. Markdown")
st.markdown("# Soy un H1")
st.markdown("## Soy un H2")
st.markdown("### Soy un H3")
st.markdown("Este texto tiene **Negritas**")
st.markdown("Este texto tiene *Cursivas*")
st.markdown("Este texto tiene ***cursivas en negritas***")
st.markdown("[Google](https://www.google.com)")
st.markdown("---")
st.markdown("Este es un texto debajo de una linea horizontal")
st.divider()

# EXPRESIONES MATEMATICAS
st.subheader("Leccion 4. Expresiones matematicas")
st.latex("E = mc^2")
st.latex(r"""
\begin{align*}
a &= b + c \\
d &= e - f
\end{align*}
""")
st.latex(r"CH_4 + 2O_2 \rightarrow CO_2 + 2H_2O")

