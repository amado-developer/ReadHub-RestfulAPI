from rest_framework import serializers
from users.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'inpute_type' : 'password'}, write_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'is_employee',
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
        )
  
        extra_kwargs = {
            'password' :{'write_only' : True },
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            is_employee = self.validated_data['is_employee'],
            profile_picture= self.data['profile_picture'],
            age = self.validated_data['age'],
            gender = self.validated_data['gender'],
            occupation = self.validated_data['occupation'],
            address_line_1 = self.validated_data['address_line_1'],
            address_line_2 = self.validated_data['address_line_2'],
            phone_number = self.validated_data['phone_number'],
            description = self.validated_data['description'],

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'Passwords must match'})
        user.set_password(password)
        user.save() 
        return user