## Coding Kata 01
The purpose of this coding kata is to develop proficiency in the tasks listed below. It assumes you have `git`, `python`, and `docker` installed. 
* Creating repos in a Git-based version control system like GitHub
* Creating branches using GitHub's UI
* Cloning and checking out a branch using `git`
* Writing a simple Python script that listens for HTTP requests
* Writing a Dockerfile 
* Building a container image using `docker`
* Writing a CI pipeline in YAML
* Pushing changes from a local branch to a remote branch
* Writing a simple unit test
* Submiting a code review request using GitHub's UI

**Step 1.** Login to [GitHub](https://github.com/) and create a new repository.
* Set yourself as the owner
* Name it whatever you want
* Set the visibility to public
* Add a README
* Add a Python-based `.gitignore`
* Add an MIT license

**Step 2.** Create a new branch using GitHub's UI.
* Set the name to your initials followed by `/prototype` (for example, if your name is Vic Fernandez, your branch should be `vf/prototype`)
* Set the source branch to `main`

**Step 3.** Within a Linux-based environment (e.g., Windows Subsystem for Linux), open a CLI-based shell. Next, clone your repository using `git`, change directories to it using `cd`, and then, checkout the branch you created using `git`. In the example below, `cyberphor` is a GitHub username while `octo-chainsaw` is the name of a repository.
```bash
git clone https://github.com/cyberphor/octo-chainsaw
cd octo-chainsaw
git checkout vf/prototype
```

Before moving on, verify you're on the correct branch by running the command below.
```bash
git branch
``` 

**Step 4.** Open your code editor from within your current working directory (this should be the same folder as the repository you downloaded). Write a simple Python script called `backend.py` that listens for HTTP requests. Below is an example. 
```python
# Import HTTP server and handler classes from Python's standard library.
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define some variables.
ip = '0.0.0.0'
port = 8000
server_address = (ip, port)

# Define and init a variable called "api" using the classes we imported. 
api = HTTPServer(
    server_address=server_address,
    RequestHandlerClass=SimpleHTTPRequestHandler
)

# Start the HTTP server.
print("Listening for HTTP requests...")
api.serve_forever()
```

**Step 5.** Create a simple HTML file called `index.html`. Below is an example. 
```html
<html>
    <head>
    <title>octo-chainsaw</title>
    </head>
    <body>
    <h1>octo-chainsaw</h1>
    Hello world!
    </body>
</html>
```

**Step 6.** Start your HTTP server using the command below and then, open a browser to `http://localhost:8000`.
```bash
python backend.py
```

**Step 7.** Once you confirm your code works, stop your HTTP server (CTRL + C).

**Step 8.** Create a Dockerfile. Below is an example. 
```dockerfile
# Define the base image to use.
FROM alpine

# Set the working directory.
WORKDIR /home/octochainsaw

# Install Python.
RUN apk add python3

# Copy our source code.
COPY backend.py backend.py
COPY index.html index.html

# Create a non-root user with no password (-D).
RUN adduser -D octochainsaw -h /home/octochainsaw

# Set permissions.
RUN chown -R octo:octochainsaw /home/octochainsaw

# Switch to a non-root user.
USER octochainsaw

# Identify what TCP port will be used by our server.
EXPOSE 8000

# Start the server.
CMD ["python", "backend.py"]
```

**Step 9.** Build a container image using the Dockerfile you just created. 
```bash
docker build -t octo-chainsaw -f backend/Dockerfile .
```
