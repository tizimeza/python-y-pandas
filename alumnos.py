
import pandas as pd
import matplotlib.pyplot as plt
data = {
"Alumno": ["Ana", "Luis", "María", "Pedro"],
"Matemática": [8, 6, 9, 7],
"Lengua": [7, 5, 8, 6]
}
df = pd.DataFrame(data)
df.plot(x="Alumno", y="Matemática", kind="barh", color="skyblue")
plt.title("Notas de Matemática")
plt.show()
