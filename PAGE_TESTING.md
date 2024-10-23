## Below is a list of descriptions for the pages that will be implemented for our project, TechShadow.

### For each page, it will include:
1. Page Title
2. Page Description (include a mockup or hand drawn image of the page)
3. Parameters needed for the page
4. Data needed to render the page
5. Link destinations for the page
6. List of tests for verifying the rendering of the page



# Page One: Landing Page
**Title:** Landing Page

**Description:** The main entry point for visitors, providing an overview of the platform and its purpose — connecting tech professionals with individuals seeking job shadowing opportunities.

**Parameters Needed:**
- If user is logged in, User ID (to display user name at top)
- If user is not logged in, None

**Data Needed:**
- No data is needed to/from backend

**Link Destinations:**
- Navbar links
    - Home: landing page
    - Login: login page
    - Shadow: Opportunities Page
    - Signup: Signup Page
    - contact: Contact Page
- In page links:
    - "I want to shadow someone" button: Opportunities Page
    - "I want to offer a shadow" button: Create Opportunity Page
**List of Tests:**

---

# Page Two: Account Page
**Title:** Account Page

**Description:** A personalized page where users can manage their profile, view saved/created opportunities, and track shadowing requests.

**Parameters Needed:**
- User ID (identifies which user's account page is being accessed)
- Section (to navigate to user profile settings, created or saved opportunities, and shadow requests)
- Action (edit sections as needed)

**Data Needed:**

**Link Destinations:**
- Navbar links
    - Home: landing page
    - Login: login page
    - Shadow: Opportunities Page
    - Signup: Signup Page
    - contact: Contact Page
- In page links:
    - "Update account" button: directs to signup page (reused for put requests for account update)

**List of Tests:**

---

# Page Three: Opportunities Page
**Title:** Opportunities Page

**Description:** A listing of all available job shadowing opportunities, filtered by role, location, and other preferences.

**Parameters Needed:**
- Search query (Used to filter oppportunities based on keywords)
- Filters (parameters to search by role, location, date, times available, experience level)

**Data Needed:**

**Link Destinations:**
- Navbar links
    - Home: landing page
    - Login: login page
    - Shadow: Opportunities Page
    - Signup: Signup Page
    - contact: Contact Page
- In page links: N/A
**List of Tests:**

---

# Page Four: Create an Opportunity Page
**Title:** Create an Opportunity Page

**Description:** A form where professionals can post new shadowing opportunities, including details like job role, location, times available, etc.
**Parameters Needed:**
- User ID (Identifies which use is creating the opportunity)
- Form (Form to fill out information for available opportunity)

**Data Needed:**

**Link Destinations:**
- Navbar links
    - Home: landing page
    - Login: login page
    - Shadow: Opportunities Page
    - Signup: Signup Page
    - contact: Contact Page
- In page links:
    - "Submit opportunity" button: links to Opportunities page
    
**List of Tests:**

---

# Page Five: Contact Page
**Title:** Contact Page

**Description:** A simple page for users to reach out to the platform's support team with inquiries or feedback about the job shadowing experience.

**Parameters Needed:**
- Form (for user to fill out to contact company)

**Data Needed:**

**Link Destinations:**
- Navbar links
    - Home: landing page
    - Login: login page
    - Shadow: Opportunities Page
    - Signup: Signup Page
    - contact: Contact Page
- In page links: N/A

**List of Tests:**

___


# Page Six: Login Page
**Title:** Login Page

**Description:** Simple page containing a login form that allows users to log into their accounts. Automatically redirects to Account page once the user successfully logs in.

**Parameters Needed:**
- Form (for user to fill out to login)

**Data Needed:**

**Link Destinations:**
- Navbar links
    - Home: landing page
    - Login: login page
    - Shadow: Opportunities Page
    - Signup: Signup Page
    - contact: Contact Page
- In page links:
    - "Submit form button": directs to account page is successful
**List of Tests:**

___


# Page Seven: Signup Page
**Title:** Login Page

**Description:** Simple page containing a sign up form that allows users to create an accounts. Automatically redirects to Account page once the user successfully logs in.

**Parameters Needed:**
- Form (for user to fill out to create account)

**Data Needed:**

**Link Destinations:**
- Navbar links
    - Home: landing page
    - Login: login page
    - Shadow: Opportunities Page
    - Signup: Signup Page
    - contact: Contact Page
- In page links:
    - "Submit form button": directs to account page is successful

**List of Tests:**
