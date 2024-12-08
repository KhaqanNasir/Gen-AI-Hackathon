import streamlit as st

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="AI DRIVEN DAILY NEWS GENERATOR",
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

    # Title and Logo Section
    col1, col2 = st.columns([1, 1])  # Adjust the ratio if needed
    with col1:
        st.markdown("<h1 style='font-size: 80px;'>AI DRIVEN DAILY NEWS CONTENT GENERATOR 📰🌍📡</h1>", unsafe_allow_html=True)
    with col2:
        st.image("logo.png", width=600)

    # Features Section
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
         <a href="/Home_Page">Home Page</a>
         <a href="/page02">Page 02</a>
         <a href="/page03">Page 03</a>
         <a href="/About_Us">About Us</a>
      </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
        unsafe_allow_html=True
    )

    st.sidebar.success("Select a page above.")

# Run App
if __name__ == "__main__":
    main()
