from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """Shortcut for creating serialisation objects
    - Automatic determined set of fields
    - Simple Default Implementations for the create() and update() methods

    Args:
        serializers (_type_): _description_
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']
        
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
# class SnippetSerializer(serializers.Serializer):
#     """
#     Method that initialises fields
#     """
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template':'textarea.html' })
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.

#         Args:
#             validated_data (_type_): _description_

#         Returns:
#             _type_: _description_
#         """
#         return super().create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.languages = validated_data.get('languages', instance.languages)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance