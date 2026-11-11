document.documentElement.classList.add('js');
(function(){
 const toggler=document.querySelector('.menu-toggle'); const menu=document.getElementById('nav-links');
 if(toggler&&menu){
   toggler.addEventListener('click',()=>{const show=!menu.classList.contains('open');menu.classList.toggle('open',show);toggler.setAttribute('aria-expanded',String(show));toggler.setAttribute('aria-label',show?'Close navigation':'Open navigation')});
   menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{menu.classList.remove('open');toggler.setAttribute('aria-expanded','false')}));
   document.addEventListener('keydown',e=>{if(e.key==='Escape'){menu.classList.remove('open');toggler.setAttribute('aria-expanded','false')}});
 }
 const reveals=[...document.querySelectorAll('.reveal')];
 if('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches){
   const ob=new IntersectionObserver(entries=>{for(const e of entries){if(e.isIntersecting){e.target.classList.add('visible');ob.unobserve(e.target)}}},{threshold:0.04,rootMargin:'0px 0px 20px 0px'});
   reveals.forEach(el=>ob.observe(el));
 } else reveals.forEach(el=>el.classList.add('visible'));
 const btns=[...document.querySelectorAll('.filter')],rows=[...document.querySelectorAll('.portfolio-row')];
 btns.forEach(btn=>btn.addEventListener('click',()=>{
   const category=btn.dataset.filter;
   btns.forEach(b=>{const yes=b===btn;b.classList.toggle('active',yes);b.setAttribute('aria-pressed',String(yes))});
   rows.forEach(row=>{const visible=category==='all'||row.dataset.category===category;row.hidden=!visible;if(visible)row.classList.add('visible')});
 }));
 const lightbox=document.querySelector('.lightbox');
 if(lightbox){
   const close=lightbox.querySelector('.lightbox-close'),img=lightbox.querySelector('img'),caption=lightbox.querySelector('p');let prev=null;
   function hide(){lightbox.classList.remove('open');lightbox.setAttribute('aria-hidden','true');document.body.style.overflow='';if(prev)prev.focus()}
   document.querySelectorAll('.image-open').forEach(b=>b.addEventListener('click',()=>{prev=b;img.src=b.dataset.full;img.alt=b.querySelector('img').alt;caption.textContent=b.dataset.caption;lightbox.classList.add('open');lightbox.setAttribute('aria-hidden','false');document.body.style.overflow='hidden';close.focus()}));
   close.addEventListener('click',hide);lightbox.addEventListener('click',e=>{if(e.target===lightbox)hide()});
   document.addEventListener('keydown',e=>{if(e.key==='Escape'&&lightbox.classList.contains('open'))hide()});
 }
 const year=document.getElementById('year');if(year)year.textContent=new Date().getFullYear();
})();
