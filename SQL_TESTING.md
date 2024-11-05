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
**Table Name:** Opportunities

**Table Description:**
Stores data about open shadowing opportunities

**Table Fields:**
- Field 1: 
    - Name: `opportunityID`
    - Description: Integer; unique identifier for each opportunity (primary key)
- Field 2:
    - Name: `position`
    - Description: String; job title or position name for the shadowing opportunity (e.g., "Software Developer")
- Field 3:
    - Name: `job_description`
    - Description: String; a brief description of the position, outlining responsibilities and expectations
- Field 4:
    - Name: `is_remote`
    - Description: Boolean; indicates if the opportunity is remote
- Field 5:
    - Name: `is_in_person`
    - Description: Boolean; indicates if the opportunity is in-person
- Field 6:
    - Name: `status`
    - Description: String; represents the status of the opportunity (open, pending, or closed). Only open opportunities should be visible on the webpage.
- Field 7:
    - Name: `required_skills`
    - Description: String; list of relevant skills or keywords for the opportunity (e.g., "Python, SQL, Machine Learning") to facilitate search matching.
- Field 8:
    - Name: `location`
    - Description: String; location of the opportunity for in-person roles (e.g., "New York, NY"), which could also serve as a filter.


**List of Tests to verify table:**
- Test 1: Ensure `opportunityID` is unique and non-null
- Test 2: Verify that `only` open opportunities are displayed in listings by default
- Test 3: Check that both `is_remote` and `is_in_person` cannot be true at the same time.
- Test 4: Validate that `position` and `job_description` fields accept text entries without exceeding character limits
- Test 5: Ensure `required_skills` field supports comma-separated values and performs keyword-based search correctly.
- Test 6: Verify filtering options allow querying by `is_remote`, `is_in_person`, `status`, and `location`.

**Data Access Methods**
- Method 1:
    - Name: `get_available_opportunities`
    - Description: Retrieves all `open` opportunities, optionally filtered by `is_remote`, `is_in_person`, and `location`
    - Parameters: Optional filters (`is_remote`, `is_in_person`, `location`)
    - Return Values: List of available opportunities including `opportunityID`, `position`, `job_description`, and `status`
    - List of tests for verifying each access method:
        - Test 1: Verify correct filtering based on `is_remote`, `is_in_person`, and `location`.
        - Test 2: Ensure only `open` opportunities are returned.
- Method 2:
    - Name: `search_opportunities_by_skill`
    - Description: Retrieves opportunities based on a search query for specific skills.
    - Parameters: `skill_query` (string of keywords).
    - Return Values: List of matching opportunities with relevant fields
    - List of tests for verifying each access method:
        - Test 1: Check that search results correctly match entries in `required_skills`
        - Test 2: Verify performance with multiple search keywords
- Method 3:
    - Name: `get_opportunity_details`
    - Description: Retrieves detailed information for a specific opportunity
    - Parameters: `opportunityID`
    - Return Values: All fields for the specified opportunity
    - List of tests for verifying each access method:
        - Test 1: Validate that the correct opportunity details are returned based on `opportunityID`
        - Test 2: Confirm `opportunityID` entries are correctly cross-referenced with user access permissions if needed

# Table Three: Contact Messages
**Table Name:** 
Messages

**Table Description:**
Stores messages between app users

**Table Fields:**
- Field 1: 
    - Name:`UserID`
    - Description: string; ID of current user who is logged in
- Field 2: 
    - Name:`messageID`
    - Description: ID of the current mesage
- Field 3: 
    - Name:`message_content`
    - Description: The content of the message
- Field 4: 
    - Name: `created_at`
    - Description: Timestamp the first message was sent
- Field 5: `UserID2`
    - Description: User ID of user you are corresponding with, which should be used to look up name from users table and display in messages
- Field 6: 
    - Name: `responded_at`
    - Description: Time the last message was sent
- Field 7: 
    - Name: `status`
    - Description: Current status of message (read, unread, draft)

**List of Tests to verify table:**
- Test 1: Check that `userID` exists in table `users`
- Test 2: Check that `userID2` exists in the table `users`
Test 3: Verify that `userID` allows for mulitple messages from the same user 
Test 4: Ensure `userID` is required and does not allow a Null value
Test 4: Ensure `messageID` is unique for each message
Test 5: Check that `messageID` auto increments 
Test 6: Ensure `message_content` is of type string 
Test 7: Ensure `create_at` defaults to current date and time of first message
Test 8: Ensure `responded_at` defaults to current date and time of the message reeponse
Test 9: Ensure `responded_at` is created after `create_at`
Test 10: Ensure `status` returns only values of 'read', 'unreaed', or 'draft'
Test 11: Check that default value for `status` is 'unread'

**Data Access Methods**
- Method 1:
    - Name: `get_all_user_info` 
    - Description: Take in `userID` and returns needed values for messages such as first name, last name, and is_mentor or is_shadow. This will be used to grab both user 1 and user 2 info
    - Parameters: `userID`
    - Return Values: `username`, `first_name`, `last_name`, `is_mentor`, `is_shadow`
    - List of tests for verifying each access method: valid_user_Id, invalid_user_ID, null_user_ID, user_role
- Method 2: 
    - Name: `get_all_message_info`
    - Description: Takes in a user ID and returns user's message information, separating each message into a separate table row
    - Parameters: `userID`
    - Return Values: Message values `messageID`, `message_content`, `userID2`, `create_at`, `responded_at`, `status`
    - List of tests for verifying each access method: valid_user_Id, invalid_user_ID, null_user_ID, no_message_content, status_validity, date_and_time_accuracy
