import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


#replace authenticator key below with your API key
authenticator = IAMAuthenticator('')
service = NaturalLanguageUnderstandingV1(
    version = '2019-07-12',
    authenticator=authenticator
)

#replace URL with URL provided by IBM interface
service.set_service_url('')

response = service.analyze(url='https://www.nationalgeographic.com/animals/mammals/d/domestic-dog/', 
    features = Features(entities=EntitiesOptions(), keywords=KeywordsOptions(), emotion=EmotionOptions(targets=['dog', 'dogs']))).get_result()

print(json.dumps(response, indent=2))
