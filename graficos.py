
import pandas as pd
import matplotlib.pyplot as plt
data = {
"Alumno": ["Ana", "Luis", "María", "Pedro"],
"Matemática": [8, 6, 9, 7],
"Lengua": [7, 5, 8, 6]
}
df = pd.DataFrame(data)
df["Matemática"].plot(kind="pie", labels=df["Alumno"], autopct="%1.1f%%")
plt.title("Distribución de notas en Matemática")
plt.ylabel("") # Oculta etiqueta extra
plt.show()