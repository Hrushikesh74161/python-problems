import random
EntitiesList = ['kolkata', 'delhi', 'mumbai']
utteranceList = ['How far is <> from <>', 'How is weather in <>']
choices = []
output = []
substring = '<>'
for x in utteranceList:
 initial = x.find('<>')
 final = x.rfind('<>')
 if(initial == final):
  for y in EntitiesList:
   output.append(x.replace('<>', y))
print(output)
 