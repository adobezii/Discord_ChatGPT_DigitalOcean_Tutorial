from src import bot
from dotenv import load_dotenv
import os
import sys
from flask import Flask, jsonify
import threading

load_dotenv()

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="OK")

def run_web_server():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

def check_version() -> None:
    import pkg_resources
    import src.log

    logger = src.log.setup_logger(__name__)

    # Read the requirements.txt file and add each line to a list
    with open('requirements.txt') as f:
        required = f.read().splitlines()

    # For each library listed in requirements.txt, check if the corresponding version is installed
    for package in required:
        # Use the pkg_resources library to get information about the installed version of the library
        package_name, package_version = package.split('==')
        installed = pkg_resources.get_distribution(package_name)
        # Extract the library name and version number
        name, version = installed.project_name, installed.version
        # Compare the version number to see if it matches the one in requirements.txt
        if package != f'{name}=={version}':
            logger.error(f'{name} version {version} is installed but does not match the requirements')
            sys.exit()

if __name__ == '__main__':
    check_version()

    # Run Flask server in a separate thread
    threading.Thread(target=run_web_server, daemon=True).start()

    # Start your Discord bot as you normally do
    bot.run_discord_bot()
