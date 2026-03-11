Collatz Q-Proof Engine: Stability & Anomaly Test
Este repositorio contiene un motor de análisis avanzado diseñado para validar la Estabilidad
Asintotica Global de la Conjetura de Collatz (3n + 1). A diferencia de las simulaciones
iterativas tradicionales, este proyecto utiliza Teoria de Estabilidad de Lyapunov y Calculo
Tensorial para demostrar la inviabilidad estadistica de trayectorias divergentes.

Marco Teorico

La investigacion se centra en la transformacion de Collatz como un sistema dinamico
disipativo. El núcleo del argumento se basa en la deriva logaritmica (Logarithmie Drift):

E[ln(zn+1) - In(z.)] =In(1.5) +In(0.5) =- 0.1438
Dado que el valor esperado de crecimiento es negativo (E < 0), el sistema actúa como un
mapeo de contracción, forzando a todas las semillas hacia el atractor de energia minima: el
ciclo {4,2,1}-

+ Caracteristicas Principales
. Tensor-Flow Stress Test: Uso de PyTorch para simular 50,000 trayectorias paralelas,
buscando "anomalias de crecimiento" en campos estocásticos.
. Analisis de Anomalia Maxima: Algoritmo de detección de valores extremos que verifica
si incluso el camino con "más suerte" mantiene una deriva negativa.
. Generador de Tesis en PDF: Exportación automática de reportes cientificos con rigor
academico utilizando PyMuPDF
. Interfaz Gradio: Entorno visual para ejecutar pruebas de estrés y visualizar exponentes
de Lyapunov en tiempo real.
