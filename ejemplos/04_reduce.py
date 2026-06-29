from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

valor_local = rank + 1

suma_total = comm.reduce(valor_local, op=MPI.SUM, root=0)

print(f"Rank {rank}: valor local = {valor_local}")

if rank == 0:
    print(f"Suma total de los valores locales = {suma_total}")
