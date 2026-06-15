import streamlit as st
from streamlit_option_menu import option_menu
from read_data import get_names, load_person_data, get_picture_path
from read_pandas import make_power_hr_plot, zone_bar_plot, read_my_activity
from ekgdata import EKGdata
from PIL import Image


#Aushwal zwischen anzeige

with st.sidebar:
    page = option_menu(
        menu_title="Navigation",
        options=["EKG-App", "Power / HR Analyse"],
        icons=["heart", "activity"],
        default_index=0
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


####################################################
# EKG-Test auswählen
####################################################

    selected_person = None

    for person in person_data:

        full_name = (
            person["firstname"]
            + " "
            + person["lastname"]
        )

        if full_name == current_user:
            selected_person = person
            break


    if selected_person is not None:

        ekg_tests = selected_person["ekg_tests"]

        test_options = {}

        for i, test in enumerate(ekg_tests, start=1):
            test_options[f"Test {i}"] = test["id"]

        selected_test_name = st.selectbox(
            "EKG-Test auswählen",
            options=list(test_options.keys())
        )

        selected_test_id = test_options[selected_test_name]

        ekg = EKGdata.load_by_id(selected_test_id)

        ekg.find_peaks()

        hr = ekg.calculate_avg_hr()

        if hr is not None:
            st.metric(
                "Durchschnittliche Herzfrequenz",
                f"{hr:.1f} bpm"
            )

        fig = ekg.plot_time_series()

        st.plotly_chart(
            fig,
            use_container_width=True
        )



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

    
