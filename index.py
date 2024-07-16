import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
file_path = './data/ERM2014_Resultados_Regional.xlsx'
excel_data = pd.ExcelFile(file_path)

# Cargar los datos de la primera hoja
df = pd.read_excel(file_path, sheet_name='Hoja1')

# Agrupar los datos por organización política y sumar los votos
grouped_data = df.groupby('Organización Política')['Votos'].sum().reset_index()

# Ordenar los datos por la cantidad de votos
grouped_data = grouped_data.sort_values(by='Votos', ascending=False)

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['Organización Política'],
        grouped_data['Votos'], color='skyblue')
plt.xlabel('Organización Política')
plt.ylabel('Votos')
plt.title('Votos por Organización Política')
plt.xticks(rotation=90)  # Rotar las etiquetas del eje x para mejor legibilidad
plt.tight_layout()  # Ajustar el diseño para evitar recortes
plt.show()
