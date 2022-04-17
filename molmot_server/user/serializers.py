from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate
from rest_auth.registration.serializers import RegisterSerializer

from user.models import *

# JWT 사용을 위한 설정
JWT_DECODE_HANDLER=api_settings.JWT_DECODE_HANDLER
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

# 회원가입
class CustomRegisterSerializer(RegisterSerializer):
    username= models.CharField(
        max_length=50,
        null=False,
        unique=False
    )  
    age = models.IntegerField(
        null=True,
        blank=True
    )  
    gender= models.CharField(blank=True, default='N',max_length=1, null=True)
    birth=models.CharField(max_length=10,null=True,blank=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data() # username, password, email이 디폴트
        data_dict['age'] = self.validated_data.get('age', '')
        data_dict['gender'] = self.validated_data.get('gender', '')
        data_dict['birth'] = self.validated_data.get('birth', '')

        return data_dict

# 로그인 
class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password", None)
        # 사용자 아이디와 비밀번호로 로그인 구현(<-> 사용자 아이디 대신 이메일로도 가능)
        user = authenticate(email=email, password=password)

        if user is None:
            return {'email': 'None'}
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            
            update_last_login(None, user)

        except Member.DoesNotExist:
            raise serializers.ValidationError(
                'User with given username and password does not exist'
            )
        return {
            'email': user.email,
            'token': jwt_token
        }
        
# 사용자 정보 추출
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('email', 'age', 'gender', 'birth')