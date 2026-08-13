import csv
from collections import defaultdict
from pathlib import Path


def calcular_promedio_por_estacion(archivo: Path) -> dict[str, float]:
    """Lee el CSV y calcula el tiempo promedio por estación."""
    tiempos_por_estacion: dict[str, list[float]] = defaultdict(list)

    with archivo.open(encoding="utf-8") as f:
        lector = csv.DictReader(f, skipinitialspace=True)
        for fila in lector:
            fila = {k.strip(): v for k, v in fila.items() if k}
            estacion = fila["estacion"].strip()
            tiempo = float(fila["tiempo_seg"].strip())
            tiempos_por_estacion[estacion].append(tiempo)

    return {
        estacion: sum(tiempos) / len(tiempos)
        for estacion, tiempos in sorted(tiempos_por_estacion.items())
    }


def main() -> None:
    archivo = Path("datos/tiempos.csv")
    promedios = calcular_promedio_por_estacion(archivo)

    print("Tiempo promedio por estación (segundos):")
    print("-" * 40)
    for estacion, promedio in promedios.items():
        print(f"{estacion}: {promedio:.2f} s")


if __name__ == "__main__":
    main()
