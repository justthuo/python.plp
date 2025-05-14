# data_analysis_assignment.py

# ------------------------------
# 📦 Imports
# ------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# For error handling
def main():
    try:
        # ------------------------------
        # 🧪 Task 1: Load and Explore Dataset
        # ------------------------------
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

        print("✅ First 5 rows of the dataset:")
        print(df.head())

        print("\n🧾 Data types and structure:")
        print(df.info())

        print("\n🔎 Missing values:")
        print(df.isnull().sum())

        # ------------------------------
        # 🧮 Task 2: Basic Data Analysis
        # ------------------------------
        print("\n📊 Descriptive statistics:")
        print(df.describe())

        print("\n📈 Average measurements per species:")
        print(df.groupby("species").mean())

        # ------------------------------
        # 📊 Task 3: Data Visualization
        # ------------------------------
        sns.set(style="whitegrid")

        # 1. Line chart – Sepal and Petal Length over index
        plt.figure(figsize=(8, 4))
        plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length', color='blue')
        plt.plot(df.index, df['petal length (cm)'], label='Petal Length', color='green')
        plt.title("Line Chart: Sepal vs Petal Length Over Index")
        plt.xlabel("Index")
        plt.ylabel("Length (cm)")
        plt.legend()
        plt.tight_layout()
        plt.savefig("line_chart.png")
        plt.show()

        # 2. Bar chart – Avg petal length by species
        plt.figure(figsize=(6, 4))
        df.groupby("species")["petal length (cm)"].mean().plot(kind='bar', color='coral')
        plt.title("Bar Chart: Average Petal Length per Species")
        plt.ylabel("Average Petal Length (cm)")
        plt.xlabel("Species")
        plt.tight_layout()
        plt.savefig("bar_chart.png")
        plt.show()

        # 3. Histogram – Sepal length distribution
        plt.figure(figsize=(6, 4))
        plt.hist(df['sepal length (cm)'], bins=15, color='skyblue', edgecolor='black')
        plt.title("Histogram: Sepal Length Distribution")
        plt.xlabel("Sepal Length (cm)")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig("histogram.png")
        plt.show()

        # 4. Scatter plot – Sepal vs Petal length
        plt.figure(figsize=(6, 4))
        sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
        plt.title("Scatter Plot: Sepal vs Petal Length")
        plt.xlabel("Sepal Length (cm)")
        plt.ylabel("Petal Length (cm)")
        plt.tight_layout()
        plt.savefig("scatter_plot.png")
        plt.show()

        # Observations
        print("\n📝 Observations:")
        print("- Iris-virginica generally has the largest petal and sepal measurements.")
        print("- Iris-setosa has the smallest petal lengths.")
        print("- Clear clusters are visible in the scatter plot by species.")

    except FileNotFoundError:
        print("❌ Error: Dataset file not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
