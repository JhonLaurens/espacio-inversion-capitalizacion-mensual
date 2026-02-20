import math

from data_manager import DataManager
from financial_math import FinancialMath
from validations import get_valid_number


def generar_proyeccion_geometrica(p0, r, n_meses):
    """
    Genera la secuencia de proyección geométrica.
    Adaptado de generar_secuencia_cn (Tema-01_ejemplo #8.py).
    """
    secuencia = []
    for mes in range(n_meses + 1):
        monto_geom = FinancialMath.calcular_interes_compuesto(p0, r, mes)
        monto_arit = FinancialMath.calcular_interes_simple(p0, r, mes)

        secuencia.append(
            {
                "Mes": mes,
                "Capital_Geometrico": round(monto_geom, 2),
                "Capital_Aritmetico": round(monto_arit, 2),
                "Diferencia": round(monto_geom - monto_arit, 2),
            }
        )
    return secuencia


def mostrar_tabla_proyeccion(secuencia):
    """
    Muestra la tabla de proyección en consola.
    Adaptado de mostrar_secuencia (Tema-01_ejemplo #7.py).
    """
    print("\n" + "=" * 85)
    print(
        f"{'Mes':<5} | {'Capital Geométrico (C)':<25} | {'Capital Aritmético (S)':<25} | {'Diferencia':<15}"
    )
    print("-" * 85)

    for fila in secuencia:
        print(
            f"{fila['Mes']:<5} | ${fila['Capital_Geometrico']:<24,.2f} | ${fila['Capital_Aritmetico']:<24,.2f} | ${fila['Diferencia']:<14,.2f}"
        )

    print("=" * 85)


def main():
    print("\n--- ESPACIO PARA INVERSIÓN CON CAPITALIZACIÓN MENSUAL ---")
    print(
        "Este programa calcula el crecimiento de una inversión usando interés compuesto."
    )
    print("Ingrese 'Q' o 'X' en cualquier momento para salir.\n")

    # Valores por defecto del ejercicio
    DEFAULT_P0 = 8000000.0
    DEFAULT_R = 0.012
    DEFAULT_N = 36

    use_defaults = input(
        f"¿Desea usar los valores por defecto del ejercicio (P0=${DEFAULT_P0:,.0f}, r={DEFAULT_R*100}%, n={DEFAULT_N})? (s/n): "
    ).lower()

    if use_defaults == "s":
        p0 = DEFAULT_P0
        r = DEFAULT_R
        n = DEFAULT_N
    else:
        p0 = get_valid_number("Ingrese el Capital Inicial (P0): ", float, min_val=0)
        if p0 is None:
            return

        r_percent = get_valid_number(
            "Ingrese la Tasa de Interés Mensual (%): ", float, min_val=0
        )
        if r_percent is None:
            return
        r = r_percent / 100.0

        n = get_valid_number("Ingrese el Número de Meses (n): ", int, min_val=0)
        if n is None:
            return

    print("\nCalculando proyección para:")
    print(f"Capital Inicial (P0): ${p0:,.2f}")
    print(f"Tasa Mensual (r): {r*100:.2f}%")
    print(f"Período (n): {n} meses")

    # 1. Generar Proyección (Conteo / Progresión)
    secuencia = generar_proyeccion_geometrica(p0, r, n)

    # 2. Mostrar Tabla
    mostrar_tabla_proyeccion(secuencia)

    # 3. Calcular Duplicación
    meses_dup = FinancialMath.calcular_meses_duplicacion(r)
    print("\n--- Análisis de Duplicación ---")
    print(f"Tiempo teórico para duplicar la inversión: {meses_dup:.2f} meses")
    print(f"Tiempo práctico (meses enteros): {math.ceil(meses_dup)} meses")

    # 4. Validar Resultado Final (Criterio de Aceptación)
    capital_final = secuencia[-1]["Capital_Geometrico"]
    print(f"\nCapital Final al mes {n}: ${capital_final:,.2f}")

    # 5. Exportar CSV
    exportar = input("\n¿Desea exportar el reporte a CSV? (s/n): ").lower()
    if exportar == "s":
        DataManager.exportar_csv(secuencia)


if __name__ == "__main__":
    main()
