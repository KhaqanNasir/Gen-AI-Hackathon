import streamlit as st

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Testing | Home Page",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Main Page Layout
def main():
    # Global CSS to apply the Poppins font
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
    html, body, [class*="css"], *{
        font-family: 'Poppins', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title and Logo
    st.title("Testing")
    st.subheader("Testing")
    st.header("Features")    
    features = [
        {
            "title": "Feature 01",
            "description": "Description ...."
        },
        {
            "title": "Feature 02",
            "description": "Description ...."
        },
        {
            "title": "Feature 03",
            "description": "Description ...."
        },
        {
            "title": "About Us",
            "description": "Discover the vision, team, and journey behind this app. Join us on our mission to innovate education! 🌟"
        }
    ]

    for feature in features:
    st.subheader(feature['title'])
    st.write(feature['description'])
  

    # Navigation Buttons
    st.markdown("<h1 style='text-align: center;'>🚀 Explore Our Chatbots</h1>", unsafe_allow_html=True)
    st.markdown("""
      <div style='text-align:center;'>
         <a href="/CV_Analysis">Page 01</a>
         <a href="/Real_Time_Text-to-Voice">Page 02</a>
         <a href="/Profile_Pic_Generator">Page 03</a>
         <a href="/About_Us">👤 About Us</a>
      </div>
    """, unsafe_allow_html=True)
  
    # Footer
    st.markdown("---")
    st.markdown(
      '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
       unsafe_allow_html=True)

    st.sidebar.success("Select a page above.")

# Run App
if __name__ == "__main__":
    main()