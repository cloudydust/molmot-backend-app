from calendar import c
from email.policy import default
from pyexpat import model
from django.db import models
import uuid
from fcm_django.models import FCMDevice

from user.models import Member, MemberFCMDevice
# Create your models here.
from django_celery_beat.models import CrontabSchedule, PeriodicTask

class Organization(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(
        max_length=50,
        null=False,
        unique=False
    )   
    location=models.CharField(
        max_length=50,
        null=True,
        unique=False,
        blank=True
    )   
    link=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name

class Support(models.Model): 

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    bizId=models.CharField(
        verbose_name='정책 번호',
        max_length=50,
        null=True
    )   
    title=models.CharField(
        max_length=50,
        null=True,
        unique=False
    )   
    detail=models.TextField(verbose_name='상세 설명',blank=True)
    submit_link=models.URLField(blank=True,null=True,verbose_name='관련 링크',)
    organizer=models.CharField(
        verbose_name='주관사',
        max_length=50,
        null=True
    )
    start_date=models.DateTimeField(verbose_name='시작 날짜',null=True,blank=True)
    end_date=models.DateTimeField(verbose_name='마감 날짜',null=True,blank=True)
    rqutPrdCn=models.TextField(verbose_name='신청 기간',null=True,blank=True)
    plcyTpNm=models.TextField(verbose_name='정책 유형',null=True,blank=True)
    qualifications=models.TextField(verbose_name='신청 대상',null=True,blank=True)
    located_in=models.CharField(verbose_name='지역',max_length=50,null=True,unique=False,blank=True)
    hits = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return str(self.title)

    @property
    def click(self):
        self.hits +=1
        self.save()


    class Meta:
        ordering = ['-end_date']  

#분야..
class Subscribe(models.Model):

    COLORED = (    #색깔 분류
        ('pink', 'pink'),
        ('yellow', 'yellow ')
    )

    colored=models.CharField(verbose_name='색깔 분류',max_length=10,choices=COLORED,null=True)
    organizer_id=models.ForeignKey(Organization,verbose_name='관심있는 분야',null=True,on_delete=models.CASCADE)
    member_id=models.ForeignKey(Member,null=True,on_delete=models.CASCADE)

class Channel(models.Model):
    category=models.CharField(verbose_name='카테고리',max_length=50,null=True,blank=True,unique=True)
    channel_name=models.CharField(verbose_name='구독할 채널 작명',max_length=50,null=True,unique=True)
    organizer_id=models.ForeignKey(Organization,verbose_name='관련 제도',null=True,on_delete=models.CASCADE)
    member_id=models.ForeignKey(Member,null=True,on_delete=models.CASCADE)


class SupportBookMark(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    support_id=models.ForeignKey(Support,verbose_name='제도/지원금',null=True,on_delete=models.CASCADE)
    member_id=models.ForeignKey(Member,null=True,on_delete=models.CASCADE)

class SupportNotification(PeriodicTask):
    organizer_id=models.ForeignKey(Organization,blank=True,verbose_name='정부 및 기관, 주관사',null=True,on_delete=models.CASCADE)
    support_id=models.ForeignKey(Support,blank=True,verbose_name='제도/지원금',null=True,on_delete=models.CASCADE)
    user_device_info=models.ForeignKey(FCMDevice,blank=True,verbose_name='유저 디바이스 정보',null=True,on_delete=models.CASCADE)
    member_device_info=models.ForeignKey(MemberFCMDevice,blank=True,verbose_name='멤버 디바이스 정보',null=True,on_delete=models.CASCADE)
    noti_on_time=models.DateTimeField(null=True,blank=True,verbose_name='푸시알림 전송할 시간')
    #유저의 On_&_off 필터링 
    interval_time=models.IntegerField(verbose_name='인터벌 시간 설정',default=7,null=True,blank=True)
    noti_on_or_off=models.BooleanField(default=False)

    class Meta:
        verbose_name = ("SupportNotification")


class SupportScheduledNotification(models.Model):
    
    member_device_info=models.ForeignKey(MemberFCMDevice,verbose_name='멤버 디바이스 정보',null=True,on_delete=models.CASCADE)
    user_device_info=models.ForeignKey(FCMDevice,verbose_name='유저 디바이스 정보',null=True,on_delete=models.CASCADE)
    sched_noti=models.ForeignKey(SupportNotification,verbose_name='예정되어있는 알림',null=True,on_delete=models.CASCADE)
    noti_on_time=models.DateTimeField(null=True,verbose_name='푸시알림 전송할 시간')
    #유저의 On_&_off 필터링 
    noti_on_or_off=models.BooleanField(default=False)

    class Meta:
        verbose_name = ("SupportScheduledNotification")



class RecordingList(models.Model):
    
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    support_id=models.ForeignKey(Support,verbose_name='제도/지원금',null=True,on_delete=models.CASCADE)
    member_id=models.ForeignKey(Member,null=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("RecordingList")
