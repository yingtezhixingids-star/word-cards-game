import lex, unicodedata, re
from g2p_en import G2p
g=G2p()
def deacc(w): return ''.join(c for c in unicodedata.normalize('NFD',w) if unicodedata.category(c)!='Mn')
def demote(ph): return [p[:-1]+'2' if p[-1]=='1' else p for p in ph]
def one_primary(ph):
    vi=[i for i,p in enumerate(ph) if p[-1].isdigit()]
    if not vi: return ph
    if not any(ph[i][-1]=='1' for i in vi):
        j=next((i for i in vi if ph[i][-1]=='2'),vi[0]); ph=list(ph); ph[j]=ph[j][:-1]+'1'
    seen=False; out=[]
    for p in ph:
        if p[-1]=='1':
            if seen: p=p[:-1]+'2'
            seen=True
        out.append(p)
    return out
def guess(w):
    lw=deacc(w.lower()).replace("'s",'')
    if lex.pron(lw): return lex.pron(lw),'acc'
    if re.fullmatch(r'[A-Z0-9]{2,}',w):
        return None,'abbr'
    # plural
    for suf,add in (('ies',None),('es',['IH0','Z']),('s',['Z'])):
        if lw.endswith(suf):
            b=lw[:-3]+'y' if suf=='ies' else lw[:-len(suf)]
            pb=lex.pron(b)
            if pb:
                if suf=='ies': return pb+['Z'],'pl'
                last=pb[-1]
                if suf=='s': return pb+(['S'] if last in ('P','T','K','F','TH') else ['IH0','Z'] if last in('S','Z','SH','CH','JH','ZH') else ['Z']),'pl'
                if last in('S','Z','SH','CH','JH','ZH'): return pb+add,'pl'
    if lw in ('anther','paneer','shaobing'): return one_primary(g(lw)),'g2p'
    # british/alt spellings and suffixes
    ALT={'chequered':'checkered','chilli':'chili','mantlepiece':'mantelpiece','defraction':'diffraction','archeologist':'archaeologist','archeology':'archaeology','crystalized':'crystallized','flextime':'flextime'}
    if lw in ALT and lex.pron(ALT[lw]): return lex.pron(ALT[lw]),'alt'
    for suf,add in (('ed',None),('ing',['IH0','NG']),('er',['ER0']),('ers',['ER0','Z'])):
        if lw.endswith(suf) and len(lw)>len(suf)+3:
            for b in [lw[:-len(suf)], lw[:-len(suf)]+'e']+([lw[:-len(suf)-1]] if lw[-len(suf)-1]==lw[-len(suf)-2] else []):
                pb=lex.pron(b)
                if pb and lex.ZF(b)>=2.5:
                    if suf=='ed': add=['IH0','D'] if pb[-1] in ('T','D') else ['T'] if pb[-1] in ('P','K','F','S','SH','CH','TH') else ['D']
                    return pb+add,'suf'
    # compound
    if lw in ('cooksonia','parkour','prepositions','interdental'): return one_primary(g(lw)),'g2p'
    best=None
    for i in range(3,len(lw)-2):
        a,b=lw[:i],lw[i:]
        pa,pb=lex.pron(a),lex.pron(b)
        za,zb=lex.ZF(a),lex.ZF(b)
        ok=(len(a)>=4 and len(b)>=4 and za>=3.5 and zb>=3.5) or (min(len(a),len(b))==3 and max(len(a),len(b))>=4 and min(za,zb)>=4.5 and max(za,zb)>=3.5)
        if re.search(r'(ian|ese|er|ers|ing|ism|ic)$',lw) and not lw.endswith(('ing',)) : ok=ok and len(b)>=4 and zb>=4
        if pa and pb and ok:
            sc=min(len(a),len(b))
            if not best or sc>best[0]: best=(sc,pa+demote(pb))
    if best: return best[1],'cmp'
    return one_primary(g(lw)),'g2p'
if __name__=='__main__':
    import sys
    out=[];kinds={}
    for w in open('oov.txt').read().split('\n'):
        w=w.strip()
        if not w: continue
        ph,k=guess(w); kinds[k]=kinds.get(k,0)+1
        if ph: out.append(f"{w.lower()} {' '.join(ph)}  # {k}")
        else: out.append(f"#ABBR {w}")
    open('oov_guess.txt','w').write('\n'.join(out)); print(kinds)
