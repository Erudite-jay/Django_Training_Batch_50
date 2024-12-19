from rest_framework import serializers
from.models import User

# Normal 
# class UserSerializer(serializers.Serializer):
#     username=serializers.CharField(max_length=50)
#     age=serializers.IntegerField()
#     mobile_number = serializers.CharField(max_length=10)
#     email = serializers.EmailField()

#model serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

