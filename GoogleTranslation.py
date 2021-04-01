import os
from google.cloud import translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'GoogleTranslationAPIKey.json'

def translate_text(text="YOUR_TEXT_TO_TRANSLATE", project_id="YOUR_PROJECT_ID"):
    """Translating Text."""
    translatedText = ""
    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{project_id}/locations/{location}"

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",  # mime types: text/plain, text/html
            "source_language_code": "en-US",
            "target_language_code": "ja",
        }
    )

    # Display the translation for each input text provided
    for translation in response.translations:
        #print("Translated text: {}".format(translation.translated_text))
        translatedText = format(translation.translated_text)
    return translatedText

def NewLineToStringList(string):
    stringList = string.split("\n")
    return stringList
def JapaneseDotToStringList(string):
    stringList = string.split("。")
    return stringList
def StringListToSingleLine(stringList):
    stringLine = ""
    for x in stringList:
        stringLine= (stringLine+x+". ");
    return stringLine
def CombineEngAndJP(EnList,JpList):
    for index in range(len(EnList)):
        print(EnList[index])
        print(JpList[index])
text = "Topic. Sub Category. Sub Category 2. Sub Category 3. Sub Category 4. Content. URL"
projectID = "phrasal-bruin-309308"




text="""Overview of the eye tracking demo samples
Setting up the MRTK eye tracking samples"""


EnStringList = NewLineToStringList(text)
EnStringLine = StringListToSingleLine(EnStringList)
JpStringLine = translate_text(EnStringLine, projectID)
JpStringList = JapaneseDotToStringList(JpStringLine)
CombineEngAndJP(EnStringList, JpStringList)


