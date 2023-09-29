from my_requests import MyRequests


# User
def create_user_with_array(id, username, first_name, last_name, email, password, phone, user_status, id_2, username_2,
                           first_name_2, last_name_2, email_2, password_2, phone_2, user_status_2):
    """
    Creates list of users with given input array
    """
    payload = [
        {
            "id": id,
            "username": username,
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "password": password,
            "phone": phone,
            "userStatus": user_status
        },
        {
            "id": id_2,
            "username": username_2,
            "firstName": first_name_2,
            "lastName": last_name_2,
            "email": email_2,
            "password": password_2,
            "phone": phone_2,
            "userStatus": user_status_2
        }
    ]
    url = "user/createWithArray"
    return MyRequests.post(url, json=payload)


def create_user_with_list(id, username, first_name, last_name, email, password, phone, user_status, id_2, username_2,
                          first_name_2, last_name_2, email_2, password_2, phone_2, user_status_2):
    """
    Creates list of users with given input list
    """
    payload = [
        {
            "id": id,
            "username": username,
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "password": password,
            "phone": phone,
            "userStatus": user_status
        },
        {
            "id": id_2,
            "username": username_2,
            "firstName": first_name_2,
            "lastName": last_name_2,
            "email": email_2,
            "password": password_2,
            "phone": phone_2,
            "userStatus": user_status_2
        }
    ]
    url = "user/createWithList"
    return MyRequests.post(url, json=payload)


def get_user_by_username(username):
    """
    Get user by username
    """
    url = f"user/{username}"
    return MyRequests.get(url)


def update_user_by_username(id, username, first_name, last_name, email, password, phone, user_status):
    """
    Update user. This can only be done by the logged-in user
    """
    url = f"user/{username}"
    payload = {
        "id": id,
        "username": username,
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": user_status
    }
    return MyRequests.put(url, json=payload)


def delete_user_by_username(username):
    """
    Delete user. This can only be done by the logged-in user
    Parameters:
    username *: string
    (path)
    """
    url = f"user/{username}"
    payload = {"id": 12442343244, "username": "poke_user2", "firstName": "pikachu2", "lastName": "pokemon2",
               "email": "pokemon2@test.com", "password": "Wafsoheruh43@", "phone": "+1247862984723", "userStatus": 0}
    return MyRequests.delete(url, json=payload)


def login_user(username, password):
    """
    Logs user into the system
    """
    url = "user/login"
    payload = {"username": username, "password": password}
    return MyRequests.get(url, json=payload)


def logout_user():
    """
    Logs out current logged-in user session
    """
    url = "user/logout"
    return MyRequests.get(url)


def create_user(id, username, first_name, last_name, email, password, phone, user_status):
    """
    Function create user. This can only be done by the logged-in user
    """
    payload = {
        "id": id,
        "username": username,
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": user_status
    }
    url = "user"
    return MyRequests.post(url, json=payload)
