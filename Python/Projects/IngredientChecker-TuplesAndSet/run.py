my_tuples = (1,2,3)

cordinates = (10,20,30)
x,y,z = cordinates

print(x,y,z)


fruits = ("apple", "banana","cherry")
for fruit in fruits:
    print(fruit )


# sets 

my_sets = {1,2,3}
ingredients = {"flour","sugar","butter"}
print(ingredients)


#---- ingredientts check ----


recipe_ingredients = {"flour", "sugar", "butter", "eggs", "milk"}


user_input = input("Enter the ingredients you have (separated by commas): ")
user_ingredients = set(user_input.split(", "))


missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients
 

print("\n--- Ingredient Check Results ----")
if missing_ingredients:
print(f"You are missing the following ingredients: {', '.join(missing_ingredients)}")
else:
print("You have all the ingredients needed.")

if extra_ingredients:
print(f"You have extra ingredients: {', '.join(extra_ingredients)}")
else:
print("You have all the ingredients needed.")


