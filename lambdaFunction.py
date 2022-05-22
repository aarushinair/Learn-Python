# using the lambda function
lambda_cube = lambda y: y*y*y

print(lambda_cube(5))


# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)


# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
 
print(uppered_animals)
