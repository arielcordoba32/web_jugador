import os
import shutil
from jinja2 import Environment, FileSystemLoader

# ============================================================
# DATOS DE LOS JUGADORES
# ============================================================
jugadores = [
    {
        # --- Identificación ---
        "slug": "ariel-cordoba",
        "nombre_jugador": "Ariel Córdoba",

        # --- Datos personales ---
        "fecha_nacimiento": "03/03/1990",
        "edad": 36,
        "nacionalidad": "Argentina",

        # --- Datos físicos ---
        "altura": "1,75 m",
        "peso": "78 kg",
        "perfil_habil": "Zurdo",

        # --- Posición ---
        "posicion": "Lateral Izquierdo",
        "segunda_posicion": "Segundo Marcador Central",
        "club_actual": "Sp. Belgrano La Para (2026)",

        # --- Atributos clave (lista de dicts con nombre y valor sobre 100) ---
        "atributos_claves": [
            {"nombre": "Marcación e Intercepción",    "valor": 90},
            {"nombre": "Lectura Táctica / Anticipación", "valor": 88},
            {"nombre": "Juego Aéreo",                 "valor": 82},
            {"nombre": "Proyección y Centros",        "valor": 85},
            {"nombre": "Liderazgo y Voz de Mando",    "valor": 92},
        ],

        # --- Trayectoria (lista de dicts, de más reciente a más antigua) ---
        "trayectoria": [
            {
                "periodo":     "2026",
                "club":        "Sp. Belgrano La Para",
                "liga":        "Liga Regional de Fútbol San Francisco (LRFSF)",
                "descripcion": "Referente defensivo y capitán del equipo, liderando la zaga central y la banda izquierda.",
            },
            {
                "periodo":     "2025",
                "club":        "Atl. Miramar",
                "liga":        "Liga Regional de Fútbol San Francisco (LRFSF) - Torneo Absoluto",
                "descripcion": "Refuerzo clave para afrontar el Torneo Absoluto de la liga regional.",
            },
            {
                "periodo":     "2014 - 2023",
                "club":        "Sp. Belgrano La Para",
                "liga":        "Liga Regional de Fútbol San Francisco (LRFSF)",
                "descripcion": "Ciclo histórico de 9 años de gran regularidad, consolidación y múltiples campeonatos/competencias locales.",
            },
            {
                "periodo":     "2013 - 2014",
                "club":        "Pacífico de Alvear",
                "liga":        "Torneo Argentino B",
                "descripcion": "Experiencia federal compitiendo a nivel nacional en una de las ligas más físicas y competitivas del país.",
            },
            {
                "periodo":     "2013",
                "club":        "Sp. Belgrano La Para",
                "liga":        "Liga Regional de Fútbol San Francisco (LRFSF)",
                "descripcion": "Paso importante para afianzar minutos en primera división en la exigente liga regional cordobesa.",
            },
            {
                "periodo":     "2012",
                "club":        "Atl. Policial de Catamarca",
                "liga":        "Torneo Argentino B",
                "descripcion": "Paso por el histórico club catamarqueño sumando experiencia valiosa en torneos del Consejo Federal.",
            },
            {
                "periodo":     "2011 - 2012",
                "club":        "Talleres de Córdoba",
                "liga":        "Torneo Argentino A",
                "descripcion": "Inicio de carrera en una institución gigante del interior del país, formando parte de su plantel en el Torneo Argentino A.",
            },
        ],

        # --- Video ---
        "video_id":        "iKopVYHMYYM",
        "titulo_video":    "Mejores jugadas",
        "descripcion_video": "Revisá mis movimientos defensivos, anticipaciones, proyecciones y juego aéreo en partidos oficiales.",
    },

    # ---- JUGADOR DE EJEMPLO (ficticio) -------------------------
    {
        "slug": "mariano-gomez",
        "nombre_jugador": "Mariano Gómez",
        "fecha_nacimiento": "15/06/1993",
        "edad": 32,
        "nacionalidad": "Argentina",
        "altura": "1,82 m",
        "peso": "81 kg",
        "perfil_habil": "Diestro",
        "posicion": "Defensa Central",
        "segunda_posicion": "Volante Defensivo",
        "club_actual": "Deportivo Ejemplo FC (2026)",
        "atributos_claves": [
            {"nombre": "Anticipación",              "valor": 88},
            {"nombre": "Juego Aéreo",               "valor": 91},
            {"nombre": "Marca al Hombre",           "valor": 86},
            {"nombre": "Salida con Balón",          "valor": 80},
            {"nombre": "Liderazgo Defensivo",       "valor": 89},
        ],
        "trayectoria": [
            {
                "periodo":     "2024 - 2026",
                "club":        "Deportivo Ejemplo FC",
                "liga":        "Liga Regional Ejemplo",
                "descripcion": "Capitán defensivo y pilar del sistema de juego del equipo.",
            },
            {
                "periodo":     "2020 - 2023",
                "club":        "Atlético Muestra",
                "liga":        "Torneo Provincial",
                "descripcion": "Destacado en defensa de zona y en la organización del bloque defensivo.",
            },
            {
                "periodo":     "2015 - 2019",
                "club":        "Club Demo Sur",
                "liga":        "Torneo Argentino B",
                "descripcion": "Formación en divisiones nacionales, desarrollando solidez técnica y táctica.",
            },
        ],
        "video_id":        "iKopVYHMYYM",
        "titulo_video":    "Highlights Defensa Central",
        "descripcion_video": "Compilado de recuperaciones de balón, marcas individuales, coberturas y juego aéreo.",
    },
]


# ============================================================
# FUNCIÓN GENERADORA
# ============================================================
def generar_paginas():
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)

    try:
        template = env.get_template('template.html')
    except Exception as e:
        print(f"Error al cargar template.html: {e}")
        return

    output_base_dir = 'dist_jugadores'
    os.makedirs(output_base_dir, exist_ok=True)

    archivos_estaticos = ['style.css', 'script.js', 'profile.png']

    for jugador in jugadores:
        dir_jugador = os.path.join(output_base_dir, jugador['slug'])
        os.makedirs(dir_jugador, exist_ok=True)

        contenido_renderizado = template.render(**jugador)

        ruta_index = os.path.join(dir_jugador, 'index.html')
        with open(ruta_index, 'w', encoding='utf-8') as f:
            f.write(contenido_renderizado)

        for archivo in archivos_estaticos:
            if os.path.exists(archivo):
                shutil.copy(archivo, os.path.join(dir_jugador, archivo))
            else:
                print(f"  Advertencia: recurso estático '{archivo}' no encontrado.")

        print(f"✔  Sitio generado: {dir_jugador}/index.html  ({jugador['nombre_jugador']})")


if __name__ == '__main__':
    generar_paginas()
