"""ReadHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from books.views import BookViewSet
<<<<<<< HEAD
from comments.views import CommentViewSet
from equipments.views import EquipmentViewSet
from magazines.views import MagazineViewSet
from storebranches.views import StoreBrachViewSet
from studyclassrooms.views import StudyClassrooomViewSets
from digital_books.views import digital_bookViewSet
from audio_books.views import Audio_BookViewSet
from promotions.views import PromotionViewSet
from equipment_assigments.views import Equipment_AssigmentViewSet
from studyclassrooms_reservations.views import StudyClassrooms_ReservationViewSet
=======
from users.views import RegistrationViewSet
from rest_framework_jwt.views import (
    obtain_jwt_token, 
    refresh_jwt_token
)
>>>>>>> 8a1d7a51a278dfa293e689b43fdbcdb7c18a8e1d

app_name = "users"
router = routers.DefaultRouter()
router.register(r'^Books', BookViewSet)
<<<<<<< HEAD
router.register(r'^Comments', CommentViewSet)
router.register(r'^Equipments', EquipmentViewSet)
router.register(r'^Magazines', MagazineViewSet)
router.register(r'^StoreBranches',StoreBrachViewSet)
router.register(r'^Digital_Books', digital_bookViewSet)
router.register(r'^StudyClassrooms', StudyClassrooomViewSets)
router.register(r'^Audio_Books', Audio_BookViewSet)
router.register(r'^Promotions', PromotionViewSet)
router.register(r'^Equipment_Assigments', Equipment_AssigmentViewSet)
router.register(r'^StudyClassrooms_Reservations', StudyClassrooms_ReservationViewSet)


=======
router.register(r'^Register', RegistrationViewSet)
>>>>>>> 8a1d7a51a278dfa293e689b43fdbcdb7c18a8e1d

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/token-auth/', obtain_jwt_token),

    url(r'^api/token-refresh/', refresh_jwt_token),
    url(r'^api/v1/', include(router.urls)),
]
