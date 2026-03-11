## Computational Verification Report

**Numbers tested:** 3000  
**Divergent trajectories:** None detected  
**Non-trivial cycles:** None detected (only 4–2–1)  

**Record stopping time:** 372  
**Record seed:** 7,237,231  

**Conclusion:**  
The results are consistent with known Collatz behaviour, but they do **not** constitute a proof.
📘 Collatz Counterexample Scanner
Análisis computacional experimental de la Conjetura de Collatz usando datos extraídos de video

Este proyecto implementa un escáner computacional que toma un video como entrada, extrae valores numéricos a partir de los píxeles y analiza cada número bajo la dinámica de la Conjetura de Collatz. El objetivo es detectar:

Trayectorias divergentes

Ciclos no triviales

Tiempos de parada excepcionalmente altos

Aunque no constituye una prueba matemática, este enfoque permite explorar el comportamiento de Collatz desde una perspectiva computacional y probabilística.

🚀 Características principales
Procesamiento de video cuadro por cuadro

Conversión de píxeles RGB en semillas numéricas

Análisis completo de la trayectoria de Collatz

Detección automática de ciclos no triviales

Registro del tiempo de parada máximo

Generación de:

Informe matemático

Dataset en CSV

Gráfica de análisis

Todo ello accesible mediante una interfaz interactiva construida con Gradio.
“Los píxeles del video actúan como un generador pseudoaleatorio natural, permitiendo explorar el espacio numérico de forma no sesgada.”
