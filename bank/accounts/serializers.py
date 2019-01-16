from django.utils import timezone
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):

    creation_date = serializers.DateTimeField(read_only=True)

    class Meta:

        model = Account
        fields = ('id', 'owner', 'balance', 'creation_date')

    def validate(self, data):
        if data['balance'] < 0:
            raise serializers.ValidationError('The balance cannot to be negative')
        # elif data['creation_date'] != timezone.now:
        #     raise serializers.ValidationError('The creation date is auto')
        return data