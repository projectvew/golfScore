from django.db.models.query import QuerySet
from django.utils import dateformat,timezone
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponse
import datetime
from django.views.generic import ListView,CreateView,TemplateView
from golfScore_app.models import GolfHouseMaster,Round
from golfScore_app.forms import RoundCreateForm
# # Create your views here.
# def helloworld(request):
#     return HttpResponse('round Hello World!')
# def test(request):
#     return HttpResponse('round test')

today = datetime.datetime.today().date()

class GolfHouseListView(ListView):
    model = GolfHouseMaster
    template_name = 'round_pages/list_golfhouse.html'
    def get_context_data(self):
            disp_data = super().get_context_data()
            # page_title を追加する
            disp_data['title'] = 'hoge'
            d = timezone.now()
            dt_now = d.strftime('%Y/%m/%d %A %H:%M:%S')
            disp_data['date'] = dt_now
            
            return disp_data


class RoundCreateView(CreateView):
    form_class = RoundCreateForm
    model = Round
    template_name = 'round_pages/input_round.html'
    def get_context_data(self, **kwargs):
        

    # def get_form_kwargs(self, *args, **kwargs):
    #     kwgs = super().get_form_kwargs(*args, **kwargs)
    #     kwgs["house_id"] = self.request.GET.get("pk")
    #     return kwgs