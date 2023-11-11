a = int(input("alice-candies : "))
b = int(input("bob-candies : "))
c = int(input("carol-candies : "))

#số kẹo mỗi người được nhận
d = (a+b+c)//3

#số kẹo bị đập
e = (a+b+c)%3

print("số kẹo mỗi người đươc nhận là : ", d)
print("số kẹo bị đập là : ", e)