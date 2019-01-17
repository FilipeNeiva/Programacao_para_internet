from django.utils import timezone
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):

    creation_date = serializers.DateTimeField(allow_null=True)

    class Meta:

        model = Account
        fields = ('id', 'owner', 'balance', 'creation_date')


    def validate_balance(self, balance):
        if balance < 0:
            raise serializers.ValidationError('The balance cannot to be negative')

        return balance

    def validate_creation_date(self, creation_date):
        if creation_date:
            raise serializers.ValidationError('The creation date is auto')

        return timezone.now()
