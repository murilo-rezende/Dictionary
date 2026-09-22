Dictionary

Video Demo: https://www.youtube.com/watch?v=zc33dsl9b04

Description:

Dictionary is a web-based application designed to allow users to create and manage their own personalized language dictionary. The main goal of the application is to provide a simple, intuitive, and organized platform where users can store words from any language along with their respective meanings and lexical categories. This tool can be especially useful for language learners, writers, linguists, or anyone interested in building a customized vocabulary database for personal or academic use.

When the user first accesses the application, they are presented with a login page. This page serves as the main authentication gateway to ensure that each user’s data remains private and secure. The login form requires a registered username and password. If the user has already created an account, they can simply enter their credentials and proceed to access their personal dictionary. The authentication process verifies the information against the stored data in the database and, if the credentials are valid, creates a secure session for the user.

For new users who do not yet have an account, there is a registration page available. The registration page allows users to create an account by choosing a unique username and a secure password. The system may include validation mechanisms to ensure that usernames are not duplicated and that passwords meet minimum security requirements, such as length or character complexity. Once the user submits the registration form, their information is securely stored in the database. After successful registration, a session is created, and the user is automatically redirected to the homepage.

The homepage serves as an introduction to the dictionary application. It provides a brief overview of the platform’s purpose and functionality, helping users understand how to navigate and use the features effectively. The layout is designed to be clean and user-friendly. At the upper right-hand side of the page, there is a navigation bar (navbar) that allows users to access the main sections of the application. This navbar remains consistent across pages, ensuring easy navigation at all times.

One of the primary features accessible through the navbar is the “Add Word” section. In this section, users can add new entries to their dictionary. The form typically includes input fields for the word itself, its meaning or definition, and its lexical category. The lexical category allows users to classify the word according to grammatical types such as noun, verb, adjective, adverb, or other relevant categories. This classification helps maintain organization and makes it easier to filter and search for words later.

When the user submits the form to add a new word, a POST request is sent to the server. This request contains the word, its meaning, and its lexical category. The backend processes the request and stores the data in the database. Each word entry is associated with the specific user account that created it, ensuring that users can only access and manage their own dictionary entries. After the word is successfully added, the system may display a confirmation message or redirect the user to another page.

Another important section available through the navbar is the “Word List” page. This page displays all the words that the user has previously added to their dictionary. The words are presented in a structured table format, with columns showing the word, its meaning, and its lexical category. This tabular layout provides a clear and organized overview of the stored entries.

In addition to simply displaying the words, the Word List page includes a search bar. The search functionality allows users to filter the displayed words by entering a specific term. As the user types into the search bar, the system can dynamically filter the table to show only the entries that match the search query. This feature improves usability, especially when the user’s dictionary contains a large number of entries.

If the user decides that a particular word is no longer needed, the application provides a “Remove Word” page. This page contains a dropdown list populated with the existing words in the user’s dictionary. The user can select a word from the dropdown menu and confirm the deletion. Once confirmed, the system sends a request to the backend to remove the selected word from the database. After deletion, the word will no longer appear in the Word List table.

Overall, the Dictionary web application combines user authentication, data management, and interactive features to provide a secure and efficient platform for managing personalized vocabulary collections. By integrating account-based sessions, database storage, organized tables, search functionality, and deletion options, the application ensures that users can easily add, view, filter, and remove words according to their needs.
