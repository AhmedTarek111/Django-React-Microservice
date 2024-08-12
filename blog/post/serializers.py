from rest_framework import serializers
from .models import Post , Comments , Postlikes

class PostSerialzer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id','author','title','content','puplish_date']
        
        def get_total_likes(self,obj):
            total_likes = Postlikes.objects.filter(post = obj).count()
            return total_likes
        
        def get_total_comments(self,obj):
            total_comments = Comments.objects.filter(post = obj).count()
            return total_comments 
        
class PostLikesSerializer(serializers.Modelesrializer):
    class Meta:
        model = Postlikes
        fields = ['id','post','user_id']
        
class CommentsSerialzer(serializers.Modelserializer):
    class Meta:
        model = Comments
        fields = ['id','post','content','user_id','puplish_date']
        