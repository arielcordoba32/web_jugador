import os
import shutil
from jinja2 import Environment, FileSystemLoader

# Lista de datos de los jugadores
jugadores = [
    {
        "slug": "ariel-cordoba",
        "nombre_jugador": "Ariel Córdoba",
        "video_id": "iKopVYHMYYM",
        "titulo_video": "Mejores jugadas",
        "descripcion_video": "Revisá mis movimientos defensivos, anticipaciones, proyecciones y juego aéreo en partidos oficiales."
    },
    {
        "slug": "mariano-gomez",
        "nombre_jugador": "Mariano Gómez",
        "video_id": "iKopVYHMYYM",  # Se utiliza el mismo ID de ejemplo
        "titulo_video": "Highlights Defensa Central",
        "descripcion_video": "Compilado de recuperaciones de balón, marcas individuales, coberturas y juego aéreo."
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

        # Renderizar la plantilla con las variables del jugador
        contenido_renderizado = template.render(
            nombre_jugador=jugador['nombre_jugador'],
            video_id=jugador['video_id'],
            titulo_video=jugador['titulo_video'],
            descripcion_video=jugador['descripcion_video']
        )

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
