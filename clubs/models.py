from django.db import models


# Create your models here.
class Club(models.Model):
    clubName = models.CharField(max_length=200)
    clubLogoUrl = models.CharField(max_length=200)
    clubDescription = models.TextField(max_length=400)
    clubWebpageUrl = models.CharField(max_length=200)
 #   clubImagesUrl = ArrayField(models.CharField(max_length=200), blank=True)
    class Meta:
                unique_together = ('clubName','clubWebpageUrl')
                ordering = ['clubName']   
    def __str__(self):
        return self.clubName
    
    
        
class clubImagesUrl(models.Model):
        url = models.CharField(max_length=100)
        order = models.IntegerField()
        club = models.ForeignKey(Club, related_name='clubImageUrl', on_delete=models.CASCADE)
        
        class Meta:
                unique_together = ('url','order')
                ordering = ['order']
                
        def __str__(self):
                return self.url

class Member(models.Model):
     memberName = models.CharField(max_length=100)
     order = models.IntegerField()
     memberPosition = models.CharField(max_length=100)
     memberImageUrl = models.CharField(max_length=400)
     club = models.ForeignKey(Club, related_name='member', on_delete=models.CASCADE)
     
     class Meta:
        unique_together = ('memberName', 'memberPosition', 'memberImageUrl','order')
        ordering = ['order']
     
     def __str__(self):
        return self.memberName

     
class ClubNotice(models.Model):
      club = models.ForeignKey(Club,related_name="notice",on_delete=models.CASCADE)
      noticeTitle=models.CharField(max_length=100)
      noticeDate = models.DateField(auto_now_add=True,
                                             db_index=True)
      eventImageUrl = models.CharField(max_length=200)
      eventDescription = models.TextField(max_length=400)
      eventVenue = models.CharField(max_length=100)
      eventTime = models.CharField(max_length=100)
      eventDate = models.DateField(blank=True, null=True)
      googleFormUrl=models.CharField(max_length=200, blank=True)
      
      class Meta:
        unique_together = ('noticeTitle','noticeDate')
        ordering = ['noticeDate']
     

      def __str__(self):
        return self.noticeTitle
        

#refrence
#class Album(models.Model):
#    album_name = models.CharField(max_length=100)
#    artist = models.CharField(max_length=100)
#
#class Track(models.Model):
#    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
#    order = models.IntegerField()
#    title = models.CharField(max_length=100)
#    duration = models.IntegerField()

#    class Meta:
#        unique_together = ('album', 'order')
#        ordering = ['order']

#    def __unicode__(self):
#        return '%d: %s' % (self.order, self.title)

#serializers code
#class AlbumSerializer(serializers.ModelSerializer):
#    tracks = serializers.StringRelatedField(many=True)

#    class Meta:
#        model = Album
#        fields = ('album_name', 'artist', 'tracks')

#this would serializwe
#{
#    'album_name': 'Things We Lost In The Fire',
#    'artist': 'Low',
#    'tracks': [
#        '1: Sunflower',
#        '2: Whitetail',
#        '3: Dinosaur Act',
#        ...
#    ]
#}
#

