# Automated Document Processing & Information Extraction System

## Overview
This project is an **OCR-based document processing system** designed to extract and analyze information from invoices and receipts.

It focuses on building an **end-to-end pipeline for document understanding**, including image processing, text extraction, and future structured data parsing.

---

## Key Features
- Upload invoices/receipts (PDF, PNG, JPG)
- Convert PDF → Image using `pdf2image`
- Extract text using **EasyOCR**
- Display OCR output with **confidence scores**
- Interactive **Streamlit-based web interface**

---

## System Pipeline
The system is designed as a modular pipeline:

1. Document Upload (PDF/Image)
2. PDF → Image Conversion
3. OCR Processing (EasyOCR)
4. Text Output with Confidence Scores
5. *(Planned)* Structured Data Extraction

---

## Current Implementation
- Implemented OCR pipeline using EasyOCR  
- Built a **Streamlit web interface** for real-time document upload and preview  
- Integrated PDF processing using `pdf2image`  
- Extracted raw text along with confidence scores for evaluation  

---

## In Progress / Planned Enhancements
- OpenCV-based preprocessing:
  - Denoising  
  - Adaptive thresholding  
  - Contour detection  

- Structured data extraction:
  - Vendor name  
  - Invoice number  
  - Date  
  - Total amount  

- Regex-based entity parsing  
- Accuracy evaluation for extracted fields  

---


---

## Tech Stack
- Python  
- Streamlit  
- EasyOCR    
- pdf2image  

---

## How to Run

```bash
git clone https://github.com/vaishrs/Automated-Document-Processing.git
cd Automated-Document-Processing

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py


Notes

This project is actively being developed and extended into a complete document intelligence system with structured extraction and improved accuracy.
