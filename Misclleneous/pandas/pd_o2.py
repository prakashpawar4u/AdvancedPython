# Sample data for production and consumption
import pandas as pd
import matplotlib.pyplot as plt


production_data = {
    "region": [
        "North America",
        "North America",
        "North America",
        "North America",
        "North America",
    ],
    "country": ["USA", "USA", "USA", "USA", "USA"],
    "year": [1965, 1966, 1967, 1968, 1969],
    "production": [9014, 9579, 10219, 10600, 10828],
    "consumption": [11522, 12100, 12567, 13405, 14153],
}

# Convert to DataFrame
df_production = pd.DataFrame(production_data)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(
    df_production["year"], df_production["production"], label="Production", marker="o"
)
plt.plot(
    df_production["year"], df_production["consumption"], label="Consumption", marker="x"
)
plt.xlabel("Year")
plt.ylabel("Amount (in units)")
plt.title("Production vs Consumption Over Years")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
