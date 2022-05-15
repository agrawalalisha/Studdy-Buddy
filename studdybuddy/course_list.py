import requests

def getCourseList():
    course_list = []
    data = requests.get('https://api.devhub.virginia.edu/v1/courses').json()
    # populates course_list with unique courses of the form: "course_mnemonic course_number"
    for course in data["class_schedules"]['records']:
        if (course[0]+" "+course[1]) not in course_list:
            course_list.append(course[0]+" "+course[1])
    return course_list
    