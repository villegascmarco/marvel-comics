# Marvel Comics

[![Docker Pulls](https://img.shields.io/docker/pulls/villegascmarco/marvel-comics_app_container.svg)](https://hub.docker.com/r/villegascmarco/marvel-comics_app_container)

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

# Marvel-comics: End-point documentation

## End-point: Search Characters

### Method: POST

> ```
> http://127.0.0.1:5000/searchComics
> ```

### Body (**raw**)

```json
{
  "type": "character", // Optional attribute, accept either character or comic as value.
  "filter": "%Spider-Man%" // Mandatory if "type" attribute is present.
}
```

### Response

```json
{
  "action": "", //Action performed description.
  "result": [] //Related characters found
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Search All Characters

### Method: POST

> ```
> http://127.0.0.1:5000/searchComics
> ```

### Body (**raw**)

```json
{}
```

### Response

```json
{
  "action": "", //Action performed description.
  "result": [] //Character list
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Search Comics

### Method: POST

> ```
> http://127.0.0.1:5000/searchComics
> ```

### Body (**raw**)

```json
{
  "type": "comic", // Optional attribute, accept either character or comic as value.
  "filter": "Spider-Man%" // Mandatory if "type" attribute is present.
}
```

### Response

```json
{
  "action": "", //Action performed description.
  "result": [] //Related comics found
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Users Add

### Method: POST

> ```
> http://127.0.0.1:5000/users/add
> ```

### Body (**raw**)

```json
{
  "email": "an@email.com", // Mandatory field
  "password": "a_fancy_password:123", // Mandatory field

  // Any other field is custom, you can create your own fields
  "name": "My Name",
  "age": 99
}
```

### Response

```json
{
  "action": "", //Action performed description.
  "result": [] //New user info without password
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Users Login

### Method: POST

> ```
> http://127.0.0.1:5000/users/login
> ```

### Body (**raw**)

```json
{
  "email": "an@email.com",
  "password": "a_fancy_password:123"
}
```

### Response

```json
{
  "action": "", //Action performed description.
  "result": [] //User info and its TOKEN
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: addToLayaway

### Method: POST

> ```
> http://127.0.0.1:5000/addToLayaway
> ```

### Headers

| Content-Type | Value                          |
| ------------ | ------------------------------ |
| token        | YOUR_TOKEN_FROM_LOGIN_ENDPOINT |

### Body (**raw**)

```json
{
  "comics_to_add": [59551, 102588, 98309] // Marvel comics ids.
}
```

### Response

```json
{
  "action": "", //Action performed description.
  "result": [] //Inserted comics info
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: getLayawayList

Get a list with the related comics of one user.

### Method: POST

> ```
> http://127.0.0.1:5000/getLayawayList
> ```

### Headers

| Content-Type | Value                          |
| ------------ | ------------------------------ |
| token        | YOUR_TOKEN_FROM_LOGIN_ENDPOINT |

### Body (**raw**)

```json
{
  "field_target": "id", // Field you want to sort by
  "order_by": "desc" // Either asc or desc
}
```

### Response

```json
{
  "action": "", //Action performed description.
  "result": [] //Related info
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

Powered By: [postman-to-markdown](https://github.com/bautistaj/postman-to-markdown/)
