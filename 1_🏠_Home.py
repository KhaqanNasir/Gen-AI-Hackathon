import streamlit as st

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Home | AI News Generator",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add Open Graph meta tags for better social sharing
st.markdown("""
    <head>
        <meta property="og:title" content="Home | AI News Generator" />
        <meta property="og:description" content="Empowering you to stay ahead with AI-curated, real-time news from around the globe. Experience the future of content generation, tailored just for you!" />
        <meta property="og:image" content="logo.png" />
        <meta property="og:type" content="website" />
    </head>
""", unsafe_allow_html=True)

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
        st.markdown("<h1 style='font-size: 60px; margin-top: 20px;'>AI DRIVEN DAILY NEWS CONTENT GENERATOR</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 20px; color: gray;'>Empowering you to stay ahead with AI-curated, real-time news from around the globe. Experience the future of content generation, tailored just for you!</p>",
        unsafe_allow_html=True)
        st.markdown("<p style='font-size: 20px; color: gray;'>Your trusted partner for reliable, dynamic, and innovative news solutions. 🚀🤝</p>",
        unsafe_allow_html=True)
        st.markdown("""<ul style='font-size: 18px; color: gray;'>
               <li>🌟 Generate news articles in seconds.</li>
               <li>🧠 Powered by cutting-edge AI algorithms.</li>
               <li>🌍 Covering global events with precision.</li>
               <li>📡 Designed for journalists, students, and professionals alike.</li>
           </ul>""",unsafe_allow_html=True)
    with col2:
        st.image("logo.png", width=600)

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
