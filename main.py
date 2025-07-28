import streamlit as st
import base64

st.set_page_config(page_title="AutoFolio Pro", layout="wide")

st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}
h1, h2, h3 {
    color: #38bdf8;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
}
.stButton > button {
    background-color: #38bdf8;
    color: black;
    font-weight: bold;
    border-radius: 12px;
    transition: all 0.3s ease-in-out;
}
.stButton > button:hover {
    background-color: #0ea5e9;
    color: white;
    transform: scale(1.05);
}
input, textarea {
    border-radius: 8px !important;
}
.block-container {
    padding-top: 1rem;
}
</style>
"""", unsafe_allow_html=True)

st.title("💼 AutoFolio Pro")

st.markdown("### Select what you want to generate:")
option = st.radio("Choose:", ["Resume", "Portfolio", "Both"])

with st.form("form"):
    st.markdown("#### 👤 Basic Information")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    about = st.text_area("About Me (short bio)")

    if option in ["Resume", "Both"]:
        st.markdown("#### 📄 Resume Details")
        education = st.text_area("Education")
        experience = st.text_area("Experience")
        skills = st.text_input("Skills (comma separated)")

    if option in ["Portfolio", "Both"]:
        st.markdown("#### 🖼️ Portfolio Projects")
        project1 = st.text_input("Project 1 Title")
        project1_desc = st.text_area("Project 1 Description")
        project2 = st.text_input("Project 2 Title")
        project2_desc = st.text_area("Project 2 Description")
        linkedin = st.text_input("LinkedIn URL")
        github = st.text_input("GitHub URL")

    submit = st.form_submit_button("🚀 Generate")

if submit:
    st.success("✅ Portfolio Generated Below")

    st.markdown("---")
    st.markdown(f"## 👤 {name}")
    st.markdown(f"📧 {email} | 📱 {phone}")

    st.markdown(f"### 🧠 About Me\n{about}")

    if option in ["Resume", "Both"]:
        st.markdown(f"### 🎓 Education\n{education}")
        st.markdown(f"### 💼 Experience\n{experience}")
        st.markdown(f"### 🛠️ Skills\n`{skills}`")

    if option in ["Portfolio", "Both"]:
        st.markdown("### 🖼️ Projects")
        st.markdown(f"**{project1}**\n- {project1_desc}")
        st.markdown(f"**{project2}**\n- {project2_desc}")
        st.markdown(f"🔗 [GitHub]({github}) | [LinkedIn]({linkedin})")

    st.markdown("---")
    st.markdown("🖨️ You can print or export this page as PDF using browser's print option.")
