from data_loading_pipeline import load_all_data
from helpers import save_to_csv
from config import data_path, output_path
import os

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

# Convert percentage_of_variance_ to a DataFrame
variance_df = pd.DataFrame({'percentage_of_variance': mca.percentage_of_variance_})

# Save to CSV
save_to_csv(variance_df, "mca_percentage_of_variance.csv")

# Plotting the scree plot
plt.plot(range(1, len(mca.percentage_of_variance_)+1), mca.percentage_of_variance_, marker='o')
plt.xlabel("Component number")
plt.ylabel("Explained inertia (%)")
plt.title("Scree Plot (MCA)")
plt.grid(True)
fig_path = os.path.join(output_path, "scree_plot_mca.png")
plt.savefig(fig_path)
print(f"{fig_path} saved")

# column coordinates and contributions
col_coords = mca.column_coordinates(mca_data)
save_to_csv(col_coords, "mca_col_coords.csv")

col_contrib = mca.column_contributions_
save_to_csv(col_contrib, "mca_col_contrib.csv")

# # Create column names for components
# component_names = [f"Component_{i+1}" for i in range(projected.shape[1])]

# print(component_names)
# # Convert projected to DataFrame
# components_df = pd.DataFrame(projected, columns=component_names)

#Merge with the original cleaned DataFrame
merged_df = pd.concat([cleaned, projected], axis=1)

print(projected.head(10))
print(merged_df.head(10))

# Export to CSV
save_to_csv(merged_df, "survey_with_projected_values.csv")
