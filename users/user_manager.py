from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, UserManager

'''

first_name (varchar 50) null = false
last_name (varchar 50) null = false
user_name (varchar 50) null = false
password (varchar 20) null = false
is_employee (boolean) null = true
picture
age
gender
occupation
address line 1
address line 2  (optional)
phone_number
description

'''

class UserManager(BaseUserManager):
     use_in_migrations = True

     def create_user(self, email, first_name, last_name, password
                    ,is_employee, picture, age, gender
                    , occupation, adress_line_1, adress_line_2
                    , phone_number, description 
                    ):

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            is_employee = is_employee,
            picture = picture,
            age = age,
            gender = gender,
            occupation = occupation,
            adress_line_1 = adress_line_1,
            adress_line_2 = adress_line_2,
            phone_number = phone_number,
            description = description
        )
        
        user.set_password(password)
        user.save()
        return user