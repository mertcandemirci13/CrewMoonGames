"""
MoonGames - PM Otomatik Arka Plan Sistemi
Groq API ile çalışır — TAMAMEN ÜCRETSİZ, PC kapalı olsa bile!
"""
import os
import datetime
import time
import urllib.request
import json

GROQ_KEY = os.environ.get("GROQ_API_KEY", "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")

def sor(rol, sistem, soru):
    print(f"\n{'='*50}\n[{rol}] çalışıyor...\n{'='*50}")
    time.sleep(8)  # Kota aşımını önle
    data = json.dumps({
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": sistem},
            {"role": "user", "content": soru}
        ],
        "max_tokens": 400
    }).encode()
    req = urllib.request.Request(
        "https://api.groq.com/openai/v1/chat/completions",
        data=data,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {GROQ_KEY}"}
    )
    with urllib.request.urlopen(req) as r:
        yanit = json.loads(r.read())["choices"][0]["message"]["content"]
    print(yanit)
    return yanit

bugun = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

pazar = sor("Pazar Araştırmacısı",
    "Sen MoonGames'in Pazar Araştırmacısısın. MetroMatch offline bulmaca oyunu yapıyorsunuz.",
    "CEO için günlük pazar özeti: 1) Offline oyun trendi, 2) Rakip hareketi, 3) Fırsat. Türkçe, 4 cümle.")

tasarim = sor("Oyun Tasarımcısı",
    "Sen MoonGames'in Oyun Tasarımcısısın. MetroMatch — 6x6 emoji eşleştirme oyunu.",
    "Bugünkü tasarım notu: 1) Önerilen yeni özellik, 2) UX iyileştirmesi. Türkçe, 4 cümle.")

gelistirme = sor("Yazılım Mimarı",
    "Sen MoonGames'in Yazılım Mimarısın. Flutter ile offline oyun geliştiriyorsunuz.",
    "Teknik durum: 1) Sprint ilerlemesi, 2) Risk, 3) Öncelik. Türkçe, 4 cümle.")

test = sor("QA Mühendisi",
    "Sen MoonGames'in QA Mühendisisin.",
    "Test raporu: 1) Test senaryosu, 2) Kritik bug riski, 3) Release durumu. Türkçe, 4 cümle.")

ozet = sor("Proje Yöneticisi",
    "Sen MoonGames'in Proje Yöneticisisin. CEO'ya günlük brifing hazırlıyorsun.",
    f"Ekip raporlarına bakarak CEO brifing yaz:\nPazar: {pazar[:200]}\nTasarım: {tasarim[:200]}\nGeliştirme: {gelistirme[:200]}\nTest: {test[:200]}\n\n1) Proje durumu %, 2) Kritik karar, 3) Yarının önceliği, 4) CEO aksiyonu. Türkçe.")

dosya = f"rapor_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.txt"
with open(dosya, "w", encoding="utf-8") as f:
    f.write(f"""
╔══════════════════════════════════════════════╗
   🌙 MOONGAMES — GÜNLÜK OTOMATİK RAPOR
   {bugun}
╚══════════════════════════════════════════════╝

📊 PAZAR ARAŞTIRMACISI
{'─'*46}
{pazar}

🎨 OYUN TASARIMCISI
{'─'*46}
{tasarim}

💻 YAZILIM MİMARİ
{'─'*46}
{gelistirme}

🔍 QA MÜHENDİSİ
{'─'*46}
{test}

📋 PROJE YÖNETİCİSİ — CEO BRİFİNG
{'─'*46}
{ozet}
""")

print(f"\n✅ Rapor kaydedildi: {dosya}")
