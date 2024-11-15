import random
import time
import csv
import io
from datetime import datetime, timedelta


def generate_random_data():
    """Generate a random date, temperature, and pressure."""
    # Generate random date within the past 30 days
    date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime(
        "%Y-%m-%d.%H:%M:%S"
    )

    # Generate random temperature and pressure values
    temperature = round(
        random.uniform(-10, 35), 2
    )  # Temperature between -10 and 35 degrees Celsius
    pressure = round(random.uniform(950, 1050), 2)  # Pressure between 950 and 1050 hPa

    return {"date": date, "temperature": temperature, "pressure": pressure}


def generate_csv_data():
    """Generate CSV formatted data."""
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["date", "temperature", "pressure"])

    # Write header
    writer.writeheader()

    # Generate and write random data rows
    for _ in range(random.randint(1, 5)):  # Generate between 1 and 5 rows of data
        writer.writerow(generate_random_data())

    return output.getvalue()
