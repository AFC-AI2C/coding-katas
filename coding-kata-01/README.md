## Coding Kata 01
The purpose of this coding kata is to develop proficiency in the tasks listed below. It assumes you have `git`, `python`, `docker`, and a code editor installed. 
* Create a repository in a Git-based version control system like GitHub
* Create a branch using GitHub's UI
* Clone and check out a branch using `git`
* Write a CI pipeline in YAML
* Push changes from a local branch to a remote branch
* Write a simple Python script that listens for HTTP requests
* Write a Dockerfile 
* Build a container image using `docker`
* Run a container locally using `docker`
* Submit a Pull Request using GitHub's UI

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

**Step 3.** Within a Linux-based environment (e.g., Windows Subsystem for Linux), open a CLI-based shell. Next, clone your repository using `git`, change directories to it using `cd`, and then, checkout the branch you created using `git`. In the example below, `cyberphor` is a GitHub username while `peacefield` is the name of a repository.
```bash
git clone https://github.com/cyberphor/peacefield
cd peacefield
git checkout vf/prototype
```

Before moving on, verify you're on the correct branch by running the command below.
```bash
git branch
``` 

**Step 4.** Create a directory called `.github` that contains another directory called `workflows`. Then, create a file called `ci-pipeline.yml` under `.github/workflows`. Add the content below to the `ci-pipeline.yml` file.
```yaml
# Set the pipeline name.
name: Continuous Integration

# Set pipeline execution criteria.
on:
  push

# Define all jobs within the pipeline.
jobs:

  # Define the test job.
  test:
    name: test
    runs-on: ubuntu-latest
    steps:

      # Install Python.
      - name: python
        uses: actions/setup-python@v5
        with:
          python-version: 3.12

      # Install Python dependencies.
      - name: pip
        run: python -m pip install black

      # Download the source code.
      - name: clone
        uses: actions/checkout@v4

      # Conduct a QA test.
      - name: black
        run: black --diff --color --check .

  # Define the pre-build-scan job.
  pre-build-scan:
    name: pre-build-scan
    needs: test
    runs-on: ubuntu-latest
    container:
      image: semgrep/semgrep

    steps:
      # Download the source code.
      - name: clone
        uses: actions/checkout@v4
      
      # Conduct a SAST scan.
      - name: semgrep
        run: semgrep scan --config auto

  # Define the build job.
  build:
    name: build
    needs: pre-build-scan
    runs-on: ubuntu-latest
    steps:

      # Download the source code.
      - name: clone
        uses: actions/checkout@v4

      # Build the container image.
      - name: docker
        run: docker build .
```

**Step 5.** Commit the changes made to the local branch to the remote branch of your repository using the commands below. Review the pipeline results in the GitLab UI, but do not take action on them yet.
```bash
git add -A
git commit -m "Added a CI pipeline"
git push
```

**Step 6.** Open your code editor from within your current working directory (this should be the same folder as the repository you downloaded). Write a simple Python script called `backend.py` that listens for HTTP requests. Below is an example. 
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

**Step 7.** Create an HTML file called `index.html` in the root of your repository. Below is an example. 
```html
<html>
    <head>
        <title>peacefield</title>
    </head>
    <body>
        <h1>peacefield</h1>
        Hello world!
    </body>
</html>
```

**Step 8.** Start your HTTP server using the command below and then, verify it works by openining a browser to `http://localhost:8000`. You should see your HTML page.
```bash
python backend.py
```

**Step 9.** Once you confirm your code works, stop your HTTP server (CTRL + C). Then, commit the changes you've made and review the pipeline results in the GitLab UI. Address any findings relating to your source code before moving onto the next step. 
```bash
git add -A
git commit -m "Added a backend"
git push
```

**Step 10.** Create a Dockerfile. Below is an example. 
```dockerfile
# Define the base image to use.
FROM alpine

# Set the working directory.
WORKDIR /home/peacefield

# Install Python.
RUN apk add python3

# Copy our source code.
COPY backend.py backend.py
COPY index.html index.html

# Create a non-root user with no password (-D).
RUN adduser -D peacefield -h /home/peacefield

# Set permissions.
RUN chown -R peacefield:peacefield /home/peacefield

# Switch to a non-root user.
USER peacefield

# Identify what TCP port will be used by our server.
EXPOSE 8000

# Start the server.
CMD ["python", "backend.py"]
```

**Step 11.** Create a container image using the Dockerfile you just created.  
```bash
docker build -t peacefield/backend:v1.0.0 -f Dockerfile .
```

**Step 12.** Create a container using the container image you just created. 
```bash
docker run --name peacefield-backend -d -p 8000:8000 -t peacefield/backend:v1.0.0 
```

**Step 13.** Verify your container is working by opening a browser to `http://localhost:8000`. As before, you should see your HTML page. Once you verify the container is working, stop it by using the command below.
```bash
docker stop peacefield-backend
```

**Step 14.** Commit the changes you made and review the pipeline results in the GitLab UI. Address all findings before moving onto the next step. 
```bash
git add -A
git commit -m "Added a Dockerfile"
git push
```

**Step 15.** Submit a Pull Request using GitHub's UI so your changes are pulled into the `main` branch.
