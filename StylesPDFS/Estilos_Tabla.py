from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

def Tabla_Resultados(datos):

    tabla = Table(datos, colWidths=[150, 100], hAlign='LEFT')

    estilo_tabla = TableStyle([
        ('FONT', (0,0), (-1, 0), 'Helvetica-Bold', 12, 14),
    ('TEXTCOLOR', (0,0), (-1, 0), colors.black),
    ('LEADING', (0,0), (-1,0), 16),
    ('ALIGNMENT', (0,0), (-1,0), 'CENTER'),
    ('VALIGN', (0,0), (-1,0), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#2C3E50')),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#F8F9F9')),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.lightgrey),
    ])

    tabla.setStyle(estilo_tabla)

    return tabla