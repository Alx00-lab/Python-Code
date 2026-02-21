import pandas as pd
import random

first_names = ["Alexis", "Jordan", "Taylor", "Morgan", "Casey", 
               "Riley", "Quinn", "Parker", "Avery", "Blake"]
last_names = ["Martin", "Smith", "Johnson", "Williams", "Brown", 
              "Jones", "Garcia", "Miller", "Davis", "Rodriguez"]

try:
    unique_names = []
    while len(unique_names) < 200:
        name = f"{random.choice(first_names)} {random.choice(last_names)} {random.randint(1, 999)}"
        if name not in unique_names:
            unique_names.append(name)

    # Map each unique name to a customer ID
    customer_mapping = {name: f"CUST-{i+1:04d}" for i, name in enumerate(unique_names)}

    # Generate 800 rows of customer data
    rows = []
    for _ in range(800):
        name = random.choice(unique_names)
        rows.append({
            "customer_id": customer_mapping[name],
            "customer_name": name
        })

    # Save to CSV
    df_customers = pd.DataFrame(rows)
    df_customers.to_csv("Customer_dim.csv", index=False)

except ValueError:
    print("Code not working")
else:
    print("CSV created: 'Customer_dim.csv' with 800 rows and 200 unique customers.")