const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file:///mnt/user-data/outputs/word-cards/index.html');await p.evaluate(()=>localStorage.setItem('wordcards.lang','ja'));await p.reload();await p.waitForTimeout(1500);
const r=await p.evaluate(()=>{const o=[];const add=(t)=>{if(t)o.push([t,(ALT[t]||[])[0]||''])};
WORDS.forEach(w=>{add(w.en);add(w.ex);add(w.hint)});SCENES.forEach(s=>[s.foe,s.boss].forEach(f=>f&&add(f.line)));add(LG.sample);return {lang:LANG,n:WORDS.length,adv:WORDS.filter(w=>w.adv).length,o}});
fs.writeFileSync('tts/texts-ja.json',JSON.stringify(r.o));console.log(r.lang,r.n,r.adv,r.o.length,new Set(r.o.map(x=>x[0])).size);console.log(r.o.slice(0,4),r.o.slice(-3));await b.close();})();
