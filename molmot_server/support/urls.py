from django.shortcuts import render
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

from support import views



#ViewSet을 이용한 라우팅 방식 이용 
router = DefaultRouter()
router.register('support-notification', views.SupportNotificationViewSet)
router.register('subscribe', views.SubscribeViewSet)
router.register('channel', views.ChannelViewSet)


urlpatterns = [
    path('support-info-view/<uuid:support_id>/',SupportInfoView.as_view()),
    path('support-filter-view/',SupportFilterInfoView.as_view()),
    path('subscribe-info-view/<uuid:member_id>/',SubscribeInfoView.as_view()),

    
    
]


urlpatterns += router.urls