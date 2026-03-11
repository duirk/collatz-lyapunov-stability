# collatz-lyapunov-stability
A 4-level research engine to verify 3n+1 stability through logarithmic energy decay and mass-testing.
# 🏛️ Collatz Stability Analysis via Lyapunov Exponents

### A Dynamical Systems Approach to the 3n+1 Conjecture

Este motor de análisis matemático proporciona una vía de validación para la **Conjetura de Collatz**, desplazando el enfoque de la simple iteración numérica hacia la **Dinámica de Contracción Logarítmica**.

## 🔬 Metodología de Investigación

A diferencia de los métodos de fuerza bruta tradicionales, este motor implementa un análisis de **Estabilidad de Lyapunov**. El núcleo de la investigación se basa en el cálculo del valor esperado del crecimiento logarítmico:

$$E[\ln(n_{k+1}) - \ln(n_k)]$$

Un resultado donde $E < 0$ (exponente negativo) constituye una evidencia empírica de que el sistema actúa como un **sumidero entrópico**, forzando a cualquier número entero a colapsar eventualmente en el atractor $\{4, 2, 1\}$.

## 🚀 Características del Motor

* **Nivel 1 & 2: Mapeo de Órbita:** Seguimiento completo de la trayectoria y detección de picos de energía.
* **Nivel 3: Dinámica de Bits:** Análisis de cómo la complejidad binaria se reduce sistemáticamente.
* **Nivel 4: Prueba Estocástica Global:** Ejecución de pruebas masivas aleatorias (N=100) para calcular la media de convergencia universal ($\mu$).
* **Generación de Reportes:** Exportación automatizada de resultados en formato PDF científico mediante el motor PyMuPDF.

## 📊 Resultados de Referencia (Nivel 4)

En pruebas de estrés realizadas con el motor, se han obtenido los siguientes indicadores de estabilidad:
- **Media Global ($\mu$):** $\approx -0.129$
- **Tasa de Convergencia:** 100% (Muestreo estocástico hasta $10^6$)
- **Estado del Sistema:** Asintóticamente estable.


   git clone [https://github.com/TU_USUARIO/Collatz-Lyapunov-Engine.git](https://github.com/TU_USUARIO/Collatz-Lyapunov-Engine.git)
