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
    
    st.markdown("""
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">
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
            "github": "=KhaqanNasir",
            "linkedin": "khaqan-nasir",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'member01.jpg')
        },
        {
            "name": "Muhammad Adnan Tariq",
            "github": "adnaan-tariq",
            "linkedin": "adnaantariq",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'member02.JPG')
        },
        {
            "name": "Muhammad Ibtisiam Afzal",
            "github": "ibtisamafzal",
            "linkedin": "ibtisamafzal",
            "image": os.path.join(os.path.dirname(__file__), 'assets', 'member03.JPG')
        }
    ]

    cols = st.columns(len(team_members))
    for col, member in zip(cols, team_members):
         with col:
            # Encode image to base64
            encoded_image = encode_image(member['image'])
        
            # HTML structure with background color and adjusted image height
            st.markdown(f"""
            <div style='background-color: #f8f9fa; border-radius: 10px; padding: 20px; margin-bottom: 20px; text-align: center;'>
                <div style='background-color: #ffffff; border-radius: 50%; width: 200px; height: 200px; margin: 0 auto; display: flex; justify-content: center; align-items: center;'>
                    <img src="data:image/jpeg;base64,{encoded_image}" alt="{member['name']}" style='width: 100%; height: 100%; object-fit: cover; border-radius: 50%;'>
                </div>
                <div style='font-size: 22px; font-weight: 600; color: #5F6366; margin-top: 10px;'>{member['name']}</div>
                <div style='font-size: 18px; color: #5F6366; margin-top: 5px;'>
                    <a href='https://github.com/{member["github"]}' target='_blank' style='font-size: 20px; color: #000000; margin-right: 10px;'>
                        <i class="fab fa-github" style="font-size: 20px; color: #000000; margin-right: 5px;"></i> GitHub
                    </a>
                    <a href='https://linkedin.com/in/{member["linkedin"]}' target='_blank' style='font-size: 20px; color: #0077B5;'>
                        <i class="fab fa-linkedin" style="font-size: 20px; color: #0077B5; margin-right: 5px;"></i> LinkedIn
                    </a>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; font-weight: 600; font-size: 16px;">
            💻 Developed with ❤️ using Streamlit | © 2024
        </div>
    """, unsafe_allow_html=True)
    
# Run the application
if __name__ == "__main__":
    st.set_page_config(
        page_title="About Us | Testing",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    main()
