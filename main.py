import streamlit as st
from read_data import get_names, load_person_data


# Eine Überschrift der ersten Ebene
st.write("# EKG APP")

# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

# Eine Auswahlbox
person_data = load_person_data()

user_list = get_names(person_data)

print (user_list)

current_user = st.selectbox(
    'Versuchsperson',
    options = user_list, key="sbVersuchsperson")




#st.write(f"the selectetd user: {current_user}")