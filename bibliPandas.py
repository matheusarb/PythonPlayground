# ferramenta que insere dois tipos de dados ao Python
# Series e DataFrame

# Series é como um vetor de dados(unidimensional) array?, capaz de armazenar diferentes tipos de dados
# DataFrame é um conjunto de Series ou um contêiner para Series

import pandas as pd

pd.Series(data= None, index= None, dtype= None, name= None, copy= False, fastpath= False)
pd.Series(data=5)
test = pd.Series('Heello worldd'.split())
# print(test)

pd.DataFrame()
# pd.read_json()

df = pd.read_csv("dados.csv")
print('df')
