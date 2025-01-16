import pandas as pd
import matplotlib.pyplot as plt

# Sample data for cpu and iowait
data = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "dt": [
        "2024-06-26 09:22:37",
        "2024-06-26 09:42:37",
        "2024-06-26 09:15:37",
        "2024-06-26 09:03:37",
        "2020-05-27 23:09:31",
        "2020-05-27 23:09:32",
        "2024-04-26 09:22:37",
        "2024-05-26 09:42:37",
        "2024-05-26 09:15:37",
        "2024-04-26 09:03:37",
        "2020-04-27 23:09:31",
        "2020-04-27 23:09:32",
        "2024-06-26 11:56:37",
    ],
    "cpu": [
        86.60,
        71.88,
        47.08,
        63.51,
        48.35,
        49.45,
        86.60,
        71.88,
        47.08,
        63.51,
        48.35,
        49.45,
        75.44,
    ],
    "iowait": [
        34.51,
        6.85,
        37.20,
        26.80,
        11.00,
        24.00,
        34.51,
        6.85,
        37.20,
        26.80,
        11.00,
        24.00,
        21.86,
    ],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert 'dt' to datetime
df["dt"] = pd.to_datetime(df["dt"])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df["dt"], df["cpu"], label="CPU", marker="o")
plt.plot(df["dt"], df["iowait"], label="IO Wait", marker="x")
plt.xlabel("Date Time")
plt.ylabel("Percentage")
plt.title("CPU and IO Wait over Time")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
