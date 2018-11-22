from rest_framework import serializers
from .models import *

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('order','memberName','memberPosition','memberImageUrl')

class ClubImageUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = clubImagesUrl
        fields = ('order','url')        
        
class ClubSerializer(serializers.ModelSerializer):
    member = MemberSerializer(many=True,read_only=True)
    clubImageUrl = ClubImageUrlSerializer(many=True,read_only=True)
    
    class Meta:
        model=Club
        fields=('clubName','clubLogoUrl','clubDescription','clubWebpageUrl','member','clubImageUrl')
 
class NoticeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=ClubNotice
        fields=('noticeTitle','noticeDate','eventImageUrl','eventDescription','eventVenue','eventTime','eventDate','googleFormUrl')
               
class ClubSerializerForNotice(serializers.ModelSerializer):
    notice = NoticeSerializer(many=True,read_only=True)
    
    class Meta:
        model=Club
        fields=('clubName','clubLogoUrl','clubWebpageUrl','notice')
        

    
