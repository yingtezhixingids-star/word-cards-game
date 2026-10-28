const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file:///mnt/user-data/outputs/word-cards/index.html');await p.waitForTimeout(1500);
const r=await p.evaluate(()=>{const o={w:[],ex:[],hint:[],line:[]};
WORDS.filter(w=>!w.adv).forEach(w=>{o.w.push(w.en);if(w.ex)o.ex.push(w.ex);if(w.hint)o.hint.push(w.hint);});
SCENES.forEach(s=>{[s.foe,s.boss].forEach(f=>{if(f&&f.line)o.line.push(f.line)})});o.lang=LANG;o.sample=LG.sample;o.adv=WORDS.filter(w=>w.adv).length;return o;});
fs.writeFileSync('tts/texts.json',JSON.stringify(r));
console.log(r.lang,r.adv,Object.entries(r).map(([k,v])=>k+':'+(Array.isArray(v)?v.length+'/'+new Set(v).size:v)).join(' '));
console.log(r.hint.slice(0,3),r.line.slice(0,3));await b.close();})();
