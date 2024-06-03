import pandas as pd
data={
       'Sr.no':[1,2,3,4,5,6,7,8,9,10],
       'players name':['dhoni','kl rahul', 'kunal ','pooran','badoni', 'stonish','navin','siddarth','mosin','hudda'],
       'jerseyno':[99,45,76,82,52,96,36,75,46,24],
       'run':[265,47,91,73,79,82,81,29,93,90],}

df=pd.DataFrame(data)
print("DataFrame:-")
print(df)   



#import pandas as pd
import numpy as np
s = pd.DataFrame(np.arange(1,11).reshape(2,5))
print("Reshaped series:",)
print(s)
print("Size of the dataFrame:",df.shape)




print("Head:")
print(df.head(3))

print("\nTail:")
print(df.tail(3))



print("Missing values:")
print(df.isnull().any())






import pandas as pd
data={
       'Sr.no':[1,2,3,4,5,6,7,8,9,10],
       'players name':['dhoni','kl rahul', 'kunal ','pooran','badoni', 'stonish','navin','siddarth','mosin','hudda'],
       'jerseyno':[99,45,76,82,52,96,36,75,46,24],
       'run':[265,47,91,73,79,82,81,29,93,90],}

df=pd.DataFrame(data)
print("DataFrame:-")
print(df)


print("\n HERE IS YOUR LOCATION FROM ROW NO 2 TO ROW NO 7 ,AND COLUMN NO  2 TO CLOUMN NUMBER 5")
print(df.iloc[2:7,2:5])