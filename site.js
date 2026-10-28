const form=document.getElementById('requestForm');if(form){form.addEventListener('submit',e=>{e.preventDefault();const f=new FormData(form),select=document.getElementById('service'),fa=document.documentElement.lang==='fa';const text=(fa?'خدمت':'Leistung')+': '+select.selectedOptions[0].text+'\n'+(fa?'نام':'Name')+': '+f.get('name')+'\n'+(fa?'شهر':'Ort')+': '+f.get('city')+'\n\n'+f.get('message');document.getElementById('summary').textContent=text;document.getElementById('emailRequest').href='mailto:info@hs-bauwerk.de?subject='+encodeURIComponent('Projektanfrage – '+select.selectedOptions[0].text)+'&body='+encodeURIComponent(text);document.getElementById('requestResult').hidden=false;});document.getElementById('copySummary').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(document.getElementById('summary').textContent);document.getElementById('copyStatus').textContent=document.documentElement.lang==='fa'?'کپی شد':'Kopiert';}catch{document.getElementById('copyStatus').textContent=document.documentElement.lang==='fa'?'متن را انتخاب و کپی کنید.':'Bitte den Text markieren und kopieren.';}});}

const mobileMenu=document.querySelector('.mobile-menu');
if(mobileMenu){
mobileMenu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{mobileMenu.open=false;}));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&mobileMenu.open){mobileMenu.open=false;mobileMenu.querySelector('summary').focus();}});
document.addEventListener('click',e=>{if(!mobileMenu.contains(e.target))mobileMenu.open=false;});
}
