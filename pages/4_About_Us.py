import streamlit as st
import os
import base64

# Load Poppins font globally
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Encode images in base64 format for embedding
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_image

# Main function
def main():
    load_css()

    # Page Title
    st.title("About Us")
    st.write("""
    Welcome to the **About Us** page! We are a passionate team dedicated to building innovative tools that help students achieve their academic goals. 
    Thank you for using our platform—we hope it enhances your learning journey! 🚀
    """)

    # Team Section
    st.header("Meet the Team")
    team_members = [
        {
            "name": "Muhammad Khaqan Nasir",
            "github": "https://github.com/KhaqanNasir",
            "linkedin": "https://linkedin.com/in/khaqan-nasir",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'member01.jpg')
        },
        {
            "name": "Muhammad Adnan Tariq",
            "github": "https://github.com/adnaan-tariq",
            "linkedin": "https://www.linkedin.com/in/adnaantariq/",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'member02.jpg')
        },
        {
            "name": "Muhammad Ibtisiam Afzal",
            "github": "https://github.com/ibtisamafzal",
            "linkedin": "https://www.linkedin.com/in/ibtisamafzal/",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'member03.jpg')
        }
    ]

    # Display team members
    cols = st.columns(len(team_members))
    for col, member in zip(cols, team_members):
        with col:
            encoded_image = encode_image(member['image'])
            st.image(f"data:image/jpeg;base64,{encoded_image}", width=150, caption=member['name'])
            st.write(f"[![GitHub](https://img.shields.io/badge/GitHub-000?style=flat-square&logo=github&logoColor=white)]({member['github']})")
            st.write(f"[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)]({member['linkedin']})")

    # Footer
    st.markdown("---")
    st.write("💻 Developed with ❤️ using Streamlit | © 2024")

# Run the application
if __name__ == "__main__":
    st.set_page_config(
        page_title="About Us | Testing",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    main()
