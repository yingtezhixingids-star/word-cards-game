const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 860 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file:///mnt/user-data/outputs/word-cards/index.html'); await p.waitForTimeout(400);
  await p.evaluate(() => { S.settings.unlockAll = true; startFinal('body'); });
  const st = () => p.evaluate(() => F ? { r: F.round, hp: F.hp, mis: F.mistakes, r1: F.r1.queue.length, q2: F.r2.queue.length + (F.r2.mons || []).filter(m => !m.dying).length, r3: F.r3.items.filter(x => !x.done).length } : SCREEN);
  await p.waitForTimeout(2300);
  await p.evaluate(() => { const w = $$('#fstage .lw')[0], m = [...$$('#fstage .lm')].find(x => x.dataset.id !== w.dataset.id); w.click(); m.click(); });
  let g = 0; while (g++ < 50) {
    const r = await p.evaluate(() => { if (!F || F.round !== 0) return 'next'; const ws = [...$$('#fstage .lw:not(.gone)')]; if (!ws.length) return 'wait'; const w = ws[0]; const m = [...$$('#fstage .lm:not(.gone)')].find(x => x.dataset.id === w.dataset.id); w.click(); m.click(); return 'ok'; });
    if (r === 'next') break; await p.waitForTimeout(r === 'wait' ? 500 : 120);
  }
  await p.waitForTimeout(1700); await p.screenshot({ path: 'shots/td-pick.png' }); await p.click('.tdl.hell'); await p.waitForTimeout(400);
  console.log('r2 start', await st());
  // one wrong pad, one breach, rest kills
  await p.evaluate(() => { const live = F.r2.mons.filter(m => !m.dying); const ens = live.map(m => W[m.id].en); const pad = [...$$('#pads .pad:not(.ruin)')].find(x => !ens.includes(W[x.dataset.id].en)); pad.click(); });
  console.log('wrong', await st());
  await p.evaluate(() => { F.r2.mons.find(m => !m.dying).s = .999; }); await p.waitForTimeout(300); console.log('breach', await st());
  await p.waitForTimeout(9000); console.log('hell live', await p.evaluate(() => F.r2.mons.filter(m=>!m.dying).length)); await p.screenshot({ path: 'shots/td-hell.png' });
  g = 0; while (g++ < 60) {
    const r = await p.evaluate(() => { if (!F || F.round !== 1) return 'next'; if (F.r2.over) { r2Restart(); return 'over'; } if (!F.r2.mons) return 'wait'; if ($('.tdpick')) { $('.tdl.normal').click(); return 'wait'; } const m = F.r2.mons.find(m => !m.dying); if (!m) { F.r2.last = 0; return 'wait'; } const pad = [...$$('#pads .pad:not(.ruin)')].find(x => W[x.dataset.id].en === W[m.id].en); if (!pad) { m.s = .999; return 'doomed'; } pad.click(); return 'ok'; });
    if (r === 'next') break; await p.waitForTimeout(r === 'over' ? 100 : 700);
  }
  await p.waitForTimeout(2800); console.log('r3 start', await st()); await p.screenshot({ path: 'shots/r3-1.png' });
  await p.evaluate(() => { const cur = F.r3.items.find(x => !x.done); const o = [...$$('#fstage .opt')].find(x => W[x.dataset.id].en !== W[cur.id].en); o.click(); });
  console.log('r3 wrong', await st()); await p.waitForTimeout(500); await p.screenshot({ path: 'shots/r3-2.png' }); await p.waitForTimeout(2500);
  g = 0; while (g++ < 40) {
    const r = await p.evaluate(() => { if (!F || F.round !== 2) return 'next'; if (F.r3.busy) return 'wait'; const cur = F.r3.items.find(x => !x.done); if (!cur) return 'wait'; const o = [...$$('#fstage .opt')].find(x => W[x.dataset.id].en === W[cur.id].en); o.click(); return 'ok'; });
    if (r === 'next') break; await p.waitForTimeout(r === 'wait' ? 800 : 300);
  }
  await p.waitForTimeout(3000); console.log('end', await st(), await p.evaluate(() => JSON.stringify(S.stars)));
  console.log(errs); await b.close();
})();
