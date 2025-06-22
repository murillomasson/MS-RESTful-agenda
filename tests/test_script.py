import requests
import time

BASE_URL = "http://api:8000"


def wait_for_api(retries=10, delay=3):
    for i in range(retries):
        try:
            response = requests.get(f"{BASE_URL}/")
            if response.status_code == 200:
                print("API is ready!")
                return
        except requests.exceptions.ConnectionError:
            pass
        print(f"Waiting for API... ({i+1}/{retries})")
        time.sleep(delay)
    raise Exception("API did not start in time.")


def create_contact():
    payload = {
        "name": "Jane Doe",
        "category": "personal",
        "phones": [
            {"number": "555-1234", "type": "mobile"},
            {"number": "555-5678", "type": "landline"}
        ]
    }

    response = requests.post(f"{BASE_URL}/contacts/", json=payload)
    print("Create Contact Response:", response.status_code)
    print(response.json())
    return response.json()["id"]


def get_contact(contact_id):
    response = requests.get(f"{BASE_URL}/contacts/{contact_id}")
    print(f"Get Contact {contact_id} Response:", response.status_code)
    print(response.json())


def list_contacts():
    response = requests.get(f"{BASE_URL}/contacts/")
    print("List Contacts Response:", response.status_code)
    print(response.json())


def graphql_list_contacts():
    query = """
    query {
        listContacts {
            id
            name
            category
            phones {
                number
                type
            }
        }
    }
    """
    response = requests.post(f"{BASE_URL}/graphql", json={"query": query})
    print("GraphQL - List Contacts Response:", response.status_code)
    print(response.json())


def graphql_create_contact():
    mutation = """
    mutation {
        createContact(
            name: "GraphQL User",
            category: personal,
            phones: ["mobile:77777", "landline:88888"]
        ) {
            id
            name
            category
            phones {
                number
                type
            }
        }
    }
    """
    response = requests.post(f"{BASE_URL}/graphql", json={"query": mutation})
    print("GraphQL - Create Contact Response:", response.status_code)
    print(response.json())


if __name__ == "__main__":
    wait_for_api()
    contact_id = create_contact()
    get_contact(contact_id)
    list_contacts()
    
    graphql_create_contact()
    graphql_list_contacts()
