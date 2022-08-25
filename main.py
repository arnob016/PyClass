

class Information:
    
    def __init__(self, name, id, section, email):
        self.name = name
        self.id = id
        self.section = section
        self.email = email
no=1

link= []
for i in range(no):
    link.append(Information(input(f"Student no {i}\n Enter Your Name: "),input("Enter Student ID: "),input("Enter Section: "),input("Enter your email: ")))
    
for s in range(no):
    print(f"Student {s}'s student ID is", link[s].id,"\n\
        His name is", link[s].name,"\n\
            He is a student of",link[s].section,"\n\
                section and his email is",)#link.email)