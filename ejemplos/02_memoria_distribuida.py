from mpi4py import MPI
import socket

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
hostname = socket.gethostname()

contador = 0
contador += rank + 1

print(f"Proceso {rank} en {hostname}: contador local = {contador}")
