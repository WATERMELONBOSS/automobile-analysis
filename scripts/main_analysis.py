import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Create output directory
os.makedirs("outputs", exist_ok=True)

# Load dataset
df = pd.read_excel("data/Automobile_data.xlsx")

# Basic exploration
print("Shape:", df.shape)
print("Missing values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)
print("\nSummary Statistics:\n", df.describe())

# Plot 1: Vehicle make
plt.figure(figsize=(20, 5))
sns.countplot(x="make", data=df, palette="viridis")
plt.title("Distribution of Vehicle Makes")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("outputs/vehicle_make_distribution.png")
plt.close()

# Plot 2: Aspiration types
plt.figure(figsize=(10, 5))
sns.countplot(y="aspiration", data=df, palette="Set2")
plt.title("Aspiration Type Count")
plt.tight_layout()
plt.savefig("outputs/aspiration_distribution.png")
plt.close()

# Plot 3: Body Style
plt.figure(figsize=(12, 6))
sns.countplot(y="body-style", data=df, palette="coolwarm")
plt.title("Body Style Distribution")
plt.tight_layout()
plt.savefig("outputs/body_style_distribution.png")
plt.close()

# Plot 4: Engine size distribution
plt.figure(figsize=(25, 8))
sns.countplot(x="engine-size", data=df, color="purple")
plt.title("Engine Size Count")
plt.tight_layout()
plt.savefig("outputs/engine_size_distribution.png")
plt.close()

# Plot 5: Engine Size vs. Curb Weight
plt.figure(figsize=(20, 10))
sns.barplot(x="engine-size", y="curb-weight", data=df, palette="mako")
plt.title("Engine Size vs Curb Weight")
plt.tight_layout()
plt.savefig("outputs/engine_vs_weight.png")
plt.close()

# Plot 6: Engine Size vs Drive Wheels
plt.figure(figsize=(20, 10))
sns.countplot(x="engine-size", hue="drive-wheels", data=df)
plt.title("Engine Size vs Drive Wheels")
plt.tight_layout()
plt.savefig("outputs/engine_drive_wheels.png")
plt.close()

# Plot 7: Cylinders count
plt.figure(figsize=(20, 10))
sns.countplot(x="num-of-cylinders", data=df, color="orange")
plt.title("Cylinder Count")
plt.tight_layout()
plt.savefig("outputs/cylinder_count.png")
plt.close()

# Plot 8: Heatmap of correlations
plt.figure(figsize=(18, 14))
correlation = df.select_dtypes(include=['int64', 'float64']).corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png")
plt.close()

print("✅ Analysis complete. All plots saved in the 'outputs' folder.")
