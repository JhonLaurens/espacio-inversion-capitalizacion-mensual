
import math

class FinancialMath:
    """
    Módulo de cálculos financieros puros.
    Aplica principios de Progresiones Geométricas.
    
    Implementa:
    - Pn = P0 * (1+r)^n (Regla del Producto en Conteo)
    - n = ln(2) / ln(1+r) (Duplicación)
    """
    
    @staticmethod
    def calcular_interes_compuesto(p0: float, r: float, n: int) -> float:
        """
        Calcula el capital final usando la fórmula de interés compuesto.
        Equivale a una progresión geométrica donde cada mes es un factor multiplicativo.
        
        Args:
            p0: Capital inicial.
            r: Tasa de interés mensual (decimal).
            n: Número de meses.
        
        Returns:
            Capital acumulado en el mes n.
        """
        # Aplicación de Regla del Producto (Factorial/Exponencial)
        return p0 * math.pow(1 + r, n)

    @staticmethod
    def calcular_interes_simple(p0: float, r: float, n: int) -> float:
        """
        Calcula el capital final usando la fórmula de interés simple (Progresión Aritmética).
        
        Args:
            p0: Capital inicial.
            r: Tasa de interés mensual (decimal).
            n: Número de meses.
        
        Returns:
            Capital acumulado en el mes n.
        """
        # Progresión Aritmética: A_n = P0 + (n * P0 * r)
        return p0 + (n * p0 * r)

    @staticmethod
    def calcular_meses_duplicacion(r: float) -> float:
        """
        Calcula el tiempo necesario para duplicar la inversión.
        
        Args:
            r: Tasa de interés mensual (decimal).
            
        Returns:
            Número de meses (float).
        """
        if r <= 0:
            return float('inf')
        return math.log(2) / math.log(1 + r)
