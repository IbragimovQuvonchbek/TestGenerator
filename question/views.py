from .utils import create_docx_file  # Import the functions


def download_randomized_docx(request):
    return create_docx_file()
