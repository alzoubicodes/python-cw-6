# write your code here
# Part 1
person = {

    "name" : "Mahdi",
    "age" : "18",
    "hobbies" : ["Programing", "Weapon duel", "Photography"],
}
print(person['name'])
print(person['age'])

# Part 2
person['age'] = '25'
person['country'] = 'Kuwait'
print(person)
print(len(person))

# Part 3
person["hobbies"].append('hacking')

def check_hobbies(person):
    if len(person["hobbies"]) >= 3:
        print("WOW YOU ARE AMAZING")

check_hobbies(person)