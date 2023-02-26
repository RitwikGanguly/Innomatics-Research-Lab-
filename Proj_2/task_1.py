import streamlit as st
from PIL import Image

from pathlib import Path

cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = cur_dir / "assets" / "cv.pdf"
prof_pic = cur_dir / "assets" / "profile-pic.png"



# Description
PAGE_TITLE = "RESUME | RITWIK GANGULY"
PAGE_ICON = ":fire:"
NAME = "Ritwik Ganguly"
DESCRIPTION = """
I am a CSE student, currently in 3rd year and enthusiastic in data science, data analysis & Machine Learning, aspire to learn new thing at every second. 
"""
EMAIL = "gangulyritwik2003.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/ritwik-ganguly-148aa2203",
    "GitHub": "https://github.com/RitwikGanguly",
}
PROJECTS = {
    "🏆 Virtual Mouse - Can control the courser with two fingers": "https://github.com/RitwikGanguly/Virtual-Mouse-Project",
    "🏆 Data Analysis Project - Multiple EDA Projects": "https://github.com/RitwikGanguly/Data_Analysis_Ritwik",
    "🏆 Webscraping - Done web scraping": "https://github.com/RitwikGanguly/Flipkart_web_Scriping"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hi!! :red[Everyone]")
st.subheader("welcome all 😎😎😎😎")

# Load pdf and profile pic


with open(resume_file, "rb") as pdf_file:
    pdf = pdf_file.read()

prof = Image.open(prof_pic)


# Header section

col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(prof, width=220)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label= ":reminder_ribbon: Download Resume",
        data = pdf,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📩", EMAIL)

st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write('\n')
st.subheader("Knowledge & Self-declaration ")
st.write(
    """
- ✔️ Currently a student, studied in 3rd year
- ✔️ Intermediate knowledge in python, still exploring and trying to grasp a good hand in python
- ✔️ Has understanding in data science and trying to find the hardness behind the easy word ML 
- ✔️ Has team management and problem solving capability
- ✔️ Always try to learn new things through challenges and tasks 
- ✔️ Some time get confused to himself and has somewhat little patience
"""
)

# --- SKILLS ---

st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy), Java, C 
- 📊 Data Visulization: MS Excel, Plotly, seaborn, matplotlib, 
- 📚 Modeling: Logistic regression, linear regression, decition trees, KNN, K-Means, Neural Network
- 🗄️ Databases: MySQL
    """
)

st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("✍️", "**Human Resource Intern | Aashman Foundation**")
st.write("02/2022 - 10/2022")
st.write(
    """
- ► Started as a Human Resource Intern and later ward promoted to Assistant Supervisor
- ► Got LOR and Certificate
"""

)

st.write("🌏️", "**Data Science Intern | The Sparks Foundation**")
st.write("02/2022 - 04/2022")
st.write(
    """
- ► Done 4 real life projects and got LOR as well
"""
)

st.write("🧠", "**Data Science Intern | Innomatics Research Lab**")
st.write("02/2023 - present")
st.write(
    """
- ► <Will write So many things in this section 😊😊>
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")





