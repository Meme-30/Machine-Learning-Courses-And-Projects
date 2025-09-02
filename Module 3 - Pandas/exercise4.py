import pandas as pd
expenses = pd.Series({'Andrew':200,'Bob':150,'Claire':450})

bob_expense = expenses['Bob']
print(bob_expense)