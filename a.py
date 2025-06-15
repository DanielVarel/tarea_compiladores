import re  # Importamos el módulo de expresiones regulares

def validar_fechas(texto):
    # 1. Buscar fechas en formato corto (YY-MM-DD)
    # \b indica límite de palabra, \d{2} busca exactamente dos dígitos
    fechas_cortas = re.findall(r'\b\d{2}-\d{2}-\d{2}\b', texto)

    # 2. Buscar fechas en formato largo (ej. sábado, 15 de junio de 2024)
    # \w+ busca una palabra (día), \d{2} busca el día del mes (dos dígitos), \w+ el nombre del mes, \d{4} el año
    fechas_largas = re.findall(r'\b\w+, \d{2} de \w+ de \d{4}\b', texto)

    # 3. Mostrar resultados
    if fechas_cortas:
        print("✅ Fechas en formato corto encontradas:", fechas_cortas)
    else:
        print("❌ No se encontraron fechas en formato corto.")

    if fechas_largas:
        print("✅ Fechas en formato largo encontradas:", fechas_largas)
    else:
        print("❌ No se encontraron fechas en formato largo.")

# 🎓 Ejemplo de uso
texto = """
Hoy es sábado, 15 de junio de 2024.
También tenemos una fecha abreviada: 24-06-15.
Y otra larga: lunes, 03 de marzo de 2025.
"""
validar_fechas(texto)
