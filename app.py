import streamlit as st
import gspread
import pandas as pd
from datetime import datetime

# --- Configuración de la página ---
st.set_page_config(
    page_title="Encuesta Comunidad Pavas",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Encabezado de imagen ---
try:
    # Asegúrate de que el archivo 'logo_pavas.png' esté en la misma carpeta
    st.image("logo_pavas.png", width=700)
except FileNotFoundError:
    st.warning("Advertencia: El archivo 'logo_pavas.png' no se encontró.")

# --- Título y descripción ---
st.markdown("<h1 style='text-align: center; color: green;'>Encuesta Comunidad Pavas</h1>", unsafe_allow_html=True)
st.markdown("Por favor, responda las siguientes preguntas sobre la seguridad en su barrio.")

# --- Formulario de la encuesta ---
with st.form(key='encuesta_seguridad_pavas'):
    
    st.subheader("1. Calificación de la seguridad")
    seguridad = st.radio(
        "Pensando en su día a día, ¿cómo calificaría la seguridad de su barrio?",
        ('Muy Seguro', 'Seguro', 'Ni seguro ni inseguro', 'Inseguro', 'Muy Inseguro'),
        index=2
    )

    st.subheader("2. Principal preocupación")
    preocupacion = st.text_area(
        "¿Cuál es la principal preocupación de seguridad que afecta a su familia?",
        height=100
    )

    st.subheader("3. Descripción de un delito (opcional)")
    descripcion_delito = st.text_area(
        "En caso de haber mencionado un delito, ¿puede dar una pequeña descripción de cómo se realiza?",
        help="Este campo es opcional y sirve para obtener más detalles.",
        height=100
    )

    st.subheader("4. Lugares y horarios")
    lugares_evitados = st.text_area(
        "¿Hay algún lugar o alguna hora del día que usted o su familia evitan por seguridad?",
        height=100
    )

    st.subheader("5. Una sola petición")
    peticion = st.text_area(
        "Si pudiera pedir UNA SOLA COSA para que usted y sus hijos se sientan más seguros, ¿qué sería?",
        height=100
    )

    st.subheader("6. Presencia policial")
    fuerza_publica = st.radio(
        "¿Ver más presencia de la Fuerza Pública en la calle le haría sentir más seguro/a?",
        ('Sí', 'No', 'No estoy seguro/a')
    )
    
    st.markdown("---")
    
    submit_button = st.form_submit_button(label='➡️ Enviar Encuesta')

# --- Lógica para guardar las respuestas ---
if submit_button:
    try:
        # Autenticar con Google Sheets
        # Esto usará las credenciales del archivo .streamlit/secrets.toml
        gc = gspread.service_account_from_dict(st.secrets["gcp_service_account"])
        
        # Abrir la hoja de cálculo por su nombre
        sh = gc.open("ComunidadPavas")
        
        # Seleccionar la primera hoja de trabajo (worksheet)
        worksheet = sh.get_worksheet(0)
        
        # Crear la fila con los datos del formulario y el timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fila_datos = [
            timestamp,
            seguridad,
            preocupacion,
            descripcion_delito,
            lugares_evitados,
            peticion,
            fuerza_publica
        ]
        
        # Agregar la nueva fila al final de la hoja
        worksheet.append_row(fila_datos)
        
        st.success("¡Gracias por completar la encuesta! Tus respuestas han sido enviadas a la hoja de cálculo. 🎉")
        
        # Mostrar las respuestas para confirmación
        st.markdown("---")
        st.subheader("Resumen de tus respuestas:")
        st.write(f"**1. Seguridad en el barrio:** {seguridad}")
        st.write(f"**2. Principal preocupación:** {preocupacion}")
        st.write(f"**3. Descripción del delito:** {descripcion_delito}")
        st.write(f"**4. Lugares evitados:** {lugares_evitados}")
        st.write(f"**5. Petición para seguridad:** {peticion}")
        st.write(f"**6. Presencia policial:** {fuerza_publica}")
        
    except Exception as e:
        st.error(f"Ocurrió un error al intentar guardar los datos: {e}")
        st.info("Asegúrate de que el Google Sheet se llama 'ComunidadPavas' y que lo has compartido con la cuenta de servicio.")
