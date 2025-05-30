from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    def create(self, validated_data):
        author = Author.objects.create(**validated_data)
        return author

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name",
            instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name",
            instance.last_name
        )
        instance.pseudonym = validated_data.get(
            "pseudonym",
            instance.pseudonym
        )
        instance.age = validated_data.get(
            "age",
            instance.age
        )
        instance.retired = validated_data.get(
            "retired",
            instance.retired
        )
        instance.save()
        return instance
