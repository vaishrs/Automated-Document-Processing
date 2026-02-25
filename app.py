import streamlit as st
from PIL import Image
import io
import os
from pdf2image import convert_from_path
import tempfile
import easyocr

st.title("Automated Document Processing MVP")
st.write("Upload a PDF or image of an invoice/receipt")

# EasyOCR reader (loads on startup — English only for now)
@st.cache_resource
def load_easyocr():
    return easyocr.Reader(['en'], gpu=False)  # gpu=False for CPU; change to True if you have NVIDIA GPU

reader = load_easyocr()

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_name = uploaded_file.name
    file_type = uploaded_file.type.lower()
    file_size_kb = uploaded_file.size / 1024

    st.subheader(f"Uploaded: {file_name} ({file_size_kb:.1f} KB)")

    # Temporary file path (needed for pdf2image)
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file_name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    display_image = None

    try:
        # Handle PDF or Image
        if "pdf" in file_type:
            images = convert_from_path(tmp_path, first_page=1, last_page=1)
            if images:
                display_image = images[0]
                st.image(display_image, caption="First page of PDF", width=700)
                st.success(f"PDF converted successfully ({len(images)} page(s) total)")
            else:
                st.error("Failed to convert PDF to image.")
                display_image = None
        else:
            display_image = Image.open(uploaded_file)
            st.image(display_image, caption="Uploaded Image", width=700)

        # OCR Section
        if display_image:
            st.subheader("Raw OCR Result (EasyOCR)")
            with st.spinner("Running OCR... usually 3–12 seconds"):
                # Convert PIL image to bytes (EasyOCR accepts bytes or path)
                img_byte_arr = io.BytesIO()
                display_image.save(img_byte_arr, format='PNG')
                img_bytes = img_byte_arr.getvalue()

                # Run EasyOCR
                results = reader.readtext(img_bytes, detail=1)  # detail=1 → returns (bbox, text, confidence)

                extracted_lines = []
                for (bbox, text, conf) in results:
                    extracted_lines.append(f"{text.strip()} (conf: {conf:.2f})")

                full_text = "\n".join(extracted_lines) if extracted_lines else "No text detected."

                st.text_area("Extracted Text + Confidences", full_text, height=400)

                if extracted_lines:
                    st.success(f"OCR complete! Found {len(extracted_lines)} text blocks.")
                else:
                    st.warning("No text detected — we will add preprocessing next to improve this.")

    except Exception as e:
        st.error(f"Error during processing: {str(e)}")
        st.info("Tip: Make sure the image is clear and printed text. Handwritten text is harder.")

    finally:
        # Clean up temporary file
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)

st.info("Next steps once OCR works well:\n"
        "1. Add OpenCV preprocessing (grayscale, resize, threshold)\n"
        "2. Extract structured fields (vendor, date, invoice#, total) using regex + keywords\n"
        "3. Save to SQLite + add search UI")