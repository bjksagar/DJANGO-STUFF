from .models import Book
from rest_framework import serializers

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Book
#         fields="__all__"  #here we include all the fields of the Book Model

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=30)
    author = serializers.CharField(max_length=30)
    pub_date = serializers.DateField()

    class Meta:
        model=Book
        fields = '__all__'

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
