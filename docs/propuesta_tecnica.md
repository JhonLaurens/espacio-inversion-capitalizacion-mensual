# Propuesta Técnica Simplificada: Sistema de Inversión con Capitalización Mensual

## 1. Introducción

Este documento presenta una propuesta técnica simplificada para la implementación del módulo "Espacio para Inversión con Capitalización Mensual" como un proyecto académico. El enfoque principal es la ejecución local mediante Python, priorizando la claridad del código y la exactitud matemática sobre la robustez empresarial (microservicios, seguridad avanzada, etc.). Se mantiene la opción de interfaz gráfica vía MCP/Stich para cumplir con los requisitos extendidos.

## 2. Alcance del Proyecto

El sistema se desarrollará como una aplicación local (Script/CLI) que permite:

1.  Calcular proyecciones de inversión con interés compuesto.
2.  Comparar visual y numéricamente el crecimiento geométrico vs. aritmético.
3.  Exportar resultados a archivos locales (CSV/PDF).

**Nota**: Se simplifican los requisitos de "Alta Disponibilidad" y "Roles Complejos" (Admin/Auditor) para centrarse en la lógica de negocio y la experiencia de usuario local.

## 3. Requisitos Funcionales Simplificados

1.  **Simulación de Inversión**:
    - Entrada: Capital ($P_0$), Tasa ($r$), Tiempo ($n$).
    - Proceso: Cálculo mes a mes usando fórmulas de progresiones geométricas.
    - Salida: Tabla en consola y archivo CSV.

2.  **Cálculos Matemáticos (Núcleo)**:
    - Interés Compuesto: $P_n = P_0 (1+r)^n$.
    - Tiempo de Duplicación: $n = \ln(2) / \ln(1+r)$.

3.  **Interfaz de Usuario**:
    - **Principal**: Consola (CLI) interactiva.
    - **Opcional/Avanzada**: Integración con MCP para visualización gráfica si el entorno lo soporta.

## 4. Arquitectura de Software (Monolito Modular)

Se utilizará una estructura de módulos Python simples, ejecutables localmente sin necesidad de servidores complejos.

### 4.1. Estructura de Archivos

- `main.py`: Punto de entrada y orquestador (CLI).
- `financial_math.py`: Biblioteca de funciones matemáticas puras (Interés, Duplicación).
- `data_manager.py`: Manejo de exportación a CSV/TXT.
- `validations.py`: Lógica de validación de entradas.

### 4.2. Integración con Ejemplos Existentes (Reutilización de Código)

Se adaptarán directamente los scripts de `docs\1_CONTEO`:

1.  **Motor Matemático**:
    - Basado en `Tema-01_ejemplo #8.py` (Secuencias Geométricas). Se transformará la función `generar_secuencia_cn` para aceptar parámetros dinámicos ($P_0, r$) en lugar de fijos.
2.  **Validación**:
    - Implementación del bucle `while True` + `try-except` de `factorial+.py` para garantizar que el usuario ingrese números válidos en la consola.
3.  **Visualización**:
    - Uso de `mostrar_secuencia` de `Tema-01_ejemplo #7.py` para imprimir los resultados mes a mes de forma legible.

## 5. Lógica de Negocio y Conteo

La aplicación se centra en la **Progresión Geométrica** como técnica de conteo:

- Cada mes es un paso en la secuencia $n$.
- El capital no se suma, se **multiplica** iterativamente.
  $$P_{n} = P_{n-1} \cdot (1+r)$$

## 6. Manejo de Datos (Persistencia Local)

En lugar de bases de datos, se usarán archivos planos:

- **Resultados**: Se guardarán en carpetas locales `outputs/reporte_inversion_[fecha].csv`.
- **Logs**: Salida estándar por consola.

## 7. Plan de Pruebas Local

1.  **Prueba de Escritorio**: Verificar manualmente que $8,000,000 \times (1.012)^{36} \approx 12,294,268$.
2.  **Prueba de Validación**: Intentar ingresar "abc" o números negativos y verificar que el script no falle (usando la lógica de `factorial+.py`).
3.  **Prueba de Exportación**: Ejecutar el script y confirmar que se crea el archivo CSV.

---

**Conclusión**: Esta arquitectura ligera permite cumplir con el objetivo académico de demostrar el dominio de las progresiones y la programación en Python, sin la sobrecarga de configurar servidores o sistemas de autenticación complejos.
