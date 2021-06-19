from django.core.validators import MaxLengthValidator
from rest_framework import serializers
from userProfile.models import Profile
import base64
from django.core.files.base import ContentFile
from  uuid import uuid4
from account.models import Account

class ProfileCreationSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField()
    class Meta:
        model = Profile
        fields = ['user_image','user_profession','user_phone_number','user_profile_name','user_address','user_email']
        extra_kwargs = {'user_email': {'required': True}}

    def save (self):
        user = Account.objects.get(email = self.validated_data["user_email"])
        profile = Profile(user=user,
                        user_profession  = self.validated_data["user_profession"],
                        user_phone_number  = self.validated_data["user_phone_number"],
                        user_image = self.validated_data["user_image"],
                        user_address = self.validated_data["user_address"],
                        user_profile_name = self.validated_data["user_profile_name"]
                        )
        profile.save()
        return profile

def base64_file(data, name=None):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))