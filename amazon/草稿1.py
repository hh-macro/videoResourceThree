import random

import pandas as pd
from DrissionPage import ChromiumPage
import time

page = ChromiumPage()

page.get(
    'https://www.amazon.com/ap/signin?clientContext=135-2939824-8502515&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fus.amazon.com%2Fgp%2Fvideo%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_t%3D1sg7MOyO7HcO2AaUnWu_BV34hTajwE_IximIOoiJZIY541AAAAAQAAAABn-gjQcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ%26location%3D%2Fgp%2Fvideo%2Fsignup%3Fref_%253Ddvah&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&accountStatusPolicy=P1&openid.assoc_handle=usflex&openid.mode=checkid_setup&countryCode=US&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
time.sleep(5)
try:

    page.ele('css:#ap_password').input('123aaa123')
    page.ele('css:#signInSubmit').click()
except:
    print('已登陆')
time.sleep(5)

page.get(
    'https://us.amazon.com/gp/video/browse/ref=atv_tv_hom_c_ob645d8d_3_smr?serviceToken=v0_Cl0KJDJmYTJhYWZlLTE3ZjctNGE1ZC1iZDM0LWM4YTE2ZGZjOGE1NhDQ7r7I4jIaLExpNitvL2dzaDBoR0NjVGdhVGdLTHptYkF6dHpuZ29zb2VJMDZ6YWhmZEk9IAESBXF1ZXJ5GAEqB2RlZmF1bHQyBmNlbnRlcjoGc2VhcmNoUglPQjY0NWQ4ZHN6AIIB8wQSKjI6T0IyMDkwM0NGODY1RUEjI01aUVdHWkxVTVZTRUdZTFNONTJYR1pMTRqwBHFzLWNvdW50cnktY29kZT1VUyZxcy1lbnRpdHlfdHlwZT0yJnBfbl9lbnRpdHlfdHlwZT0xNDA2OTE4NTAxMSZhZHVsdC1wcm9kdWN0PTAmc2VhcmNoLWFsaWFzPWluc3RhbnQtdmlkZW8mYnE9KGFuZCAoYW5kIChhbmQgKGFuZCAobm90IChvciBnZW5yZTonYXZfZ2VucmVfZXJvdGljJyBhdl9wcmltYXJ5X2dlbnJlOidhdl9nZW5yZV9lcm90aWMnKSkgKG5vdCAob3IgZ2VucmU6J2F2X2dlbnJlX2tpZHMnIGF2X3ByaW1hcnlfZ2VucmU6J2F2X2dlbnJlX2tpZHMnKSkpIChhbmQgKG9yIGdlbnJlLWJpbjonYXZfZ2VucmVfYW5pbWUnIGF2X3ByaW1hcnlfZ2VucmU6J2F2X2dlbnJlX2FuaW1lJykgZW50aXR5X3R5cGU6J1RWIFNob3cnKSkgKG5vdCBhdl9raWRfaW5fdGVycml0b3J5OidVUycpKSAobm90IGVudGl0eV90eXBlOidQcm9tb3Rpb258VHJhaWxlcnxCb251cyBDb250ZW50JykpJnB2X2Jyb3dzZV9pbnRlcm5hbF9vZmZlcj1zdWJzY3JpcHRpb258c3ZvZCZwdl9icm93c2VfaW50ZXJuYWxfYmVuZWZpdD1mcmVld2l0aGFkcyZwdl9icm93c2VfaW50ZXJuYWxfbGFuZ3VhZ2U9YWxsIgzliqjmvKvnlLXop4YwAFAAcAA%3D&jic=44%7CCgtmcmVld2l0aGFkcxIMc3Vic2NyaXB0aW9uEgRzdm9k')
time.sleep(3)
input(":")
data_content_list = []
pages_lis = page.eles('css:.Z9dd1d._56AITU')
for page_lis in pages_lis:
    section_name = page_lis.ele('css:.PPqU2v')
    full_url = page_lis.ele('css:._3HZFFn').attr('href')
    data_content_list.append({
        'aria_label': section_name,
        'href': full_url
    })
    print(full_url)
    print(section_name)
df = pd.DataFrame(data_content_list)

df.to_excel(f"./compilations/hdisneyList-{int(time.time())}.xlsx", index=False)

print(f"hdisneyList-{int(time.time())}.xlsx")
