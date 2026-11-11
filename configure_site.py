#!/usr/bin/env python3
"""Fill in a REAL public website URL for SEO and update the CV hyperlink.
Usage: python configure_site.py --url https://YOUR-GITHUB-USERNAME.github.io/
This script does not publish the site; it prepares files to upload to hosting.
Dependencies: python-docx, beautifulsoup4 (pip install python-docx beautifulsoup4)
Optional: LibreOffice for PDF export.
"""
import argparse, json, shutil, subprocess, tempfile
from pathlib import Path
from urllib.parse import urlsplit,urljoin
from xml.sax.saxutils import escape
from bs4 import BeautifulSoup
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor
R=Path(__file__).resolve().parent

def add_word_hyperlink(paragraph,label,url):
    part=paragraph.part
    rid=part.relate_to(url,RT.HYPERLINK,is_external=True)
    el=OxmlElement('w:hyperlink');el.set(qn('r:id'),rid)
    run=OxmlElement('w:r');props=OxmlElement('w:rPr')
    col=OxmlElement('w:color');col.set(qn('w:val'),'137B86');props.append(col)
    un=OxmlElement('w:u');un.set(qn('w:val'),'single');props.append(un)
    size=OxmlElement('w:sz');size.set(qn('w:val'),'16');props.append(size)
    run.append(props);t=OxmlElement('w:t');t.text=label;run.append(t);el.append(run)
    paragraph._p.append(el)

def configure(url):
    p=urlsplit(url)
    if p.scheme!='https' or not p.hostname or 'YOUR' in p.hostname.upper() or 'EXAMPLE' in p.hostname.upper():
        raise ValueError('Please provide your ACTUAL published HTTPS website address, not a placeholder.')
    base=url.rstrip('/')+'/'
    for fn in ['index.html','research.html','worm-gearbox.html']:
        file=R/fn;soup=BeautifulSoup(file.read_text(encoding='utf8'),'html.parser')
        target=base if fn=='index.html' else urljoin(base,fn)
        tag=soup.head.find('link',rel='canonical')
        if tag is None:tag=soup.new_tag('link',rel='canonical');soup.head.append(tag)
        tag['href']=target
        og=soup.head.find('meta',attrs={'property':'og:url'})
        if og is None:og=soup.new_tag('meta');og['property']='og:url';soup.head.append(og)
        og['content']=target
        for key,value in [('og:image',urljoin(base,'assets/og-cover.png'))]:
            m=soup.head.find('meta',attrs={'property':key})
            if m:m['content']=value
        tw=soup.head.find('meta',attrs={'name':'twitter:image'})
        if tw is None:tw=soup.new_tag('meta');tw['name']='twitter:image';soup.head.append(tw)
        tw['content']=urljoin(base,'assets/og-cover.png')
        tag=soup.head.find('script',attrs={'type':'application/ld+json'})
        if tag:
            content=json.loads(tag.string)
            content['url']=target
            content['image']=urljoin(base,'assets/formal-headshot.webp')
            tag.string=json.dumps(content,ensure_ascii=False)
        file.write_text(str(soup),encoding='utf8')
    pages=[base,urljoin(base,'research.html'),urljoin(base,'worm-gearbox.html')]
    xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for page in pages:xml+='  <url><loc>'+escape(page)+'</loc></url>\n'
    xml+='</urlset>\n'
    (R/'sitemap.xml').write_text(xml,encoding='utf8')
    (R/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+urljoin(base,'sitemap.xml')+'\n',encoding='utf8')
    cv=R/'docs'/'Amanullah_Research_CV_Fall2027.docx'
    d=Document(cv)
    ps=[par for par in d.paragraphs if 'RESEARCH WEBSITE' in par.text]
    if not ps:
        raise ValueError('CV template line not found. Please use the bundled starter CV.')
    par=ps[0]
    par.clear()
    rr=par.add_run('RESEARCH WEBSITE  ·  ')
    rr.bold=True;rr.font.size=Pt(8);rr.font.color.rgb=RGBColor(27,108,115)
    add_word_hyperlink(par,base,base)
    d.save(cv)
    shutil.copy2(cv,R/'Amanullah_CV_With_Live_Portfolio_Link.docx')
    lo=shutil.which('libreoffice') or shutil.which('soffice')
    if lo:
        subprocess.run([lo,'-env:UserInstallation=file:///tmp/amanullah_site_cv_render','--headless','--convert-to','pdf','--outdir',str(R/'docs'),str(cv)],capture_output=True,timeout=50)
        pdf=R/'docs'/'Amanullah_Research_CV_Fall2027.pdf'
        if pdf.exists():shutil.copy2(pdf,R/'Amanullah_CV_With_Live_Portfolio_Link.pdf')
        print('Updated academic CV Word + PDF.')
    else:
        print('Updated academic CV Word; open in Word and Save As PDF if needed.')
    (R/'PUBLIC_WEBSITE_ADDRESS.txt').write_text(base+'\n')
    print('Configured site URL:',base)
    print('Upload all refreshed site files, including the /docs and /assets folders, to your hosting repo.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url',required=True,help='The REAL, publicly live HTTPS homepage URL')
    args=parser.parse_args();configure(args.url)
