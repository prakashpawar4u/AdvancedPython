# import requests
#
# url_events = 'https://10.10.15.10/cms-service/webapi/apiservice/inventory/v1/event_alarm'
# url_virtual_netw_func = 'https://10.10.15.10/cms-service/webapi/data/nf_config?ns=-1'
# url_vnf_component = "https://10.10.15.10/cms-service/webapi/cmsManageService/getData/vnfc_config?ns=-1"
# res = requests.get(url_vnf_component, verify=False,
#                    auth=('admin', 'Ph03nix5parr0w!'),
#                    headers={'Content-Type': 'application/json', 'apiInvokerId': '5GbAm'}, timeout=10)
# print(res.status_code)
# print(res.json())


import requests

url_events = 'https://10.10.15.10/cms-service/webapi/apiservice/inventory/v1/event_alarm'
url_virtual_netw_func = 'https://10.10.15.10/cms-service/webapi/data/nf_config?ns=-1'
url_vnf_component = "https://10.10.15.10/cms-service/webapi/cmsManageService/getData/vnfc_config?ns=-1"
cell_status = "https://10.10.15.10:10443/cms-service/webapi/cmsManageService/getData/cell_status_view"
cell_status_2 = "https://10.10.83.50/cms-service/webapi/cmsManageService/getData/cell_status_view"
new = "https://10.10.15.10:10443/cms-service/webapi/cmsManageService/getData/cu_inventory"
cu_in ="https://10.10.15.10/cms-service/webapi/cmsManageService/getData/cu_inventory"
res = requests.get(cell_status, verify=False,
                   auth=('admin', 'Ph03nix5parr0w!'),
                   headers={'Content-Type': 'application/json', 'apiInvokerId': 'S3M2G'}, timeout=20)
print(res.status_code)
#print(res.json())
# print(len(res.json()['content'])) 5GbAm cED9p 9H8cm  apiInvokerId: 'MYUPu'

resp_url = requests.get(url_virtual_netw_func, verify=False,
                   auth=('admin', 'Ph03nix5parr0w!'),
                   headers={'Content-Type': 'application/json', 'apiInvokerId': 'S3M2G'}, timeout=20)
print("URL evnts",resp_url.json() )