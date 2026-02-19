MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%''' 

# Step 1: Convert matrix_string to a 2D list (matrix)
matrix = [list(word) for word in MATRIX_STR.strip().split('\n')]
# ... code to create matrix ...

# Step 2: Iterate through columns
# ... code to iterate through columns ...
lst_col = []
for i in range(len(matrix[0])):
    ls = [raw[i] for raw in matrix]
    lst_col.append(ls)
print(lst_col)
    

# Step 3: Filter alpha characters
# ... code to filter alpha characters ...
for col in lst_col:
    letters = ''.join(list(filter(str.isalpha,col)))
    print(letters)

# Step 4: Replace symbols with spaces
decoded_message = ""
for col in lst_col:
    for ch in col:
        if ch.isalpha():
            decoded_message += ch
        else:
            # on ajoute un espace seulement si le dernier char n'est pas déjà un espace
            if decoded_message and decoded_message[-1] != " ":
                decoded_message += " "

decoded_message = decoded_message.strip()
print(decoded_message)




# Step 5: Print the decoded message
print(decoded_message)