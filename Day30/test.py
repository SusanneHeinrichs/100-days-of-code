# try:
#     file = open("A_file.txt")
#     a_dict = {"hey": "ja"}
#     print(a_dict["hey"])
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# except FileNotFoundError:
#     print("This file does not exist.")
#     file = open("a_file.txt", "w")
#     file.write("Hey")
# else:
#     content = file.read()
#     print(content)
# finally:
#  raise KeyError("This error I made up") 

height = float(input("Height: "))
weight = int(input("Weight: "))
 
if height> 3:
    raise ValueError("Human heights are not higher than 3 meters")
if weight > 250:
    raise ValueError("Human heights are not higher than 250")


bmi = weight / height ** 2
print(bmi)