const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file:///mnt/user-data/outputs/word-cards/index.html'); await p.waitForTimeout(500);
  // 随机答对答错，检查：游戏结束时对手防御必须为 0；进行中 防御 = 剩余要答对的张数
  for (let run = 0; run < 30; run++) {
    const r = await p.evaluate(async (seed) => {
      S.settings.fx = false;
      const ids = WORDS.slice(seed * 7, seed * 7 + 6).map(w => w.id);
      startBattle({ title: 't', foe: SC.body.foe, ids, key: null });
      const log = []; let steps = 0;
      while (B && steps < 200) {
        steps++;
        if (B.hp !== B.queue.length + 1) return 'MISMATCH hp=' + B.hp + ' q=' + B.queue.length;
        const right = Math.random() < .6;
        const hpBefore = B.hp;
        answer(right ? B.target : B.hand.find(x => x !== B.target));
        if (B) { if (B.hp !== hpBefore + (right ? -1 : 1)) return 'HPSTEP'; }
        if (B && B.hp <= 0) { nextRound(); break; }
        if (B) nextRound();
      }
      return SCREEN === 'victory' ? 'ok ' + steps : 'end? ' + SCREEN;
    }, run);
    if (!r.startsWith('ok')) { console.log('FAIL', run, r); }
  }
  console.log('done', errs);
  await b.close();
})();
