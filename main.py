import streamlit as st
from read_data import get_names, load_person_data, get_picture_path
from PIL import Image

col1, col2 = st.columns(2)


with col1:
    st.write("# EKG APP")
    st.write("## Versuchsperson auswählen")

# Eine Auswahlbox
person_data = load_person_data()
user_list = get_names(person_data)

print (user_list)

with col1:
    current_user = st.selectbox(
        'Versuchsperson',
        options = user_list, key="sbVersuchsperson")


with col2:
    picture_path = get_picture_path(
        person_data,
        current_user
    )
    image = Image.open(picture_path)
# Anzeigen eines Bilds mit Caption
    st.image(image, caption=current_user)