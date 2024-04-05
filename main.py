from qbClient import AuthClient
import constants as cfg
import requests
from future.moves.urllib.parse import urlencode
import streamlit as st

auth_client = AuthClient(**cfg.client_secrets)

# Get revenue data from Profits/Losses
def getRevenue(accessToken, start_date, end_date):
    base_url = 'https://sandbox-quickbooks.api.intuit.com'
    url = f'{base_url}/v3/company/{cfg.qBData["realm_id"]}/reports/ProfitAndLoss?start_date={start_date}&end_date={end_date}&minorversion=70'
    #print(url)
    auth_header = f'Bearer {accessToken}'
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json',
        'Content-Type': 'text/plain'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("getRevenueData Success")
        return response.json()  # Return the entire JSON
    else:
        print(f"Failed to retrieve revenue data. Status code: {response.status_code}")
        return None
    
def refresh_token():
    response = auth_client.refresh(refresh_token=cfg.refreshToken)
    return response

# Function to fetch total income for a given year
def fetch_income_for_year(year, accessToken):
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    revenue_data = getRevenue(accessToken, start_date, end_date)
    if revenue_data:
        for row in revenue_data.get("Rows", {}).get("Row", []):
            # Check if "Header" exists and if "Income" is in the first column
            if "Header" in row and row["Header"]["ColData"][0].get("value") == "Income":
                # Ensure "Summary" and "ColData" exist and "ColData" has at least 2 elements
                if "Summary" in row and "ColData" in row["Summary"] and len(row["Summary"]["ColData"]) >= 2:
                    total_income = row["Summary"]["ColData"][1].get("value")
                    return total_income
                else:
                    # Log details if the expected data isn't present
                    print(f"Data format issue in year {year}: 'Summary' or 'ColData' missing or 'ColData' too short.")
    else:
        print(f"No revenue data returned for year {year}.")
    return None


# Main loop to get total income from 2019 through 2024
income_by_year = {}
response = refresh_token()  # Initial token refresh
accessToken = response["access_token"]

for year in range(2019, 2025):  # 2025 because range stops before the end value
    total_income = fetch_income_for_year(year, accessToken)
    if total_income is not None:
        income_by_year[str(year)] = float(total_income.replace(',', ''))  # Remove commas and convert to float for the graph
    else:
        # Handle the possibility of needing to refresh the token during the loop
        response = refresh_token()
        accessToken = response["access_token"]
        total_income = fetch_income_for_year(year, accessToken)  # Retry with new token
        if total_income:
            income_by_year[str(year)] = float(total_income.replace(',', ''))

#print(income_by_year)
# Example output: {2023: '912.25', 2024: '9288.52'}

# Streamlit code for displaying the bar chart
st.title('Revenue')
st.bar_chart(income_by_year)