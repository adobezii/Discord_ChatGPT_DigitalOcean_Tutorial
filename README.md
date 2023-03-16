Deploying a Discord bot with Flask on DigitalOcean

## Orignally coding from Zero6992/chatGPT-discord-bot https://github.com/Zero6992/chatGPT-discord-bot
## For How to work in discord, please check his repo, A million thanks. 
## This repo only focus in How to Setup in Digitalocean to keep the server running.

## Code Fixed by ChatGPT4

Deploying a Discord bot with Flask on DigitalOcean
==================================================

This tutorial will guide you through deploying a Discord bot with Flask on DigitalOcean.

Prerequisites
-------------

1.  A Discord bot with source code.
2.  A DigitalOcean account.

Step 1: Set up a Flask server
-----------------------------

1.  Add Flask to your project's requirements.txt file:

makefile

```makefile
Flask==2.1.1
```

2.  Create a Flask server in your project:

python

```python
from flask import Flask, jsonify
import threading

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="OK")

def run_web_server():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

if __name__ == "__main__":
    # Run Flask server in a separate thread
    threading.Thread(target=run_web_server, daemon=True).start()

    # Start your Discord bot as you normally do
    bot.run_discord_bot()
```

Step 2: Create a DigitalOcean App
---------------------------------

1.  Log in to your DigitalOcean account.
2.  Click on the "Apps" tab on the left sidebar.
3.  Click on the "Launch Your App" button.
4.  Choose the repository containing your Discord bot's source code.
5.  Configure the app's settings:
    1.  Add a `discord_bot_token` environment variable with your bot's token.
    2.  Set the "Run command" to `python main.py` (or the appropriate command for your project).
    3.  Set the "HTTP route" to `/health`.
    4.  Set the "HTTP port" to `8080` (or the appropriate port number you specified in your Flask server code).
6.  Click on "Launch Basic App" to start the deployment process.

Step 3: Modify the DigitalOcean App specification
-------------------------------------------------

1.  Once your app is deployed, go to the "Settings" tab of your app in the DigitalOcean dashboard.
2.  Click on the "Edit App Spec" button.
3.  Add a `health` object under the `services` object in the app spec:

yaml

```yaml
services:
- environment_slug: python
  github:
    branch: main
    deploy_on_push: true
    repo: your/repo
  health:
    http_path: /health
  http_port: 8080
  instance_count: 1
  instance_size_slug: basic-xxs
  name: your-app-name
  run_command: python main.py
```

4.  Save your changes and redeploy your app.

Your Discord bot should now be running with the Flask server handling health checks on DigitalOcean. You can monitor your app's logs and status on the DigitalOcean dashboard.
