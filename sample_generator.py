import random
from datetime import datetime, timedelta
import csv

# Helper functions
def random_visa():
    return str(random.randint(4000000000000000, 4999999999999999))

def random_mastercard():
    return str(random.randint(5100000000000000, 5599999999999999))

def random_amex():
    return str(random.randint(340000000000000, 349999999999999))

def random_discover():
    return str(random.randint(6011000000000000, 6011999999999999))

def random_name():
    first_names = ["Thuy", "Luu", "Vinh", "Linh", "Nam", "Hoa", "Minh", "Tuan", "Phuc", "An"]
    last_names = ["Nguyen", "Tran", "Le", "Pham", "Hoang", "Vo", "Dang", "Do", "Ngo", "Bui"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def random_expiry():
    future_date = datetime.today() + timedelta(days=random.randint(30, 5 * 365))
    return future_date.strftime("%m/%Y")

# Generate data
cards = []
for _ in range(50):
    card_type = random.choice(["visa", "master", "amex", "discover", "invalid"])
    if card_type == "visa":
        number = random_visa()
    elif card_type == "master":
        number = random_mastercard()
    elif card_type == "amex":
        number = random_amex()
    elif card_type == "discover":
        number = random_discover()
    else:
        number = str(random.randint(7000000000000000, 799999999999999999))  # Invalid or unknown

    expiry = random_expiry()
    name = random_name()
    cards.append([number, expiry, name])

# Save to CSV
csv_path = "sample_credit_cards.csv"
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(cards)

csv_path
