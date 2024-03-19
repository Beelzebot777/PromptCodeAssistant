import os

def estructura_de_carpetas(directorio, prefijo=''):
    """
    Recursively generates the folder structure of a directory.

    Args:
        directorio (str): The path of the directory to generate the structure for.
        prefijo (str, optional): The prefix to be added to each line of the structure. Defaults to ''.

    Returns:
        str: The generated folder structure.

    """
    resultado = ''  # Variable para acumular la estructura de las carpetas
    with os.scandir(directorio) as entradas:
        for entrada in entradas:
            if entrada.is_dir() and not any(substring in entrada.name for substring in ["env", "venv", ".git", ".vscode", "__pycache__"]):
                resultado += f"{prefijo}+ {entrada.name}\n"  # Añade el nombre del directorio al resultado
                nuevo_prefijo = prefijo + "|  "
                # Llamada recursiva y concatenación del resultado
                resultado += estructura_de_carpetas(entrada.path, nuevo_prefijo)
            elif entrada.is_file():
                resultado += f"{prefijo}- {entrada.name}\n"  # Añade el nombre del archivo al resultado
    return resultado
