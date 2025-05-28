from rest_framework import serializers
from articles.models import Article
from favourites.models import Favourite
from ratings.models import Rating


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    favourite_id = serializers.SerializerMethodField()
    favourites_count = serializers.ReadOnlyField()
    rating_id = serializers.SerializerMethodField()
    ratings_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):

        if value is None or value == '':
            return value

        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')

        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_favourite_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            favourite = Favourite.objects.filter(
                owner=user, article=obj
            ).first()
            return favourite.id if favourite else None
        return None

    def get_rating_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            rating = Rating.objects.filter(
                owner=user, article=obj
            ).first()
            return rating.id if rating else None
        return None

    class Meta:
        model = Article
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'created_on', 'updated_on', 'publisher', 'subject',
            'title', 'link',  'image', 'body', 'favourite_id',
            'favourites_count', 'rating_id', 'ratings_count',
            'comments_count'
        ]
