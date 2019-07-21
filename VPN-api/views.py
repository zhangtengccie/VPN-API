# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import xmltodict
import json
import requests
from django.http import HttpResponse

# Create your views here.
def vpn_permission(request):
    if request.method == 'GET':
        id = request.GET.get('id', False)
        data = dict()
        if id:
            params = {
                'id': id,
            }
            res = requests.get('http://10.27.35.11:10000/GetInfoByEmployeeID', params=params)
            res_json = res.json()
            if res_json['Msg'] is None:
                name = res_json['Data']['sAMAccountName']
                url = 'https://10.168.66.103/api/?type=export&category=configuration&REST_API_TOKEN=1933743768'

                header = {"Authorization": "Basic YXBpYWRtaW46QXV0b2hvbWUxNjgkJDExMjg="}
                vpn_res_xml = requests.get(url=url, headers=header, verify=False).text
                vpn_res_json = xmltodict.parse(vpn_res_xml)
                global_protect = vpn_res_json['config']['devices']['entry']['vsys']['entry']['global-protect']
                client_config = global_protect['global-protect-portal']['entry'][1]['client-config']
                member = client_config['configs']['entry']['source-user']['member']
                print member
                # member = vpn_res_json['config']['devices']['entry']['vsys']['entry']['global-protect']['global-protect-portal']['entry'][1]['client-config']['configs']['entry']['source-user']['member']
                if name in member:
                    data = {
                        'data': True,
                        'msg': '',
                    }
                else:
                    data = {
                        'data': False,
                        'msg': '{}({}) hava not HK-VPN permission'.format(name, id),
                    }
            else:
                data = {
                    'data': False,
                    'msg': res_json['Msg'],
                }
        else:
            data = {
                'data': False,
                'msg': '缺少参数工号',

            }
        return HttpResponse(json.dumps(data), content_type="application/json")
