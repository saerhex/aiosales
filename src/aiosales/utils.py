from io import BytesIO

from xhtml2pdf import pisa


def extract_values_from_dict(data, *, keys):
    return [
        data[key]
        for key
        in keys
    ]


def generate_pdf(html):
    result = BytesIO()
    pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    return result.getvalue()
