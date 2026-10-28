# 单词卡牌（Word Cards）

把背单词变成打牌：拆卡包、出牌对战、塔防、听小故事填空，按记忆规律自动安排复习。纯网页实现（一个 `index.html`），可以直接用浏览器打开，也可以打包成安卓 App。

- 英语：14 个生活大区、180 个场景、2880 个基础词，每个词有插图、中文、例句、英文提示、美式音标和重读标注
- 日语：同样 2880 个词（假名 + 罗马音读法）
- 全部单词、例句、提示和听力小故事都有内置录音（离线可用）
- 跟读打分（浏览器 / 手机的语音识别）、录音对比
- 不联网、不注册、无广告，进度保存在本机

> 本仓库只包含程序和基础词部分。安卓正式版里的「进阶词」词库不在本仓库中。

## 快速开始

用 Chrome 或 Edge 打开 `app/index.html` 即可（跟读打分需要联网的语音识别，推荐 Edge）。

## 目录

| 路径 | 内容 |
|---|---|
| `app/index.html` | 全部程序（界面、对战、塔防、复习、录音播放） |
| `app/data/01-…14-*.js` | 英语基础词库（每个文件一个大区） |
| `app/data/hints-*.js`、`hintszh-*.js` | 英文提示及中文 |
| `app/data/stories-en.js` | 180 段听力小故事 |
| `app/data/pron-en.js` | 音节、音标、句子语调标注 |
| `app/data/ja/`、`ko/`、`th/` | 日语、韩语、泰语词库（韩语、泰语目前在界面中隐藏） |
| `app/data/audio-*.js` + `app/audio/` | 内置录音索引和 Opus 音频 |
| `app/images/` | 卡片插图（SVG） |
| `tools/` | 生成插图、读音标注、录音、外语词库、安卓打包的脚本 |

## 安卓打包

`tools/android/` 里有 `MainActivity.java`（WebView 外壳 + 系统语音识别桥）、图标脚本和打包脚本 `integrate2.sh`（aapt / javac / d8 / zipalign / apksigner）。脚本里的路径按自己的环境修改，签名请使用你自己的 keystore（不要提交到仓库）。

## 录音

录音用开源语音模型 [Kokoro-82M](https://github.com/hexgrad/kokoro)（Apache-2.0）离线合成：英语 `af_heart`，日语 `jm_kumo`。脚本在 `tools/tts/`：

1. `node extract.js` / `extract_story.js` / `extract_ja.js` 导出要读的文本
2. `python3 gen.py`（英语）、`python3 gen_ja.py`（日语）合成，可断点续跑
3. `python3 mkmap.py` 生成 `app/audio/` 和 `app/data/audio-*.js`

日语读音以词库里的假名为准（`jag2p.py`），避免汉字误读。

## 许可

- 程序代码（`app/index.html`、`tools/` 里的脚本和安卓源码）：**GNU AGPL-3.0**（见 `LICENSE`）。可以使用、修改、再发布，包括商用，但发布修改版或以网络服务形式提供时，必须以 AGPL-3.0 公开全部源代码。
- 内容（词库文本、例句、提示、小故事、插图、录音）：**CC BY-NC 4.0**（见 `LICENSE-content`）。非商业用途免费，需署名；**商业用途须先取得书面授权**。
- 「卡牌游戏英语大冒险」「卡牌游戏日语大冒险」「单词卡牌」的名称和图标不在开源许可范围内。
- 需要商业授权（例如闭源使用代码、商用内容），请联系 北京英特之星科技有限公司：8071378@qq.com
- 第三方：Kokoro 模型 Apache-2.0；misaki（日语转音素）Apache-2.0；读音标注工具使用 CMU Pronouncing Dictionary（BSD）。

© 2026 北京英特之星科技有限公司
