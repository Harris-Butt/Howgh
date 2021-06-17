from account.api.serializers import RegistrationSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from account.models import Account





@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def registration_view(request):
	if request.method == 'POST':
		data = {}
		email = request.data.get('email', '0').lower()
		if validate_email(email) != None:
			data['error_message'] = 'That email is already in use.'
			data['response'] = 'Error'
			data['error'] = "true"
			return Response(data)

		username = request.data.get('username', '0')
		if validate_username(username) != None:
			data['error_message'] = 'That username is already in use.'
			data['response'] = 'Error'
			data['error'] = "true"
			return Response(data)

		serializer = RegistrationSerializer(data=request.data)
		
		if serializer.is_valid():
			account = serializer.save()
			data["error"] = 'false'
			data['success_message'] = 'successfully registered new user.'
			data['email'] = account.email
			data['username'] = account.username
			data['pk'] = account.pk
		else:
			data = serializer.errors
		return Response(data)

def validate_email(email):
	print("validate_email")
	try:
		account = Account.objects.get(email=email)
	except Account.DoesNotExist:
		return None
	if account != None:
		return email

def validate_username(username):
	account = None
	try:
		account = Account.objects.get(username=username)
	except Account.DoesNotExist:
		return None
	if account != None:
		return username

def validate_password(user_email,user_password):
	account = None
	account = Account.objects.get(email=user_email)
	print(f'printing account in validate password {account}')
	account_password = check_password(user_password,account.password)
	if account_password == False:
		account = None
	if account != None:
		print(user_password)
		return user_password

@api_view(['POST', ])
def login_view(request):
	if request.method == 'POST':
		authenticated_email = None
		authenticated_password = None
		data = {}
		email = request.data.get('email', '0').lower()
		print(email)
		authenticated_email = validate_email(email)
		print(authenticated_email)
		if  authenticated_email == None:
			data['error_message'] = 'Email or password does not match'
			data['error'] = "true"
			return Response(data)
		user_password = request.data.get('password', '0')
		authenticated_password = validate_password(authenticated_email,user_password)
		if authenticated_password == None:
			data['error_message'] = 'Email or password does not match'
			data['error'] = "true"
			return Response(data)

		if authenticated_email != None and authenticated_password != None:
			data["success_message"] = "user successfully login"
			data['error'] = "false"
			return Response(data)
		return Response(data)


