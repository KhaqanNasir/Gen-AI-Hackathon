# import streamlit as st

# # Set page configuration (must be the first Streamlit command)
# st.set_page_config(
#     page_title="Home | AI News Generator",
#     page_icon="🏠",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # Main Page Layout
# def main():
#     # Global CSS to apply the Poppins font
#     st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
#     html, body, [class*="css"], *{
#         font-family: 'Poppins', sans-serif;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # Title and Logo Section
#     col1, col2 = st.columns([1, 1])  # Adjust the ratio if needed
#     with col1:
#         st.markdown("<h1 style='font-size: 60px; margin-top: 20px;'>AI DRIVEN DAILY NEWS CONTENT GENERATOR</h1>", unsafe_allow_html=True)
#         st.markdown("<p style='font-size: 20px; color: gray;'>Empowering you to stay ahead with AI-curated, real-time news from around the globe. Experience the future of content generation, tailored just for you!</p>",
#         unsafe_allow_html=True)
#         st.markdown("<p style='font-size: 20px; color: gray;'>Your trusted partner for reliable, dynamic, and innovative news solutions. 🚀🤝</p>",
#         unsafe_allow_html=True)
#         st.markdown("""<ul style='font-size: 18px; color: gray;'>
#                <li>🌟 Generate news articles in seconds.</li>
#                <li>🧠 Powered by cutting-edge AI algorithms.</li>
#                <li>🌍 Covering global events with precision.</li>
#                <li>📡 Designed for journalists, students, and professionals alike.</li>
#            </ul>""",unsafe_allow_html=True)
#     with col2:
#         st.image("logo.png", width=600)


#     # Footer
#     st.markdown("---")
#     st.markdown(
#         '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
#         unsafe_allow_html=True
#     )

#     st.sidebar.success("Select a page above.")

# # Run App
# if __name__ == "__main__":
#     main()

import streamlit as st

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Home | AI News Generator",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Main Page Layout
def main():
    # Custom CSS for horizontal navigation bar with responsiveness
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
    html, body, [class*="css"], *{
        font-family: 'Poppins', sans-serif;
    }

    /* Remove the sidebar */
    .css-18e3th9 {
        display: none;
    }

    /* Navbar Styling */
    .navbar {
        background-color: #0077b5;  /* Blue background */
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 20px;
        position: sticky;
        top: 0;
        width: 100%;
        z-index: 1000;
    }

    .navbar a {
        color: white;
        padding: 12px 20px;
        text-decoration: none;
        font-size: 18px;
        text-align: center;
        display: inline-block;
        transition: background-color 0.3s ease;
    }

    .navbar a:hover {
        background-color: #005f87;  /* Darker blue on hover */
        color: white;
        border-radius: 5px;
    }

    .navbar a.active {
        background-color: #004e72;
        color: white;
        border-radius: 5px;
    }

    /* Navbar for smaller screens (Mobile responsiveness) */
    @media (max-width: 768px) {
        .navbar {
            flex-direction: column;
            align-items: flex-start;
        }

        .navbar a {
            width: 100%;
            text-align: left;
            padding: 12px;
        }
    }

    /* Hamburger Menu */
    .hamburger {
        display: none;
        cursor: pointer;
        font-size: 30px;
        color: white;
    }

    .navbar-links {
        display: flex;
    }

    @media (max-width: 768px) {
        .hamburger {
            display: block;
        }

        .navbar-links {
            display: none;
            flex-direction: column;
            width: 100%;
        }

        .navbar-links.active {
            display: flex;
        }
    }

    /* Content Adjustments */
    .content {
        margin-top: 80px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Add the Navbar with links
    st.markdown("""
    <div class="navbar">
        <div class="navbar-links">
            <a href="1_Home.py" class="active">Home</a>
            <a href="2_about.py">About</a>
            <a href="3_contact.py">Contact</a>
            <a href="4_faqs.py">FAQs</a>
            <a href="5_privacy.py">Privacy</a>
            <a href="6_cookie.py">Cookie Policy</a>
        </div>
        <span class="hamburger" onclick="toggleNavbar()">&#9776;</span>
    </div>
    """, unsafe_allow_html=True)

    # JavaScript for Hamburger Menu Toggle
    st.markdown("""
    <script>
    function toggleNavbar() {
        var navbarLinks = document.querySelector('.navbar-links');
        navbarLinks.classList.toggle('active');
    }
    </script>
    """, unsafe_allow_html=True)

    # Title and Logo Section
    col1, col2 = st.columns([1, 1])  # Adjust the ratio if needed
    with col1:
        st.markdown("<h1 style='font-size: 60px; margin-top: 20px;'>AI DRIVEN DAILY NEWS CONTENT GENERATOR</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 20px; color: gray;'>Empowering you to stay ahead with AI-curated, real-time news from around the globe. Experience the future of content generation, tailored just for you!</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 20px; color: gray;'>Your trusted partner for reliable, dynamic, and innovative news solutions. 🚀🤝</p>", unsafe_allow_html=True)
        st.markdown("""<ul style='font-size: 18px; color: gray;'>
            <li>🌟 Generate news articles in seconds.</li>
            <li>🧠 Powered by cutting-edge AI algorithms.</li>
            <li>🌍 Covering global events with precision.</li>
            <li>📡 Designed for journalists, students, and professionals alike.</li>
        </ul>""", unsafe_allow_html=True)
    with col2:
        st.image("logo.png", width=600)

    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
        unsafe_allow_html=True
    )

# Run App
if __name__ == "__main__":
    main()

