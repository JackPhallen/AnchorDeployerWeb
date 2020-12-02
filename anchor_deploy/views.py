import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .deployer import deploy, getip, check

# curl -d "clusterName=test&region=test&maxNodes=test&minNodes=test&projectName=test" http://127.0.0.1:8000/anchor/deploy


def _decode(body):
    body_unicode = body.decode('utf-8')
    return json.loads(body_unicode)


@csrf_exempt
def deploy_view(request):
    post_data = _decode(request.body)
    result = deploy(post_data['clusterName'], post_data['region'], str(post_data['maxNodes']),
                    str(post_data['minNodes']), post_data['projectName'])
    data = {}
    data['success'] = result
    data_json = json.dumps(data)
    return HttpResponse(data_json, content_type='application/json')


@csrf_exempt
def getip_view(request):
    post_data = _decode(request.body)
    ip = getip(post_data['clusterName'])
    data = {}
    data['ip'] = ip
    data_json = json.dumps(data)
    return HttpResponse(data_json, content_type='application/json')


@csrf_exempt
def check_view(request):
    post_data = _decode(request.body)
    result = check(post_data['clusterName'], post_data['region'], str(post_data['maxNodes']),
                    str(post_data['minNodes']), post_data['projectName'])
    data_json = json.dumps(result)
    return HttpResponse(data_json, content_type='application/json')
