
"""
if __name__ == "__main__":
    start_date = "2023-01-01"
    end_date = "2023-12-31"

    response = refresh_token()
    revenue = getRevenue(response["access_token"], start_date, end_date)
    file_path = "revenue.json"

    # Open the file in write mode and use json.dump() to write the dictionary to the file
    with open(file_path, "w") as json_file:
        json.dump(revenue, json_file, indent=4)
    
"""    """
    response = refresh_token()
    customer_data = getCustomerData(accessToken = response["access_token"])
    print("The getCustomerData method:")
    print(customer_data.text)
    print("\n\n\n")

    response2 = auth_client.get_user_info(access_token=response["access_token"])
    print("GetUserInfo method(i.e. OpenID Scope):")
    print(response2.text)
    print("\n\n\n")

    payment_data = getPaymentData(accessToken = response["access_token"])
    print(f"The getPaymentData method:")
    print(payment_data.text)"""


"""
def getCustomerData(accessToken):
    #making Request
    base_url = 'https://sandbox-quickbooks.api.intuit.com'
    url = '{0}/v3/company/{1}/companyinfo/{1}'.format(base_url, cfg.qBData["realm_id"])
    auth_header = 'Bearer {0}'.format(accessToken)
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    print("get_Customer_Data Succcess")
    return response

def getAccountData(accessToken):
    base_url = 'https://sandbox-quickbooks.api.intuit.com'
    query = "select * from Account"
    params = {
        'query': query,
        'minorversion': 70
    }
    url = f'{base_url}/v3/company/{cfg.qBData["realm_id"]}/query?{urlencode(params)}'
    print(url)
    auth_header = f'Bearer {accessToken}'
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json',
        'Content-Type': 'text/plain'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("getAccountData Success")
        return response.json()
    else:
        print(f"Failed to retrieve account data. Status code: {response.status_code}")
        return None

def refresh_token():
    response = auth_client.refresh(refresh_token=cfg.refreshToken)
    return response

def getPaymentData(accessToken):
    base_url = f'https://sandbox.api.intuit.com/quickbooks/v4/payments/charges/'
    auth_header = 'Bearer {0}'.format(accessToken)
    data = {
        'Authorization': auth_header
    }
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json;charset=UTF-8',
        'Content-type': '*/*'
    }

    response = requests.get(base_url, headers=headers)

    print("getPaymentData Succcess")

    return response"""