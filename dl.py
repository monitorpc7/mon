import sys, os
from skillshare import Skillshare, splash
#from magic import cookie

# or by class ID:
# dl.download_course_by_class_id(189505397)

cookie = "_sctr=1|1646071200000; _derived_epik=dj0yJnU9RFFqX2tRS1NmaEc0NXJkbHR0X0liZGd2bW44dHlMaVImbj1GYUVxVWl6eEZ2WXp2Zk14dFFlVzZRJm09MSZ0PUFBQUFBR0lpQ1N3JnJtPTEmcnQ9QUFBQUFHSWlDU3c; __ssid=a300c02009b94ec03761e6c67316f36; __pdst=f648d763678d4713b6f3cbdc43703321; __qca=P0-1056593284-1640178366886; _clck=1ujjzss|1|f4s|0; _gcl_au=1.1.482960909.1662626170; _scid=29a80eab-301a-4cef-8523-70ca4c2a61a8; _tt_enable_cookie=1; _ttp=d39206bf-5029-41a8-b64f-5652a2d936c6; device_session_id=fdd0008e-5cbd-442f-951a-91b90cf18941; first_landing=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; G_ENABLED_IDPS=google; g_state={\"i_l\":0}; show-like-copy=0; sm_uuid=1640178473851; ss_hide_default_banner=1662683297.512; accept_language=en-US; YII_CSRF_TOKEN=amR6WGhYdXpBSDIxbDl2bHJ4OFpoVmhqMGF3ME1HMXVu_IWchRhd2ctBm-joP7DBSI_h90exF7VegOpKoQ2n8Q%3D%3D; visitor_tracking=utm_campaign=&utm_source=&utm_medium=&utm_term=&referrer=https%3A%2F%2Fwww.google.com%2F&referring_username=; _ga_J5NPJ1XD74=GS1.1.1662911595.7.0.1662911595.0.0.0; _ga=GA1.1.247375290.1640674953; _uetsid=11832de030c111ed994deb0f525fffa0; _uetvid=ba83bcc0cf7611ebbe430b3f535a53d6; IR_gbd=skillshare.com; IR_4650=1662911597022%7C0%7C1662911597022%7C%7C; IR_PI=c8ae97bc-271e-11ec-a602-432cdb6e7d74%7C1662997997022; __stripe_mid=915b9fa2-fbb5-4aa2-b8d9-e42ee65952496f196b; __stripe_sid=d2305d6a-9dc9-40cb-9660-922a373d2af919b57c; _pin_unauth=dWlkPU9UVXhNakUzWkRBdE1EVmhPQzAwTmpOakxUaGhabVl0TjJFNFptWTVNVFprWm1NeA; __utma=99704988.731451925.1640178212.1662873925.1662911612.7; __utmc=99704988; __utmz=99704988.1662683298.2.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=99704988.|1=visitor-type=user=1; __utmt=1; __utmb=99704988.1.10.1662911612; _clsk=19s9tm2|1662912056803|2|0|b.clarity.ms/collect"

def main():
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
