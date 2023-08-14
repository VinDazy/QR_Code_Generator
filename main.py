import streamlit as st
from functions import generate_qr, hex_to_rgb
import time 
st.set_page_config(page_title="QR Code Generator",layout="wide", page_icon="💾")

st.title("QR Generator Web app")
##MainMenu {visibility: hidden;} : ADD this to hide_menu_style to hide the hamburger menu

hide_menu_style="""
<style>

footer {visibility: hidden;}
</style> 
"""
st.markdown(hide_menu_style,unsafe_allow_html=True)

input_column, output_column = st.columns(2)
with input_column:
    input_form = input_column.form(key="input")

    url = input_form.text_input("Enter website link ")
    input_form.markdown("---")
    color1, color2 = input_form.columns(2)
    with color1:
        fill_color = color1.color_picker("Fill Color")

    input_form.markdown("---")
    with color2:
        back_color = color2.color_picker("Back Color", value="#FFFFFF")

    fill_color = hex_to_rgb(fill_color)
    back_color = hex_to_rgb(back_color)
    box_size = input_form.slider("Box Size", min_value=10, max_value=30)

    input_form.markdown("---")

    border_size = input_form.slider("Boder Size", min_value=1, max_value=10)
    filename = input_form.text_input("File name")
    display = input_form.form_submit_button("Display Qr-Code")
    
    if display:
        if url == '' or filename == '':
            input_form.error("Please provide both a LINK and a FILENAME.",icon='⚠️')
        else:
            st.session_state.load_state = True  # Update load state

    # Initialize button state
    if "load_state" not in st.session_state:
        st.session_state.load_state = False

with output_column:
    output_form = output_column.form(key="output")
    
    if display or st.session_state.load_state:
        st.session_state.load_state = True  # Update load state
        
        if url != '' and filename != '':
            image = generate_qr(
                URL=url, fill_color=fill_color, back_color=back_color,
                box_size=box_size, border=border_size, filename=filename
            )

            output_form.image(image=image, caption=filename)
            
            submit = output_form.form_submit_button("Generate QR-Code")
            
            # Initialize submit state
            if "submit_state" not in st.session_state:
                st.session_state.submit_state = False
            
            # Download button inside the form with on_click action
            if submit:
                with st.spinner('Gathering resources...'):
                    time.sleep(2)
                output_form.success("Generation Completed, Qr-Code ready for download", icon="✔")
                download_button = st.download_button(
                    label="Download QR-Code",
                    data=image,
                    file_name=filename + '.png',
                    mime="image/png",
                    key="download_button",
                    help="Click to download the QR code image"
                )

                if download_button:
                    st.session_state.submit_state = True



