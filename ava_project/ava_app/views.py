from django.shortcuts import render
from django.http import JsonResponse


from .ava_src.ava import Ava

# Url that works: http://127.0.0.1:8000/api/get_ava/?longitude=5.0&latitude=5.0&radius=5.0&resolution=1&minimum_height=1&maximum_height=2

def get_ava(request):

    longitude = request.GET.get('longitude')
    latitude = request.GET.get('latitude')
    radius = request.GET.get('radius')
    resolution = request.GET.get('resolution')
    minimum_height = request.GET.get('minimum_height')
    maximum_height = request.GET.get('maximum_height')

    if longitude is None:
        return JsonResponse({'error': 'Please provide a longitude value'}, status=400)
    if latitude is None:
        return JsonResponse({'error': 'Please provide a latitude value'}, status=400)
    if radius is None:
        return JsonResponse({'error': 'Please provide a radius value'}, status=400)
    if resolution is None:
        return JsonResponse({'error': 'Please provide a resolution value'}, status=400)
    if minimum_height is None:
        return JsonResponse({'error': 'Please provide a minimum height value'}, status=400)
    
    try:
        longitude = float(longitude)
    except ValueError:
        return JsonResponse({'error': 'Longitude value must be a valid float'}, status=400)
    if longitude > 180.0 or longitude < -180.0:
        return JsonResponse({'error': 'Longitude value must be between -180.0 and 180.0'}, status=400)
    
    try:
        latitude = float(latitude)
    except ValueError:
        return JsonResponse({'error': 'Latitude value must be a valid float'}, status=400)
    if latitude > 180.0 or latitude < -180.0:
        return JsonResponse({'error': 'Latitude value must be between -90.0 and 90.0'}, status=400)
    
    try:
        radius = float(radius)
    except ValueError:
        return JsonResponse({'error': 'radius value must be a valid float'}, status=400)
    if radius < .1:
        return JsonResponse({'error': 'radius value must be greater than .1 kilometers'}, status=400)
    
    try:
        resolution = float(resolution)
    except ValueError:
        return JsonResponse({'error': 'resolution value must be a valid float'}, status=400)
    if resolution < .001:
        return JsonResponse({'error': 'resolution value must be between greater than .001 kilometers'}, status=400)
    if radius%resolution != 0:
        return JsonResponse({'error': 'radius / resolution must be an integer'}, status=400)
    
    try:
        minimum_height = int(minimum_height)
    except ValueError:
        return JsonResponse({'error': 'min_height value must be a valid float'}, status=400)
    if minimum_height < 0:
        return JsonResponse({'error': 'min_height value must be greater than 0 meters'}, status=400)
    

    if maximum_height is None:
        maximum_height = minimum_height
    try:
        maximum_height = int(maximum_height)
    except ValueError:
        return JsonResponse({'error': 'max_height value must be a valid float'}, status=400)
    if maximum_height < 0:
        return JsonResponse({'error': 'maximum_height value must be greater than 0 meters'}, status=400)
    if maximum_height < minimum_height:
        return JsonResponse({'error': 'maximum_height value must be greater than min height value'}, status=400)
    
    print(request)
    result = "hello world"

    ava = Ava(longitude,latitude,radius,resolution,minimum_height,maximum_height)
    ava.calc_viewsheds()

    areas = [fam.total_vs_area for fam in ava.fams]

    response = ava.get_response()
    print(len(ava.fams[0].graph.get_new_coords()))
    return JsonResponse(response)
