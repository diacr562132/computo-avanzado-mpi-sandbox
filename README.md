# Cómputo Avanzado — MPI Sandbox

Este repositorio contiene un ambiente de práctica para la Semana 3 del curso Cómputo Avanzado.

## Objetivo

Practicar:

- MPI
- rank y size
- memoria distribuida
- comunicación entre procesos
- reducción de datos
- Monte Carlo con MPI

## Cómo abrir el Codespace

1. Presiona el botón verde `Code`.
2. Entra a la pestaña `Codespaces`.
3. Presiona `Create codespace on main`.
4. Espera a que el ambiente termine de construirse.

## Verificar ambiente

En la terminal ejecuta:

```bash
python3 --version
mpirun --version
python3 -c "from mpi4py import MPI; print('mpi4py funcionando')"
