import os
import pandas as pd
import matplotlib.pyplot as plt

RESULTADOS_DIR = "Resultados"

def principal():
    print("Cargando datos...", end="\n\n")
    modelo = leer_modelo("C:/Users/Freddy/OneDrive/Escritorio/Proyectos py/Repositorio 1 github/Evaluacion 4._analisis_de_datos/model.txt")

    try:
        os.mkdir(RESULTADOS_DIR)
    except FileExistsError:
        pass
    
    print("Matriz de figuras de dispersión de los primeros 1000 registros", end="\n\n")
    graficar_dispersion_primeros_1000(modelo)

    print("Matriz de figuras de dispersión de los primeros 1000 registros"
          " con mayor velocidad de viento", end="\n\n")
    graficar_dispersion_mayor_velocidad_1000(modelo)

    print("Histograma de la velocidad del viento con 36 particiones", end="\n\n")
    graficar_histograma_velocidad(modelo)

    print("Histórico mensual de la velocidad media del viento", end="\n\n")
    velocidad_media_mensual(modelo)
    print("Freddy Jaimes 30391404")


def leer_modelo(ruta):
    modelo = pd.read_csv(ruta, sep="\s+", skiprows=3,
                         usecols=["YYYYMMDD", "HHMM", "M(m/s)", "D(deg)"],
                         parse_dates={"MarcaTemporal": [0, 1]}, index_col="MarcaTemporal")
    modelo.rename(columns={"M(m/s)": "Velocidad(m/s)",
                           "D(deg)": "Direccion(deg)"},
                  inplace=True)
    return modelo

def graficar_dispersion_primeros_1000(modelo):
    # Seleccionar las primeras 1000 filas para "Velocidad(m/s)" y "Direccion(deg)"
    subconjunto = modelo.iloc[:1000]
    velocidad = subconjunto["Velocidad(m/s)"]
    direccion = subconjunto["Direccion(deg)"]
    
    # Crear un gráfico de dispersión
    plt.scatter(velocidad, direccion, alpha=0.2)
    plt.xlabel("Velocidad(m/s)")
    plt.ylabel("Direccion(deg)")
    plt.title("Gráfico de Dispersión de los Primeros 1000 Registros")
    plt.show()

def graficar_dispersion_mayor_velocidad_1000(modelo):
    # Seleccionar las 1000 filas con mayor "Velocidad(m/s)"
    mayores_velocidades = modelo.nlargest(1000, "Velocidad(m/s)")
    
    # Suponiendo que "Direccion(deg)" es la columna a graficar contra "Velocidad(m/s)"
    plt.scatter(mayores_velocidades["Velocidad(m/s)"], mayores_velocidades["Direccion(deg)"], alpha=0.2)
    plt.xlabel("Velocidad(m/s)")
    plt.ylabel("Direccion(deg)")
    plt.title("Gráfico de Dispersión de las Mayores 1000 Velocidades")
    plt.show()

def graficar_histograma_velocidad(modelo):
    # Graficar el histograma con 36 particiones
    plt.hist(modelo["Velocidad(m/s)"], bins=36, alpha=0.75, edgecolor='black')
    
    # Añadir etiquetas y título
    plt.xlabel("Velocidad(m/s)")
    plt.ylabel("Frecuencia")
    plt.title("Histograma de las Velocidades del Viento")
    
    # Mostrar el gráfico
    plt.show()

def velocidad_media_mensual(modelo):
    mensual = modelo["Velocidad(m/s)"].groupby([modelo.index.year,
                                                modelo.index.month]).mean()
    mensual.rename_axis(index=["Año", "Mes"], inplace=True)
    print(mensual, end="\n\n")
    
    mensual.plot(legend=True, figsize=(15, 5))
    plt.show()
    return mensual


def leer_modelo(ruta):
    modelo = pd.read_csv(ruta, sep="\s+", skiprows=3,
                         usecols=["YYYYMMDD", "HHMM", "M(m/s)", "D(deg)"],
                         parse_dates={"MarcaTemporal": [0, 1]}, index_col="MarcaTemporal")
    modelo.rename(columns={"M(m/s)": "Velocidad(m/s)",
                           "D(deg)": "Direccion(deg)"},
                  inplace=True)
    return modelo


principal()
