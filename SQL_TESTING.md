<!-- Lists descriptions for tables and functions being created for the project -->

<!-- Add the following for each table -->
<!-- Table Name
Table Description
For Each field provide a name and short description
List of tests for each table -->

<!-- For each data access method (POST, PUT, GET, DELETE) required to get data to display provide the following -->
<!-- Name
Description
Parameters
Return Values
List of tests for verifying each access method -->

# Table One: Users
**Table Name:** Users

**Table Description:** 
Stores metadata about all registered users.

**Table Fields:**
- Field 1:
    - Name: `userID`
    - Description: String; primary key for table. Digest (SHA or md5) of `username`; internal alias for `username`?
- Field 1:
    - Name: `username`
    - Description: String; user's preferred `username`. Should be unique; external alias for `userID`. Alphanumeric characters only; should be at least 8 characters long.
- Field 1:
    - Name: `password_digest`
    - Description: String; one-way hash of whatever password the user initially submmitted. The actual password is not stored for security reasons.
- Field 2:
    - Name: `first_name`
    - Description: String; user's given name. Accepts alphanumeric characters, whitespace, and some alphanumeric characters (', .)
- Field 3:
    - Name: `last_name`
    - Description: String; user's family name. Accepts alphanumeric characters, whitespace, and some alphanumeric characters (', .)
- Field 6:
    - Name: `is_mentor`
    - Description: Bool; whether the user is a mentor
- Field 7:
    - Name: `is_shadower`
    - Description: Bool; whether the user wants to shadow someone
- Field 7:
    - Name: `field`
    - Description: String; self-description by the user as to what they do. Probably too variable to be searched on, but good as a profile for an end-user. Not more than 200 characters long, accepts all characters.
<br>

**List of Tests to verify table:**
- Test 1: Check that `username` does not allow whitespaces, special characters, or nonlatin characters to be added.
- Test 2: Check that `username` allows all alphanumeric characters.
- Test 3: Check that `username` does not allow whitespaces, special characters, or nonlatin characters to be added.
- Test 4: Check that `username` is at least 8 characters long.
- Test 5: Check that `username` accesses the correct information for a given user
- Test 5: Check that `username` accesses the correct information for a given user
- Test 6: Check that querying with `userID` and `username` access the same information in `get_public_user_info`.
- Test 7: Check that `password_digest` and `userID` are not returned after querying the table with `get_public_user_info`
- Test 8: Check that querying with `username` fails when querying information in `get_all_user_info`.
- Test 9: Check that querying with `userID` succeeds and returns all fields when querying information in `get_all_user_info`.


**Data Access Methods**
- Method 1:
    - Name: `get_public_user_info`
    - Description: Takes a user identifier (`username` or `user_ID`), and returns all information except for `password_digest` and `userID`. Intended for public-facing applications.
    - Parameters: `username` or `user_ID`
    - Return Values: Tab-separated string containing `username`, `first_name`, `last_name`, `is_mentor`, `is_shadower` and `field`. All strings should be quoted to prevent strange behavior.

- Method 2:
    - Name: `get_all_user_info`
    - Description: Takes a user identifier (`user_ID`), and returns all information <u>including</u> `password_digest` and `userID`. Intended for inward-facing applications. Should not be used unless you actually need access to `password_digest` or `userID`.
    - Parameters: `user_ID`
    - Return Values: Tab-separated string containing `username`, `first_name`, `last_name`, `is_mentor`, `is_shadower` and `field`. All strings should be quoted to prevent strange behavior.

# Table Two: Opportunities
**Table Name:**

**Table Description:**

**Table Fields:**
- Field 1:
    - Name:
    - Description:
- Field 2:
    - Name:
    - Description:
- Field 3:
    - Name:
    - Description:

**List of Tests to verify table:**
- Test 1:
- Test 2:

**Data Access Methods**
- Method 1:
    - Name: 
    - Description:
    - Parameters:
    - Return Values:
    - List of tests for verifying each access method:
- Method 2:
    - Name:
    - Description:
    - Parameters:
    - Return Values:
    - List of tests for verifying each access method:

# Table Three: Contact Messages
**Table Name:**

**Table Description:**

**Table Fields:**
- Field 1:
    - Name:
    - Description:
- Field 2:
    - Name:
    - Description:
- Field 3:
    - Name:
    - Description:

**List of Tests to verify table:**
- Test 1:
- Test 2:

**Data Access Methods**
- Method 1:
    - Name:
    - Description:
    - Parameters:
    - Return Values:
    - List of tests for verifying each access method:
- Method 2:
    - Name:
    - Description:
    - Parameters:
    - Return Values:
    - List of tests for verifying each access method:
