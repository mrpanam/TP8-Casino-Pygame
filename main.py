import numpy as np
from random import choices
fruits=["ananas","cerise","orange","pasteque","pomme_dor"]
jetons=0
gains={"ananas" :50,"cerise":15,"orange":5,"pasteque":150,"pomme_dor":10000}

#print(choices(fruits,k=3))
print("tirage:")
proba_fruit=[0.2,0.25,0.4,0.1,0.05]

result=np.random.choice(fruits,3,proba_fruit)

print(result)
if result[0] == result[1] == result[2]:
    jetons=gains[result[0]]
    print(f"gagne 3 {result[0]} vous avez obtenu  {jetons} jetons ")
else:
    print("perdu ")