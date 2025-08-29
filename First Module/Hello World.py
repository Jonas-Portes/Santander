print ("Hello, World!")

person = {
    "name": "Juan", 
    "age": 25, 
    "city": "Madrid"
          }

person = {"name": "Juan", "age": 25, "city": "Madrid"}
person.update({"profession": "Engineer"})

def multiply(a, b):
    return a * b
 
result = multiply(5, 3) + multiply(2, 4)


def function():
    if 1+1==32:
        raise Exception("Error description")


try:
    function()
except Exception as e:
    print(f"Error: {str(e)}")
    
print((not True) or (False and True) )

x = 5
y = "3"
z = x + int(y)
print(z)


site = ['getcracked', 'cj', 'c++', 'python', 'rust']
idx = 3
site[idx], idx = 'urcracked', 4
print(site)

name = 'Tatum'
text = 'I like a girl named Tiffany, but she has a boyfriend. Despite that, she entertained my advances.'

if text.find(name):
    print('You have her interest, but not her attention.')
else:
    print('You have her attention, but not her interest.')
    
π = 3.14159265
print(π)



x = 1
y = 1
print(x-----y)