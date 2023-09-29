import pytest
from json.decoder import JSONDecodeError
from pet_requests import *
from src.test_data import *
import allure


@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("payload", [PetPayloads.CAT.value])
@pytest.mark.parametrize("file", [FileNames.JPG_FILE.value, FileNames.PNG_FILE.value])
@pytest.mark.parametrize("additional_metadata", [AdditionalMetadatas.JPG_METADATA.value])
@allure.epic("Pets_tests")
def test_update_image(file, api_key, payload, additional_metadata):
    """
    Test update image
    Parameters:
    petId *: integer($int64)
    (path)
    additionalMetadata: string
    (formData)
    file: file
    (formData)
    """
    # Check if a pet with the given ID exists and delete it
    find_by_pet_id_response = find_by_pet_id(pet_id=payload ["id"])
    if find_by_pet_id_response.status_code == 200:
        delete_pet_response = delete_pet(pet_id=payload ["id"], api_key=api_key)
        assert delete_pet_response.status_code == 200, "Wrong response code for delete pet"

    # Add a new pet
    add_pet_response = add_pet(pet_id=payload ["id"],
                               category=payload ["category"],
                               name=payload ["name"],
                               photo_urls=payload ["photoUrls"],
                               tags=payload ["tags"],
                               status=payload ["status"])
    assert add_pet_response.status_code == 200, "Wrong response code for add pet"

    # Upload an image for the pet
    image_update_response = upload_image_pet(pet_id=payload ["id"],
                                             file_path=file ["file_path"],
                                             additional_metadata=additional_metadata)

    # Check the response status code (modify this based on the actual API behavior)
    assert image_update_response.status_code == 200, "Wrong response code for image update"

    # Parse the response JSON to extract values
    try:
        parsed_response_text = image_update_response.json( )
    except JSONDecodeError:
        print("Response does not contain valid JSON")

    # Check if the additional metadata is present in the response message
    assert additional_metadata in parsed_response_text.get("message"), "Additional metadata not found in response"

    # Check if the file name is present in the response message
    assert file ["file_name"] in parsed_response_text.get("message"), "File name not found in response"

    # Retrieve the pet to verify the photoUrls
    find_if_response = find_by_pet_id(payload ["id"])

    # Parse the response JSON to extract values
    try:
        parsed_response_find_if = find_if_response.json( )
    except JSONDecodeError:
        print("Response does not contain valid JSON")

    # Verify that photoUrls are not empty (modify this assertion if necessary)
    assert parsed_response_find_if.get("photoUrls"), "photoUrls is empty"

    # Delete the pet
    delete_pet_response = delete_pet(parsed_response_find_if.get("id"), api_key)
    assert delete_pet_response.status_code == 200, "Wrong response code for delete pet"
