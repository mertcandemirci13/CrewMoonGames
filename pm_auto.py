"""
MoonGames - PM Otomatik Arka Plan Sistemi
GitHub Actions ile çalışır — PC kapalı olsa bile!
"""
import anthropic
import os
import datetime

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

def sor(rol, sistem, soru):
    print(f"\n{'='*50}\n[{rol}] çalışıyor...\n{'='*50}")
    msg = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=600,
        system=sistem,
        messages=[{"role": "user", "content": soru}]
    )
    yanit = msg.content[0].text
    print(yanit)
    return yanit

bugun = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

# ── PAZAR ARAŞTIRMACISI ─────────────────────────────
pazar = sor(
    "Pazar Araştırmacısı",
    "Sen MoonGames'in Pazar Araştırmacısısın. Offline mobil bulmaca oyunları (MetroMatch) yapıyorsunuz. CEO için günlük pazar özeti hazırlıyorsun.",
    "Bugün için kısa pazar özeti hazırla: 1) Offline oyun pazarında trend, 2) Rakip hareketi, 3) CEO için 1 fırsat. Türkçe, 5 cümle max."
)

# ── OYUN TASARIMCISI ────────────────────────────────
tasarim = sor(
    "Oyun Tasarımcısı",
    "Sen MoonGames'in Oyun Tasarımcısısın. MetroMatch — 6x6 emoji eşleştirme oyunu tasarlıyorsun.",
    "Bugün için oyun geliştirme notu hazırla: 1) Hangi özelliği geliştirdin/öneriyorsun, 2) Bir yeni mekanik fikri, 3) Kullanıcı deneyimi notu. Türkçe, 5 cümle max."
)

# ── YAZILIM MİMARİ ──────────────────────────────────
gelistirme = sor(
    "Yazılım Mimarı",
    "Sen MoonGames'in Yazılım Mimarısın. Flutter ile offline mobil oyun geliştiriyorsunuz.",
    "Bugün için teknik durum raporu: 1) Sprint'teki ilerleme, 2) Teknik borç/risk, 3) Öncelikli görev. Türkçe, 5 cümle max."
)

# ── QA MÜHENDİSİ ────────────────────────────────────
test = sor(
    "QA Mühendisi",
    "Sen MoonGames'in QA Mühendisisin. Her şeyde hata bulursun.",
    "Bugün için test raporu: 1) Test ettiğin senaryo, 2) Bulduğun/tahmin ettiğin kritik bug, 3) Release için risk. Türkçe, 5 cümle max."
)

# ── PROJE YÖNETİCİSİ — ÖZET ─────────────────────────
ozet = sor(
    "Proje Yöneticisi",
    "Sen MoonGames'in Proje Yöneticisisin. Tüm ekipleri koordine ediyorsun. CEO'ya günlük brifing hazırlıyorsun.",
    f"""Bugünkü ekip raporlarına bakarak CEO için günlük brifing hazırla:

PAZAR: {pazar}
TASARIM: {tasarim}
GELİŞTİRME: {gelistirme}
TEST: {test}

Brifing şunları içersin:
1. Genel proje durumu (ilerleme %)
2. Bugünün en kritik kararı
3. Yarın için öncelik
4. CEO için 1 aksiyon maddesi

Türkçe, net, kısa."""
)

# ── RAPORU KAYDET ────────────────────────────────────
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
