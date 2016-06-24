
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("pi.csv")

df.plot(kind='bar', x='no', y='pi')

plt.xlabel("money")
plt.ylabel("pi")
plt.grid()
plt.savefig("pi.pdf")
plt.show()

plt.close()