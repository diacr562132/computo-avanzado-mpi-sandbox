from mpi4py import MPI
import random
import time
import math

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

total_puntos = 1_000_000
puntos_por_proceso = total_puntos // size

inicio = time.perf_counter()

dentro_local = 0

for _ in range(puntos_por_proceso):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y <= 1:
        dentro_local += 1

dentro_total = comm.reduce(dentro_local, op=MPI.SUM, root=0)

fin = time.perf_counter()

if rank == 0:
    puntos_usados = puntos_por_proceso * size
    pi_aprox = 4 * dentro_total / puntos_usados
    error = abs(math.pi - pi_aprox)

    print(f"Procesos MPI: {size}")
    print(f"Puntos totales usados: {puntos_usados}")
    print(f"Puntos dentro del círculo: {dentro_total}")
    print(f"Pi aproximado: {pi_aprox}")
    print(f"Error: {error}")
    print(f"Tiempo: {fin - inicio:.6f} s")
