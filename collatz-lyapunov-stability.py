import gradio as gr
import multiprocessing as mp
import random
import math
import time

# --- CONFIGURACIÓN TÉCNICA ---
MAX_ITER = 15000  # Máximo de pasos antes de considerar que un número diverge

def check_collatz(n):
    """
    Función optimizada para un solo número.
    Retorna (pasos, max_valor, lyapunov_exponent, seed)
    """
    initial_n = n
    steps = 0
    max_val = n
    log_sum = 0
    
    curr = n
    while curr > 1 and steps < MAX_ITER:
        prev = curr
        if curr % 2 == 0:
            curr //= 2
        else:
            curr = (3 * curr + 1) // 2
            steps += 1 # Compensamos el paso extra
        
        # Cálculo de estabilidad (Lyapunov local)
        # Intentamos ver si la tasa de crecimiento es negativa en promedio
        log_sum += math.log(curr / prev)
        
        if curr > max_val:
            max_val = curr
        steps += 1
        
    lyapunov = log_sum / steps if steps > 0 else 0
    
    # Si no llegó a 1, ¡encontramos algo sospechoso!
    found_anomaly = (curr > 1)
    
    return found_anomaly, steps, max_val, lyapunov, initial_n

def search_worker(num_to_test):
    """Función que ejecutará cada núcleo de tu CPU"""
    local_record_steps = 0
    local_record_seed = 0
    
    for _ in range(num_to_test):
        # Generamos un número aleatorio masivo (entre 10^20 y 10^30)
        seed = random.randint(10**20, 10**30)
        anomaly, steps, _, _, s = check_collatz(seed)
        
        if anomaly:
            return (True, s, steps)
        
        if steps > local_record_steps:
            local_record_steps = steps
            local_record_seed = s
            
    return (False, local_record_seed, local_record_steps)

def launch_search(total_numbers):
    total_numbers = int(total_numbers)
    cpus = mp.cpu_count()
    numbers_per_cpu = total_numbers // cpus
    
    start_time = time.time()
    
    # Ejecución en paralelo
    with mp.Pool(cpus) as pool:
        results = pool.map(search_worker, [numbers_per_cpu] * cpus)
    
    end_time = time.time()
    
    # Procesar resultados de todos los núcleos
    global_record_steps = 0
    global_record_seed = 0
    found_seed = None
    
    for anomaly, seed, steps in results:
        if anomaly:
            found_seed = seed
        if steps > global_record_steps:
            global_record_steps = steps
            global_record_seed = seed
            
    duration = end_time - start_time
    
    if found_seed:
        return f"🚨 ¡ANOMALÍA DETECTADA! Semilla: {found_seed}. Este número no regresó a 1 en {MAX_ITER} pasos."
    
    report = f"""
    --- REPORTE TÉCNICO DE ALTA VELOCIDAD ---
    Núcleos de CPU utilizados: {cpus}
    Total de números analizados: {total_numbers}
    Tiempo transcurrido: {duration:.2f} segundos
    Velocidad: {int(total_numbers/duration)} números/seg
    
    RESULTADOS:
    - No se encontraron ciclos ajenos al 4-2-1.
    - No se detectaron divergencias infinitas.
    
    RÉCORD DE ESTA SESIÓN:
    - Semilla: {global_record_seed}
    - Pasos hasta llegar a 1: {global_record_steps}
    
    ESTADO PARA EL CONCURSO:
    La conjetura sigue invicta. Para ganar, el reporte debería decir 'ANOMALÍA DETECTADA'.
    """
    return report

# Interfaz de Gradio
demo = gr.Interface(
    fn=launch_search,
    inputs=gr.Number(label="Cantidad total de números a probar (ej. 1,000,000)", value=500000),
    outputs=gr.Textbox(label="Resultado del Escaneo Multiproceso", lines=15),
    title="Collatz Deep Search v2.0 (Parallel Edition)"
)

if __name__ == "__main__":
    demo.launch()
