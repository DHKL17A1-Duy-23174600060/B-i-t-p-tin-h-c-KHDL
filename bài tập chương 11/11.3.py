# 11.3
def find_animal(animal_list,animal):
    count= 0
    for a in animal_list:
        if a == animal:
            count+=1
        return animal_list,count
    animal_list = ['ant','bear','cat','dog','elephant','fish','goat','hippo']
    animal='bear'
    result=find_animal(animal_list,animal)
    print("List of animal",result[0])
    print("Numbers of animal",result[1])