import json

# file_open=open('data.txt','r')
# print("file open",file_open)

# load_data= file_open.read()

# print("load data",load_data)

# file_open.close()

# # file_open.read()

# print("load data",load_data)


# this is for file open , here is using r(read mode)
with open("data.txt", "r") as file_open:
    print("file_open",file_open)
    load_data = file_open.read()
    # print("load data", load_data)  we can write inside with  also


# print("load data", load_data)  

#  this is for write file , w for write 

# with open('new_file.txt','w') as file_open:
#     file_open.write("virat kohli is the biggest batsman in the world \n")
#     file_open.write("he is legend")

# with open("new_file.txt",'w') as file_open:
#     file_open.write('pahle wala sb mita diya')
    
with open("new_file.txt", "a") as f:
    f.write("\n mode a use kr rha hu \n")
    f.write("virat kohli")



#  json file ko read se open krke dekhte hai kya milta hai

with open("products.json", "r") as f:
    data = f.read()

# print("type",type(data))
# print(f"data aa gya : {data}")  data aa gya but string me hai 
# data[0]["name"] ye error dega kuy ki string hai 



#  ye json file read krne ke liye hai 
with open("products.json", "r") as f:
    products = json.load(f)
    #  json.load() string data ko list of dict me convert krta hai jo hme chhaiye tbhi ham koi bhi operation kr skte hai dict wala

# print(type(products))
# print(len(products))
# # print(f"products data : {products}")
# print(f"products data single  : {products[0]["name"]}")


products.append({"id": 13, "name": "Test Item"})

with open("products.json", "w") as f:
    json.dump(products, f, indent=2)


with open("products.json", "r") as f:
    data= json.load(f)



print(f"data aaya after update krne ke bad : {data[13]['name']}" )
