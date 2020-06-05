from rest_framework import serializers
from users.models import User
from adquisitions.models import Collection
from adquisitions.serializers import CollectionSerializer
import uuid
from rest_framework import permissions
class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'inpute_type' : 'password'}, write_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'profile_picture',
            'password',
            'password2',
            'age',
            'gender',
            'occupation',
            'address_line_1',
            'address_line_2',
            'phone_number',
            'description',
            'balance',
            'is_admin',
        )
  
        extra_kwargs = {
            'password' :{'write_only' : True },
        }

    def save(self):      
        user = User(
        email=self.data['email'],
        first_name = self.data['first_name'],
        last_name = self.data['last_name'],
        profile_picture= self.data['profile_picture'],
        age = self.data['age'],
        gender = self.data['gender'],
        occupation = self.data['occupation'],
        address_line_1 = self.data['address_line_1'],
        address_line_2 = self.data['address_line_2'],
        phone_number = self.data['phone_number'],
        description = self.data['description'],
        balance = self.data['balance'],
     )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'Passwords must match'})
        user.is_admin = self.data['is_admin']
        user.set_password(password)
    
        user.save() 

        return user

        # else:
        #     user = User.objects.get(pk=self.data['id'])
        #     user.profile_picture = self.validated_data['profile_picture']
        #     user.save()
        #     return user
        

        