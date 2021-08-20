import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = "Tobtti2zBiUJyjvDvs7KAPJfQvY6bHy0vbJ8djBBlFNW"
url = "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/7c913f86-ac98-47c3-a8dc-7a8db2a1e24d"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2021-08-17',
        authenticator=authenticator)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')


def englishToFrench(englishText):
    translation = language_translator.translate(text=englishText,
            model_id='en-fr').get_result()
    jsonTranslate = json.dumps(translation, indent=2,
                               ensure_ascii=False)
    frenchText = jsonTranslate['translations'][0]['translation']
    return frenchText


def frenchToEnglish(frenchText):
    translation = language_translator.translate(text=frenchText,
            model_id='fr-en').get_result()
    jsonTranslate = json.dumps(translation, indent=2,
                               ensure_ascii=False)
    englishText = jsonTranslate['translations'][0]['translation']
    return englishText
