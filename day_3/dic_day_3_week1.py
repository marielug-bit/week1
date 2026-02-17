sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict['class']['student']['marks']['history'])

print("aa"+'bb')

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]
del sample_dict['name']
del sample_dict['salary']
#del sample_dict['name','salary'] ne marche pas 
# sample_dict = {k: v for k, v in sample_dict.items() if k not in keys_to_remove}
print(sample_dict)

lst = [1,2,3]
def multiply(x):
    return x*2

print(list(map(multiply,lst)))
print(lst)