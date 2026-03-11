import multiprocessing as mp
import random
import math
import time
import os

# --- CONFIGURACIÓN DE ALTO RENDIMIENTO ---
MAX_ITER = 20000        # Aumentamos el límite para dar margen a números gigantes
BATCH_SIZE = 1000000    # Cuántos números probar por cada ráfaga (1 millón)
LOG_FILE = "registro_collatz.txt"

def check_collatz(n):
    initial_n = n
    steps = 0
    curr = n
    while curr > 1 and steps < MAX_ITER:
        if curr % 2 == 0:
            curr //= 2
        else:
            curr = (3 * curr + 1) // 2
            steps += 1
        steps += 1
    
    # Retorna True si NO llegó a 1 (ANOMALÍA)
    return (curr > 1), steps, initial_n

def worker(num_tests):
    local_record_steps = 0
    local_record_seed = 0
    
    for _ in range(num_tests):
        # Buscamos en el rango de 30 a 40 dígitos (Territorio poco explorado)
        seed = random.randint(10**30, 10**40)
        anomaly, steps, s = check_collatz(seed)
        
        if anomaly:
            return (True, s, steps)
        
        if steps > local_record_steps:
            local_record_steps = steps
            local_record_seed = s
            
    return (False, local_record_seed, local_record_steps)

def ejecutar_caceria():
    cpus = mp.cpu_count()
    print(f"🚀 Iniciando cacería en {cpus} núcleos...")
    print(f"📁 Los resultados se guardarán en: {os.path.abspath(LOG_FILE)}")
    
    while True: # Bucle infinito hasta que lo detengas o encuentres algo
        start_t = time.time()
        
        with mp.Pool(cpus) as pool:
            # Dividimos el millón de números entre los núcleos
            results = pool.map(worker, [BATCH_SIZE // cpus] * cpus)
        
        # Procesar ráfaga
        max_s = 0
        max_seed = 0
        for anomaly, seed, steps in results:
            if anomaly:
                mensaje = f"🚨 !!! ANOMALÍA DETECTADA !!! Semilla: {seed} - Pasos: {steps}\n"
                print(mensaje)
                with open(LOG_FILE, "a") as f:
                    f.write(mensaje)
                return # Detener todo si ganamos el concurso
            
            if steps > max_s:
                max_s = steps
                max_seed = seed
        
        end_t = time.time()
        log_msg = f"[{time.ctime()}] Analizados {BATCH_SIZE} números en {end_t-start_t:.2f}s. Récord pasos: {max_s} (Semilla: {max_seed})\n"
        print(log_msg.strip())
        
        with open(LOG_FILE, "a") as f:
            f.write(log_msg)

if __name__ == "__main__":
    try:
        ejecutar_caceria()
    except KeyboardInterrupt:
        print("\nCacería pausada por el usuario.")
