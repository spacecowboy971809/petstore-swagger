import pytest
from pet_requests import *
from src.test_data import *
import allure


@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("payload", [PetPayloads.RACCOON.value])
@pytest.mark.parametrize("file", [BadFileNames.TEXT_FILE.value])
@pytest.mark.parametrize("additional_metadata", [AdditionalMetadatas.JPG_METADATA.value])
@allure.epic("Pets_tests")
def test_update_image_bad_file_type(file, api_key, payload, additional_metadata):
    """
    Test update image, bad file type
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
        delete_pet(pet_id=payload ["id"], api_key=api_key)

    # Add a new pet
    add_pet_response = add_pet(pet_id=payload ["id"],
                               category=payload ["category"],
                               name=payload ["name"],
                               photo_urls=payload ["photoUrls"],
                               tags=payload ["tags"],
                               status=payload ["status"])
    assert add_pet_response.status_code == 200, "Wrong response code for add pet"

    # Upload an image for the pet with an invalid file type
    image_update_response = upload_image_pet(pet_id=payload ["id"],
                                             file_path=file ["file_path"],
                                             additional_metadata=additional_metadata)

    # Check that the response status code indicates an error (modify this based on the actual API behavior)
    assert image_update_response.status_code != 200, "Wrong response code for image update"

    # Check the error message in the response (modify this based on the actual API response structure)
    error_message = image_update_response.json( ).get("message")
    assert "Invalid file type" in error_message, "Invalid file type error message not found in response"
