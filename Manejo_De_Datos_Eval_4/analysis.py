# Análisis de datos de viento
import os
import pandas as pd
import matplotlib.pyplot as plt

DIRECTORIO_RESULTADOS = "Resultados"

def main():
    print("Cargando datos...", end="\n\n")
    modelo = leer_modelo("Manejo_De_Datos_Eval_4/Datos/modelo.txt")

    try:
        os.mkdir(DIRECTORIO_RESULTADOS)
    except FileExistsError:
        pass

    print("Matriz de gráficos de dispersión de los primeros 1000 registros", end="\n\n")
    graficar_dispersion_primeros_1000(modelo)

    print("Matriz de gráficos de dispersión de los primeros 1000 registros"
          " con mayor velocidad de viento", end="\n\n")
    graficar_dispersion_velocidad_mayor_1000(modelo)

    print("Histograma de velocidad del viento con 36 particiones", end="\n\n")
    graficar_histograma_velocidad(modelo)

    print("Histórico mensual de la velocidad media del viento", end="\n\n")
    mensual = velocidad_media_mensual(modelo)

    print("Tabla de velocidad media mensual del viento", end="\n\n")
    tabla_mensual = tabla_desde_historico(mensual)

    print("Gráfico de la velocidad media mensual del viento por año", end="\n\n")
    graficar_historico_mensual(tabla_mensual)


def graficar_dispersion_primeros_1000(modelo):
    pass

def graficar_dispersion_velocidad_mayor_1000(modelo):
    pd.plotting.scatter_matrix(modelo.nlargest(1000, "Velocidad(m/s)"))
    plt.show()

def graficar_histograma_velocidad(modelo):
    pass

def velocidad_media_mensual(modelo):
    mensual = modelo["Velocidad(m/s)"].groupby([modelo.index.year,
                                                 modelo.index.month]).mean()
    mensual.rename_axis(index=["Año", "Mes"], inplace=True)
    print(mensual, end="\n\n")
    mensual.to_csv(DIRECTORIO_RESULTADOS + "/hist_mens_vel_media_viento.txt", "\t")
    mensual.plot(legend=True, figsize=(15, 5))
    plt.show()
    return mensual

def tabla_desde_historico(mensual):
    pass

def graficar_historico_mensual(tabla_mensual):
    pass

def leer_modelo(ruta):
    modelo = pd.read_csv(ruta, sep="\s+", skiprows=3,
                         usecols=["YYYYMMDD", "HHMM", "M(m/s)", "D(grados)"],
                         parse_dates={"MarcaTemporal": [0, 1]}, index_col="MarcaTemporal")
    modelo.rename(columns={"M(m/s)": "Velocidad(m/s)",
                           "D(grados)": "Dirección(grados)"},
                  inplace=True)
    return modelo