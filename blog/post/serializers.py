from rest_framework import serializers
from .models import Post , Comments , Postlikes

class PostSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','author','title','content','puplish_date']
        
class PostLikesSerializer(serializers.Modelesrializer):
    class Meta:
        model = Postlikes
        fields = ['id','post','user_id']
        
class CommentsSerialzer(serializers.Modelserializer):
    class Meta:
        model = Comments
        fields = ['id','post','content','user_id','puplish_date']