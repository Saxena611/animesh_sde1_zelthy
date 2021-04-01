# SDE1 ASSIGNMENT - ZELTHY

_Language: Python3
Virtual Environment Setup : Run command <pip or pipenv (depending upon the venv)> install -r requirements.txt

## Assignment 1:
Write a python class that is able to send an email from the terminal to a given email address
using smtplib library.

Solution:
Along, with send_mail I have tried to simulate a user management functionality as well.
This has enabled this challenge solution to be used by multiple user without actually exposing their gmail credentials as hardcoded parameters.
Inside package assignment_1 it comprises of thress file with the functionality as defined below:

- configure_user.py : 
    - This script configure the user gmail credentials and safely stores them into the os using keyring technique.
    - Creates and maintains a user_configurations.txt file which maintains the list of users registered.
    - Command : python -m assignment_1.configure_user 
    - You will be asked to enter your gmail username and password which will be safely stored as secret in os.
- mail_sender.py :
    - This script will shoot an email to the provided recipients.
    - This will first make you login by verifying the password on the provided username.
    - Command : python -m assignment_1.send_email
- retrieve_validate_user_password:
    - This is internally used by configure_user and mail_sender for validating existing user and password matching.
    - Type of usermanagement.

***Output**
Terminal Output:
![assignment1_terminal](https://user-images.githubusercontent.com/29275475/113243737-329e7e00-92d1-11eb-802e-2ce15255e688.PNG)
Email Recieved:
![assignment1_email](https://user-images.githubusercontent.com/29275475/113243809-5366d380-92d1-11eb-947b-3605d46b4359.PNG)


## Assignment 2:
Write a python class that is able to return the meaning of an English language word provided to it
in the terminal. (Use https://dictionaryapi.dev/)

Solution :
Wrote a class file dictionary_search_main.py which instantiates constanst.py. constansts.py comprises of property values which are required by the DictionarySearch class
hitting the api. The class DictionarySearch provides user the flexibility to switch between differenct language as well . However , default language is set as english.

- dictionary_search.py
    - This takes the word as input from the user creates object for DictionarySearch and make the right method call i.e. search_word() for getting the response from the API.
    - Command : python -m assignment_2.dictionary_search
- dictionary_search_main.py
    - Comprises of  the class DictionarySearch constructor initializes the url and methods get_api_link() forms the right api url on the basis of parameters provided. 
    - Method search_word() makes request to the formed url and parses the response in the required way.
- constants.py
    - Comprises of class RestConf which keeps all the required property.

**Output**
Terminal Output:
![asssingment_2](https://user-images.githubusercontent.com/29275475/113243889-81e4ae80-92d1-11eb-8d3d-e2da5cc2178b.PNG)


## Assignment 3:
Write a python class that is able to return the flight distance between two cities given their
latitude and longitude coordinates.

Solution:
Using the defined approach of haversine formula wrote a class CityDistance which comprises  HaversineFormula as inner class.
The city distance holds dependency on haversine algorithm it is good to have it as a inner class.Inner class allows better
code readablity and ensures hiding.

- city_distance.py
    - This comprises of class CityDistance which takes comma seperated latitude and longitude string along with direction as parameter.
    - Internally , it parses the string and fetches longitude and latitude and calculates the distance.
    - Sample input : 51.5074 N, 0.1278 W
    - Command : python -m assignment_3.city_distance

**Output**
Terminal Output:
![assignment_3](https://user-images.githubusercontent.com/29275475/113243967-aa6ca880-92d1-11eb-8881-b9476e7db1f3.PNG)
