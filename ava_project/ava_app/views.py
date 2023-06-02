from django.shortcuts import render

from django.http import JsonResponse


# import sys
# path_root = Path(__file__).parents[2]
# sys.path.append(str(path_root))
# print(sys.path)
from .ava_src.ava import Ava

def get_ava(request, number):
    result = str(number)

    min_height = 0
    max_height = 6
    r = 3
    s = 1
    ava = Ava(37,-82,r,s,min_height,max_height)
    ava.calc_viewsheds()

    areas = [fam.total_vs_area for fam in ava.fams]
    return JsonResponse({'result': result})
