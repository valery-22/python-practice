

def calculate_pi(n_iter):
    """
    Calcula el número PI utilizando el método de Leibniz.

    Args:
        n_iter (int): Número de iteraciones.

    Returns:
        float: Valor aproximado de PI.
    """

    sum = 0.0
    for i in range(1, n_iter + 1):
        sign = 1.0 if i % 2 == 1 else -1.0
        sum += sign / (2 * i - 1)

    pi = 4 * sum
    return pi

def main():
    """
    Función principal que ejecuta el cálculo de PI en paralelo.
    """

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        n_iter_total = 9e9
        n_iter_per_process = n_iter_total // size

        # Enviar el número de iteraciones a cada proceso
        for i in range(1, size):
            comm.Send(n_iter_per_process, dest=i)

    else:
        # Recibir el número de iteraciones del proceso 0
        n_iter_per_process = comm.Recv(source=0)

    # Calcular PI en cada proceso
    pi_partial = calculate_pi(n_iter_per_process)

    # Reducir los valores parciales de PI en el proceso 0
    if rank == 0:
        pi_total = 0.0
        for i in range(1, size):
            pi_partial_recv = comm.Recv(source=i)
            pi_total += pi_partial_recv

        print(f"Valor aproximado de PI: {pi_total}")
    else:
        comm.Send(pi_partial, dest=0)

if __name__ == "__main__":
    main()
