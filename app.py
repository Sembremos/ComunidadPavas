import streamlit as st

# --- Configuración de la página ---
st.set_page_config(
    page_title="Encuesta Comunidad Pavas",
    layout="centered",
    initial_sidebar_state="collapsed"
)
# --- Encabezado de imagen y texto justificado ---
# --- Encabezado de imagen y texto justificado ---
try:
    # Asegúrate de que el archivo 'logo_pavas.png' esté en tu repositorio de GitHub
    st.image("logo_pavas.png", width=700)
except FileNotFoundError:
    st.warning("Advertencia: El archivo 'logo_pavas.png' no se encontró. Asegúrate de que está en la misma carpeta que 'app.py'.")
    
# --- Título y descripción ---
st.markdown("<h1 style='text-align: center; color: green;'>Encuesta Comunidad Pavas</h1>", unsafe_allow_html=True)
st.markdown("Por favor, responda las siguientes preguntas sobre la seguridad en su barrio.")

# --- Formulario de la encuesta ---
# Usamos st.form para agrupar todos los elementos de la encuesta.
with st.form(key='encuesta_seguridad_pavas'):
    
    # 1. Pregunta sobre la calificación de seguridad (escala)
    st.subheader("1. Calificación de la seguridad")
    seguridad = st.radio(
        "Pensando en su día a día, ¿cómo calificaría la seguridad de su barrio?",
        ('Muy Seguro', 'Seguro', 'Ni seguro ni inseguro', 'Inseguro', 'Muy Inseguro'),
        index=2  # Opción por defecto: "Ni seguro ni inseguro"
    )

    # 2. Pregunta sobre la principal preocupación
    st.subheader("2. Principal preocupación")
    preocupacion = st.text_area(
        "¿Cuál es la principal preocupación de seguridad que afecta a su familia?",
        height=100
    )

    # 3. Descripción del delito (opcional)
    st.subheader("3. Descripción de un delito (opcional)")
    descripcion_delito = st.text_area(
        "En caso de haber mencionado un delito, ¿puede dar una pequeña descripción de cómo se realiza?",
        help="Este campo es opcional y sirve para obtener más detalles.",
        height=100
    )

    # 4. Lugares o horas a evitar
    st.subheader("4. Lugares y horarios")
    lugares_evitados = st.text_area(
        "¿Hay algún lugar o alguna hora del día que usted o su familia evitan por seguridad?",
        height=100
    )

    # 5. Petición para mayor seguridad
    st.subheader("5. Una sola petición")
    peticion = st.text_area(
        "Si pudiera pedir UNA SOLA COSA para que usted y sus hijos se sientan más seguros, ¿qué sería?",
        height=100
    )

    # 6. Presencia de la Fuerza Pública
    st.subheader("6. Presencia policial")
    fuerza_publica = st.radio(
        "¿Ver más presencia de la Fuerza Pública en la calle le haría sentir más seguro/a?",
        ('Sí', 'No', 'No estoy seguro/a')
    )
    
    st.markdown("---")
    
    # Botón para enviar el formulario
    submit_button = st.form_submit_button(label='➡️ Enviar Encuesta')

# --- Lógica después de enviar el formulario ---
if submit_button:
    # Aquí puedes procesar los datos de la encuesta.
    # Por ahora, solo mostraremos un mensaje de éxito.
    st.success("¡Gracias por completar la encuesta! Tus respuestas han sido enviadas.")
    
    # Opcionalmente, puedes mostrar las respuestas para confirmación.
    st.markdown("---")
    st.subheader("Resumen de tus respuestas:")
    st.write(f"**1. Seguridad en el barrio:** {seguridad}")
    st.write(f"**2. Principal preocupación:** {preocupacion}")
    st.write(f"**3. Descripción del delito:** {descripcion_delito}")
    st.write(f"**4. Lugares evitados:** {lugares_evitados}")
    st.write(f"**5. Petición para seguridad:** {peticion}")
    st.write(f"**6. Presencia policial:** {fuerza_publica}")
