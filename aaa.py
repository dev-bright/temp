from pypdf import PdfReader

def check_pdf_encryption(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        if reader.is_encrypted:
            try:
                reader.decrypt('')
                print(f"The PDF file '{pdf_path}' is encrypted but not protected by a password.")
            except:
                print(f"The PDF file '{pdf_path}' is encrypted and protected by a password.")
        else:
            print(f"The PDF file '{pdf_path}' is not encrypted.")



def get_pdf_permissions(pdf_path):

    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        if reader.is_encrypted:
            try:
                reader.decrypt('')
                print(f"The PDF file '{pdf_path}' is encrypted but not protected by a password.")
            except:
                print(f"The PDF file '{pdf_path}' is encrypted and protected by a password.")
                return
        else:
            print(f"The PDF file '{pdf_path}' is not encrypted.")

        permissions = reader.user_access_permissions.to_dict()

        permission_mapping = {
            "print": "Printing",
            "modify": "Modifying",
            "copy": "Content copying",
            "annot-forms": "Commenting",
            "fill-forms": "Form filling",
            "extract": "Content copying for accessibility",
            "assemble": "Document assembly",
            "print-high-res": "High-resolution printing"
        }

        print(permissions)
        for key, description in permission_mapping.items():
            is_allowed = permissions.get(key, False)
            print(f"{description}: {'Allowed' if is_allowed else 'Not Allowed'}")

# 使用例
check_pdf_encryption("sample_edit.pdf")
check_pdf_encryption("sample.pdf")


# PDFファイルのパスを指定
pdf_path = 'sample_edit.pdf'
get_pdf_permissions(pdf_path)