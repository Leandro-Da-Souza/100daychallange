# programming_dictionary = {
#     "Bug" : "An error",
#     "Function": "A piece of code that is resuable."
# }

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# programming_dictionary["Loop"] = "code running over and over and over and over."

# print(programming_dictionary)

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
def add_grades(scores: dict, grades: dict):
    for student in scores:
        if scores[student] < 70:
            grades[student] = "Fail"
        elif scores[student] >= 71 and scores[student] <= 80:
            grades[student] = "Acceptable"
        elif scores[student] >= 81 and scores[student] <= 90:
            grades[student] = "Exceeds Expectations"
        else:
            grades[student] = "Outstanding"
    return grades
    
student_grades = add_grades(student_scores, {})
# 🚨 Don't change the code below 👇
print(student_grades)

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12}
# }

# french_cities = travel_log["France"]
# travel_log["France"] = {"cities_visited": french_cities}
# travel_log["France"]["total_visits"] = 5

# print(travel_log)

travel_log = [
    {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
    },
    {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country: str, visits: int, cities: list):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
