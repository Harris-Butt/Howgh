from userProfile.api.serializers import ProfileCreationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from userProfile.models import Profile
import base64
from django.core.files.base import ContentFile
from  uuid import uuid4
import json
@api_view(['POST', ])
def create(request):
    if request.method == "POST":
        data = {}
        user_image = request.data.get('user_image','0')
        user_image = base64_to_image(user_image)
        name = request.data.get('user_profile_name','0')
        email = request.data.get('user_email','0')
        user_profession = request.data.get('user_profession','0')
        address = request.data.get('user_address','0')
        user_phone_number = request.data.get('user_phone_number','0')

        serializer = ProfileCreationSerializer(data={"user_image":user_image,"user_profile_name":name,"user_email":email,"user_phone_number":user_phone_number,"user_profession":user_profession,"user_address":address})
        if serializer.is_valid():
            profile = serializer.save()
            data["error"] = 'false'
            data['success_message'] = 'Profile is successfully created.'
            data["user_profile_name"] = name
            data["user_image"] = profile.user_image.url
            data["user_profession"] = user_profession
            data["user_address"] = address
            data["user_phone_number"] = user_phone_number
            return Response(data)
        else:
            data["error"] = "true"
            data ["error_message"] = serializer.errors

            return Response(data)
import base64
def base64_to_image(base64_string):
    format, imgstr = base64_string.split(';base64,')
    ext = format.split('/')[-1]
    return ContentFile(base64.b64decode(imgstr), name=uuid4().hex + "." + ext)