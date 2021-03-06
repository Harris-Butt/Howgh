
from django.db.models import fields
from rest_framework import serializers
from account.models import Account


class RegistrationSerializer(serializers.ModelSerializer):


	class Meta:
		model = Account
		fields = ['email', 'username', 'password']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		account = Account(
					email=self.validated_data['email'].lower(),
					username=self.validated_data['username']
				)
		password = self.validated_data['password']
		account.set_password(password)
		account.save()
		return account

