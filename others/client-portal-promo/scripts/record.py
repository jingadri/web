import json,subprocess,time,shutil,os
from playwright.sync_api import sync_playwright
N=json.load(open('narration.json'))
D=[float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'vo/{i}.mp3']))for i in range(10)]
GAP=0.7
CURSOR="""
(()=>{if(window.__c)return;const c=document.createElement('div');window.__c=c;
c.style.cssText='position:fixed;z-index:2147483647;width:26px;height:26px;border-radius:50%;background:rgba(36,122,132,.35);border:3px solid #247A84;pointer-events:none;left:-50px;top:-50px;transform:translate(-50%,-50%);transition:transform .12s';
document.documentElement.appendChild(c);
addEventListener('mousemove',e=>{c.style.left=e.clientX+'px';c.style.top=e.clientY+'px'},true);
addEventListener('mousedown',()=>c.style.transform='translate(-50%,-50%) scale(.6)',true);
addEventListener('mouseup',()=>c.style.transform='translate(-50%,-50%) scale(1)',true);})()
"""
OUTRO="""
(()=>{const o=document.createElement('div');o.style.cssText='position:fixed;inset:0;z-index:2147483646;background:#0f2a33;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:28px;opacity:0;transition:opacity 1.2s;font-family:Inter,system-ui,sans-serif;color:#fff';
o.innerHTML='<img src="supplements/0_kreatbio_logo.png" style="height:110px;background:#fff;padding:22px 40px;border-radius:18px"><div style="font-size:58px;font-weight:700">Your data, made clear.</div><div style="font-size:34px;color:#7fd1d6">kreatbio.com/client-portal</div>';
document.body.appendChild(o);requestAnimationFrame(()=>requestAnimationFrame(()=>o.style.opacity=1));})()
"""
with sync_playwright() as p:
    b=p.chromium.launch(channel='chrome')
    ctx=b.new_context(viewport={'width':1920,'height':1080},record_video_dir='rec',record_video_size={'width':1920,'height':1080})
    t_ctx=time.time()
    pg=ctx.new_page()
    pg.goto('http://localhost:8765/client-portal.html'); pg.wait_for_timeout(1500); pg.evaluate(CURSOR)
    pg.mouse.move(960,900)
    nav=lambda i: pg.locator('#nav .nav-item').nth(i)
    def go(loc,steps=18):
        bb=loc.bounding_box(); pg.mouse.move(bb['x']+bb['width']/2,bb['y']+bb['height']/2,steps=steps)
    def click(loc): go(loc); pg.wait_for_timeout(250); pg.mouse.click(*[v for v in (lambda bb:(bb['x']+bb['width']/2,bb['y']+bb['height']/2))(loc.bounding_box())])
    def scroll(total,secs,x=1100,y=600):
        pg.mouse.move(x,y,steps=8)
        pg.evaluate("""([total,secs])=>new Promise(res=>{
          let el=document.elementFromPoint(1100,600),sc=null;
          while(el&&el!==document.body){const cs=getComputedStyle(el);if(/auto|scroll/.test(cs.overflowY)&&el.scrollHeight>el.clientHeight+50){sc=el;break}el=el.parentElement}
          const get=()=>sc?sc.scrollTop:window.scrollY,set=v=>sc?sc.scrollTo(0,v):window.scrollTo(0,v);
          const s0=get(),t0=performance.now();
          const f=t=>{let k=Math.min(1,(t-t0)/(secs*1000));k=k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2;set(s0+total*k);k<1?requestAnimationFrame(f):res()};requestAnimationFrame(f)})""",[total,secs])
    starts=[];t_first=None
    for i in range(10):
        t0=time.time()
        if i==0: t_first=t0; starts.append(0.0)
        else: starts.append(t0-t_first)
        L=D[i]+GAP
        if i==0:
            pg.wait_for_timeout(int((L-3.2)*1000)); click(pg.locator('[data-example-code="120000001"]'))
        elif i==1:
            pg.wait_for_timeout(3000); pg.evaluate(CURSOR)
            for sel in ['Overall','Composition','Diversity','Relationship','Function']:
                try: go(pg.get_by_text(sel,exact=True).first,25); pg.wait_for_timeout(700)
                except Exception as e: print('hover',sel,e)
        elif i==2: click(nav(1)); pg.wait_for_timeout(1000); scroll(520,L-5.2)
        elif i==3:
            click(nav(2)); pg.wait_for_timeout(1000)
            try: click(pg.get_by_text('Next step').first); pg.wait_for_timeout(1500); click(pg.get_by_text('Next step').first)
            except Exception as e: print('next',e)
        elif i==4: click(nav(3)); pg.wait_for_timeout(1000); scroll(650,L-5.2)
        elif i==5: click(nav(4)); pg.wait_for_timeout(1000); scroll(620,L-5.2)
        elif i==6: click(nav(5)); pg.wait_for_timeout(1000); scroll(520,L-5.2)
        elif i==7: click(nav(6)); pg.wait_for_timeout(1000); scroll(560,L-5.2)
        elif i==8:
            click(nav(7)); pg.wait_for_timeout(2500); scroll(420,1.8); click(nav(11)); pg.wait_for_timeout(800)
        elif i==9:
            click(pg.get_by_text('Exit report').first); pg.wait_for_timeout(1500); pg.evaluate(OUTRO)
        rem=L-(time.time()-t0)
        if rem>0: pg.wait_for_timeout(int(rem*1000))
        else: print('scene',i,'overran by',-rem)
    pg.wait_for_timeout(1500)
    off=t_first-t_ctx
    vp=pg.video.path(); ctx.close(); b.close()
    shutil.copy(vp,'raw.webm'); json.dump({'off':off,'starts':starts,'D':D},open('timing.json','w')); print('off',off,starts)
