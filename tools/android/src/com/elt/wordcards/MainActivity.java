package com.elt.wordcards;

import android.Manifest;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.SharedPreferences;
import android.graphics.Insets;
import android.net.Uri;
import android.os.Build;
import android.provider.Settings;
import android.text.SpannableStringBuilder;
import android.text.Spanned;
import android.text.method.LinkMovementMethod;
import android.text.style.ClickableSpan;
import android.util.TypedValue;
import android.view.View;
import android.view.WindowInsets;
import android.widget.FrameLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.window.OnBackInvokedCallback;
import android.window.OnBackInvokedDispatcher;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Color;
import android.os.Bundle;
import android.speech.RecognitionListener;
import android.speech.RecognizerIntent;
import android.speech.SpeechRecognizer;
import android.speech.tts.TextToSpeech;
import android.webkit.JavascriptInterface;
import android.webkit.PermissionRequest;
import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import java.util.ArrayList;
import java.util.Locale;
import org.json.JSONArray;
import org.json.JSONObject;

/** 单词卡牌：网页版装进 App；读音用手机的文字转语音，跟读用手机的语音识别。 */
public class MainActivity extends Activity implements TextToSpeech.OnInitListener {
    private static final int REQ_MIC = 11, REQ_SPEECH = 12;
    private WebView web;
    private TextToSpeech tts;
    private volatile boolean ttsReady = false;
    private SpeechRecognizer recognizer;
    private String target = "";               // 要跟读的内容，用来提示识别器
    private boolean wordMode = true;          // 单词模式：短词用搜索式识别
    private ArrayList<String> lastPartial;    // 识别过程中的半成品结果
    private volatile String langTag = "en-US";   // 正在学的语言（英语 en-US / 泰语 th-TH ……）
    private volatile int langStatus = -1;          // 1 = 手机有这种语言的语音，0 = 没有，-1 = 还不知道
    private static final int PRIVACY_VERSION = 1;  // 隐私政策有重大修改时 +1，用户需要重新同意
    private SharedPreferences prefs;
    private FrameLayout root;
    private static final int BG = Color.rgb(29, 28, 25);

    @Override
    protected void onCreate(Bundle state) {
        super.onCreate(state);
        getWindow().setStatusBarColor(BG);
        getWindow().setNavigationBarColor(BG);
        prefs = getSharedPreferences("wordcards", MODE_PRIVATE);
        root = new FrameLayout(this);
        root.setBackgroundColor(BG);
        setContentView(root);
        // Android 15 起应用默认铺满全屏：给内容让出状态栏、导航栏和刘海的位置
        if (Build.VERSION.SDK_INT >= 35) {
            root.setOnApplyWindowInsetsListener(new View.OnApplyWindowInsetsListener() {
                public WindowInsets onApplyWindowInsets(View v, WindowInsets wi) {
                    Insets i = wi.getInsets(WindowInsets.Type.systemBars() | WindowInsets.Type.displayCutout() | WindowInsets.Type.ime());
                    v.setPadding(i.left, i.top, i.right, i.bottom);
                    return WindowInsets.CONSUMED;
                }
            });
        }
        // Android 13 起的返回手势
        if (Build.VERSION.SDK_INT >= 33) {
            getOnBackInvokedDispatcher().registerOnBackInvokedCallback(OnBackInvokedDispatcher.PRIORITY_DEFAULT,
                new OnBackInvokedCallback() { public void onBackInvoked() { handleBack(); } });
        }
        // 先同意隐私政策，才开始使用（同意前不启动任何功能）
        if (prefs.getInt("privacy", 0) >= PRIVACY_VERSION) startApp();
        else showPrivacy();
    }

    // ================= 隐私政策 =================
    private int dp(float v) { return (int) TypedValue.applyDimension(TypedValue.COMPLEX_UNIT_DIP, v, getResources().getDisplayMetrics()); }

    private TextView bigText(CharSequence t) {
        TextView tv = new TextView(this);
        tv.setText(t);
        tv.setTextSize(TypedValue.COMPLEX_UNIT_SP, 19);
        tv.setLineSpacing(0, 1.3f);
        tv.setTextColor(Color.rgb(40, 38, 34));
        tv.setPadding(dp(22), dp(14), dp(22), dp(6));
        return tv;
    }

    private void link(SpannableStringBuilder b, String text, final String doc) {
        int st = b.length();
        b.append(text);
        b.setSpan(new ClickableSpan() { public void onClick(View v) { showDoc(doc); } }, st, b.length(), Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
    }

    private AlertDialog.Builder dialog() {
        return new AlertDialog.Builder(this, android.R.style.Theme_Material_Light_Dialog_Alert);
    }

    private void bigButtons(AlertDialog d) {
        for (int w : new int[]{DialogInterface.BUTTON_POSITIVE, DialogInterface.BUTTON_NEGATIVE, DialogInterface.BUTTON_NEUTRAL}) {
            if (d.getButton(w) != null) d.getButton(w).setTextSize(TypedValue.COMPLEX_UNIT_SP, 19);
        }
    }

    private void showPrivacy() {
        SpannableStringBuilder b = new SpannableStringBuilder();
        b.append("欢迎使用「单词卡牌」！\n\n在您开始使用前，请仔细阅读");
        link(b, "《隐私政策》", "privacy");
        b.append("和");
        link(b, "《用户协议》", "terms");
        b.append("。我们向您简单说明：\n\n"
            + "1. 本应用不联网、不需要注册，没有广告，不收集您的姓名、手机号、位置等个人信息。\n"
            + "2. 学习进度只保存在这部手机里，不会上传。\n"
            + "3. 只有在您点「跟读」时，才会申请使用麦克风，用来听您的发音并打分；您可以拒绝，其他功能照常使用。\n\n"
            + "点「同意」表示您已阅读并同意上述内容。");
        TextView tv = bigText(b);
        tv.setMovementMethod(LinkMovementMethod.getInstance());
        tv.setLinkTextColor(Color.rgb(46, 110, 60));
        ScrollView sv = new ScrollView(this);
        sv.addView(tv);
        AlertDialog d = dialog().setTitle("隐私政策和用户协议").setView(sv).setCancelable(false)
            .setPositiveButton("同意", new DialogInterface.OnClickListener() { public void onClick(DialogInterface di, int w) {
                prefs.edit().putInt("privacy", PRIVACY_VERSION).apply();
                startApp();
            } })
            .setNegativeButton("不同意", new DialogInterface.OnClickListener() { public void onClick(DialogInterface di, int w) { confirmDisagree(); } })
            .create();
        d.show(); bigButtons(d);
    }

    private void confirmDisagree() {
        AlertDialog d = dialog().setTitle("温馨提示").setCancelable(false)
            .setView(bigText("需要您同意《隐私政策》和《用户协议》后才能使用「单词卡牌」。\n\n本应用不联网、不收集个人信息，您可以放心使用。如果仍不同意，应用将退出。"))
            .setPositiveButton("再看看", new DialogInterface.OnClickListener() { public void onClick(DialogInterface di, int w) { showPrivacy(); } })
            .setNegativeButton("退出应用", new DialogInterface.OnClickListener() { public void onClick(DialogInterface di, int w) { finishAndRemoveTask(); } })
            .create();
        d.show(); bigButtons(d);
    }

    /** 显示隐私政策 / 用户协议全文（应用里自带的网页，不联网） */
    private void showDoc(String doc) {
        WebView w = new WebView(this);
        w.getSettings().setJavaScriptEnabled(false);
        w.getSettings().setTextZoom(100);
        w.setWebViewClient(new WebViewClient());
        w.loadUrl("file:///android_asset/www/" + doc + ".html");
        w.setLayoutParams(new FrameLayout.LayoutParams(-1, (int) (getResources().getDisplayMetrics().heightPixels * 0.7)));
        FrameLayout box = new FrameLayout(this);
        box.addView(w);
        AlertDialog d = dialog().setView(box).setPositiveButton("关闭", null).create();
        d.show(); bigButtons(d);
    }

    /** 撤回同意：清除记录并退出，下次打开重新询问 */
    private void revokePrivacy() {
        AlertDialog d = dialog().setTitle("撤回同意")
            .setView(bigText("撤回后，应用会立即退出；下次打开时需要重新同意才能使用。\n\n您的学习进度仍保存在手机里，不会被删除。如要删除，请在「设置」里点「清空全部进度」，或直接卸载应用。"))
            .setPositiveButton("确定撤回", new DialogInterface.OnClickListener() { public void onClick(DialogInterface di, int w) {
                prefs.edit().remove("privacy").apply();
                finishAndRemoveTask();
            } })
            .setNegativeButton("取消", null).create();
        d.show(); bigButtons(d);
    }

    // ================= 麦克风：用到时先说明用途，再请系统授权 =================
    private interface Then { void go(boolean ok); }
    private Then micThen;

    private void askMic(final Then then) {
        if (checkSelfPermission(Manifest.permission.RECORD_AUDIO) == PackageManager.PERMISSION_GRANTED) { then.go(true); return; }
        final boolean askedBefore = prefs.getBoolean("micAsked", false);
        // 以前拒绝过并选了「不再询问」：系统不会再弹窗，只能去设置里打开
        if (askedBefore && !shouldShowRequestPermissionRationale(Manifest.permission.RECORD_AUDIO)) {
            AlertDialog d = dialog().setTitle("需要麦克风权限")
                .setView(bigText("跟读打分要用麦克风听您的发音。您之前关闭了这个权限。\n\n请在手机设置里打开：「权限」→「麦克风」→「允许」。"))
                .setPositiveButton("去设置", new DialogInterface.OnClickListener() { public void onClick(DialogInterface di, int w) {
                    try { startActivity(new Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS, Uri.parse("package:" + getPackageName()))); } catch (Exception e) {}
                    then.go(false);
                } })
                .setNegativeButton("暂不", new DialogInterface.OnClickListener() { public void onClick(DialogInterface di, int w) { then.go(false); } })
                .setCancelable(false).create();
            d.show(); bigButtons(d);
            return;
        }
        AlertDialog d = dialog().setTitle("🎤 使用麦克风")
            .setView(bigText("跟读需要使用麦克风：\n\n• 只在您点「跟读」或「录音」时才听；\n• 声音交给手机自带的语音识别来打分；\n• 本应用不保存、不上传您的录音。\n\n接下来手机会询问是否允许，请点「允许」或「仅使用期间允许」。"))
            .setPositiveButton("好的", new DialogInterface.OnClickListener() { public void onClick(DialogInterface di, int w) {
                prefs.edit().putBoolean("micAsked", true).apply();
                micThen = then;
                requestPermissions(new String[]{Manifest.permission.RECORD_AUDIO}, REQ_MIC);
            } })
            .setNegativeButton("暂不", new DialogInterface.OnClickListener() { public void onClick(DialogInterface di, int w) { then.go(false); } })
            .setCancelable(false).create();
        d.show(); bigButtons(d);
    }

    private void startApp() {
        web = new WebView(this);
        web.setBackgroundColor(Color.rgb(36, 35, 31));
        root.addView(web, new FrameLayout.LayoutParams(-1, -1));
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setAllowFileAccess(true);
        s.setTextZoom(100);
        s.setMediaPlaybackRequiresUserGesture(false);
        web.setWebChromeClient(new WebChromeClient() {
            // 网页里的「录音对比」要用麦克风：有权限就放行，没有就先问用户
            @Override
            public void onPermissionRequest(final PermissionRequest req) {
                runOnUiThread(new Runnable() { public void run() {
                    askMic(new Then() { public void go(boolean ok) {
                        if (ok) req.grant(req.getResources()); else req.deny();
                    } });
                } });
            }
        });
        web.setWebViewClient(new WebViewClient());
        web.addJavascriptInterface(new Bridge(), "AndroidTTS");
        tts = new TextToSpeech(this, this);
        web.loadUrl("file:///android_asset/www/index.html");
    }

    @Override
    public void onInit(int status) {
        if (status != TextToSpeech.SUCCESS) return;
        ttsReady = true;
        applyLang();
    }

    /** 按正在学的语言设置发音 */
    private void applyLang() {
        if (!ttsReady) return;
        Locale loc = Locale.forLanguageTag(langTag);
        int r = tts.setLanguage(loc);
        if (r == TextToSpeech.LANG_MISSING_DATA || r == TextToSpeech.LANG_NOT_SUPPORTED) {
            r = tts.setLanguage(new Locale(loc.getLanguage()));
        }
        langStatus = (r == TextToSpeech.LANG_MISSING_DATA || r == TextToSpeech.LANG_NOT_SUPPORTED) ? 0 : 1;
        if (langStatus == 0 && langTag.startsWith("en")) tts.setLanguage(Locale.ENGLISH);
    }

    /** 把结果交给网页 */
    private void js(final String code) {
        web.post(new Runnable() { public void run() { web.evaluateJavascript(code, null); } });
    }

    private Intent speechIntent() {
        Intent i = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
        i.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL,
                wordMode ? RecognizerIntent.LANGUAGE_MODEL_WEB_SEARCH : RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
        i.putExtra(RecognizerIntent.EXTRA_PARTIAL_RESULTS, true);
        // 多等一会儿再结束，老人停顿一下不会被截断
        i.putExtra(RecognizerIntent.EXTRA_SPEECH_INPUT_COMPLETE_SILENCE_LENGTH_MILLIS, 1500L);
        i.putExtra(RecognizerIntent.EXTRA_SPEECH_INPUT_POSSIBLY_COMPLETE_SILENCE_LENGTH_MILLIS, 1500L);
        i.putExtra(RecognizerIntent.EXTRA_SPEECH_INPUT_MINIMUM_LENGTH_MILLIS, 800L);
        // 告诉识别器要读的是哪个词（Android 13 以上有效）
        if (target != null && target.length() > 0) {
            ArrayList<String> bias = new ArrayList<String>();
            bias.add(target);
            i.putStringArrayListExtra("android.speech.extra.BIASING_STRINGS", bias);
        }
        i.putExtra(RecognizerIntent.EXTRA_LANGUAGE, langTag);
        i.putExtra(RecognizerIntent.EXTRA_LANGUAGE_PREFERENCE, langTag);
        i.putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 5);
        i.putExtra(RecognizerIntent.EXTRA_PROMPT, langTag.startsWith("th") ? "请用泰语读出来" : langTag.startsWith("ja") ? "请用日语读出来" : langTag.startsWith("ko") ? "请用韩语读出来" : "请用英语读出来");
        i.putExtra(RecognizerIntent.EXTRA_CALLING_PACKAGE, getPackageName());
        return i;
    }

    private void startListen() {
        if (checkSelfPermission(Manifest.permission.RECORD_AUDIO) != PackageManager.PERMISSION_GRANTED) {
            askMic(new Then() { public void go(boolean ok) {
                if (ok) startListen(); else js("onSpeechError('denied')");
            } });
            return;
        }
        if (ttsReady) tts.stop();
        lastPartial = null;
        if (SpeechRecognizer.isRecognitionAvailable(this)) {
            if (recognizer == null) {
                recognizer = SpeechRecognizer.createSpeechRecognizer(this);
                recognizer.setRecognitionListener(new Listener());
            }
            recognizer.cancel();
            recognizer.startListening(speechIntent());
        } else {
            try { startActivityForResult(speechIntent(), REQ_SPEECH); }
            catch (Exception e) { js("onSpeechError('unavailable')"); }
        }
    }

    private void sendResults(ArrayList<String> list) {
        if (list == null || list.isEmpty()) list = lastPartial;
        if (list == null || list.isEmpty()) { js("onSpeechError('no-match')"); return; }
        js("onSpeechResult(" + new JSONArray(list).toString() + ")");
    }

    class Listener implements RecognitionListener {
        public void onReadyForSpeech(Bundle b) { js("onSpeechReady()"); }
        public void onBeginningOfSpeech() { js("window.onSpeechHeard&&onSpeechHeard()"); }
        public void onRmsChanged(float v) {}
        public void onBufferReceived(byte[] b) {}
        public void onEndOfSpeech() {}
        public void onError(int e) {
            // 短单词常被判成"没听清"(7)或"超时"(6)：如果过程中已经听到了内容，就用它来打分
            if ((e == SpeechRecognizer.ERROR_NO_MATCH || e == SpeechRecognizer.ERROR_SPEECH_TIMEOUT)
                    && lastPartial != null && !lastPartial.isEmpty()) { sendResults(lastPartial); return; }
            js("onSpeechError(" + e + ")");
        }
        public void onResults(Bundle b) { sendResults(b.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION)); }
        public void onPartialResults(Bundle b) {
            ArrayList<String> r = b.getStringArrayList(SpeechRecognizer.RESULTS_RECOGNITION);
            if (r != null && !r.isEmpty() && r.get(0) != null && r.get(0).trim().length() > 0) lastPartial = r;
        }
        public void onEvent(int t, Bundle b) {}
    }

    @Override
    public void onRequestPermissionsResult(int code, String[] perms, int[] grants) {
        if (code != REQ_MIC || micThen == null) return;
        Then t = micThen; micThen = null;
        t.go(grants.length > 0 && grants[0] == PackageManager.PERMISSION_GRANTED);
    }

    @Override
    protected void onActivityResult(int code, int result, Intent data) {
        super.onActivityResult(code, result, data);
        if (code != REQ_SPEECH) return;
        if (result == RESULT_OK && data != null) sendResults(data.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS));
        else js("onSpeechError('no-speech')");
    }

    class Bridge {
        @JavascriptInterface
        public void speak(String text, float rate, boolean queue) {
            if (!ttsReady || text == null) return;
            tts.setSpeechRate(rate);
            tts.speak(text, queue ? TextToSpeech.QUEUE_ADD : TextToSpeech.QUEUE_FLUSH, null, "w" + System.nanoTime());
        }

        @JavascriptInterface
        public void stop() { if (ttsReady) tts.stop(); }

        @JavascriptInterface
        public boolean ready() { return ttsReady; }

        /** 切换正在学的语言，例如 "th-TH" */
        @JavascriptInterface
        public void setLang(String tag) {
            if (tag == null || tag.length() == 0) return;
            langTag = tag; langStatus = -1;
            runOnUiThread(new Runnable() { public void run() { applyLang(); } });
        }

        /** 手机有没有这种语言的语音：1 有，0 没有，-1 还不知道 */
        @JavascriptInterface
        public int langStatus() { return langStatus; }

        /** 打开手机的「文字转语音」设置，方便下载语音包 */
        @JavascriptInterface
        public void openTtsSettings() {
            runOnUiThread(new Runnable() { public void run() {
                try { Intent i = new Intent("com.android.settings.TTS_SETTINGS"); i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK); startActivity(i); }
                catch (Exception e) {
                    try { Intent i = new Intent(TextToSpeech.Engine.ACTION_INSTALL_TTS_DATA); i.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK); startActivity(i); } catch (Exception e2) {}
                }
            } });
        }

        @JavascriptInterface
        public void listen(final String text, final String kind) {
            runOnUiThread(new Runnable() { public void run() {
                target = text == null ? "" : text;
                wordMode = !"sentence".equals(kind);
                startListen();
            } });
        }

        /** 打开隐私政策 / 用户协议全文 */
        @JavascriptInterface
        public void openDoc(final String doc) {
            if (!"privacy".equals(doc) && !"terms".equals(doc)) return;
            runOnUiThread(new Runnable() { public void run() { showDoc(doc); } });
        }

        /** 撤回隐私政策同意 */
        @JavascriptInterface
        public void revokePrivacy() {
            runOnUiThread(new Runnable() { public void run() { MainActivity.this.revokePrivacy(); } });
        }

        @JavascriptInterface
        public void stopListen() {
            runOnUiThread(new Runnable() { public void run() { if (recognizer != null) recognizer.cancel(); } });
        }
    }

    @Override
    public void onBackPressed() { handleBack(); }

    private void handleBack() {
        if (web == null) { finish(); return; }
        web.evaluateJavascript("typeof androidBack==='function'?androidBack():'exit'", new ValueCallback<String>() {
            @Override
            public void onReceiveValue(String v) { if (v == null || v.contains("exit")) finish(); }
        });
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (web != null) web.onPause();      // 切到后台：网页暂停，不计学习时间
        if (ttsReady) tts.stop();
        if (recognizer != null) recognizer.cancel();
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (web != null) web.onResume();
    }

    @Override
    protected void onDestroy() {
        if (tts != null) tts.shutdown();
        if (recognizer != null) recognizer.destroy();
        if (web != null) web.destroy();
        super.onDestroy();
    }
}
