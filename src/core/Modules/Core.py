
def UmlautCorrectors(text:str):
     return text.replace('Ã\x84', 'Ä').replace("Ã\x9f" ,'ß').replace("Ã¼",'ü').replace("Ã¤",'ä').replace("Ã¶",'ö').replace('Ã\x9c','Ü').replace('Ã\x96','Ö')

def WordBigFirstLetter(text):
     if text[0].isupper():
          pass
     else:
          text = text[0].upper() + text[1:]
     return text



