from my_requests import MyRequests
import os


# Pet
def find_by_pet_id(pet_id):
    """
    Find pet by ID
    Parameters:
    petId *: integer($int64)
    (path)
    """
    url = f"pet/{pet_id}"
    return MyRequests.get(url)


def upload_image_pet(pet_id, file_path, additional_metadata):
    """
    Uploads an image
    Parameters:
    petId *: integer($int64)
    (path)
    additionalMetadata: string
    (formData)
    file: file
    (formData)
    """
    url = f"pet/{pet_id}/uploadImage"
    script_directory = os.path.dirname(os.path.abspath(__file__))
    files = {'file': open(os.path.join(script_directory, file_path), 'rb'), "additionalMetadata": additional_metadata}
    return MyRequests.post(url, files=files)


def add_pet(pet_id, category, name, photo_urls, tags, status):
    """
    Add a new pet to the store
    body *:object:
    (body)
        Pet{
        id: integer($int64)
        Category:
        {id: integer($int64)
        name: string}
        name*: string
        photoUrls*: string
        tags:
        {id: integer($int64)
        name: string}
        status:	string
        pet status in the store
        Enum: [ available, pending, sold ]
        }
    """
    url = "pet"
    payload = {
        "id": pet_id,
        "category": category,
        "name": name,
        "photoUrls": photo_urls,
        "tags": tags,
        "status": status
    }
    return MyRequests.post(url, json=payload)


def update_pet(pet_id, category, name, photo_urls, tags, status):
    """
    Update an existing pet
    body *: object:
    (body)
        Pet:
        { id: integer($int64)
        Category:
        {id: integer($int64)
        name: string}
        name*: string
        photoUrls*: string
        tags:
        {id: integer($int64)
        name: string}
        status:	string
        pet status in the store
        Enum: [ available, pending, sold ]
    """
    url = f"pet"
    payload = {
        "id": pet_id,
        "category": category,
        "name": name,
        "photoUrls": photo_urls,
        "tags": tags,
        "status": status
    }
    return MyRequests.put(url, json=payload)


def find_by_status(status):
    """
    Finds Pets by status
    Parameters:
    status *: array[string]
    (query)
    Status values that need to be considered for filter
    Available values : available, pending, sold
    """
    payload = {"status": status}
    url = "pet/findByStatus"
    return MyRequests.get(url, json=payload)


def update_pet_with_form(pet_id, name, status):
    """
    Updates a pet in the store with form data
    Parameters:
    petId *: integer($int64)
    (path)
    name: string
    (formData)
    status: string
    (formData)
    """
    payload = {"name": name, "status": status}
    url = f"pet/{pet_id}"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return MyRequests.post(url, json=payload, headers=headers)


def delete_pet(pet_id, api_key):
    """
    Deletes a pet
    Parameters:
    api_key:string
    (header)
    petId *: integer($int64)
    (path)
    """
    headers = {"api_key": api_key}
    url = f"pet/{pet_id}"
    return MyRequests.delete(url, headers=headers)


def delete_pet_without_api_key(pet_id):
    """
    Deletes a pet without api key
    """
    payload = {"petId": pet_id}
    url = f"pet/{pet_id}"
    return MyRequests.delete(url, json=payload)

