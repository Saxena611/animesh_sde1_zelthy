import json
import requests
from requests.exceptions import HTTPError
from assignment_2.constants import RestConf

class DictionarySearch:
    """
    Makes api call to dictionary_search a word. Forms the api url on the basis of the dynamic parameters provided.
    Method search_word:
    :param word : Word you are looking meaning for.
    :param language (deafult = "English") : Langugage . Can be overriden. Refer to api doc.
    Internally , initializes RestConf class where parameters like api_url and default language are setup.
    """
    
    def __init__(self):
        self.api_url = RestConf.DICT_API_URL
    
    def get_apilink(self,word,language=RestConf.LAN):
        return self.api_url.format(language,word)
        
    def search_word(self,word,language=RestConf.LAN):
        """
        This method makes get request to the api and parses response for fetching the meaning of the requested word.
        """
        output = ""
        api_link = self.get_apilink(word,language)
        request_success = True
        try:
            response = requests.get(api_link)
            response.raise_for_status()
        except HTTPError as http_err:
            output = "Http error occured . " + str(http_err)
            request_success = False
        except Exception as ex:
            output = "Other Exception Occured . " + str(ex)
            request_success = False
        
        if request_success == True and response.status_code == 200:
            data = response.content
            jsonify = json.loads(data)
            meaning_list = jsonify[0].get("meanings")
            count = 0
            for meaning_dict in meaning_list:
                count += 1
                partOfspeech = meaning_dict.get("partOfSpeech")
                meaning = meaning_dict.get("definitions")[0].get("definition")
                output_response = str(count) + ".) " +  partOfspeech + "." + meaning + "\n"
                output += output_response
        return output

