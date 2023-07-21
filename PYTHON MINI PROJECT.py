import pandas as pd
import openpyxl

# Read the Excel file
df = pd.read_excel("data.xlsx")

# Filter the incident tickets with status Active
active_tickets = df[df["Status"] == "Active"]

# Group the active incident tickets by error description
grouped_tickets = active_tickets.groupby(["Error_description"])

# Create a list of email messages
email_messages = []
for error_description, tickets in grouped_tickets:
    email_message = """
    Subject: Incident tickets for {error_description}

    The following incident tickets are for {error_description} and have a status of {status}:

    | Incident number | Application | Date | Error description | Status |
    | ------------- | -------- | ---- | ------------- | -------- |
    {incident_tickets}
    """.format(
        error_description=error_description,
        status="Active",
        incident_tickets=tickets.to_string(index=False),
    )
    email_messages.append(email_message)

# Send the email messages
from_email = "your_capgemini_email_address@gmail.com"
to_email = "client_email_address@gmail.com"

for email_message in email_messages:
    print(from_email, to_email, email_message)











