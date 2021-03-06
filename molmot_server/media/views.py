from django.shortcuts import render
from rest_framework import generics
from media.models import UIPhoto
from rest_framework.views import APIView
from rest_framework.response import Response

from media.serializers import UIPhotoSerializer
from rest_framework.decorators import permission_classes, authentication_classes
from django.core import serializers
from support.models import Support, SupportScheduledNotification
from support.serializers import HomeSupportSerializer, SupportSerializer,SupportNotificationSerializer,SupportNotification,HomeSupportNotificationSerializer
from user.models import Member, MemberFCMDevice


@authentication_classes([])
@permission_classes([]) 
class HomeLoadImageView(generics.ListAPIView):
    serializer_class = UIPhotoSerializer

    def get_queryset(self):
        field = self.kwargs['field']
        indexnum = self.kwargs['index']
        return UIPhoto.objects.filter(field=field,indexnum=indexnum)




@authentication_classes([])
@permission_classes([]) 
class GetHomeUIInfoView(APIView):
    def get(self,request):
        
        uiphotos=UIPhotoSerializer(UIPhoto.objects.all(),many=True)
        #3개가 없을 경우에 대한 에러 처리 
        hottag=HomeSupportSerializer(Support.objects.all().order_by('-hits')[:6],many=True)
        return Response({"hottag":hottag.data,"uiphoto":uiphotos.data})

    #알람서비스 추가되면 추가 개발예정
    def get(self,request,member_id):
        hottag=HomeSupportSerializer(Support.objects.all().order_by('-hits')[:6],many=True)
        uiphotos=UIPhotoSerializer(UIPhoto.objects.all(),many=True)
        obj=Member.objects.get(pk=member_id)
        if (obj.is_smart_recommed):
            #3개가 없을 경우에 대한 에러 처리
            alarm_list=HomeSupportNotificationSerializer(SupportNotification.objects.filter(member_device_info=MemberFCMDevice.objects.get(user=member_id)).order_by('-noti_on_time')[:3],many=True)
            print(alarm_list.data)
            #3개가 없을 경우에 대한 에러 처리 
           
            return Response({"hottag":hottag.data,"uiphoto":uiphotos.data,"alarm_list":alarm_list.data})
        else:
            return Response({"hottag":hottag.data,"uiphoto":uiphotos.data})

    
@authentication_classes([])
@permission_classes([]) 
class GetMemberhasSmartResult(APIView):

    #알람서비스 추가되면 추가 개발예정
    def get(self,request,member_id):
        obj=Member.objects.get(pk=member_id)
        return Response({"is_smart_recommed":obj.is_smart_recommed})