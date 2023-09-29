# Swagger Petstore API Testing Checklist

## Pet
### POST /pet/{petId}/uploadImage
Uploads an image of a pet

**Positive:**
- [ ] Pet_id exists, File is in popular image formats
- [ ] Pet_id does not exist, response code: != 200

**Negative:**
- [ ] File is not an image

### POST /pet
Add a new pet to the store

**Positive:**
- [ ] Valid request with correct parameters
- [ ] Request without name or photoUrls
- [ ] Request with an existing ID

**Negative:**
- [ ] Request with incorrect data types

### PUT /pet
Update an existing pet
**Positive:**
- [ ] Valid request with correct parameters
- [ ] Request without name or photoUrls

**Negative:**
- [ ] Request with incorrect data types

### GET /pet/findByStatus
Finds Pets by status

**Positive:**
- [ ] Valid request with correct parameters
- [ ] Request with a status not in the list

### GET /pet/{petId}
Find pet by ID

**Positive:**
- [ ] Valid request with correct parameters
- [ ] Request with a non-existing ID

**Negative:**
- [ ] Request with an incorrect ID type

### POST /pet/{petId}
Updates a pet in the store with form data

**Positive:**
- [ ] Valid request with correct parameters
- [ ] Request with a status not in enum

### DELETE /pet/{petId}
Deletes a pet

**Positive:**
- [ ] Valid request with correct parameters
- [ ] PetId not exist
- [ ] Invalid petId
**Negative:**
- [ ] Use an invalid api_key
- [ ] Use no api_key

## Store

### POST /store/order
Place an order for a pet

**Positive:**
- [ ] Valid request with correct parameters
- [ ] PetId not exist
- [ ] Order id already exits

**Negative:**
- [ ] Invalid request parameters

### GET /store/order/{orderId}
Find purchase order by ID

**Positive:**
- [ ] Valid request with an existing order ID
- [ ] Valid request with a non-existing order ID

**Negative:**
- [ ] Invalid order ID format

### DELETE /store/order/{orderId}
Delete purchase order by ID

**Positive:**
- [ ] Valid request with an existing order ID
- [ ] Valid request with a non-existing order ID

**Negative:**
- [ ] Invalid order ID format

### GET /store/inventory
Returns pet inventories by status

**Positive:**
- [ ] Valid request, counting status works


## Users

### POST /user/createWithArray
Creates list of users with given input array

**Positive:**
- [ ] Logged-in user, Valid request with correct parameters
- [ ] Logged-in user, duplicate user

**Negative:**
- [ ] Use incorrect data types
- [ ] Request without being logged-in

### POST /user/createWithList
Creates list of users with given input array
**Positive:**
- [ ] Logged-in user, Valid request with correct parameters
- [ ] Logged-in user, duplicate user

**Negative:**
- [ ] Use incorrect data types
- [ ] Request without being logged-in

### GET /user/{username}
Get user by username

**Positive:**
- [ ] Valid request with an existing username
- [ ] Valid request with a non-existing username


### PUT /user/{username}
Updated user

**Positive:**
- [ ] Valid request with an existing username and correct parameters

**Negative:**
- [ ] Request without being logged in

### DELETE /user/{username}
Delete user

**Positive:**
- [ ] Logged-in user, valid request with an existing username
- [ ] Logged-in user, user not existing

**Negative:**
- [ ] Request without being logged in

### GET /user/login
Logs user into the system

**Positive:**
- [ ] Correct username/password

**Negative:**
- [ ] Invalid username/password supplied

### GET /user/logout
Logs out current logged-in user session

**Positive:**
- [ ] User is logged-in
- [ ] User is not logged-in

### POST /user
Create user

**Positive:**
- [ ] Logged-in user, Valid request with correct parameters
- [ ] Logged-in user, duplicate user

**Negative:**
- [ ] Use incorrect data types
- [ ] Request without being logged-in

### [Main page](https://github.com/spacecowboy971809/petstore-swagger)
