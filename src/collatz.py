import matplotlib.pyplot as plt

def collatz_sequence(n):
    """Calcula la secuencia de Collatz para un número dado"""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

results = [] # Lista para almacenar los resultados de la secuencia de Collatz

for n in range(1, 100):
    sequence = collatz_sequence(n)
    iterations = len(sequence) - 1 # El número de iteraciones es la longitud de la secuencia menos 1
    results.append((n, iterations))


# Graficar los resultados
x = [result[1] for result in results]
y = [result[0] for result in results]
xaxis = np.array([2, 8])

# Y axis parameter:
yaxis = np.array([4, 9])

plt.plot(xaxis, yaxis)

plt.scatter(x, y, s=2)
plt.xlabel("Número de iteraciones")
plt.ylabel("Número de comienzo")
plt.title("Secuencia de Collatz para números entre 1 y 100")
plt.savefig("collatz.png")
