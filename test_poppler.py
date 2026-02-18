from pdf2image import pdfinfo_from_path

print("pdf2image imported OK!")

try:
    # We intentionally give a fake file — we only care that it doesn't complain about poppler
    pdfinfo_from_path("fake_nonexistent.pdf")
except Exception as e:
    error_msg = str(e)
    print("\nTest result:")
    print("Error message:", error_msg)
    
    if "poppler" in error_msg.lower() or "PDFInfoNotInstalled" in error_msg:
        print("→ PROBLEM: Poppler is NOT found / not in PATH")
    elif "No such file" in error_msg or "does not exist" in error_msg or "could not find" in error_msg.lower():
        print("→ SUCCESS: Poppler seems correctly installed and in PATH!")
        print("   (The file-not-found error is expected — that's what we wanted to see)")
    else:
        print("→ Unexpected error — paste this full message")