import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator('lfpdfmB9ops-FzNEnOL4-tgq3KtTANC6aG3sEIVPnHnM')
service = NaturalLanguageUnderstandingV1(
    version = '2019-07-12',
    authenticator=authenticator
)

service.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/10148b27-408a-47cc-8349-5c81466afe97')

response = service.analyze(url='https://www.nationalgeographic.com/animals/mammals/d/domestic-dog/', 
    features = Features(entities=EntitiesOptions(), keywords=KeywordsOptions(), emotion=EmotionOptions(targets=['dog', 'dogs']))).get_result()

print(json.dumps(response, indent=2))
