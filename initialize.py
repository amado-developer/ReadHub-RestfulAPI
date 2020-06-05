from users.models import User
from authors.models import Author
from magazines.models import Magazine
from equipments.models import Equipment
from digital_books.models import Digital_Book
from equipments.models import Equipment
from digitalBooksPDF.models import DigitalBookPDF
from magazinesPDF.models import MagazinesPDF
from django.core.files import File

###ADMIN###
admin = User()
admin.email = 'admin@readhub.com'
admin.set_password('adminRH33')
admin.first_name = 'Admin'
admin.last_name = 'Root'
admin.age = 100
admin.gender = 'U'
admin.occupation = 'Admin'
admin.address_line_1 = 'Admin'
admin.phone_number = 'Admin'
admin.is_admin = True
admin.save()

###USERS####
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


###AUTHORS###
jkrowling = Author()
jkrowling.first_name = 'Joanne'
jkrowling.last_name = 'Rowling'
jkrowling.age = 52
jkrowling.gender = 'F'
jkrowling.pseudonym = 'J.K. Rowling'
jkrowling.nationality = 'British'
jkrowling.save()

cslewis = Author()
cslewis.first_name = 'Clive'
cslewis.last_name = 'Lewis'
cslewis.age = 0
cslewis.gender = 'M'
cslewis.pseudonym = 'C.S. Lewis'
cslewis.nationality = 'British'
cslewis.save()


###BOOKS###
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
hp3.doi = '121-241'
hp3.cover.save('hp3-EN.jpg', File(open('./assets/hp3En.jpg', 'rb')))
hp3.save()

narnia1 = Digital_Book()
hp3.name = 'The Chronicles of Narnia 1'
hp3.author = cslewis
hp3.language = 'EN'
hp3.publisher = 'Bloomsburry'
hp3.edition = 3
hp3.price = 12
hp3.release_date = '1978-1-1'
hp3.doi = '821-234'
hp3.cover.save('narnia1.jpg', File(open('./assets/narnia1.jpg', 'rb')))
hp3.save()

###Magazines###
ariana = Magazine()
ariana.name = 'Girlfriend'
ariana.author = 'issue'
ariana.volume = 3
ariana.release_date = '2018-9-9'
ariana.number = 2
ariana.cover.save('ariana.jpg', File(open('./assets/ariana.jpg', 'rb')))
ariana.price = 15
ariana.save()

victoria = Magazine()
victoria.name = 'Girl''s Life Magazine'
victoria.author = 'GL'
victoria.volume = 2
victoria.release_date = '2019-3-27'
victoria.number = 8
victoria.cover.save('victoria.jpg', File(open('./assets/victoria.jpg', 'rb')))
victoria.price = 10
victoria.save()

liz = Magazine()
liz.name = 'Bella'
liz.author = 'Josh Reed'
liz.volume = 126
liz.release_date = '2019-03-27'
liz.number = 1
liz.cover.save('liz.jpg', File(open('./assets/liz.jpg', 'rb')))
liz.price = 23.99
liz.save()

#Equipment
headphone = Equipment()
headphone.name = 'Headphone'
headphone.type = 'Audio'
headphone.quantity = 30

projector = Equipment()
projector.name = 'Projector'
projector.type = 'Video'
projector.quantity = 10

ipad = Equipment()
ipad.name = 'iPad'
ipad.type = 'Electronic'
ipad.quantity = 8

#BooksPDF
hp1PDF =  DigitalBookPDF()
hp1PDF.book = hp1
hp1PDF.pdf.save('hp1.pdf', File(open('./assets/hp1.pdf', 'rb')))

hp2PDF =  DigitalBookPDF()
hp2PDF.book = hp1
hp2PDF.pdf.save('hp2.pdf', File(open('./assets/hp2.pdf', 'rb')))

hp3PDF =  DigitalBookPDF()
hp3PDF.book = hp1
hp3PDF.pdf.save('hp3.pdf', File(open('./assets/hp3.pdf', 'rb')))

narnia1PDF =  DigitalBookPDF()
narnia1PDF.book = hp1
narnia1PDF.pdf.save('narnia1.pdf', File(open('./assets/narnia1.pdf', 'rb')))

#MagazinePDF
m1 =  MagazinesPDF()
m1.magazine = ariana
m1.pdf.save('No_45.pdf', File(open('./assets/No_45.pdf', 'rb')))

m2 =  MagazinesPDF()
m2.magazine = ariana
m2.pdf.save('No_46.pdf', File(open('./assets/No_46.pdf', 'rb')))

m3 =  MagazinesPDF()
m3.magazine = ariana
m3.pdf.save('No_48.pdf', File(open('./assets/No_48.pdf', 'rb')))