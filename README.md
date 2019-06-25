# Send google doc file to email
## Setup
### Set up environment
```
pip install -r requirements.txt
```
### Create config files
Create following files in the same directory with **main.py**
```
touch credentials.json
touch client_id.json
touch contacts.txt
touch content.json
```
### Get google app password
1. Follow instructions in [here](https://support.google.com/mail/answer/185833?hl=en) to get app password.
2. Change email and app password in **credentials.json**
```
{
    "email": "<your email>",
    "app_password": "<your app password>"
}
```
### Get google OAuth2 credentials 
1. Follow instructions in [here](https://developers.google.com/adwords/api/docs/guides/authentication) to OAuth2 credentials.
2. Paste all information of json file you downloaded into **client_id.json**
### Set up content of email
Config your subject and file id in **content.json**
```
{
    "subject": "<your subject>",
    "file_id": "<your file id>"
}
```
### Set of user email(s) to send
Write your user email(s) in **contacts.txt** in the same directory with **main.py**
```
john john@gmail.com
marry marry@gmail.com
```
## Usage
To send google doc file as a content to email
```
python main.py <file_id>
```
*Note: You may be login for fisrt time to get app code*