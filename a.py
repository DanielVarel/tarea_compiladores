import re  # Importamos el módulo de expresiones regulares


def validar_texto(texto):
    
#inciso inciso a
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
#fin inciso a

texto_de_prueba = """
Hoy es sábado, 15 de junio de 2024. También tenemos una fecha abreviada: 24-06-15. Y otra larga: lunes, 03 de marzo de 2025.
"""
validar_texto(texto_de_prueba)

#inicio inciso b

textoB = "El Perro del vecino duerme en el jardín. Mi perro duerme en mi cuarto."

# Reemplaza "perro" por "gato" sin importar si son mayúsculas
resultado = re.sub(r"\bperro\b", "gato", textoB, flags=re.IGNORECASE)

print("Texto original:", textoB)
print("Texto modificado:", resultado)

#fin inciso b

#inicio inciso e

contrasenas = ["Clave123!", "insegura", "Segura2025", "P@ssword1", "Fuerte*2025"]

# Regex para validar contraseña segura
regex_segura = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$"

for c in contrasenas:
    if re.fullmatch(regex_segura, c):
        print(f"Contraseña segura: {c}")
    else:
        print(f"Contraseña insegura: {c}")

#fin inciso e