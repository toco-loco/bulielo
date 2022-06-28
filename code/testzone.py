from club import *
from elo import *

dortmund = club(1,"bvb",2306)
schalke = club(2,"s04",2077)

test = elo_pred(dortmund.elo,schalke.elo)
print(test[0])