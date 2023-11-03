import streamlit as st
from PIL import Image
import style

st.title("Style Transfer Webapp")

# Select the Input image and style option

img = st.sidebar.selectbox("Select Image",
                   options=('amber.jpg', 'person.jpg'))

style_name = st.sidebar.selectbox("Select style",
                                  options=('candy', 'mosaic', 'rain_princess', 'udnie'))

model = "saved_models/" + style_name + ".pth"
input_image = "images/content-images/" + img 
output_image = "images/output-images/" + img.split(".")[0] + "-" + style_name + "." + img.split(".")[1]

# input images

st.write("### Source Image:")
image = Image.open(input_image)
st.image(image, width=200)

clicked = st.button("Stylize")

if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)

    st.write("### Output Image :")

    image = Image.open(output_image)
    st.image(image, width=200)