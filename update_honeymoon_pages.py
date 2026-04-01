from pathlib import Path

def update_file(path, replacements, insert_marker, insert_html):
    p = Path(path)
    t = p.read_text(encoding='utf-8')
    for old, new in replacements.items():
        t = t.replace(old, new)
    if insert_marker and insert_html and insert_marker in t:
        t = t.replace(insert_marker, insert_html + insert_marker)
    p.write_text(t, encoding='utf-8')

# 6N7D updates
path6 = 'honeymoon-6n7d.html'
repl6 = {
    '<title>Andaman 6N7D Package — Andaman Tours</title>': '<title>Andaman 6N7D Package — Andaman Tours</title>',
    '<strong>6 Days / 7 Nights</strong>Duration': '<strong>7 Days / 6 Nights</strong>Duration',
    'The most complete Andaman experience. Six days across five islands': 'The most complete Andaman experience. Seven days across six islands',
    '<div class="section-title">Your <em>Andaman</em><br>6-Day Itinerary</div>': '<div class="section-title">Your <em>Andaman</em><br>7-Day Itinerary</div>',
    '<li>5 breakfasts included</li>': '<li>6 breakfasts included</li>',
    '<div class="section-title">What Makes 5N6D<br>The <em>Ultimate</em> Choice</div>': '<div class="section-title">What Makes 6N7D<br>The <em>Ultimate</em> Choice</div>',
    'Book 5N6D Package': 'Book 6N7D Package',
    'Ready for<br><em>Six Days in Andaman?</em>': 'Ready for<br><em>Seven Days in Andaman?</em>',
    '5 nights accommodation (3★–4★ hotels, twin sharing)': '6 nights accommodation (3★–4★ hotels, twin sharing)',
    'Daily breakfast (5 breakfasts)': 'Daily breakfast (6 breakfasts)',
    'Andaman 5N6D — ₹27,999': 'Andaman 6N7D — ₹35,999',
    'andaman-5n6d-package.html': 'andaman-6n7d-package.html',
    '<a href="andaman-6n7d-package.html" class="compare-btn active-pkg">6N7D — ₹35,999 ✦</a>': '<a href="andaman-6n7d-package.html" class="compare-btn active-pkg">6N7D — ₹35,999 ✦</a>'
}

insert_marker = '    </div>\n  </div>\n</section>\n\n<!-- HIGHLIGHTS -->'
insert_html_6 = '''      <div class="day-card">
        <div class="day-num">Day 07 · Leisure</div>
        <div class="day-title">Port Blair — Relaxation & Local Culture</div>
        <img class="day-img" src="https://images.unsplash.com/photo-1501436513142-3d1207f0da83?w=700&q=80" alt="Port Blair Leisure">
        <p class="day-body">Enjoy a relaxed morning with breakfast at your hotel. Explore local markets, historic sites like the Anthropological Museum, and optional activities such as a sunset cruise or spa session. Prepare for the final departure day with a romantic dinner by the sea.</p>
        <div class="day-activities">
          <div class="activity-tag">☕ Leisurely Morning</div>
          <div class="activity-tag">🛍️ Local Market</div>
          <div class="activity-tag">🌅 Sunset Cruise</div>
          <div class="activity-tag">🧖 Spa Options</div>
        </div>
      </div>\n'''

update_file(path6, repl6, insert_marker, insert_html_6)

# 7N8D updates
path7 = 'honeymoon-7n8d.html'
repl7 = {
    '<title>Andaman 7N8D Package — Andaman Tours</title>': '<title>Andaman 7N8D Package — Andaman Tours</title>',
    '<div class="badge-val">7 Nights · 8 Days</div>': '<div class="badge-val">7 Nights · 8 Days</div>',
    '<strong>8 Days / 7 Nights</strong>Duration': '<strong>8 Days / 7 Nights</strong>Duration',
    'The most complete Andaman experience. Eight days across six islands': 'The most complete Andaman experience. Eight days across six islands',
    '<div class="section-title">Your <em>Andaman</em><br>8-Day Itinerary</div>': '<div class="section-title">Your <em>Andaman</em><br>8-Day Itinerary</div>',
    '<li>7 breakfasts included</li>': '<li>7 breakfasts included</li>',
    '<div class="section-title">What Makes 7N8D<br>The <em>Ultimate</em> Choice</div>': '<div class="section-title">What Makes 7N8D<br>The <em>Ultimate</em> Choice</div>',
    'Book 7N8D Package': 'Book 7N8D Package',
    'Ready for<br><em>Eight Days in Andaman?</em>': 'Ready for<br><em>Eight Days in Andaman?</em>',
    '5 nights accommodation (3★–4★ hotels, twin sharing)': '7 nights accommodation (3★–4★ hotels, twin sharing)',
    'Daily breakfast (5 breakfasts)': 'Daily breakfast (7 breakfasts)',
    'Andaman 5N6D — ₹27,999': 'Andaman 7N8D — ₹44,999',
    'andaman-5n6d-package.html': 'andaman-7n8d-package.html',
    '<a href="andaman-7n8d-package.html" class="compare-btn active-pkg">7N8D — ₹44,999 ✦</a>': '<a href="andaman-7n8d-package.html" class="compare-btn active-pkg">7N8D — ₹44,999 ✦</a>'
}

insert_html_7 = '''      <div class="day-card">
        <div class="day-num">Day 07 · Relax</div>
        <div class="day-title">Havelock Island — Free Beach Day</div>
        <img class="day-img" src="https://images.unsplash.com/photo-1493558103817-58b2924bce98?w=700&q=80" alt="Havelock Leisure">
        <p class="day-body">Wake up to another idyllic morning on Havelock. Enjoy an optional morning scuba dive or leisure time at Radhanagar Beach. Spend the evening at the resort with a private candlelight dinner and cultural show.</p>
        <div class="day-activities">
          <div class="activity-tag">🏖️ Beach Time</div>
          <div class="activity-tag">🤿 Optional Dive</div>
          <div class="activity-tag">🍽️ Romantic Dinner</div>
          <div class="activity-tag">🎶 Culture Show</div>
        </div>
      </div>

      <div class="day-card">
        <div class="day-num">Day 08 · Departure</div>
        <div class="day-title">Port Blair — Farewell & Flight Home</div>
        <img class="day-img" src="https://images.unsplash.com/photo-1533236891007-5e2f0017f51f?w=700&q=80" alt="Port Blair Departure">
        <p class="day-body">Transfer back to Port Blair after breakfast, shop for souvenirs at Aberdeen Bazaar, and enjoy an optional city walk or museum visit. Board your return flight with unforgettable memories of an 8-day Andaman adventure.</p>
        <div class="day-activities">
          <div class="activity-tag">🚤 Ferry to Port Blair</div>
          <div class="activity-tag">🛍️ Souvenir Shopping</div>
          <div class="activity-tag">🏛️ Optional Museum Visit</div>
          <div class="activity-tag">✈️ Airport Drop</div>
        </div>
      </div>
'''

insert_marker7 = '    </div>\n  </div>\n</section>\n\n<!-- HIGHLIGHTS -->'

update_file(path7, repl7, insert_marker7, insert_html_7)

print('Files updated with final corrections.')
