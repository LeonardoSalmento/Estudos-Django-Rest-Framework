from profiles.models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['url', 'first_name', 'last_name', 'phone_number']