from django.shortcuts import render
from .models import Composition, Configs, Work
from collections import namedtuple
import json


def configurations():
    configs = Configs.objects.all()
    config_dict = {}
    Point = namedtuple('config', ('int_val', 'float_val', 'str_val', 'bool_vale'))
    for config in configs:
        config_dict[config.variable] = Point(
            config.int_val,
            config.float_val,
            config.str_val,
            config.bool_val,
        )
    return config_dict


def comp_work(comp_major_mats, comp_minor_mats):
    work_query = Work.objects.all()
    work_dict = {}
    for work in work_query:
        work_dict[work.task] = {'minutes': work.minutes, 'people': work.people}

    work_dict['find_major']['minutes'] *= comp_major_mats
    work_dict['pull_major']['minutes'] *= comp_major_mats
    work_dict['return_major']['minutes'] *= comp_major_mats
    work_dict['weigh_major']['minutes'] *= comp_major_mats
    work_dict['weigh_minor']['minutes'] *= comp_minor_mats

    return work_dict


def calculator(request):
    comp_query = Composition.objects.order_by('-major_components')
    json_dict = {}
    for comp in comp_query:
        comp_str = 'c_' + comp.composition
        json_dict[comp_str] = {}
        json_dict[comp_str]['select_id'] = (str(comp) + '_select')
        json_dict[comp_str]['comp'] = comp.composition

        work_data = comp_work(comp.major_components, comp.minor_components)

        json_dict[comp_str]['work_data'] = work_data
    py_data = json.dumps(json_dict)
    config_dict = configurations()
    max_preweighs = config_dict['max_preweighs'].int_val + 1
    batch_count = range(max_preweighs)
    data_map = {'comp_list': comp_query,
                'batch_count': batch_count,
                'py_data': py_data
                }
    return render(request, 'preweigh_calculator/calculator.html', data_map)