from enum import Enum

class APIKeys(Enum):
    VALID_API_KEY = "75309586-a480-43a8-a656-8228fab29bac"

class BadAPIKeys(Enum):
    INVALID_API_KEY = "25309586-a480-43a8-a656-8228fab29baa"
    NULL_API_KEY = None

class PetPayloads(Enum):
    DOG = {
        "id": 5244223213,
        "category": {"id": 1, "name": "dogs"},
        "name": "test Doggie",
        "photoUrls": ["https://creapills.com/wp-content/uploads/2022/03/40-photos-animaux-hybrides-reddit-35-1.jpg"],
        "tags": [{"id": 0, "name": "dogs_available"}],
        "status": "available"
    }
    CAT = {
        "id": 5244223214,
        "category": {"id": 2, "name": "cats"},
        "name": "test_cat",
        "photoUrls": [
            "https://creapills.com/wp-content/uploads/2022/03/40-photos-animaux-hybrides-reddit-35-1.jpg",
            "https://t1.gstatic.com/licensed-image?q=tbn:ANd9GcRRv9ICxXjK-LVFv-lKRId6gB45BFoNCLsZ4dk7bZpYGblPLPG-9aYss0Z0wt2PmWDb"
        ],
        "tags": [{"id": 0, "name": "cats_pending"}],
        "status": "pending"
    }
    RACCOON = {
        "id": 5244223215,
        "category": {"id": 3, "name": "racoons"},
        "name": "racoon 123 %",
        "photoUrls": [],
        "tags": [{"id": 0, "name": "racoons_sold"}],
        "status": "sold"
    }
    NULL_PAYLOAD = {
        "id": None,
        "category": None,
        "name": "test_racoon_2",
        "photoUrls": None,
        "tags": None,
        "status": None
    }
    INVALID_CATEGORY_ID = {
        "id": 5244223216,
        "category": {"id": "test_string", "name": "test_string"},
        "name": "test_pet_name",
        "photoUrls": [
            "https://creapills.com/wp-content/uploads/2022/03/40-photos-animaux-hybrides-reddit-35-1.jpg"],
        "tags": [{"id": 0, "name": "test1"}],
        "status": "test"
    }
    EMPTY_CATEGORY_NAME = {
        "id": 5244223216,
        "category": {"id": 4, "name": ""},
        "name": "doggie",
        "photoUrls": [
            "https://creapills.com/wp-content/uploads/2022/03/40-photos-animaux-hybrides-reddit-35-1.jpg"],
        "tags": [{"id": "test_string", "name": "test1"}],
        "status": "available"
    }
    INVALID_NAME = {
        "id": 5244223216,
        "category": {"id": "test_string", "name": "Test_string"},
        "name": None,
        "photoUrls": None,
        "tags": [{"id": 0, "name": "test1"}],
        "status": "available"
    }
    INVALID_ID = {
        "id": "test_string",
        "category": {"id": 4, "name": ""},
        "name": "doggie",
        "photoUrls": [
            "https://creapills.com/wp-content/uploads/2022/03/40-photos-animaux-hybrides-reddit-35-1.jpg"],
        "tags": [{"id": 0, "name": "test1"}],
        "status": "available"
    }

class FileNames(Enum):
    JPG_FILE = {"file_name" : "photo_2023-08-10_14-04-34.jpg",
                "file_path" : "src/photo_2023-08-10_14-04-34.jpg"}
    PNG_FILE = {"file_name" : "photo_2023-08-10_14-04-34.png",
                "file_path" : "src/photo_2023-08-10_14-04-34.png"}

class BadFileNames(Enum):
    TEXT_FILE = {"file_name" : "test.txt",
                 "file_path" : "src/test.txt"}


class AdditionalMetadatas(Enum):
    JPG_METADATA = "AdditionalMetadata"

class UserPayloads(Enum):
    USER = {
        "id": 684535235,
        "username": "1test12424",
        "first_name": "test_first_name",
        "last_name": "test_last_name",
        "email": "1testmail@mail.com",
        "password": "1pass123",
        "phone": "135928757953",
        "user_status": 0
    }
    USER_2 = {
        "id": 684535236,
        "username": "6test12424",
        "first_name": "test_first_name_6",
        "last_name": "test_last_name_6",
        "email": "1testmail_6@mail.com",
        "password": "1pass123_6",
        "phone": "135928757956",
        "user_status": 1
    }
    USER_BAD_ID = {
        "id": "test",
        "username": "1test124256789",
        "first_name": "test_first_name",
        "last_name": "test_last_name",
        "email": "1testmail@mail.com",
        "password": "1pas2123",
        "phone": "135928757953",
        "user_status": 0
    }
    USER_BAD_STATUS = {
        "id": 1225325,
        "username": "1test12424",
        "first_name": "test_first_name",
        "last_name": "test_last_name",
        "email": "1testmail@mail.com",
        "password": "1pass123",
        "phone": "135928757953",
        "user_status": "test"
    }


class OrderPayloads(Enum):
    ORDER_PLACED = {
            "id": 1,
            "petId": 5244223213,
            "quantity": 2,
            "shipDate": "2023-09-22T22:20:35.100",
            "status": "placed",
            "complete": True
        }
    ORDER_APPROVED = {
            "id": 2,
            "petId": 5244223213,
            "quantity": 3,
            "shipDate": "2023-09-22T22:20:35.100",
            "status": "approved",
            "complete": False
        }
    ORDER_DELIVERED = {
            "id": 3,
            "petId": 5244223213,
            "quantity": 1,
            "shipDate": "2023-09-22T22:20:35.100",
            "status": "delivered",
            "complete": True
        }
    ORDER_BAD_ID = {
            "id": "test",
            "petId": 5244223213,
            "quantity": 1,
            "shipDate": "2023-09-22T22:20:35.100",
            "status": "delivered",
            "complete": True
        }
    ORDER_BAD_PET_ID = {
            "id": 9,
            "petId": "test",
            "quantity": 1,
            "shipDate": "2023-09-22T22:20:35.100",
            "status": "delivered",
            "complete": True
        }
    ORDER_BAD_COMPLETE = {
            "id": 8,
            "petId": 5244223213,
            "quantity": 1,
            "shipDate": "2023-09-22T22:20:35.100",
            "status": "delivered",
            "complete": "test"
        }

    ORDER_BAD_STATUS = {
            "id": 4,
            "petId": 5244223213,
            "quantity": 1,
            "shipDate": "2023-09-22T22:20:35.100",
            "status": "test",
            "complete": True
        }
    ORDER_BAD_SHIPDATE = {
            "id": 5,
            "petId": 5244223213,
            "quantity": 1,
            "shipDate": "test",
            "status": "delivered",
            "complete": True
        }
