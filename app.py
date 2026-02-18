import streamlit as st
from PIL import Image
import io

st.title("Automated Document Processing MVP")
st.write("Upload a PDF or image of an invoice/receipt")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_type = uploaded_file.type
    
    st.subheader("Uploaded File")
    
    if "pdf" in file_type:
        st.info("PDF detected — we'll convert to image soon. For now showing metadata.")
        # Placeholder — later we'll add pdf2image here
        st.write(f"File name: {uploaded_file.name}")
        st.write(f"Size: {uploaded_file.size / 1024:.1f} KB")
    else:
        # It's an image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    
    st.success("File received! Next: add OCR & extraction.")