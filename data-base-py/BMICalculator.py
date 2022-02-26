def calculate_BMI(weight, height):
    print(weight / (height * height))

def get_person_data():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    calculate_BMI(weight ,height)

get_person_data()