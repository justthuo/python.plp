
# 🌍 COVID-19 Global Trends Analysis (Python Script)

# 📥 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# 📄 Load Data
try:
    df = pd.read_csv("owid-covid-data.csv")
    print("✅ Data loaded successfully")
except FileNotFoundError:
    print("❌ File not found. Please ensure 'owid-covid-data.csv' is in your working directory.")
    exit()

# 🔍 Data Exploration
print("\n📌 Columns:")
print(df.columns)
print("\n🔍 Preview Data:")
print(df.head())

# ❓ Check Missing Values
print("\n🧯 Missing Values:")
print(df.isnull().sum())

# 🧹 Data Cleaning
countries = ['Kenya', 'United States', 'India']
df = df[df['location'].isin(countries)]
df['date'] = pd.to_datetime(df['date'])
df = df.dropna(subset=['total_cases', 'total_deaths', 'total_vaccinations'])
df.fillna(0, inplace=True)

# 💹 Visualizations

# Line Plot: Total Cases Over Time
plt.figure(figsize=(10, 6))
for country in df['location'].unique():
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_cases'], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.tight_layout()
plt.savefig("total_cases_over_time.png")
plt.show()

# Line Plot: Total Deaths Over Time
plt.figure(figsize=(10, 6))
for country in df['location'].unique():
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_deaths'], label=country)
plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.tight_layout()
plt.savefig("total_deaths_over_time.png")
plt.show()

# Line Plot: Total Vaccinations Over Time
plt.figure(figsize=(10, 6))
for country in df['location'].unique():
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_vaccinations'], label=country)
plt.title("Vaccination Rollout Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.tight_layout()
plt.savefig("vaccinations_over_time.png")
plt.show()

# Scatter Plot: Total Cases vs Total Deaths
df['death_rate'] = df['total_deaths'] / df['total_cases']
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='total_cases', y='total_deaths', hue='location')
plt.title("Total Cases vs. Total Deaths")
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.tight_layout()
plt.savefig("cases_vs_deaths.png")
plt.show()

# ✅ Summary
print("\n🧠 Key Insights (write manually or log results):")
print("- India had the fastest vaccine rollout among the selected countries.")
print("- United States had a high number of cases but relatively lower death rate over time.")
print("- Kenya shows a steady but slower growth in vaccinations compared to others.")
# 🌍 COVID-19 Global Trends Analysis (Python Script)

# 📥 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# 📄 Load Data
try:
    df = pd.read_csv("owid-covid-data.csv")
    print("✅ Data loaded successfully")
except FileNotFoundError:
    print("❌ File not found. Please ensure 'owid-covid-data.csv' is in your working directory.")
    exit()

# 🔍 Data Exploration
print("\n📌 Columns:")
print(df.columns)
print("\n🔍 Preview Data:")
print(df.head())

# ❓ Check Missing Values
print("\n🧯 Missing Values:")
print(df.isnull().sum())

# 🧹 Data Cleaning
countries = ['Kenya', 'United States', 'India']
df = df[df['location'].isin(countries)]
df['date'] = pd.to_datetime(df['date'])
df = df.dropna(subset=['total_cases', 'total_deaths', 'total_vaccinations'])
df.fillna(0, inplace=True)

# 💹 Visualizations

# Line Plot: Total Cases Over Time
plt.figure(figsize=(10, 6))
for country in df['location'].unique():
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_cases'], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.tight_layout()
plt.savefig("total_cases_over_time.png")
plt.show()

# Line Plot: Total Deaths Over Time
plt.figure(figsize=(10, 6))
for country in df['location'].unique():
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_deaths'], label=country)
plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.tight_layout()
plt.savefig("total_deaths_over_time.png")
plt.show()

# Line Plot: Total Vaccinations Over Time
plt.figure(figsize=(10, 6))
for country in df['location'].unique():
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_vaccinations'], label=country)
plt.title("Vaccination Rollout Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.tight_layout()
plt.savefig("vaccinations_over_time.png")
plt.show()

# Scatter Plot: Total Cases vs Total Deaths
df['death_rate'] = df['total_deaths'] / df['total_cases']
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='total_cases', y='total_deaths', hue='location')
plt.title("Total Cases vs. Total Deaths")
plt.xlabel("Total Cases")
plt.ylabel("Total Deaths")
plt.tight_layout()
plt.savefig("cases_vs_deaths.png")
plt.show()

# ✅ Summary
print("\n🧠 Key Insights (write manually or log results):")
print("- India had the fastest vaccine rollout among the selected countries.")
print("- United States had a high number of cases but relatively lower death rate over time.")
print("- Kenya shows a steady but slower growth in vaccinations compared to others.")