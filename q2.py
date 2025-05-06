import csv

# Dictionary to hold the temperature data for each station across multiple years
years = {}
stations = {}

# Load data from CSV files for each year (1986-2005)
for year in range(1986, 2005):
    try:
        # Open the CSV file for the current year
        with open(f'temperature_data/stations_group_{year}.csv') as f:
            reader = csv.reader(f)
            header = next(reader)  # Skip the header row
            # Store the temperature data for each station in the 'years' dictionary
            # Row[0] contains the station name, and rows 4 onwards contain the temperature data
            years[year] = {row[0]: list(map(float, row[4:])) for row in reader}
    except FileNotFoundError:
        # Handle case where the file for a specific year doesn't exist
        print(f"File for year {year} not found.")
        continue

# Combine the temperature data across all years for each station
for year, data in years.items():
    for station, temps in data.items():
        # If the station isn't already in the 'stations' dictionary, initialize it with an empty list
        if station not in stations:
            stations[station] = []
        # Add the temperature data for this station to the 'stations' dictionary
        stations[station].extend(temps)

# Calculate the average temperature for each month across all stations and years
# List to store the sum of temperatures for each month
monthly_averages = [0] * 12
for station_temps in stations.values():
    for i in range(12):
        # Add the temperature data for each month
        monthly_averages[i] += station_temps[i]
# Divide the total for each month by the number of stations to get the average
monthly_averages = [round(total / len(stations), 2)
                    for total in monthly_averages]

# Save the monthly average temperatures to a file
with open('monthly_average_temp.txt', 'w') as f:
    f.write("Monthly Average Temperatures:\n")
    # Write the average temperature for each month
    f.write("\n".join([f"Month {i + 1}: {avg}" for i,
            avg in enumerate(monthly_averages)]))

# Define the months for each season
seasons = {
    "Summer": [11, 0, 1],  # Dec, Jan, Feb
    "Autumn": [2, 3, 4],   # Mar, Apr, May
    "Winter": [5, 6, 7],   # Jun, Jul, Aug
    "Spring": [8, 9, 10]   # Sep, Oct, Nov
}

# Calculate the average temperature for each season
season_averages = {}
for season, months in seasons.items():
    # Calculate the average temperature for each season by summing the monthly averages for the months of that season
    season_averages[season] = round(
        sum(monthly_averages[m] for m in months) / len(months), 2
    )

# Save the seasonal average temperatures to a file
with open('seasonal_average_temp.txt', 'w') as f:
    f.write("\n\nSeasonal Average Temperatures:\n")
    # Write the average temperature for each season
    for season, avg in season_averages.items():
        f.write(f"{season}: {avg}\n")

# Find the station with the largest temperature range (max temperature - min temperature)
largest_range_station = max(
    stations.items(), key=lambda x: max(x[1]) - min(x[1])
)
# Calculate the temperature range for this station
largest_range = round(
    max(largest_range_station[1]) - min(largest_range_station[1]), 2)

# Save the station with the largest temperature range to a file
with open('largest_temp_range_station.txt', 'w') as f:
    f.write(f"Station with Largest Temperature Range:\n")
    f.write(f"{largest_range_station[0]}: {largest_range}\n")

# Calculate the average temperature for each station across all years
station_averages = {
    station: sum(temps) / len(temps) for station, temps in stations.items()
}

# Find the warmest station (station with the highest average temperature)
warmest_station = max(station_averages.items(), key=lambda x: x[1])
# Find the coolest station (station with the lowest average temperature)
coolest_station = min(station_averages.items(), key=lambda x: x[1])

# Save the warmest and coolest stations to a file
with open('warmest_and_coolest_station.txt', 'w') as f:
    f.write("Warmest Station:\n")
    f.write(f"{warmest_station[0]}: {round(warmest_station[1], 2)}\n\n")
    f.write("Coolest Station:\n")
    f.write(f"{coolest_station[0]}: {round(coolest_station[1], 2)}\n")

print("Data processing completed successfully. Output files have been generated.")
