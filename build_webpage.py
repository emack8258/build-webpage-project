# Generate a new web file
import time
import os, shutil, subprocess

docker_name = "Dockerfile"
DOCKER_FILE = os.path.join('./', "Docker", "html_generator", "Dockerfile")
build_dockerfile = DOCKER_FILE.replace('\\', '/')
docker_commands = {
    "ls": ["docker", "container", "ls"],
    "build": ["docker", "build", "-t", "js-web-app", "-f", build_dockerfile, "."],
    "compose_up": ["docker", "compose", "up", "--build", "-d"], # 
    "compose_down": ["docker", "compose", "down"],
    "stop": ["docker", "stop", "js-web-app"],
    "remove": ["docker", "rm", "js-web-app"]
}

docker_desktop = os.path.expandvars(
    r"%ProgramFiles%\Docker\Docker\Docker Desktop.exe"
)

def display_menu():
    first_line = "0:\tNew webpage"
    second_line = "1:\tContinue working..."
    third_line = "2:\tClean up and exit"

    menu = [first_line, second_line, third_line]
    print("\nSelect the webpage building option.\n")
    for txt in menu:
        print(txt)

    return True

def create_page():
    """
    1. Create a new html file using write method
    2. Write the script tag only to the file
    Returns: Content for the new webpage
    """
    html = "index.html"

    # The jss file will create all content in the html file
    content = """
        <script src="index.js">
        </script> 
    """
    with open(html, 'w') as webfile:
        webfile.write(content)

    print("New html page was created.")
    return True

def write_dockerfile(file):
    dockerfile_content = f"""
# Use a lightweight Nginx image to serve static files
FROM nginx:alpine

# Copy the content
COPY . /usr/share/nginx/html

"""
    with open(file, 'w') as df:
        df.write(dockerfile_content)
    print(f" [+] Created {file}")
    return True

def wait_for_docker():
    for n in range(30):
        result = subprocess.run(
            ["docker", "info"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("Docker engine is running.")
            return True
        
        time.sleep(2)

    print("Docker did not start in time.")
    return False

def container_config(yaml):
    compose_content = f"""version: '3.8'

services:
  web:
    # Build the image from the Dockerfile
    build: 
      context: .
      dockerfile: Docker/html_generator/Dockerfile
    image: js-web-app
    container_name: js-web-app
    # Map port 8080
    ports:
      - "8080:80"
    # Restart the container if it stops
    restart: always
"""
    with open(yaml, 'w') as cy:
        cy.write(compose_content)
    print(f" [+] Created {yaml}")
    return True

def run_cmd(cmd_list):
    try:
        result = subprocess.run(
            cmd_list,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        
        if result.stderr:
            print(result.stderr)

    except FileNotFoundError:
        print(f"Error: Command not found: {cmd_list[0]}")

    return True

def docker_handler(commands, exe):
    # Function to orchestrate docker actions
    compose_filename = "docker-compose.yml"
    container_config(compose_filename)

    # Start the Docker Enginer first
    print("Waiting for Docker Desktop to start...")
    run_docker = subprocess.Popen([exe])
    wait_for_docker()

    print("Creating a Docker container and image in current directory...")

    print("Building Docker image...")
    run_cmd(commands['build'])

    print("Starting container using docker compose...")
    run_cmd(commands['compose_up'])

    return True

def cleanup(commands):
    # Stopping Docker image and remove containers
    print("Removing the container...")
    run_cmd(commands["compose_down"])
    print("Stopping and removing the image...")
    run_cmd(commands['stop'])
    run_cmd(commands['remove'])
    print("\nContainers and images removed.")

    # Function to remove all content from the html document
    print("\nRemoving the html file.\n")
    try:
        os.remove("index.html")
        print("Successfully removed created html file.")
    except OSError as error:
        print(f"Unable to remove the html file: {error}.")
    finally:
        print("Clean up finished.")
    return True

# ---------- Main Logic ----------
choices = [0,1,2]
while True:
    display_menu()
    choice = int(input("Enter the option number: "))

    if choice not in choices:
        print("\nSelect from the menu...")

    match choice:
        case 0:
            print(f"Choice {choice} selected. Creating a new webpage")
            create_page()

            # Create the docker environment if it does not exist
            if not os.path.exists(DOCKER_FILE):
                os.makedirs("Docker/html_generator")
                write_dockerfile(DOCKER_FILE)

            docker_handler(docker_commands, docker_desktop)

        case 1:
            print(f"Choice {choice} selected. Continue working for 1 minute.")
            time.sleep(60)
        case 2:
            print(f"Choice {choice} selected. Enviroment is cleaned up.\nExiting afterwards.")
            cleanup(docker_commands)
            break



    

    
