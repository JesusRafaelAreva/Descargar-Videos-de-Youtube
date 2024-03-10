import os
from pytube import YouTube

def descargar_video(url, carpeta_descarga='./videos'):
    try:
        # Crear la carpeta de descarga si no existe
        if not os.path.exists(carpeta_descarga):
            os.makedirs(carpeta_descarga)

        # Crear un objeto YouTube
        video = YouTube(url)

        # Obtener la mejor resolución disponible
        stream = video.streams.get_highest_resolution()

        # Descargar el video en la carpeta especificada
        ruta_descarga = os.path.join(carpeta_descarga, f"{video.title}.mp4")
        print(f"Descargando {video.title}...")
        stream.download(ruta_descarga)
        print(f"Descarga completada. El video se ha guardado en: {ruta_descarga}")

    except Exception as e:
        print(f"Error: {str(e)}")

# Ejemplo de uso
url_youtube = "https://www.youtube.com/watch?v=v65HYuRaM5c"
descargar_video(url_youtube, carpeta_descarga='./videos')

#Codigo enn el repositorio :)
