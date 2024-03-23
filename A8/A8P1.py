total_rainfall = []
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for month in months:
    rainfall = float(input(f"Enter total rainfall for {month}: "))
    total_rainfall.append(rainfall)

total_yearly_rainfall = sum(total_rainfall)
average_monthly_rainfall = total_yearly_rainfall / 12
highest_rainfall_month = months[total_rainfall.index(max(total_rainfall))]
lowest_rainfall_month = months[total_rainfall.index(min(total_rainfall))]

print(f"Total yearly rainfall: {total_yearly_rainfall}")
print(f"Average monthly rainfall: {average_monthly_rainfall}")
print(f"Month with highest rainfall: {highest_rainfall_month}")
print(f"Month with lowest rainfall: {lowest_rainfall_month}")