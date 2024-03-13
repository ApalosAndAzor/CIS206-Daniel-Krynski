import csv

def calculate_gross_pay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        return (40 * rate) + (overtime_hours * rate * 1.5)
    else:
        return hours * rate

def format_email(first_name, last_name):
    return f"{first_name[0].lower()}{last_name.lower()}@gm.com"

def process_employees(input_file, output_file):
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as empdata, open(output_file, 'w', newline='', encoding='utf-8') as newempdata:
            reader = csv.reader(empdata)
            writer = csv.writer(newempdata)

            next(reader)

            for row in reader:
                try:
                    first_name, last_name, hours_str, rate_str = row
                    hours, rate = float(hours_str), float(rate_str)
                    gross_pay = calculate_gross_pay(hours, rate)
                    email = format_email(first_name, last_name)

                    writer.writerow([last_name, first_name, f"{gross_pay:.2f}", email])
                except ValueError:
                    print(f"Error processing row: {row}")
                    continue
    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

process_employees('A7/EmpData.csv', 'A7/newEmpData.csv')