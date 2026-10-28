# 5.11 起：分成两个独立 App。用法：bash integrate2.sh 版本号 versionCode
#   英语：包名 com.elt.wordcards（沿用老 App，覆盖升级），名称「卡牌游戏英语大冒险」，含基础+进阶词、插图、英语录音
#   日语：包名 com.elt.wordcards.ja（新 App），名称「卡牌游戏日语大冒险」，只含基础词插图和日语录音
set -e
V=$1; VC=$2
S=/tmp/claude-0/-home-claude/93378126-6411-51ca-a02c-bdadc014abd9/scratchpad
W=/mnt/user-data/outputs/word-cards
O=/mnt/user-data/outputs/android
SDK=/usr/lib/android-sdk/platforms/android-23/android.jar
sed -i "s/const APP_VERSION = '[0-9.]*';/const APP_VERSION = '$V';/" $W/index.html
sed -i "s/android:versionCode=\"[0-9]*\" android:versionName=\"[0-9.]*\"/android:versionCode=\"$VC\" android:versionName=\"$V\"/" $S/apk/AndroidManifest.xml
cd $S/apk
# Java 编译一次（R 类在 com.elt.wordcards 包里，两个版本共用）
rm -rf gen obj && mkdir gen obj
aapt package -f -m -J gen -M AndroidManifest.xml -S res -I $SDK
javac -nowarn -Xlint:-options -source 8 -target 8 -bootclasspath $S/sdk36/android.jar -d obj src/com/elt/wordcards/MainActivity.java gen/com/elt/wordcards/R.java 2>/dev/null
dalvik-exchange --dex --output=classes.dex obj 2>/dev/null
python3 -c "
import json,glob
import subprocess
adv=set(w[0] for f in glob.glob('$S/adv_*.json') for sc,ws in json.load(open(f)) for w in ws)
for ch in 'people appearance health home city food study work transport sports leisure environment nature reference'.split():
    for sc,ids in json.loads(subprocess.run(['node','$S/listids.js',ch],capture_output=True,text=True,cwd='$S').stdout): adv-=set(ids)
open('$S/apk/adv_ids.txt','w').write('\n'.join(sorted(adv)))"
for ED in en ja; do
  if [ $ED = en ]; then NAME=卡牌游戏英语大冒险; PKG=com.elt.wordcards; else NAME=卡牌游戏日语大冒险; PKG=com.elt.wordcards.ja; fi
  B=$S/build-$ED; rm -rf $B && mkdir -p $B/assets/www/images $B/assets/www/data $B/res/values
  # 资源：名称 + 图标
  python3 mkicon2.py $ED $B/res
  printf '<?xml version="1.0" encoding="utf-8"?>\n<resources><string name="app_name">%s</string></resources>\n' "$NAME" > $B/res/values/strings.xml
  # 网页：固定语言、改名
  sed "s|var EDITION = null; /\*EDITION\*/|var EDITION = {lang:'$ED', name:'$NAME'};|; s|<title>单词卡牌</title>|<title>$NAME</title>|" $W/index.html > $B/assets/www/index.html
  for f in privacy terms; do sed "s/单词卡牌/$NAME/g" $W/$f.html > $B/assets/www/$f.html; done
  if [ $ED = en ]; then
    (cd $W/data && cp *.js $B/assets/www/data/ && rm -f $B/assets/www/data/audio-ja.js)
    cp $W/images/*.svg $B/assets/www/images/; [ -f $W/images/wechat-qr.png ] && cp $W/images/wechat-qr.png $B/assets/www/images/
    mkdir -p $B/assets/www/audio && cp -r $W/audio/en $B/assets/www/audio/
  else
    (cd $W/data && for f in *.js; do case $f in adv-*|audio-en.js|pron-en.js|stories-en.js|hints*) ;; *) cp $f $B/assets/www/data/;; esac; done)
    cp -r $W/data/ja $B/assets/www/data/
    (cd $W/images && ls *.svg | sed 's/\.svg$//' | grep -vxF -f $S/apk/adv_ids.txt | sed 's/$/.svg/' | xargs -I{} cp {} $B/assets/www/images/) 
    [ -f $W/images/wechat-qr.png ] && cp $W/images/wechat-qr.png $B/assets/www/images/
    mkdir -p $B/assets/www/audio && cp -r $W/audio/ja $B/assets/www/audio/
  fi
  # 去掉指向没打包文件的 <script>（另一种语言的数据）
  python3 -c "
import re,os
p='$B/assets/www/index.html'; s=open(p,encoding='utf-8').read()
s=re.sub(r'<script src=\"([^\"]+)\"></script>\n?', lambda m: m.group(0) if os.path.exists('$B/assets/www/'+m.group(1)) else '', s)
open(p,'w',encoding='utf-8').write(s)"
  rm -f $B/u.apk $B/a.apk $B/out.apk
  aapt package -f -0 arsc -M AndroidManifest.xml --rename-manifest-package $PKG -S $B/res -A $B/assets -I $SDK -F $B/u.apk
  (cp classes.dex $B/ && cd $B && aapt add u.apk classes.dex >/dev/null)
  zipalign -f -p 4 $B/u.apk $B/a.apk
  apksigner sign --v1-signing-enabled true --v2-signing-enabled true --ks "$KEYSTORE" --ks-pass env:KS_PASS --key-pass env:KS_PASS --out $B/out.apk $B/a.apk 2>/dev/null
  apksigner verify $B/out.apk 2>/dev/null
  cp $B/out.apk "$O/$NAME-v$V.apk"
  echo "$ED $(du -h "$O/$NAME-v$V.apk" | cut -f1) svgs=$(ls $B/assets/www/images/*.svg | wc -l) audio=$(find $B/assets/www/audio -name '*.ogg' | wc -l)"
  aapt dump badging "$O/$NAME-v$V.apk" | grep -E "^package|application-label:" | head -2
done
