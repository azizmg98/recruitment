def get_skills():
    # Add at least 3 random skills for the user to select from
    skills = ["Snowboarding", "Tricking", "Shooting", "Programming", "Lifting"]
    return skills

def show_skills(skills):
    # Pretty print skills to the user
    # Write your code here
    for index, element in enumerate(skills):
        print(str(index+1)+'.', element)
    ...


def get_user_skills(skills):
    # Show the available skills and have user pick from them
    # Write your code here
    print("Please select two skills from the following list: ")
    show_skills(skills)
    skill_1 = int(input("Choose a skill by typing its' number: "))
    skill_2 = int(input("Choose a second skill by typing its' number: "))
    # user list comprehension
    #? is there a better way to pass variable from func to func
    # global applicant_skills
    applicant_skills = [skills[skill_1-1]]
    applicant_skills.append(skills[skill_2-1])
    return applicant_skills
    

def get_user_cv(skills):
    # Get the users CV from their inputs
    # Write your code here
    applicant_skills = get_user_skills(skills)
    cv = dict
    applicant_name = str(input("Please enter your name: "))
    applicant_age = int(input("Please enter your age: "))
    applicant_exp = int(input("Please enter your years of experience: "))    
    cv = {'name':applicant_name, 'age':applicant_age, 'experience': applicant_exp, 'skills':applicant_skills}
    return cv


def check_acceptance(cv, desired_skill):
    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    if (cv['age'] >= 25 and cv['age'] < 40) and (cv['experience'] > 3 ) and (desired_skill in cv['skills']):
        return True
    else:
        return False 


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the recruitment application for CODED.")
    skills = get_skills()
    cv = get_user_cv(skills)
    desired_skills = skills[2]
    

    if check_acceptance(cv, desired_skills) == True:
        print("Your application has been accepted. Welcome to the club")
    else:
        print("Your application has been rejected. We will be sure to inform you of future positions.")


if __name__ == "__main__":
    main()
