import pandas as pd
data_path = "/mnt/data/data.csv"
data = pd.read_csv(data_path)
print(data.head())
# Data Exploration
print(data.info())
print(data.describe())
print(data.isnull().sum())
print(f"Dataset shape: {data.shape}")

# Data Visualization 
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()
sns.pairplot(data)
plt.show()

