from ssl import MemoryBIO
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
    username = None
    phone_number = models.IntegerField(
        null=True,
        blank=True
    )  



    def get_cleaned_data(self):
        return {
            "password1": self.validated_data.get("password1", ""),
            "phone_number": self.validated_data.get("phone_number", ""),
            "email": self.validated_data.get("email", ""),
        }

# 로그인 
class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password", None)
        fcm_token = data.get("token", None)
        print(data)
        # 사용자 아이디와 비밀번호로 로그인 구현(<-> 사용자 아이디 대신 이메일로도 가능)

        user = authenticate(email=email, password=password)

        member_obj=Member.objects.get(email=email)

        if user is None:
            return {'email': 'None'}
        
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            if (member_obj.last_login==None):
                #로그인 업데이트 
                #update_last_login(None, user)
                return {
                    'email': user.email,
                    'token': jwt_token,
                    'logined':False
                }

            else:
                if (email=="heejeong@gmail.com"):
                    member_obj.last_login=None
                    member_obj.save()
                else:
                    update_last_login(None, user)
        except Member.DoesNotExist:
            raise serializers.ValidationError(
                'User with given username and password does not exist'
            )
        return {
            'email': user.email,
            'token': jwt_token,
            'logined':True
        }
        
# 사용자 정보 추출
class UserSerializer(serializers.ModelSerializer):
    uuid=serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ('uuid','email','phone_number','username')
    
    def get_uuid(self,data):
        try:
            obj=Member.objects.get(email=data['email'])
            return obj.uuid
        except:
            return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('uuid','email', 'username','nickname','age', 'gender', 'birth','colleage','colleage_locatedin','address','city_address','zipcode','phone_number','privacy_agreement')