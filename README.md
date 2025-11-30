# build-webpage-project

"Welcome. I create this as a demonstration on how Python can be use with Docker
to generate a webpage."

The Python script was written to save effort creating containers to host a web app
and save time generating basic web content.

I hope this project is useful to start making web content at scale!

# Requirement
Must have Docker Installed

# Python Steps
Step 1. Prompt user to create a webpage

Step 2. Based on the the input
    If option 1, then create a new webpage.
    If option 2, then continue working for one minute session.
    If optin 3, then remove all resources and start clean.

Only if option 1:
    Creates a new html file.
    Creates a new javascript file to generate web content.
    Create a docker file.
    Configure Docker YAML.
    Create image document.
    Create Docker container to host the new webpage

Feel free to share, comment or review. 

# How to Run the script
- Prepare:
    - Download the Python script & the Javascript file
    - Ensure the Python script has execute permissions
    - Install Docker if it is not already present 
    - [Special Note] This is setup for Windows OS. I plan to include a Linux version in the future.

Deploy:
    - Run the script i.e. "./build_webpage.py", "& build_webpage.py", "Invoke-Command build_webpage.py"
    - Follow the menu prompts
    - Enter "1" to create a new webpage

Post-Deploy:
    - Enter "3" at the menu prompt 




