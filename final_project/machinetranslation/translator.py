'''Module to translate text between English and French'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['api_key']
url = os.environ['url']

auth = IAMAuthenticator(apikey)
lang_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=auth)
lang_translator.set_service_url(url)

def english_to_french(english_text):
    '''Function to translate text from English to French'''
    trans_result = lang_translator.translate(text=english_text, model='eng-fr')
    translation = trans_result.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''Function to translate text from French to English'''
    trans_result = lang_translator.translate(text=french_text, model='fr-eng')
    translation = trans_result.get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
