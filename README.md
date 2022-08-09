# Marvel Comics

Microservices project using Flask to communicate with Marvel api and manage users using MongoDB.

## Set up

Pull repository and move into the project folder

```console
git clone https://github.com/villegascmarco/marvel-comics.git

cd marvel-comics
```

Create a .env file at root level with the following structure:

```
PUBLIC_KEY="YOUR_PUBLIC_KEY"
PRIVATE_KEY="YOUR_PRIVATE_KEY"
SECRET_KEY= "RANDOM_LONG_STRING" #as long or short as you want
```

Public and Private key comes from this [API documentation](https://developer.marvel.com/). Create your own keys and save it into the .env file.

Create a virtual env and open it:

**_This step is optional if you do not want to have importing errors in your editor UI. Either you perform this step or not, nothing changes in the app_**

```
python -m venv venv
```

```
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
# In Linux and MacOS
source myvenv/bin/activate
```

File structure at this point:

```
marvel-comics
└───app
│   └ ...
└───venv #Optional
│   └ ...
│   .env
│   .gitignore
│   app.py
│   docker-compose-dev.yml
│   docker-compose.yml
│   Dockerfile
│   Dockerfile.dev
│   README.md
│   requirements.txt
```

## Run environment

```
docker compose -f docker-compose-dev.yml
```
