import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("International_Education_Costs.csv")

# --- Середня вартість навчання по країнах --- #
avg_tuition_by_country = (
    data.groupby('Country')['Tuition_USD']
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))
avg_tuition_by_country.plot(kind='bar', color='skyblue')
plt.title('Середня вартість навчання за країнами', fontsize=14)
plt.xlabel('Країна', fontsize=12)
plt.ylabel('Середня вартість навчання (USD)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# --- Середня тривалість навчання за рівнем освіти --- #
avg_duration_by_level = (
    data.groupby('Level')['Duration_Years']
    .mean()
    .sort_values()
)

plt.figure(figsize=(8, 5))
avg_duration_by_level.plot(kind='barh', color='lightgreen')
plt.title('Середня тривалість навчання за рівнем освіти', fontsize=14)
plt.xlabel('Тривалість (роки)', fontsize=12)
plt.ylabel('Рівень освіти', fontsize=12)
plt.tight_layout()
plt.show()

# --- Топ-10 університетів за вартістю навчання --- #
top_10_universities = (
    data.groupby('University')['Tuition_USD']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
top_10_universities.plot(kind='bar', color='gold')
plt.title('Топ 10 університетів за вартістю навчання', fontsize=14)
plt.xlabel('Університет', fontsize=12)
plt.ylabel('Середня вартість навчання (USD)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# --- Середній візовий збір за країнами --- #
avg_visa_fee_by_country = (
    data.groupby('Country')['Visa_Fee_USD']
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))
avg_visa_fee_by_country.plot(kind='bar', color='salmon')
plt.title('Середня вартість візового збору за країнами', fontsize=14)
plt.xlabel('Країна', fontsize=12)
plt.ylabel('Середній візовий збір (USD)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()