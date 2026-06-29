from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size < 2:
    if rank == 0:
        print("Ejecuta con al menos 2 procesos.")
        print("Ejemplo: mpirun --allow-run-as-root -np 2 python3 ejemplos/03_send_recv.py")
else:
    if rank == 0:
        numero = 12
        print(f"Rank 0 envía el número {numero} al rank 1")
        comm.send(numero, dest=1, tag=100)

        resultado = comm.recv(source=1, tag=200)
        print(f"Rank 0 recibió el resultado: {resultado}")

    elif rank == 1:
        dato = comm.recv(source=0, tag=100)
        resultado = dato ** 2
        print(f"Rank 1 recibió {dato}, calculó {resultado} y lo devuelve")
        comm.send(resultado, dest=0, tag=200)
