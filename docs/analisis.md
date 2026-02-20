# Espacio para Inversión con Capitalización Mensual

## Modelo matemático

- Fórmula de interés compuesto:

  $$P_n = P_0 (1 + r)^n$$

- Variables principales:

  | Variable | Descripción             | Valor de referencia |
  | -------- | ----------------------- | ------------------- |
  | \(P_0\)  | Capital inicial         | \(8\,000\,000\)     |
  | \(r\)    | Tasa de interés mensual | \(0.012\)           |
  | \(n\)    | Número de meses         | —                   |

- El crecimiento geométrico aplica un factor multiplicativo cada período, generando una progresión exponencial.

## Cálculo específico

- El sistema computa y muestra el capital exacto para 36 meses y el desglose mensual con formato de moneda local.
- La tabla exportable en CSV incluye los valores geométricos y aritméticos por mes con redondeo al centavo.

## Duplicación del capital

- Condición de duplicación:

  $$P_n \ge 2 P_0$$

- Método logarítmico:

  $$n = \frac{\ln 2}{\ln(1 + r)}$$

- Método iterativo: multiplicación sucesiva mensual hasta alcanzar \(2P_0\) con redondeo a centavos.
- El sistema reporta ambos cálculos y el mínimo número entero de meses requerido.

## Comparación de modelos

- Modelo aritmético:

  $$A_n = P_0 + n \cdot i_m,\quad i_m = P_0 \cdot r$$

- Modelo geométrico:

  $$G_n = P_0 (1 + r)^n$$

- Gráficos comparativos para 6, 12, 24 y 36 meses visibles en la interfaz.

## Por qué domina el crecimiento geométrico

- Efecto multiplicativo: cada período escala el capital por el mismo factor, acumulando incremento sobre incremento.
- En el modelo aritmético el incremento es lineal y fijo, sin retroalimentación sobre el capital acumulado.
- Numéricamente, para tasas positivas, \((1 + r)^n\) crece más rápido que \(1 + n r\) conforme \(n\) aumenta.
- Implicaciones financieras: el interés compuesto beneficia inversiones de largo plazo y refuerza disciplina de mantenimiento del capital.
- Poder del interés compuesto: pequeñas tasas sostenidas generan crecimiento significativo, destacando la importancia de tiempo en el mercado.

## Criterios de precisión y límites

- Redondeo consistente al centavo en todos los cálculos y presentaciones.
- Manejo de capitales hasta \(100\,000\,000\) con validación de entradas y mensajes claros de error.

## Uso del sistema

- Ingresar capital inicial, tasa y meses.
- Calcular resultados, revisar tabla y gráficos.
- Exportar CSV y generar PDF desde la interfaz.
