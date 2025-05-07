# Crear un paquete para configuraciones separadas
from pathlib import Path

# Crear directorio settings
(Path(__file__).parent / 'settings').mkdir(exist_ok=True)