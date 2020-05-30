from users.models import User
from authors.models import Author
from digital_books.models import Digital_Book
from django.core.files import File

dummy = User()
dummy.email = '1@1.com'
dummy.set_password('1234')
dummy.first_name = 'Amado'
dummy.last_name = 'Garcia'
dummy.age = 26
dummy.gender = 'M'
dummy.occupation = 'Student'
dummy.address_line_1 = 'Mi casa hehe'
dummy.phone_number = '12345678'
dummy.save()


amado = User()
amado.email = 'gar181469@uvg.edu.gt'
dummy.set_password('NoeDhp2020*')
amado.first_name = 'Amado'
amado.last_name = 'Garcia'
amado.age = 26
amado.gender = 'M'
amado.occupation = 'Student'
amado.address_line_1 = 'Mi casa hehe'
amado.phone_number = '12345678'
amado.save()

sara = User()
sara.email = 'zav18893@uvg.edu.gt'
sara.set_password('Anikalinda11')
sara.first_name = 'Sara'
sara.last_name = 'Zavala'
sara.age = 20
sara.gender = 'F'
sara.occupation = 'Student'
sara.address_line_1 = 'Su casa hehe'
sara.phone_number = '87654321'
sara.save()

jkrowling = Author()
jkrowling.first_name = 'Joanne'
jkrowling.last_name = 'Rowling'
jkrowling.age = 52
jkrowling.gender = 'F'
jkrowling.pseudonym = 'J.K. Rowling'
jkrowling.nationality = 'British'
jkrowling.save()

hp1 = Digital_Book()
hp1.name = 'Harry Potter and the Philosopher''s Stone'
hp1.author = jkrowling
hp1.language = 'EN'
hp1.publisher = 'Bloomsburry'
hp1.edition = 1
hp1.price = 19.99
hp1.release_date = '1994-1-1'
hp1.doi = '123-456'
hp1.cover.save('hp1-EN.jpg', File(open('./assets/hp1En.jpg', 'rb')))
hp1.save()

hp2 = Digital_Book()
hp2.name = 'Harry Potter and the Chamber of Secrets'
hp2.author = jkrowling
hp2.language = 'EN'
hp2.publisher = 'Bloomsburry'
hp2.edition = 1
hp2.price = 19.99
hp2.release_date = '1995-1-1'
hp2.doi = '789-101'
hp2.cover.save('hp2-EN.jpg', File(open('./assets/hp2En.jpg', 'rb')))
hp2.save()

hp3 = Digital_Book()
hp3.name = 'Harry Potter and the Prisioner of Azkaban'
hp3.author = jkrowling
hp3.language = 'EN'
hp3.publisher = 'Bloomsburry'
hp3.edition = 1
hp3.price = 19.99
hp3.release_date = '1996-1-1'
hp3.doi = '121-141'
hp3.cover.save('hp3-EN.jpg', File(open('./assets/hp3En.jpg', 'rb')))
hp3.save()