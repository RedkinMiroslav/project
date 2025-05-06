import matplotlib.pyplot as plt

years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
medium_sized_budgets = [80, 85, 90, 95, 105, 110, 120]

plt.plot(years, medium_sized_budgets, marker="o", linestyle="-")

plt.title("Зміни бюджету фільмів по роках")

plt.xlabel("Рік")
plt.ylabel("Середній бюджет (млн $)")

plt.grid(True)

plt.yticks(range(min(medium_sized_budgets) - 5, max(medium_sized_budgets) + 10, 5))

plt.show()

print("Графік побудовано!")
