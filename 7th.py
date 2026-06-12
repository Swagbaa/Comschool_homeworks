# import requests
#N1

#select productname, categoryid, unit, price from products
#where price between 18 and 25
#group by price desc

#N2 -------------------------------------------------------

#select * from OrderDetails
#where quantity in (15, 12)
#group by quantity asc

#N3 -----------------------------------------------------

# items=[
# {"id": 1, "price": 50},
# {"id": 2, "price": 200},
# {"id": 3, "price": 150}
# ]
#
# for item in items:
#     if item["price"]>100:
#         print(item)

#N4 -----------------------------------------------

# companies={
# "company": {
#     "departments": [
#         {"name": "IT", "employees": [{"name": "Ana"}, {"name": "Beka"}]},
#         {"name": "HR", "employees": [{"name": "Nino"}]}
#         ]
#     }
# }
#
# for department in companies["company"]["departments"]:
#     for employee in department["employees"]:
#         print(employee["name"])

#N5 --------------------------------------------------

# students=[
#     {"name": "Ana", "grades": [90, 80, 95]},
#     {"name": "Beka", "grades": [70, 85, 88]},
#     {"name": "Nino", "grades": [100, 95, 99]}
# ]
#
# for student in students:
#     total=sum(student["grades"])
#     average=round(total/len(student["grades"]),2)
#     print(f"{student['name']}: {average}")

#N6 --------------------------------------------------

# dataset={
# "companies": [
#     {"name": "TechCorp",
#             "employees": [
#                 {"name": "Ana", "salary": 3000},
#                 {"name": "Beka", "salary": 4500}
#                 ]
#             },
#     {"name": "SoftPlus",
#             "employees": [
#                 {"name": "Nino", "salary": 5000},
#                 {"name": "Giorgi", "salary": 2500}
#                 ]
#         }
#     ]
# }
#
# for company in dataset["companies"]:
#     for employee in company["employees"]:
#         if employee["salary"]>4000:
#             print(employee["name"], "-", company["name"], "-", employee["salary"])

#N7 ---------------------------------------------------------------------------------

# url = "https://jsonplaceholder.typicode.com/users"
# respone=request.get(url)
#
# print(response.json())

#N8 ---------------------------------------------------

# url = "https://jsonplaceholder.typicode.com/posts"
#
# new = {
#     "title": "Test",
#     "body": "Hello World",
#     "userId": 5
# }
#
# response = requests.post(url, json=new)
#
# print(response.json())

#N9 ------------------------------------------------------

# url="https://jsonplaceholder.typicode.com/todos"
#
# data=request.get(url).json()
#
# total=0
# for todo in data:
#     if todo["completed"]==False
#         total+=1
#         print(todo)
#
# print(total)

#N10 ---------------------------------------------------

# posts_url = "https://jsonplaceholder.typicode.com/posts"
# users_url = "https://jsonplaceholder.typicode.com/users"
#
# posts = requests.get(posts_url).json()
# users = requests.get(users_url).json()
# 
# user_map = {user["id"]: user["name"] for user in users}
#
# for post in posts[:5]:
#     title = post["title"]
#     author = user_map[post["userId"]]
#     print(f"{title} - {author}")



