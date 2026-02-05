import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_xlabel("log2 Fold Change")
ax.set_ylabel("-log10 Adjusted p-value")
ax.set_title("Volcano plot")

plt.show()

