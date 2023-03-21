#Torrent creation
import hashlib
import bencodepy

def create_torrent(file_path, tracker_url):
    # Abre el archivo que deseas compartir y lee su contenido.
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Calcula el hash SHA1 del archivo.
    file_hash = hashlib.sha1(file_data).digest()

    # Crea un diccionario con los metadatos del archivo.
    torrent_dict = {
        'announce': tracker_url,
        'info': {
            'name': file_path,
            'length': len(file_data),
            'pieces': [file_hash],
            'piece length': 256*1024  # Tamaño de cada pieza en bytes
        }
    }   

    # Codifica el diccionario en formato bencode y escribe los datos en un archivo .torrent.
    with open(f"{file_path}.torrent", 'wb') as f:
        f.write(bencodepy.encode(torrent_dict))

    return f"{file_path}.torrent"