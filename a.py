import re  # Importamos el módulo de expresiones regulares

#inciso inciso a
def validar_fechas(texto):
    fechas_cortas = re.findall(r'\b\d{2}-\d{2}-\d{2}\b', texto)

    fechas_largas = re.findall(
        r'\b(?:lunes|martes|miércoles|jueves|viernes|sábado|domingo), \d{2} de (?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre) de \d{4}\b',
        texto,
        re.IGNORECASE)

    if fechas_cortas:
        print(" Fechas en formato corto encontradas:", fechas_cortas)
    else:
        print(" No se encontraron fechas en formato corto.")

    if fechas_largas:
        print(" Fechas en formato largo encontradas:", fechas_largas)
    else:
        print(" No se encontraron fechas en formato largo.")

texto = """
Hoy es sábado, 15 de junio de 2024.
También tenemos una fecha abreviada: 24-06-15.
Y otra larga: lunes, 03 de marzo de 2025.
"""
validar_fechas(texto)

#fin inciso a