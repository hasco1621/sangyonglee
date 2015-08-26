from django.shortcuts import render
from attendence.models import Attendence #테이블 모델 명
from django.db.models import Count
from django.db.models import Avg
from django.db.models import Max
from django.db.models import Sum

def index(request):
    attend_list = Attendence.objects.all()
    return render(request, 'attend/index.html', {
            'attend_list':attend_list
        })
# Create your views here.
