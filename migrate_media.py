"""Run on your own computer with internet access to copy screenshots out of Squarespace.
Usage: python migrate_media.py
Once completed, the website uses only locally hosted game imagery.
"""
from pathlib import Path
from urllib.request import Request, urlopen
root=Path(__file__).resolve().parent
base='https://images.squarespace-cdn.com/content/v1/60c7394b37f0f1662e0c2f90/'
assets={
'hero.jpg':'1de7a20c-2bc3-4355-b41a-b5800d8fd5cf/NopeChallenge_WebHeader.jpg',
'clowns.png':'b97ba8d8-89d5-49a2-8e50-dfb28f1a94cc/HM_NC_SS_C3_07.png',
'heights.png':'e942c81d-8830-40d1-b5fa-82727d86b758/NopeChallenge_Heights_01.png',
'spiders.png':'dab5bb74-faa5-4ed9-9e35-97aa636ba166/NopeChallenge_Spiders_01.png',
'breather.png':'9614ad95-4c01-4b55-84df-05f48b21b05d/HM_NC_Breather_02.png',
'reality.jpg':'052aefc9-08b6-4e1d-a2c5-cf285d4abca5/HM_NC_SS_C1_01.png',
}
for name,path in assets.items():
    dest=root/'assets'/name
    try:
        req=Request(base+path,headers={'User-Agent':'Mozilla/5.0'})
        with urlopen(req,timeout=35) as response: data=response.read()
        if len(data)<3000: raise ValueError('File too small')
        dest.write_bytes(data)
        print('OK',name,len(data),'bytes')
    except Exception as e: print('FAILED',name, str(e))
print('Done. Confirm all six files are present in assets/ before deploying.')
