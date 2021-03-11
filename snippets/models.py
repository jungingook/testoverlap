from django.db import models							
from django.utils import timezone

##########################
# 유저
##########################

class User(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    userID = models.CharField(max_length=30, null=False)
    userPW = models.CharField(max_length=500, null=False)
    
    class Meta:
        db_table = "User"
        # 유저 테이블
    def __str__(self):
        return self.userID
    def save(self, *args, **kwargs):
        # 만약 지금껏 생성된적 없는 id라면 created 자동 생성
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Users, self).save(*args, **kwargs)