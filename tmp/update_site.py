import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update html tag
html = html.replace('<html lang="ar" dir="rtl">', '<html lang="en" dir="ltr">')

# 2. Update title & meta description
html = html.replace('<title>سكاي جلاس Sky Glass | غرف زجاجية، كابائن شاور، أبواب منزلقة وبرجولات</title>', '<title>Sky Glass | Glass Rooms, Shower Enclosures, Sliding Facades & Pergolas Egypt</title>')
html = html.replace('content="سكاي جلاس: تصنيع وتركيب الزجاج المعماري بمصر. غرف زجاجية بدون إطار، أنظمة منزلقة، كابائن شاور سيكوريت، برجولات وواجهات زجاجية بضمان 5 سنوات."', 'content="Sky Glass: Architectural glass manufacturing and installation in Egypt. Frameless glass rooms, sliding systems, shower enclosures, pergolas & facades with 5-year warranty."')

# 3. Update CSS for .lang button
old_lang_css = '.lang{background:#fff;border:1px solid var(--line);border-radius:999px;padding:6px 14px;font:700 14px "Cairo",sans-serif;color:var(--blue2);cursor:pointer;box-shadow:0 3px 0 #a9cfe4;transition:transform .1s,box-shadow .1s}'
new_lang_css = '.lang{background:#fff;border:1px solid var(--line);border-radius:999px;padding:6px 14px;font:700 13px system-ui,-apple-system,sans-serif;color:var(--muted);cursor:pointer;box-shadow:0 3px 0 #a9cfe4;transition:transform .12s,box-shadow .12s,border-color .15s;display:inline-flex;align-items:center;gap:5px;user-select:none}.lang:hover{border-color:var(--blue);transform:translateY(-1px);box-shadow:0 4px 0 #a9cfe4}.lang:active{transform:translateY(2px);box-shadow:0 1px 0 #a9cfe4}.lang .l-sep{opacity:.35;font-weight:400}html[lang=en] .lang .l-en{color:var(--blue);font-weight:800}html[lang=en] .lang .l-ar{color:var(--muted);opacity:.65}html[lang=ar] .lang .l-ar{color:var(--blue);font-weight:800}html[lang=ar] .lang .l-en{color:var(--muted);opacity:.65}'
assert old_lang_css in html, "old_lang_css not found"
html = html.replace(old_lang_css, new_lang_css)

# 4. Update Header button
old_btn = '<button class="lang" id="lang" type="button" aria-label="Language">EN</button>'
new_btn = '<button class="lang" id="lang" type="button" aria-label="Toggle Language / تغيير اللغة"><span class="l-en">EN</span><span class="l-sep">|</span><span class="l-ar">AR</span></button>'
assert old_btn in html, "old_btn not found"
html = html.replace(old_btn, new_btn)

# Add language toggle into mobile nav
old_mobnav_end = '</div></header>'
new_mobnav_end = '<div style="padding:12px 0 4px;display:flex;align-items:center;justify-content:space-between;border-top:1px dashed var(--line);margin-top:6px"><span style="font-weight:700;font-size:14px;color:var(--muted)"><span class="ar">تغيير اللغة</span><span class="en">Switch Language</span></span><button class="lang" id="lang-mob" type="button" aria-label="Toggle Language / تغيير اللغة"><span class="l-en">EN</span><span class="l-sep">|</span><span class="l-ar">AR</span></button></div></div></header>'
assert old_mobnav_end in html, "old_mobnav_end not found"
html = html.replace(old_mobnav_end, new_mobnav_end)

# 5. Update Hero slides aria-labels to 1 / 6, 2 / 6, etc.
for i in range(1, 6):
    html = html.replace(f'aria-label="{i} / 5"', f'aria-label="{i} / 6"')

# 6. Add Slide 6 after Slide 5
slide5_marker = '</div></div></div></div>  <div class="hs-bot">'
slide6_html = '''</div></div></div></div><div class="hs-s" role="group" aria-roledescription="slide" aria-label="6 / 6" aria-hidden="true">  <img src="/assets/projects/luxury_tinted_pergola_lawn.jpg" alt="برجولة زجاجية مظللة فاخرة - سكاي جلاس" style="object-position:50% 38%" loading="lazy">  <div class="hs-in"><div class="wrap"><div class="hs-t">    <span class="badge"><span class="ar">برجولات زجاجية مظللة للحدائق</span><span class="en">Luxury Tinted Garden Pergolas</span></span>    <div class="hs-h" role="heading" aria-level="2"><span class="ar">برجولات زجاجية <b class="hl">مظللة</b> للهواء الطلق</span><span class="en">Luxury Outdoor <b class="hl">Tinted Glass</b> Pergolas</span></div>    <p><span class="ar">أنظمة زجاج سيكوريت عازل ومظلل للحدائق وتراسات الفلل، توفر خصوصية كاملة وحماية فائقة مع إطلالة طبيعية خلابة.</span><span class="en">Engineered tempered tinted glass pergolas for villa gardens and terraces, delivering privacy, weather protection, and panoramic landscape views.</span></p>    <div class="acts"><a class="btn" href="#contact"><span class="ar">اطلب عرض سعر</span><span class="en">Get a quote</span></a><a class="btn ghost" href="#projects"><span class="ar">أعمال البرجولات</span><span class="en">Pergola Projects</span></a></div>  </div></div></div></div>  <div class="hs-bot">'''
assert slide5_marker in html, "slide5_marker not found"
html = html.replace(slide5_marker, slide6_html)

# 7. Add 6th dot button
old_dots = '<span class="hs-ds"><button type="button" class="hs-d on" aria-label="1"></button><button type="button" class="hs-d" aria-label="2"></button><button type="button" class="hs-d" aria-label="3"></button><button type="button" class="hs-d" aria-label="4"></button><button type="button" class="hs-d" aria-label="5"></button></span>'
new_dots = '<span class="hs-ds"><button type="button" class="hs-d on" aria-label="1"></button><button type="button" class="hs-d" aria-label="2"></button><button type="button" class="hs-d" aria-label="3"></button><button type="button" class="hs-d" aria-label="4"></button><button type="button" class="hs-d" aria-label="5"></button><button type="button" class="hs-d" aria-label="6"></button></span>'
assert old_dots in html, "old_dots not found"
html = html.replace(old_dots, new_dots)

# 8. Add new videos to #videos section
new_videos_html = '''    <!-- Video 7 (New) -->
    <div class="video-card">
      <div class="video-wrapper" onclick="openLightboxVideo('/assets/projects/video_panoramic_enclosure.mp4', 'جولة داخلية لغرفة زجاجية ممتدة بانورامية', 'Panoramic Glass Room Enclosure Walkthrough')">
        <video poster="/assets/projects/video_panoramic_poster.jpg" preload="none" muted playsinline>
          <source src="/assets/projects/video_panoramic_enclosure.mp4" type="video/mp4">
        </video>
        <span class="video-tag"><span class="ar">تغطيات بانورامية</span><span class="en">Panoramic Room</span></span>
        <div class="video-play-overlay">
          <div class="play-btn-circle">
            <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
          </div>
        </div>
      </div>
      <div class="video-desc">
        <h4><span class="ar">جولة داخلية لغرفة زجاجية ممتدة</span><span class="en">Panoramic Glass Enclosure Walkthrough</span></h4>
        <p><span class="ar">استعراض متكامل للألواح الزجاجية البانورامية وإطلالة السماء والإضاءة الطبيعية الممتدة.</span><span class="en">Full walkthrough highlighting panoramic glass panels, sky views, and abundant daylight.</span></p>
      </div>
    </div>
    <!-- Video 8 (New) -->
    <div class="video-card">
      <div class="video-wrapper" onclick="openLightboxVideo('/assets/projects/video_terrace_sliding.mp4', 'منظومة أبواب سحابة للتراس والحديقة', 'Sliding Glass Terrace System Live Demonstration')">
        <video poster="/assets/projects/video_terrace_poster.jpg" preload="none" muted playsinline>
          <source src="/assets/projects/video_terrace_sliding.mp4" type="video/mp4">
        </video>
        <span class="video-tag"><span class="ar">واجهات منزلقة</span><span class="en">Sliding System</span></span>
        <div class="video-play-overlay">
          <div class="play-btn-circle">
            <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
          </div>
        </div>
      </div>
      <div class="video-desc">
        <h4><span class="ar">منظومة أبواب سحابة للتراس والحديقة</span><span class="en">Sliding Glass Terrace System</span></h4>
        <p><span class="ar">حركة سريعة وانسيابية ومحاذاة مثالية للأبواب الزجاجية الكبيرة بإكسسوارات قوية.</span><span class="en">Ultra-smooth sliding operation with precision alignment for wide patio openings.</span></p>
      </div>
    </div>
    <!-- Video 9 (New) -->
    <div class="video-card">
      <div class="video-wrapper" onclick="openLightboxVideo('/assets/projects/video_frameless_walkthrough.mp4', 'معاينة هندسية وتشغيل الواجهة الزجاجية', 'Architectural Glass System Operation & Sealing')">
        <video poster="/assets/projects/video_frameless_poster.jpg" preload="none" muted playsinline>
          <source src="/assets/projects/video_frameless_walkthrough.mp4" type="video/mp4">
        </video>
        <span class="video-tag"><span class="ar">تصنيع وتركيب</span><span class="en">Precision Fitting</span></span>
        <div class="video-play-overlay">
          <div class="play-btn-circle">
            <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor"><polygon points="6 3 20 12 6 21 6 3"/></svg>
          </div>
        </div>
      </div>
      <div class="video-desc">
        <h4><span class="ar">معاينة هندسية وتشغيل الواجهة الزجاجية</span><span class="en">Architectural Glass System Operation</span></h4>
        <p><span class="ar">اختبار عملي لكفاءة الفتح والغلق ومقاومة العوامل الجوية بأيدي فريق سكاي جلاس المتخصص.</span><span class="en">Field test demonstrating weatherproof sealing and smooth multidirectional movement.</span></p>
      </div>
    </div>'''

vid_anchor = '      </div>\n    </div>\n  </div>\n</div></section>'
assert vid_anchor in html, "vid_anchor not found"
html = html.replace(vid_anchor, f'      </div>\n    </div>\n{new_videos_html}\n  </div>\n</div></section>')

# 9. Add new featured item in #projects-grid under pergolas
new_project_item = '''    <!-- Item 15 (New Hero Pergola Project) -->
    <figure class="gal-item" data-cat="pergolas" onclick="openLightboxImage('/assets/projects/luxury_tinted_pergola_lawn.jpg', 'برجولة حديقة بزجاج معتم مع فريق سكاي جلاس', 'Luxury Tinted Glass Garden Pergola with Sky Glass Team')">
      <div class="img-box">
        <span class="gal-tag"><span class="ar">برجولة معتمة</span><span class="en">Tinted Pergola</span></span>
        <img src="/assets/projects/luxury_tinted_pergola_lawn.jpg" alt="برجولة حديقة بزجاج معتم فاخر وفريق سكاي جلاس" loading="lazy">
      </div>
      <figcaption>
        <b><span class="ar">برجولة حديقة بزجاج معتم فاخر</span><span class="en">Luxury Tinted Glass Garden Pergola</span></b>
        <span><span class="ar">تصميم عصري متكامل مع إطلالة الحديقة وفريق تركيب سكاي جلاس</span><span class="en">Full custom garden pavilion with privacy tint and Sky Glass installation</span></span>
      </figcaption>
    </figure>'''

proj_grid_end = '    </figure>\n  </div>\n\n  <div style="text-align:center;margin-top:38px">'
assert proj_grid_end in html, "proj_grid_end not found"
html = html.replace(proj_grid_end, f'    </figure>\n{new_project_item}\n  </div>\n\n  <div style="text-align:center;margin-top:38px">')

# 10. Update JavaScript Language Logic to default to English and always start with English
old_js_lang = '''// Language Toggle (Arabic / English)
var lb = document.getElementById("lang"), cur = "ar";
function setLang(l){
  cur = l;
  var h = document.documentElement;
  h.lang = l;
  h.dir = (l === "ar") ? "rtl" : "ltr";
  document.title = (l === "ar")
    ? "سكاي جلاس Sky Glass | غرف زجاجية، كابائن شاور، أبواب منزلقة وبرجولات"
    : "Sky Glass | Glass Rooms, Shower Enclosures, Sliding Facades & Pergolas";
  document.querySelectorAll("option[data-en]").forEach(function(o){
    o.textContent = (l === "ar") ? o.dataset.ar : o.dataset.en;
  });
  if(lb) lb.textContent = (l === "ar") ? "EN" : "ع";
  if(m) m.setAttribute("aria-label", (l === "ar") ? "القائمة" : "Menu");
  try{ localStorage.setItem("lang", l); }catch(e){}
}
if(lb) lb.addEventListener("click", function(){ setLang(cur === "ar" ? "en" : "ar"); });
try{ if(localStorage.getItem("lang") === "en"){ setLang("en"); } }catch(e){}'''

new_js_lang = '''// Language Toggle (Arabic / English) - Default English on every visit
var lb = document.getElementById("lang"), lbm = document.getElementById("lang-mob"), cur = "en";
function setLang(l){
  cur = l;
  var h = document.documentElement;
  h.lang = l;
  h.dir = (l === "ar") ? "rtl" : "ltr";
  document.title = (l === "ar")
    ? "سكاي جلاس Sky Glass | غرف زجاجية، كابائن شاور، أبواب منزلقة وبرجولات"
    : "Sky Glass | Glass Rooms, Shower Enclosures, Sliding Facades & Pergolas";
  document.querySelectorAll("option[data-en]").forEach(function(o){
    o.textContent = (l === "ar") ? o.dataset.ar : o.dataset.en;
  });
  var inpN = document.querySelector('input[name="n"]');
  if(inpN) inpN.placeholder = (l === "ar") ? "مثال: م. أحمد خليل" : "e.g. Eng. Ahmed Khalil";
  var inpP = document.querySelector('input[name="p"]');
  if(inpP) inpP.placeholder = (l === "ar") ? "01xxxxxxxxx" : "01xxxxxxxxx";
  var txtD = document.querySelector('textarea[name="d"]');
  if(txtD) txtD.placeholder = (l === "ar") ? "الموقع (المدينة / الكمبوند)، المقاسات التقريبية، وأي متطلبات خاصة..." : "Project location (city / compound), approximate dimensions, and special requirements...";
  if(m) m.setAttribute("aria-label", (l === "ar") ? "القائمة" : "Menu");
}
function toggleLang(){
  setLang(cur === "ar" ? "en" : "ar");
}
if(lb) lb.addEventListener("click", toggleLang);
if(lbm) lbm.addEventListener("click", toggleLang);
// Always load in English on every visit as requested
setLang("en");'''

assert old_js_lang in html, "old_js_lang not found"
html = html.replace(old_js_lang, new_js_lang)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('public/assets/aistudio/__________99471508.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Success!')
