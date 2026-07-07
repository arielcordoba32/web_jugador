import os
import shutil
from jinja2 import Environment, FileSystemLoader

# # Lista de datos de los jugadores
jugadores = [
    {
        "slug": "ariel-cordoba",
        "nombre_jugador": "Ariel Córdoba",
        "foto_perfil": "profile.png",
        "iniciales": "AC",
        "numero_camiseta": "3",
        "video_id": "iKopVYHMYYM",
        "titulo_video": "Mejores jugadas",
        "descripcion_video": "Revisá mis movimientos defensivos, anticipaciones, proyecciones y juego aéreo en partidos oficiales.",
        "descripcion_personal": "Como defensor con amplia experiencia, me destaco por mi versatilidad táctica, mi sentido de la ubicación, velocidad de anticipación y salida limpia por bajo.",
        # --- Datos Nuevos que agregamos a la ficha ---
        "edad": "36 años",
        "altura": "1.78 m",
        "peso": "76 kg",
        "perfil_habil": "Izquierdo",
        "fecha_nacimiento": "03/03/1990",
        "nacionalidad": "Argentina",
        "posicion": "Defensor Central",
        "segunda_posicion": "Lateral Izquierdo",
        "club_actual": "Sportivo Belgrano La Para",
        "atributos_claves": [
            {"nombre": "Marcación e intercepción", "porcentaje": "90%"},
            {"nombre": "Lectura táctica / Anticipación", "porcentaje": "88%"},
            {"nombre": "Juego aéreo", "porcentaje": "82%"},
            {"nombre": "Proyección y centros", "porcentaje": "85%"},
            {"nombre": "Liderazgo y voz de mando", "porcentaje": "95%"},
        ],
        "trayectoria": [
            {
                "periodo": "2011 - 2012",
                "club": "Talleres de Córdoba",
                "liga": "Argentino A",
            },
            {
                "periodo": "2012",
                "club": "Atletico Policial de Catamarca",
                "liga": "Argentino B",
            },
            {
                "periodo": "2013",
                "club": "Sport Club Pacífico de General Alvear",
                "liga": "Argentino B",
            },
            {
                "periodo": "2014 - 2026",
                "club": "Sportivo Belgrano La Para",
                "liga": "Liga Regional de Fútbol San Francisco",
            }
        ],
        "whatsapp": "549XXXXXXXXXX",
        "instagram": "arielcordoba9"
    },
    {
        "slug": "mariano-gomez",
        "nombre_jugador": "Mariano Gómez",
        "foto_perfil": "mariano_gomez.png",
        "iniciales": "MG",
        "numero_camiseta": "4",
        "video_id": "iKopVYHMYYM",  # Se utiliza el mismo ID de ejemplo
        "titulo_video": "Highlights Defensa Central",
        "descripcion_video": "Compilado de recuperaciones de balón, marcas individuales, coberturas y juego aéreo.",
        "descripcion_personal": "Como defensor con amplia experiencia, me destaco por mi versatilidad táctica, mi sentido de la ubicación, velocidad de anticipación y salida limpia por bajo.",
        # --- Datos Nuevos que agregamos a la ficha ---
        "edad": "28 años",
        "altura": "1.82 m",
        "peso": "79 kg",
        "perfil_habil": "Derecha",
        "fecha_nacimiento": "12/08/1997",
        "nacionalidad": "Argentina",
        "posicion": "Defensor Central",
        "segunda_posicion": "No aplica",
        "club_actual": "Agente Libre",
        "atributos_claves": [
            {"nombre": "Anticipación oportuna", "porcentaje": "92%"},
            {"nombre": "Cobertura sólida", "porcentaje": "85%"},
            {"nombre": "Juego físico", "porcentaje": "88%"},
            {"nombre": "Salida limpia", "porcentaje": "95%"},
        ],
        "trayectoria": [
            {
                "periodo": "2004 - 2010",
                "club": "Formación Juvenil",
                "liga": "Divisiones Inferiores",
            },
            {
                "periodo": "2011 - 2020",
                "club": "Torneos Regionales",
                "liga": "Liga Regional",
            },
            {
                "periodo": "2021 - Act.",
                "club": "San Lorenzo (Amateur)",
                "liga": "Primera Amateur",
            }
        ],
        "whatsapp": "549XXXXXXXXXX",
        "instagram": "marianogomez_ok"
    },
    {
        "slug": "damian-pascal",
        "nombre_jugador": "Damián Pascal",
        "foto_perfil": "damian_pascal.png",
        "iniciales": "DP",
        "numero_camiseta": "1",
        "video_id": "5qMEgNy-_zM",
        "titulo_video": "Atajadas y reflejos",
        "descripcion_video": "Compilado de atajadas, penales y juego con los pies de la última temporada.",
        "descripcion_personal": "Como arquero con gran presencia física y reflejos rápidos, me destaco por mi seguridad bajo los tres palos, el dominio del área chica y una excelente comunicación para ordenar la línea defensiva.",
        # --- Datos Nuevos que agregamos a la ficha ---
        "edad": "42 años",
        "altura": "1.85 m",
        "peso": "81 kg",
        "perfil_habil": "Derecho",
        "fecha_nacimiento": "29/12/1981",
        "nacionalidad": "Argentina",
        "posicion": "Arquero",
        "segunda_posicion": "",
        "club_actual": "Sportivo Belgrano",
        "atributos_claves": [
            {"nombre": "Reflejos Rápidos", "porcentaje": "92%"},
            {"nombre": "Juego Aéreo Seguro", "porcentaje": "85%"},
            {"nombre": "Voz de Mando", "porcentaje": "88%"},
            {"nombre": "Penales", "porcentaje": "95%"},
            {"nombre": "Seguridad bajo los Tres Palos", "porcentaje": "90%"}
        ],
        "trayectoria": [
            {
                "periodo": "2001 - 2026",
                "club": "Sportivo Belgrano La Para",
                "liga": "Liga Regional de Fútbol San Francisco",
            },
        ],
        "whatsapp": "3575402853",
        "instagram": "damipascal"
    }
]

def generar_paginas():
    # Cargar el entorno de Jinja2
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    
    try:
        template = env.get_template('template.html')
    except Exception as e:
        print(f"Error al cargar template.html: {e}")
        return

    # Carpeta base donde se guardarán todos los jugadores
    output_base_dir = 'dist_jugadores'
    os.makedirs(output_base_dir, exist_ok=True)

    # Archivos estáticos requeridos para la página
    archivos_estaticos = ['style.css', 'script.js', 'profile.png']

    for jugador in jugadores:
        # Crear la carpeta de salida específica del jugador
        dir_jugador = os.path.join(output_base_dir, jugador['slug'])
        os.makedirs(dir_jugador, exist_ok=True)

        # Renderizar la plantilla pasando automáticamente TODOS los datos del diccionario del jugador
        contenido_renderizado = template.render(**jugador)

        # Escribir el archivo index.html
        ruta_index = os.path.join(dir_jugador, 'index.html')
        with open(ruta_index, 'w', encoding='utf-8') as f:
            f.write(contenido_renderizado)

        # Copiar los recursos estáticos (CSS, JS, Imagen) para que la página funcione sola
        for archivo in archivos_estaticos:
            if os.path.exists(archivo):
                shutil.copy(archivo, os.path.join(dir_jugador, archivo))
            else:
                print(f"Advertencia: No se encontró el recurso estático {archivo} para copiarlo.")

        print(f"¡Sitio web generado con éxito para {jugador['nombre_jugador']} en: {dir_jugador}!")

if __name__ == '__main__':
    generar_paginas()
