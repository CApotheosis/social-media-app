## When you create a new Django project using the startproject command, the authentication framework is included in the default settings of your project. It consists of the django.contrib.auth application and the following two middleware classes found in the MIDDLEWARE setting of your project:
- AuthenticationMiddleware: Associates users with requests using sessions
- SessionMiddleware: Handles the current session across requests

## The authentication framework also includes the following models:
- User: A user model with basic fields; the main fields of this model are username, password, email, first_name, last_name, and is_active
- Group: A group model to categorize users
- Permission: Flags for users or groups to perform certain actions