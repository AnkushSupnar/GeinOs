from bson.objectid import ObjectId
from django.http import JsonResponse
from askcos_site.main.globals import RetroTransformer

def template(request):
    resp = {}
    resp['request'] = dict(**request.GET)
    _id = request.GET.get('id')
    transform = RetroTransformer.lookup_id(ObjectId(_id))
    transform['_id'] = _id
    transform.pop('product_smiles')
    transform.pop('name')
    refs = transform.pop('references')
    transform['references'] = map(lambda x: x.split('-')[0], refs)
    resp['template'] = transform
    return JsonResponse(resp)