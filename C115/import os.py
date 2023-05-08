import os

# Ruta de archivo de origen
src = 'source_folder/old_name.txt'

# Ruta de archivo de destino
dst = 'destination_folder/new_name.txt'

# Renombrar archivo existente
os.rename(src, dst)
