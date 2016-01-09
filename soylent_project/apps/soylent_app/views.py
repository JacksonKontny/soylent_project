from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# from soylent_project.apps.data.sr27.utils import table
from soylent_project.apps.soylent_app.models import FdGroup, FoodDes, NutData,\
        NutrDef, Weight, FoodPrice 
import json


# Create your views here.
class Home(View):
    def get(self, request):
        # query_result = FoodDes.objects.filter(long_desc__icontains='STRAW')[:10]
        # foods_list = map(lambda x: x.long_desc, query_result)
        # context = {'foods_list': foods_list}
        context = {'foods_list': []}
        return render(request,
                      'soylent_app/home.html',
                      context)

        
class FoodsAPI(View):
    def get(self, request):
        if request.is_ajax():
            q = request.GET.get('food_str', '')
            foods = FoodDes.objects\
                    .filter(long_desc__icontains=q)\
                    .filter(prices__isnull=False)
            results = []
            for food in foods:
                a = food.prices.all()[0]
                food_json = {}
                food_json['id'] = food.ndb_no
                food_json['label'] = food.long_desc
                food_json['value'] = food.long_desc
                food_json['price'] = food.prices.all()[0].cents
                results.append(food_json)
            data = json.dumps(results)
        else:
            data = 'fail'
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)

class NutrientsAPI(View):
    def get(self, request):
        if request.is_ajax():
            ndb_no = request.GET.get('ndb_no', '')
            nutrient_data = FoodDes.objects\
                    .filter(ndb_no=ndb_no).all()[0].nutrients.all()
            requirements={"Potassium, K": 4700,
                          "Calcium, Ca": 1000}
            results = []
            units = {}
            for nutrient in nutrient_data:
                nutr_desc = nutrient.nutr_no.nutrdesc
                if nutr_desc in requirements:
                    nutrient_json = {}
                    nutrient_json['name'] = nutr_desc
                    nutrient_json['value'] = round(
                            float(nutrient.nutr_val) / requirements[nutr_desc],
                            3)
                    results.append(nutrient_json)
                    units[nutr_desc] = nutrient.nutr_no.units
            json_dump = json.dumps(results)
            print json_dump
            return HttpResponse(json_dump, 'application/json')
