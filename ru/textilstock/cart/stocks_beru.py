import csv
import requests
import json

with open('/home/stani/Загрузки/ds_pi1.csv', newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=';')
    for row in rows:
        logisticPartnerId = row[1]
        #r = requests.get('http://lms.vs.market.yandex.net/externalApi/partners/' + logisticPartnerId)
        r = requests.get('http://lms.tst.vs.market.yandex.net/externalApi/partners/' + logisticPartnerId)
        resp = r.json()
        print(resp)


        # if(resp['status'] == 'ACTIVE' and resp['stockSyncEnabled'] == False) :
        #     print(resp['id'])

        new_body = dict()
        new_body['autoSwitchStockSyncEnabled'] = resp['autoSwitchStockSyncEnabled']
        new_body['locationId'] = resp['locationId']
        new_body['stockSyncEnabled'] = False
        new_body['stockSyncSwitchReason'] = resp['stockSyncSwitchReason']
        new_body['trackingType'] = resp['trackingType']
        new_body_json = json.dumps(new_body)

        print(new_body_json)

        headers = {
            'Content-type': 'application/json',
        }

        print(new_body)

        #
        # response = requests.put('http://lms.vs.market.yandex.net/externalApi/partners/'
        #                          + logisticPartnerId + '/settings', headers=headers, data=new_body_json)
        # response = requests.put('http://lms.tst.vs.market.yandex.net/externalApi/partners/'
        #                          + logisticPartnerId + '/settings', headers=headers, data=new_body_json)
        # print(response.json())





# {
#   "autoSwitchStockSyncEnabled": true,
#   "locationId": 0,
#   "stockSyncEnabled": true,
#   "stockSyncSwitchReason": "NEW",
#   "trackingType": "string"
# }