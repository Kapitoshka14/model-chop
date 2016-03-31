from datetime import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext

from purchase.models import Purchase, Product


def base(request):
    text={}
    try:
      if request.method == 'POST':
        dt=datetime.now().microsecond
        a=Purchase(number=str(dt), price=float(request.POST['ch'].replace(',','.')), status=False, body=request.POST['id'])
        a.save()
    except Exception:
      text['text']='ошибка'

    try:
      text['tov']=Product.objects.all()
      text['zak']=Purchase.objects.all()
    finally:
      return render_to_response('index.html',text,context_instance=RequestContext(request))