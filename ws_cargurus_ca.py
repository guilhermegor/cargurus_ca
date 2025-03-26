import requests
import os
from getpass import getuser
from typing import Dict, Any
from datetime import datetime
from plugins.parse_json import JsonFiles


class CarGurusCa:

  def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder created: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")

  def get_infos_mode_1(self, pg_number: int) -> Dict[str, Any]:
    url = f"https://www.cargurus.ca/Cars/searchPage.action?searchId=dca251a8-712e-4862-8b3e-375f112d5a4c&zip=H3C&distance=100&sourceContext=cargurus&inventorySearchWidgetType=AUTO&sortDir=ASC&sortType=DEAL_SCORE&srpVariation=SPT_PAGE&isDeliveryEnabled=true&spt=spt-used-cars&nonShippableBaseline=0&pageReceipt=eyJwYWdlQWxpZ25tZW50IjpbMjAsMjNdLCJzZWVuU3BvbnNvcmVkTGlzdGluZ0lkcyI6WzQxMTkyNzU0OCw0MDMxMDkzMTcsNDA4NzMzMDcxLDQwODA5MTg0NV19&pageNumber={pg_number}&filtersModified=true"
    payload = {}
    headers = {
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9,pt;q=0.8,es;q=0.7',
      'priority': 'u=1, i',
      'referer': 'https://www.cargurus.ca/Cars/spt-used-cars?px8324=p2&cgcid=2422&cgagid=1220178&sourceContext=cargurus&ax8324=174346144&type=GoogleAdWordsSearch&kw=app%20guru%20car&matchtype=b&ad=707898134621&placement=&networktype=g&device=c&devicemodel=&adposition=&physloc=9000411&intloc=&aceid=&cid=250456629&agid=17640177909&tgtid=kwd-783049272393&fid=&gad_source=1&gclid=Cj0KCQjwqIm_BhDnARIsAKBYcmtgCT9c8wE9dKKwV_FfnLFRSdcIQCwrm7k8Sio_nHkLpXog2domC5kaAnoDEALw_wcB',
      'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
      'Cookie': 'CGSC=1742952612.714.168.820988|cede558290b18df1205c443781ccaf5a; JSESSIONID=63EC96CDBF7EF3F51C4FF367BE1ADC11.www; pId=p2; adEx=px8324%3Dp2%26sourceContext%3Dcargurus%26ax8324%3D174346144%26kw%3Dapp%2Bguru%2Bcar%26matchtype%3Db%26ad%3D707898134621%26networktype%3Dg%26cid%3D250456629%26agid%3D17640177909%26tgtid%3Dkwd-783049272393%26clTi%3D2025-03-25; adId=174346144; CarGurusUserT=8RTH-91.245.254.213.1742952611717; cg-ssid=a6bb4e2ef9855b27aa25a8f43571c71e71318eeaf365835fc3945211871ef6f5; _sp_ses.8f67=*; sp-nuid=7e9d750d-ceeb-4ac1-9689-15e85eaefa8c; _gid=GA1.2.1468614603.1742952539; _li_dcdm_c=.cargurus.ca; _lc2_fpi=9f64978cf00e--01jq81290e3ckkxfytttzps4rb; _lc2_fpi_meta=%7B%22w%22%3A1742952539150%7D; _pubcid=d0464369-6b87-4b8a-9a0b-5f5ce495f771; _pubcid_cst=zix7LPQsHA%3D%3D; _gcl_gs=2.1.k1$i1742952532$u18428203; _gcl_au=1.1.175654497.1742952539; FPID=FPID2.2.nCMVxfxPnD9wHWYG5MoqWcp47uXwA%2F5wuixMmY20kPY%3D.1742952539; FPLC=vUx8wjSPI4SYiR1Q1AF8WkALYFSNdo8zuhjycwJQg25LXNKkiWCTRb5s9LgZGZH5hzvHlnq52EVMCvIwI6MFqKzCFhP214e%2FXZX%2BMlVzBktqECrMvvVpA2p3LjP5bw%3D%3D; _lr_geo_location_state=QC; _lr_geo_location=CA; _lr_sampling_rate=0; mySavedListings=%7B%22id%22%3A%22f771aebb-28cf-4693-aa17-a77f748ea6f6%22%7D; pjn-click=[{"id":"Cj0KCQjwqIm_BhDnARIsAKBYcmtgCT9c8wE9dKKwV_FfnLFRSdcIQCwrm7k8Sio_nHkLpXog2domC5kaAnoDEALw_wcB","days":20174,"type":"g"}]; _tt_enable_cookie=1; _ttp=01JQ812G94M6MHMBD2178B7MBT_.tt.1; SURVEY_SHOWN=April_2017_TV; preferredContactInfo=Y2l0eT1Nb250cmVhbCpwb3N0YWxDb2RlPUgzQypzdGF0ZT1RQypjb3VudHJ5PUNBKmhvbWVQb3N0YWxDb2RlPUgzQyo_; _gat=1; _dc_gtm_UA-4745999-4=1; dpt_cust_cookie=2; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22BKb2SJQLnaL7ruZ0JnQ5%22%2C%22expiryDate%22%3A%222026-03-26T01%3A42%3A29.339Z%22%7D; FPGSID=1.1742952618.1742953428.G-0QS2LC2KDY.cqPpgaO-Qkrp-yrymG0dFQ; _td=1a0277ab-fabe-45dc-b00b-8dba282c1f6e; datadome=CwffW7p1wYzDViUa4V6HOg4sQQ8yyNaJ2DRAo6tupHF_fuSB9cfkSye1tfCDEC8VcZiZLGUR1ZIgcF5SjYWSTcDfe3KkIVc~PG0fH7xsajTlZizxlAOWd8UgPsCyEljL; cto_bundle=UFwqe19JWiUyQkU5d1JnJTJGZVZDWE1IcTJQMjRSb3Bsb2lDaklGdTh4bnloOFEyT2VRV1NkSzZJZzg1OVIlMkJuQktOOHIzZDNpJTJGNEJBcUpGRzZDVnJQRGxBcjFJMjglMkJOb0tMSXk2MnI1OEJvY3dnZWFqRkxoRWFhcktDaldJT0JCcUd1MjE0cVFBSjFBV0VVUGxDVSUyQlVLOSUyQmdJZkNkaG1Hck9BaXJ6VWZNWWY4UyUyQk1MR0ZTYnJ5alJaZXpnWHo5UmduQVpGUGk1RlQ1RFQzcDJyUVdJd1clMkY4Nm9PYWNISVRJcFZSZlklMkJtUFFDdHJHSGRoRm1OJTJCbyUyRlJheSUyRmdyVHlDY3ZJdWkwNk11RVQzbDJ0T3R4T2lQWHZQZGcwbGUxWWU2TWtGaXBtaWI4RnpjalZXeGpiek5LdXpxelhiJTJCd1lJQW9ldDJlVmk; _ga=GA1.2.1396065042.1742952539; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%228RTH-91.245.254.213.1742952611717%22%2C%22expiryDate%22%3A%222026-03-26T01%3A42%3A52.147Z%22%7D; _uetsid=b5c7110009e111f0a08a95ba82813c9e; _uetvid=b5c72df009e111f0a2c92d501e39ad3f; _gac_UA-4745999-4=1.1742953377.Cj0KCQjwqIm_BhDnARIsAKBYcmtgCT9c8wE9dKKwV_FfnLFRSdcIQCwrm7k8Sio_nHkLpXog2domC5kaAnoDEALw_wcB; _gcl_aw=GCL.1742953377.Cj0KCQjwqIm_BhDnARIsAKBYcmtgCT9c8wE9dKKwV_FfnLFRSdcIQCwrm7k8Sio_nHkLpXog2domC5kaAnoDEALw_wcB; _ga_4WL8DDJFSY=GS1.1.1742952539.1.1.1742953395.60.0.0; _ga_0QS2LC2KDY=GS1.1.1742952540.1.1.1742953395.0.0.1530334045; _sp_id.8f67=d79b1ddb-d88f-4e86-bdc3-5bf7c3fb3465.1742952535.1.1742953397.1742952535.48b1377e-2e66-469b-897a-28f7a7827f78....0; baseZip_asOf=H3C_1742953396595; datadome=DguVD6fdfzXfASZVj27xf_oOA3jmI2wYn3sEt0O8SNn67SbDacZ_N~jJDXrsA7fB9FkiVeL4iKd~4DWE_esbkaKWaztkt0wys68fm0Y1L1AoyvboURvzY5vx8yzKmWPY; preferredContactInfo=Y2l0eT1Nb250cmVhbCpwb3N0YWxDb2RlPUgzQypzdGF0ZT1RQypjb3VudHJ5PUNBKmhvbWVQb3N0YWxDb2RlPUgzQyo_'
    }
    resp_req = requests.request("GET", url, headers=headers, data=payload)
    resp_req.raise_for_status()
    return resp_req.json()

if __name__ == "__main__":
    cls_cargurus = CarGurusCa()
    for pg_number in range(1, 300):
      name_json_file = rf"data/cargurus-pg-{pg_number}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
      json_cargurus = cls_cargurus.get_infos_mode_1(pg_number)
      blame_json = JsonFiles().dump_message(json_cargurus, name_json_file)