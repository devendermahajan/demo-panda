# importing libraries
import pandas as pd
import colorama as clr

print("="*50)
print("Data Frame - CSV Demo")
print("="*50)

# reading data from file
df = pd.read_csv('sales.csv')

# converting series to dictionary
data = dict(df['AMOUNTINFO'].describe())

# colourful output
for key,value in data.items():
    print(f"{clr.Fore.LIGHTCYAN_EX + key:>10}",end=": ")
    print(clr.Fore.LIGHTYELLOW_EX + str(round(value,2)))
print(clr.Fore.RESET,end="")
print("="*50)