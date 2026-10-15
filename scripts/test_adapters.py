#!/usr/bin/env python3
"""Local macOS acceptance: executes only the two reviewed adapters with synthetic input."""
import subprocess,os,base64,json,pathlib
root=pathlib.Path(__file__).resolve().parents[1]/'extensions'
r=[]
def run(pkg,args,text):
 return subprocess.run(args,cwd=root/(pkg+'.popclipext'),env={'POPCLIP_TEXT':text,'LANG':'en_US.UTF-8','PATH':'/usr/bin:/bin'},capture_output=True)
for s in ['', 'Hello 中文 😀', 'line one\nline two &+?#', 'f','fo','foo','é\u0301', '😀?', '$(touch /tmp/bubboo-should-not-exist)']:
 for mode in ['standard','url']:
  x=run('Base64',['/usr/bin/perl','bubboo-base64.pl',mode],s);expected=base64.b64encode(s.encode()) if mode=='standard' else base64.urlsafe_b64encode(s.encode()).rstrip(b'=');assert x.returncode==0 and x.stdout==expected,(s,x.stderr)
  y=run('Base64',['/usr/bin/perl','bubboo-base64.pl','decode'],expected.decode());assert y.returncode==0 and y.stdout==s.encode(),y.stderr
  r.append({'mode':mode,'input':s,'passed':True})
for s in ['a','Zg=','Zh==','////','AA==','!!','Zg===','a+_a']:
 x=run('Base64',['/usr/bin/perl','bubboo-base64.pl','decode'],s);assert x.returncode!=0 and not x.stdout,s
 r.append({'invalid':s,'passed':True})
for s,expected in [('the lord of the rings','The Lord of the Rings'),('hello 中文 & emoji 😀','Hello 中文 & Emoji 😀'),('a tale of two cities','A Tale of Two Cities'),('  the rise of iPhone and macOS  ','The Rise of iPhone and macOS')]:
 x=run('TitleCase',['/bin/zsh','bubboo-titlecase.zsh'],s);assert x.returncode==0 and x.stdout.decode()==expected,(s,x.stdout,x.stderr);r.append({'title':s,'expected':expected,'passed':True})
for s in ['first line\nsecond line', 'first\rsecond', 'a'*10001]:
 x=run('TitleCase',['/bin/zsh','bubboo-titlecase.zsh'],s);assert x.returncode!=0 and not x.stdout
 r.append({'boundary':'multiline or oversized title rejected','passed':True})
print(json.dumps(r,ensure_ascii=False,indent=2))
