import streamlit as st
import folium
from streamlit_folium import folium_static

# Set page configuration
st.set_page_config(
    page_title="Contact Us | AI News Generator",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Main Function
def main():
    # Apply Poppins font across the app
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
    html, body, [class*="css"], * {
        font-family: 'Poppins', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

    # Include Font Awesome CDN for icons
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)

    # Title Section
    st.markdown("<h1 style='font-size: 60px; text-align: center;'>Contact Us</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; text-align: center; color: gray;'>We'd love to hear from you! Reach out with any questions or feedback.</p>", unsafe_allow_html=True)

    # Contact Form
    st.markdown("<h2 style='font-size: 30px;'>📬 Get in Touch</h2>", unsafe_allow_html=True)
    st.write("Fill in the form below to contact us directly!")

    contact_form = st.form(key='contact_form')
    name = contact_form.text_input("Your Name")
    email = contact_form.text_input("Your Email")
    message = contact_form.text_area("Your Message")
    submit_button = contact_form.form_submit_button("Send Message")

    if submit_button:
        if name and email and message:
            st.success("Thank you for reaching out! We will get back to you soon.")
        else:
            st.error("Please fill in all the fields.")

    # Contact Information Section
    st.markdown("<h2 style='font-size: 30px;'>📍 Our Location</h2>", unsafe_allow_html=True)
    st.write("Find us at our office location:")

    # Using Folium to display a map (adjust coordinates for the specified location)
    location_map = folium.Map(location=[30.8124, 73.4655], zoom_start=14)  # M.A Jinnah Road, Okara, Pakistan coordinates
    folium.Marker([30.8124, 73.4655], popup="AI News Generator, M.A Jinnah Road, Okara, Pakistan").add_to(location_map)
    folium_static(location_map)

    # Social Media Section
    st.markdown("<h2 style='font-size: 30px;'>💬 Follow Us</h2>", unsafe_allow_html=True)
    st.write("Stay connected with us through social media:")
    social_media_links = {
        "GitHub": "https://github.com/yourprofile",
        "LinkedIn": "https://www.linkedin.com/in/yourprofile",
        "Twitter": "https://twitter.com/yourprofile"
    }

    for platform, link in social_media_links.items():
        st.markdown(f"""
        <a href='{link}' target='_blank' style='font-size: 20px; color: #0077B5; margin-right: 20px;'>
            <i class="fab fa-{platform.lower()}" style="font-size: 24px;"></i> {platform}
        </a>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; font-weight: 600; font-size: 16px;">💻 Developed with ❤️ using Streamlit | © 2024</p>',
        unsafe_allow_html=True
    )

# Run the app
if __name__ == "__main__":
    main()
