import yaml
import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")

with open("config/secrets.yaml", "r") as f:
    secrets = yaml.safe_load(f)
    
DBX_DF_HOST_DF_API_KEY = secrets["DBX"]["DBX_DF_HOST_DF_API_KEY"]
DBX_DF_HOST = secrets["DBX"]["DBX_DF_HOST"]


# Function to create a group in Databricks
def create_group(group_name:str=None):
    
    headers = {
        "Authorization": f"Bearer {DBX_DF_HOST_DF_API_KEY}",
        "Content-Type": "application/json" }
    
    if group_name == None:
        with open("config/governance.yaml", "r") as file:
            config = yaml.safe_load(file)
        
        groups = config["groups"]
        
        for group in groups:
            payload = {
                "displayName": group
                }
            
            response = requests.post(
                f"{DBX_DF_HOST}/api/2.0/preview/scim/v2/Groups",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 201:
                logging.info(f"Group '{group}' created successfully.")
            elif response.status_code == 409:
                logging.warning(f"Group '{group}' already exists.")
            else:
                logging.error(f"Error creating group'{group}': Error code {response.status_code} - {response.text}")
            
    else:
        payload = {
                "displayName": group_name
                }
        
        response = requests.post(
            f"{DBX_DF_HOST}/api/2.0/preview/scim/v2/Groups",
            headers=headers,
            json=payload
        )
        
        if response.status_code == 201:
            logging.info(f"Group '{group_name}' created successfully.")
        elif response.status_code == 409:
            logging.warning(f"Group '{group_name}' already exists.")
        else:
            logging.error(f"Error creating group'{group_name}': Error code {response.status_code} - {response.text}")