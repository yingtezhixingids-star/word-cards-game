const { chromium } = require('playwright');
(async () => {
  for (const [vw, vh, tag] of [[390, 800, 'm']]) {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: vw, height: vh } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file:///mnt/user-data/outputs/word-cards/index.html'); await p.waitForTimeout(400);
  await p.evaluate(() => { S.settings.unlockAll = true; startFinal('time'); F.r1.queue = []; });
  await p.waitForTimeout(3500); await p.click('.tdl.normal'); await p.waitForTimeout(2500);
  const st = () => p.evaluate(() => F ? { r: F.round, hp: F.hp, mis: F.mistakes, q: F.r2.queue.length, mons: F.r2.mons.length, r3: F.r3.items.filter(x => !x.done).length, castle: F.r2.castle } : SCREEN);
  console.log(tag, 'r2 start', await st());
  await p.evaluate(() => F.r2.mons.forEach(m => m.s = .35)); await p.waitForTimeout(400);
  await p.screenshot({ path: `shots/td-${tag}-1.png` });
  if (tag === 'm') { console.log(errs); await b.close(); continue; }
  // force each weapon kind once
  for (let k = 0; k < 6; k++) {
    await p.evaluate(k => { const m = F.r2.mons.find(m => !m.dying); if (!m) return; const pad = [...$$('#pads .pad')].find(x => W[x.dataset.id].en === W[m.id].en); pad.dataset.wi = k; pad.click(); }, k);
    await p.waitForTimeout(k === 4 ? 700 : 450); await p.screenshot({ path: `shots/td-w${k}.png` }); await p.waitForTimeout(1500);
    await p.evaluate(() => { if (F && F.r2.queue.length && !F.r2.mons.some(m=>!m.dying)) F.r2.last = 0; });
    await p.waitForTimeout(600);
  }
  console.log('after 6 kills', await st());
  // wrong pad
  await p.evaluate(() => { const live = F.r2.mons.filter(m => !m.dying); const ens = live.map(m => W[m.id].en); const pad = [...$$('#pads .pad:not(.ruin)')].find(x => !ens.includes(W[x.dataset.id].en)); pad.click(); });
  console.log('after wrong', await st()); await p.waitForTimeout(300); await p.screenshot({ path: 'shots/td-wrong.png' });
  // breach
  await p.evaluate(() => { const m = F.r2.mons.find(m => !m.dying); m.s = .999; }); await p.waitForTimeout(400);
  console.log('after breach', await st()); await p.screenshot({ path: 'shots/td-breach.png' });
  // game over: two more breaches
  for (let i = 0; i < 2; i++) { await p.evaluate(() => { F.r2.last = 0; }); await p.waitForTimeout(600); await p.evaluate(() => { const m = F.r2.mons.find(m => !m.dying); if (m) m.s = .999; }); await p.waitForTimeout(500); }
  console.log('after 3 breaches', await st()); await p.screenshot({ path: 'shots/td-over.png' });
  await p.evaluate(() => r2Restart()); await p.waitForTimeout(800); console.log('restart', await st());
  // finish round 2 cleanly
  let g = 0; while (g++ < 60) {
    const r = await p.evaluate(() => { if (!F || F.round !== 1) return 'next'; const m = F.r2.mons.find(m => !m.dying); if (!m) { F.r2.last = 0; return 'wait'; } const pad = [...$$('#pads .pad')].find(x => W[x.dataset.id].en === W[m.id].en && !x.classList.contains('ruin')); pad.click(); return 'ok'; });
    if (r === 'next') break; await p.waitForTimeout(1300);
  }
  console.log('r2 done', await st());
  console.log(errs); await b.close();
  }
})();
