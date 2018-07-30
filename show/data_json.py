from django.forms.models import model_to_dict
from . import models
import json


def get_json():
    tklist = models.Rent12.objects.all()

    json_list = []

    for info in tklist:
        json_dict = model_to_dict(info)
        json_list.append(json_dict)

    # print(json_list)

    # f = open('G:/project/showit/show/temp_files/data.json', 'w', encoding='utf-8')
    f = open('F:/project/showit/show/temp_files/data.json', 'w', encoding='utf-8')
    jstr = json.dumps(json_list, ensure_ascii=False, indent=4)
    f.write(jstr)
    f.close()

    return json_list

def error_json():
    wor_infos = models.Rent12.objects.raw('select * from rent.rent_12 where (abs(rent_money-pred_money)/rent_money)>1')

    json_list = []

    for info in wor_infos:
        json_dict = model_to_dict(info)
        json_list.append(json_dict)

    # print(json_list)

    # f = open('G:/project/showit/show/temp_files/err_data.json', 'w', encoding='utf-8')
    f = open('F:/project/showit/show/temp_files/err_data.json', 'w', encoding='utf-8')
    jstr = json.dumps(json_list, ensure_ascii=False, indent=4)
    f.write(jstr)
    f.close()

    return json_list

