from data_loading_pipeline import load_all_data
from helpers import save_to_excel

import pandas as pd
import prince
import matplotlib.pyplot as plt

# Load the data
raw, cleaned = load_all_data()

selected_columns = ['gender', 'age', 'status', 'income', 'method']
mca_data = cleaned[selected_columns]

# Assume df is your categorical DataFrame
mca = prince.MCA(n_components=8, random_state=42)
mca = mca.fit(mca_data)

# Project the data
projected = mca.transform(mca_data)

# View results
print(projected.head())

#row_coords = mca.row_coordinates(cleaned)
#col_coords = mca.column_coordinates(cleaned)

print("col_coords")
col_coords = mca.column_coordinates(mca_data)
print(col_coords)

print("col_contrib")
col_contrib = mca.column_contributions_
print(col_contrib)


# plt.figure(figsize=(8,6))
# plt.scatter(row_coords[0], row_coords[1], alpha=0.5)
# plt.title("MCA Projection of Individuals")
# plt.xlabel("Component 1")
# plt.ylabel("Component 2")
# plt.grid(True)
# plt.savefig("mca_individuals.png")

# plt.figure(figsize=(10,7))
# plt.scatter(col_coords[0], col_coords[1], color='red')

# for i, txt in enumerate(col_coords.index):
#     plt.annotate(txt, (col_coords[0][i], col_coords[1][i]), fontsize=9)

# plt.title("MCA Projection of Categories")
# plt.xlabel("Component 1")
# plt.ylabel("Component 2")
# plt.axhline(0, color='gray', linewidth=0.5)
# plt.axvline(0, color='gray', linewidth=0.5)
# plt.grid(True)
# plt.savefig("mca_categories.png")

#print(dir(mca))

print(mca.percentage_of_variance_)

import matplotlib.pyplot as plt

plt.plot(range(1, len(mca.percentage_of_variance_)+1), mca.percentage_of_variance_, marker='o')
plt.xlabel("Component number")
plt.ylabel("Explained inertia (%)")
plt.title("Scree Plot (MCA)")
plt.grid(True)
plt.savefig("scree_plot_mca.png")
