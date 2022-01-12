dict_list = [{'name': 'affirm', 'confidence': 0.94481849204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]
condensList = []
for x in dict_list:
 if(x not in condensList):
  condensList.append(x)
print(condensList)