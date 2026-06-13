from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors



def Estilo_Titulo():

    Titulo_Estilo = ParagraphStyle(
            'Titulo Principal',
            parent=None,
            fontSize=18,
            leading=20,
            alignment=1,
            spaceAfter=37,
        )
    
    return Titulo_Estilo


def Estilo_infoArchivo():

    estilo_info = ParagraphStyle(
        'Info Archivo',
        fontSize= 12,
        leading=15,
        alignment=0,
        spaceBefore=7,
        spaceAfter=7
    )

    return estilo_info