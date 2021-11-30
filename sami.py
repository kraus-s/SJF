import streamlit as st

# Content general
# ---------------

def title_page():
    st.title("Das Recht auf eigene Sprache: Die Situation der Sami in Norwegen")
    st.write("Diese WebApp stellt die Ergebnisse der Schweizer Jugend Forscht Studienwoche zum Thema Menschenrechte am Seminar für Nordistik der Universität Basel vor.")


def milestones_page():
    st.write("Interaktiver Zeitstrahl")
    current_year = st.select_slider("Zeitstrahl", options=milestones.keys())
    milestone = milestones[current_year]
    milestone()


# Milestones content
# ------------------


def milestone_year_1880():
    st.write("Im Jahre 1880 passiert XY")


def milestone_year_2021():
    st.write("Heute haben die Sámi mit dem Sameting ein eigenes Parlament und mit NRK Sápmi einen eigenen öffentlich-rechtlichen Rundfunk.")


def milestone_year_1950():
    st.write("1950 ändert sich etwas grundlegendes an der Rechtslage in Norwegen")

# Config
# ------

milestones = {1880: milestone_year_1880, 1950: milestone_year_1950, 2021: milestone_year_2021}
sections = {"Startseite": title_page, "Zeitstrahl": milestones_page}


# Run
#----


def main():
    st.set_page_config(layout="wide")
    st.sidebar.write("Inhaltsverzeichnis")
    section = st.sidebar.selectbox("Zu den einzelnen Abschnitten springen", sections.keys())
    selected_section = sections[section]
    selected_section()

    
if __name__ == "__main__":
    main()
