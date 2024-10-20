from User import *

class Service():
    def check_info(user:User):
        
        if int(user.age) < 10 or int(user.age) > 100:
            return "Siz xato yoshni kiritdingiz ❌ "
        
        elif not user.name.istitle() or user.name.isspace():
            return "Siz xato ism kiritdingiz ❌ "
        
        elif not user.surname.istitle() or user.surname.isspace():
            return "Siz xato sharif kiritdingiz ❌ "
        
        elif not user.phone.startswith('+') or len(user.phone) != 13:
            return "Siz xato nomer kiritdingiz ❌ "
        
        elif user.faculty.isspace():
            return "Siz fakultet tanlamadingiz ❌ "
        
        elif not user.isMale  and not user.IsFemale:
            return "Siz jins tanlamadingiz ❌ "
        
        elif user.region == 0:
            return "Siz viloyatni tanlamadingiz ❌ "
        
        elif user.kurs == 0:
            return "Siz kursni tanlamadingiz ❌ "
        
        else:
            if user.isMale :
                user.gender = "Erkak"
            else:
                user.gender = "Ayol"
                
            with open("LOYHA.txt", 'a+') as f:
                f.write(f"{user.name}, {user.surname}, {user.age}-yosh, {user.gender} ,{user.region}, {user.phone}, {user.faculty}, {user.kurs}-kurs \n")
            
       