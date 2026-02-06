You should add a dedicated section to your README, often called a "Changelog" or "Recent Updates," that lists the key changes in a clear, bulleted format. This helps teammates quickly understand what's new and where to look for changes.
Here is a suggested format focusing on the recent Flask Blueprint changes:
Recent Updates
🚀 Feature: Modularized Application Structure
We have refactored the application to use Flask Blueprints. This makes the project more organized and easier to scale.
auth Blueprint Added: A new module for all authentication-related routes (login, logout, signup).
main Blueprint Defined: The primary public-facing pages now reside in the main blueprint.
Centralized Registration: All blueprints are registered in app.py with specific url_prefix paths:
/: For the main public pages (e.g., /index, /about).
/auth/: For all authentication pages (e.g., /auth/login, /auth/register).
🛠️ Fixes & Improvements
Fixed Relative Imports: Resolved issues with module imports by ensuring the application runs correctly using the flask run command.
Dynamic Page Loading: The blueprints now use a generic show(page) function to automatically render any HTML template found in the templates/pages directory, provided the file exists.
Do you want to add instructions on how your mates can set up their local environment to run these new changes?
