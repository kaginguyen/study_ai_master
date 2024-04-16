import pandas as pd 

data = pd.DataFrame({
    "Qu1":[1,3,4,3,4],
    "Qu2":[2,3,1,2,3],
    "Qu3":[1,5,2,4,4]
})

def quick_histogram(sr: pd.Series): 
    return sr.value_counts()

result = data.apply(quick_histogram, axis = 0)

print(data)
print(result)