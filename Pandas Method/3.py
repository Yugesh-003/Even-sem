import pandas as pd
df = pd.DataFrame({
'Name': ['Kanna', 'Jithu', 'Charu'],
'Age': [20, 25, 22],
'Score': [85, 90, 88]
})

print("Original DataFrame:\n", df)


# Select a column
print("\nSelected Column:\n", df['Name'])


# Add a column
df['Passed'] = df['Score'] > 80
print("\nAfter Adding Column:\n", df)


# Add a row
row = pd.DataFrame([{'Name': 'Ammu', 'Age': 23, 'Score': 92,'Passed': True}])
df = pd.concat([df,row], ignore_index=True)
print("\nAfter Adding a New Row:\n", df)



# Delete a column
df.drop(columns='Score', inplace=True)
print("\nAfter Deleting Column:\n", df)


# Delete a row
df.drop(index=2, inplace=True)
print("\nAfter Deleting Row :\n", df)
