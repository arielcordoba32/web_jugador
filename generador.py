import os
import shutil
from jinja2 import Environment, FileSystemLoader

# # Lista de datos de los jugadores
jugadores = [
    {
        "slug": "AACC",
        "nombre_jugador": "Ariel Córdoba",
        "foto_perfil": "profile.png",
        "iniciales": "AC",
        "numero_camiseta": "3",
        "video_id": "iKopVYHMYYM",
        "titulo_video": "Mejores jugadas",
        "descripcion_video": "Revisá mis movimientos defensivos, anticipaciones, proyecciones y juego aéreo en partidos oficiales.",
        "descripcion_personal": "Como defensor con amplia experiencia, me destaco por mi versatilidad táctica, mi sentido de la ubicación, velocidad de anticipación y salida limpia por bajo.",
        # --- Datos Nuevos que agregamos a la ficha ---
        "edad": "36",
        "altura": "1.75 m",
        "peso": "78 kg",
        "perfil_habil": "Izquierdo",
        "fecha_nacimiento": "03/03/1990",
        "nacionalidad": "Argentina",
        "posicion": "Lateral Izquierdo",
        "segunda_posicion": "Central Izquierdo",
        "descripcion_compartir": "Lateral izquierdo con gran versatilidad táctica. Trayectoria, estadísticas y contacto.",
        "club_actual": "Sportivo Belgrano La Para",
        "escudo_actual": "sp_belgrano.png",  # <-- Agregá esta línea con el nombre exacto de su archivo
        "atributos_claves": [
            {"nombre": "Marcación e intercepción", "porcentaje": "90%"},
            {"nombre": "Lectura táctica / Anticipación", "porcentaje": "88%"},
            {"nombre": "Juego aéreo", "porcentaje": "82%"},
            {"nombre": "Proyección y centros", "porcentaje": "85%"},
            {"nombre": "Liderazgo y voz de mando", "porcentaje": "95%"},
        ],
        # Adentro de los datos del jugador en generador.py
        "galeria": [
            "ariel1.png",
            "ariel2.png",
            "ariel3.png",
            "ariel4.png" # Podés poner 2, 3 o 4 archivos de imagen
        ],
        "trayectoria": [
            {
                "periodo": "2014 - 2026",
                "club": "Sportivo Belgrano La Para",
                "liga": "Liga Regional de Fútbol San Francisco",
                "escudo": "sp_belgrano.png"
            },
        ],
        "whatsapp": "",
        "instagram": ""
    },
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
        "edad": "36",
        "altura": "1.75 m",
        "peso": "78 kg",
        "perfil_habil": "Izquierdo",
        "fecha_nacimiento": "03/03/1990",
        "nacionalidad": "Argentina",
        "posicion": "Lateral Izquierdo",
        "segunda_posicion": "Central Izquierdo",
        "descripcion_compartir": "Lateral izquierdo con gran versatilidad táctica. Trayectoria, estadísticas y contacto.",
        "club_actual": "Sportivo Belgrano La Para",
        "escudo_actual": "sp_belgrano.png",  # <-- Agregá esta línea con el nombre exacto de su archivo
        "atributos_claves": [
            {"nombre": "Marcación e intercepción", "porcentaje": "90%"},
            {"nombre": "Lectura táctica / Anticipación", "porcentaje": "88%"},
            {"nombre": "Juego aéreo", "porcentaje": "82%"},
            {"nombre": "Proyección y centros", "porcentaje": "85%"},
            {"nombre": "Liderazgo y voz de mando", "porcentaje": "95%"},
        ],
        # Adentro de los datos del jugador en generador.py
        "galeria": [
            "ariel1.png",
            "ariel2.png",
            "ariel3.png",
            "ariel4.png" # Podés poner 2, 3 o 4 archivos de imagen
        ],
        "trayectoria": [
            {
                "periodo": "2014 - 2026",
                "club": "Sportivo Belgrano La Para",
                "liga": "Liga Regional de Fútbol San Francisco",
                "escudo": "sp_belgrano.png"
            },
            {
                "periodo": "2013",
                "club": "Sport Club Pacífico de General Alvear",
                "liga": "Argentino B",
                "escudo": "pacifico_gral_alvear.png"
            },
            {
                "periodo": "2012",
                "club": "Atletico Policial de Catamarca",
                "liga": "Argentino B",
                "escudo": "atletico_policial.png"
            },
            {
                "periodo": "2011 - 2012",
                "club": "Talleres de Córdoba",
                "liga": "Argentino A",
                "escudo": "talleres.png"
            }
        ],
        "whatsapp": "5493575417481",
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
        "edad": "28",
        "altura": "1.82 m",
        "peso": "79 kg",
        "perfil_habil": "Derecha",
        "fecha_nacimiento": "12/08/1997",
        "nacionalidad": "Argentina",
        "posicion": "Defensor Central",
        "segunda_posicion": "No aplica",
        "club_actual": "Agente Libre",
        "escudo_actual": " ",
        "atributos_claves": [
            {"nombre": "Anticipación oportuna", "porcentaje": "92%"},
            {"nombre": "Cobertura sólida", "porcentaje": "85%"},
            {"nombre": "Juego físico", "porcentaje": "88%"},
            {"nombre": "Salida limpia", "porcentaje": "95%"},
        ],
        # Adentro de los datos del jugador en generador.py
        "galeria": [
            "foto1.jpg",
            "foto2.jpg",
            "foto3.jpg"  # Podés poner 2, 3 o 4 archivos de imagen
        ],
        "trayectoria": [
            {
                "periodo": "2004 - 2010",
                "club": "Formación Juvenil",
                "liga": "Divisiones Inferiores",
                "escudo": ""
            },
            {
                "periodo": "2011 - 2020",
                "club": "Torneos Regionales",
                "liga": "Liga Regional",
                "escudo": ""
            },
            {
                "periodo": "2021 - Act.",
                "club": "San Lorenzo (Amateur)",
                "liga": "Primera Amateur",
                "escudo": ""
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
        "edad": "42",
        "altura": "1.85 m",
        "peso": "81 kg",
        "perfil_habil": "Derecho",
        "fecha_nacimiento": "29/12/1983",
        "nacionalidad": "Argentina",
        "posicion": "Arquero",
        "segunda_posicion": "",
        "descripcion_compartir": "Arquero con gran presencia física y reflejos rápidos. Trayectoria, estadísticas y contacto.",
        "club_actual": "Sportivo Belgrano",
        "escudo_actual": "sp_belgrano.png",
        "atributos_claves": [
            {"nombre": "Reflejos Rápidos", "porcentaje": "92%"},
            {"nombre": "Juego Aéreo Seguro", "porcentaje": "85%"},
            {"nombre": "Voz de Mando", "porcentaje": "88%"},
            {"nombre": "Penales", "porcentaje": "95%"},
            {"nombre": "Seguridad bajo los Tres Palos", "porcentaje": "90%"}
        ],
        # Adentro de los datos del jugador en generador.py
        "galeria": [
            "foto1.jpg",
            "foto2.jpg",
            "foto3.jpg"  # Podés poner 2, 3 o 4 archivos de imagen
        ],
        "trayectoria": [
            {
                "periodo": "2001 - 2026",
                "club": "Sportivo Belgrano La Para",
                "liga": "Liga Regional de Fútbol San Francisco",
                "escudo": "sp_belgrano.png"
            },
        ],
        "whatsapp": "3575402853",
        "instagram": "damipascal"
    },
    {
        "slug": "sergio-ortopan",
        "nombre_jugador": "Sergio Ortopan",
        "foto_perfil": "sergio_ortopan.png",
        "iniciales": "SO",
        "numero_camiseta": "17",
        "video_id": "c6zT2LCrbWc",
        "titulo_video": "Mejores Jugadas",
        "descripcion_video": "Compilado de las mejores jugadas de Sergio Ortopan.",
        "descripcion_personal": "Defensor central con gran solidez defensiva y posición táctica, destacándose por su anticipación, potencia y capacidad para sumarse al ataque.",
        # --- Datos Nuevos que agregamos a la ficha ---
        "edad": "24",
        "altura": "1.78 m",
        "peso": "77 kg",
        "perfil_habil": "Derecho",
        "fecha_nacimiento": "17/03/2002",
        "nacionalidad": "Argentina",
        "posicion": "Defensor Central",
        "segunda_posicion": "Lateral Derecho",
        "descripcion_compartir": "Central con gran solidez defensiva y posición táctica. Trayectoria, estadísticas y contacto.",
        "club_actual": "Sportivo Belgrano",
        "escudo_actual": "sp_belgrano.png",
        "atributos_claves": [
            {"nombre": "Velocidad", "porcentaje": "92%"},
            {"nombre": "Juego Aéreo", "porcentaje": "85%"},
            {"nombre": "Anticipación", "porcentaje": "88%"},
            {"nombre": "Potencia y despliegue", "porcentaje": "95%"},
            {"nombre": "Defensa", "porcentaje": "90%"}
        ],
        "galeria": [
            "sergio1.jpeg",
            "sergio2.jpeg",
            "sergio3.png",
            "sergio4.png",
        ],
        "trayectoria": [
            {
                "periodo": "2023 - 2026",
                "club": "Sportivo Belgrano La Para",
                "liga": "Liga Regional de Fútbol San Francisco",
                "escudo": "sp_belgrano.png"
            },
            {
                "periodo": "2021 - 2023",
                "club": "Deportivo Maipú de Mendoza",
                "liga": "Liga Mendocina de Fútbol",
                "escudo": "deportivo_maipu.png"
            },
            {
                "periodo": "2010 - 2021",
                "club": "Instituto Atlético Central Córdoba",
                "liga": "Inferiores AFA",
                "escudo": "instituto_cba.png"
            },
        ],
        "whatsapp": "3575406316",
        "instagram": "sergioortopan02"
    },
    {
        "slug": "lionel-bolatti",
        "nombre_jugador": "Lionel Bolatti",
        "foto_perfil": "lio_bolatti.png",
        "iniciales": "LB",
        "numero_camiseta": "10",
        "video_id": "4fYuJTQEpXU",
        "titulo_video": "Mejores Jugadas",
        "descripcion_video": "Compilado de las mejores jugadas de Lionel Bolatti.",
        "descripcion_personal": "Jugador creativo y versátil, con gran visión de juego y capacidad para generar oportunidades de gol. Destacado por su técnica, control de balón y explosividad en el campo.",
        # --- Datos Nuevos que agregamos a la ficha ---
        "edad": "25",
        "altura": "1.74 m",
        "peso": "68 kg",
        "perfil_habil": "Izquierdo",
        "fecha_nacimiento": "05/11/2000",
        "nacionalidad": "Argentina",
        "posicion": "Media Punta",
        "segunda_posicion": "Volante Int. | Extremo Der. | Falso 9",
        "descripcion_compartir": "Media punta con gran visión de juego y capacidad para generar oportunidades de gol. Trayectoria, estadísticas y contacto.",
        "club_actual": "9 De Julio de Morteros",
        "escudo_actual": "9_de_julio_morteros.png",
        "atributos_claves": [
            {"nombre": "VIsión de Juego", "porcentaje": "92%"},
            {"nombre": "Técnica", "porcentaje": "85%"},
            {"nombre": "Presión", "porcentaje": "90%"},
            {"nombre": "Explosividad", "porcentaje": "87%"},
            {"nombre": "Control de Balón", "porcentaje": "90%"}
        ],
        "galeria": [
            "lio1.jpeg",
            "lio2.jpeg",
            "lio3.jpeg",
            "lio4.jpeg",
        ],
        "trayectoria": [
            {
                "periodo": "2024 - 2026",
                "club": "9 de Julio de Morteros",
                "liga": "Regional Amateur",
                "escudo": "9_de_julio_morteros.png"
            },
            {
                "periodo": "2022 - 2023",
                "club": "San Jorge de Brinkmann",
                "liga": "Liga Regional de Fútbol San Francisco",
                "escudo": "san_jorge_brinkmann.png"
            },
            {
                "periodo": "2018 - 2022",
                "club": "Sportivo Belgrano La Para",
                "liga": "Liga Regional de Fútbol San Francisco",
                "escudo": "sp_belgrano.png"
            },
            {
                "periodo": "2015 - 2017",
                "club": "Club Atlético Belgrano de Córdoba",
                "liga": "Liga Cordobesa de Fútbol / Inferiores AFA",
                "escudo": "belgrano_cordoba.png"
            },
        ],
        "whatsapp": "5493575404465",
        "instagram": "lionelbolatti"
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
