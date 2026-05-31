import streamlit as st
from read_data import get_names, load_person_data, get_picture_path
from read_pandas import make_power_hr_plot, zone_bar_plot, read_my_activity
from PIL import Image





#Aushwal zwischen anzeige

page = st.radio(
    "Navigation",
    ["EKG-App", "Power / HR Analyse"],
    horizontal=True
)

st.divider()

########################
#Anzeige EKG-APP
########################


if page == "EKG-App":

    # Eine Auswahlbox
    person_data = load_person_data()
    user_list = get_names(person_data)

    col1, col2 = st.columns(2)


    with col1:
        st.write("# EKG APP")
        st.write("## Versuchsperson auswählen")

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


######################
#Anzeige Power/HR Grafik
#######################

elif page == "Power / HR Analyse":

    st.title("⚡ Power & Heart Rate Analyse")

    max_hr = st.number_input("Max HR", value=190)

    df = read_my_activity()

    
    fig1 = make_power_hr_plot(df, max_hr)
    st.plotly_chart(fig1, use_container_width=True)

   
    fig2 = zone_bar_plot(df, max_hr)
    st.plotly_chart(fig2, use_container_width=True)

    
