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

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from books.views import BookViewSet
from comments.views import CommentViewSet
from equipments.views import EquipmentViewSet
from magazines.views import MagazineViewSet
from storebranches.views import StoreBrachViewSet
from studyclassrooms.views import StudyClassrooomViewSets
from digital_books.views import digital_bookViewSet
from audio_books.views import Audio_BookViewSet
from promotions.views import PromotionViewSet
from electronicbookcollections.views import ElectronicBookCollectionViewset
from equipment_assigments.views import Equipment_AssigmentViewSet
from studyclassrooms_reservations.views import StudyClassrooms_ReservationViewSet
from authors.views import AuthorViewSet;
# from users.views import registration_view, users_view, upload_profile_picture, user_view
from users.views import UserViewset
from inventories.views import InventoryViewset
from digitalBooksPDF.views import DigitalBookPDFViewSet
from adquisitions.views import CollectionViewset
from bookloans.views import BookLoanViewSet

from rest_framework_jwt.views import (
    obtain_jwt_token, 
    refresh_jwt_token
)
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static

app_name = "users"
router = routers.DefaultRouter()
router.register(r'^books', BookViewSet)
router.register(r'^comments', CommentViewSet)
router.register(r'^equipments', EquipmentViewSet)
router.register(r'^magazines', MagazineViewSet)
router.register(r'^storeBranches',StoreBrachViewSet)
router.register(r'^digital-books', digital_bookViewSet)
router.register(r'^studyclassrooms', StudyClassrooomViewSets)
router.register(r'^audio-books', Audio_BookViewSet)
router.register(r'^promotions', PromotionViewSet)
router.register(r'^equipment-assigments', Equipment_AssigmentViewSet)
router.register(r'^studyclassrooms-reservations', StudyClassrooms_ReservationViewSet)
router.register(r'^authors',AuthorViewSet)
router.register(r'^inventory', InventoryViewset)
router.register(r'^collections' ,CollectionViewset)
router.register(r'^users', UserViewset)
router.register(r'^digital-book-pdf', DigitalBookPDFViewSet)
router.register(r'^books-loan', BookLoanViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^api/v1/register', registration_view, name="register"),
    # url(r'^api/v1/users/$', users_view, name="users"),
    # url(r'^api/v1/users/(?P<pk>\d+)/$', user_view, name="user"),
    # url(r'^api/v1/users/upload-profile-picture/(?P<pk>\d+)/$', upload_profile_picture, name="profile-pic"),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/v1/token-auth/', obtain_jwt_token),
    url(r'^api/v1/token-refresh/', refresh_jwt_token),
    url(r'^api/v1/', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

