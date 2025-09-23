
import pandas as pd
import matplotlib.pyplot as plt
data = {
"HorasEstudio": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
"Nota": [4, 5, 5, 6, 6, 7, 8, 8, 9, 10]
}
df = pd.DataFrame(data)

# Gráfico de dispersión
df.plot(kind="scatter", x="HorasEstudio", y="Nota", color="blue")
plt.title("Relación entre horas de estudio y nota")
plt.xlabel("Horas de estudio")
plt.ylabel("Nota")
plt.show()
