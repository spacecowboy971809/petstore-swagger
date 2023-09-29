import pytest
from pet_requests import *
from src.test_data import *
import allure


# Test case for uploading an image when the pet does not exist
@pytest.mark.parametrize("api_key", [APIKeys.VALID_API_KEY.value])
@pytest.mark.parametrize("payload", [PetPayloads.CAT.value])
@pytest.mark.parametrize("file", [FileNames.JPG_FILE.value])
@pytest.mark.parametrize("additional_metadata", [AdditionalMetadatas.JPG_METADATA.value])
@allure.epic("Pets_tests")
@allure.description("Test upload image, pet_id does not exist")
def test_update_image_pet_not_exist(file, api_key, payload, additional_metadata):
    """
    Test update image, pet_id does not exist
    Parameters:
    petId *: integer($int64)
    (path)
    additionalMetadata: string
    (formData)
    file: file
    (formData)
    """
    # Check if a pet with the given ID exists and delete it if found
    find_by_pet_id_response = find_by_pet_id(pet_id=payload ["id"])
    if find_by_pet_id_response.status_code == 200:
        delete_pet_response = delete_pet(pet_id=payload ["id"], api_key=api_key)
        assert delete_pet_response.status_code == 200, "Wrong response code for delete pet"

    # Attempt to upload an image for the specified pet ID
    image_update_response = upload_image_pet(pet_id=payload ["id"],
                                             file_path=file ["file_path"],
                                             additional_metadata=additional_metadata)

    # Assert that the response status code indicates an error since the pet does not exist
    assert image_update_response.status_code != 200, "Wrong response code for add pet"
