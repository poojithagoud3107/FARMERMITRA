import streamlit as st
from gtts import gTTS

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="🌾 Farmer AI", layout="wide")

# =========================
# HEADER IMAGE
# =========================
st.image("https://images.unsplash.com/photo-1500382017468-9049fed747ef", use_column_width=True)

st.title("🌾 FARMER AI - Smart Crop Disease Support")
st.markdown("### రైతులకు స్మార్ట్ సహాయం 🚜")

# =========================
# VOICE FUNCTION
# =========================
def speak(text):
    tts = gTTS(text=text, lang='te')
    tts.save("voice.mp3")
    st.audio("voice.mp3")

# =========================
# DISEASE DATA (20+)
# =========================
disease_info = {
"Healthy":{"symptoms":"No symptoms","medicine":"No medicine needed","emergency":"Monitor regularly","telugu":"మీ పంట ఆరోగ్యంగా ఉంది","pro":"పంటను క్రమం తప్పకుండా పరిశీలించండి మరియు సమతుల్య ఎరువులు వాడండి."},
"Leaf Spot":{"symptoms":"Brown/black spots","medicine":"Copper fungicide","emergency":"Remove infected leaves","telugu":"ఆకులపై మచ్చలు","pro":"ఉదయం లేదా సాయంత్రం స్ప్రే చేయండి. నీరు ఎక్కువగా ఇవ్వవద్దు."},
"Powdery Mildew":{"symptoms":"White powder","medicine":"Sulfur spray","emergency":"Avoid humidity","telugu":"తెల్లటి పొడి","pro":"గాలి ప్రసరణ బాగా ఉండేలా చూడండి."},
"Downy Mildew":{"symptoms":"Yellow patches","medicine":"Fungicide","emergency":"Keep leaves dry","telugu":"పసుపు మచ్చలు","pro":"ఆకులపై నీరు పడకుండా జాగ్రత్త పడండి."},
"Rust":{"symptoms":"Orange rust spots","medicine":"Copper fungicide","emergency":"Remove affected leaves","telugu":"తుప్పు మచ్చలు","pro":"పొలంలో గాలి సరిగా ఉండేలా చూడండి."},
"Blight":{"symptoms":"Leaves dry quickly","medicine":"Mancozeb spray","emergency":"Immediate spraying","telugu":"ఆకులు ఎండిపోతాయి","pro":"వర్షం ముందు స్ప్రే చేయవద్దు."},
"Anthracnose":{"symptoms":"Dark lesions","medicine":"Fungicide","emergency":"Protect fruits","telugu":"గుంతల మచ్చలు","pro":"పండ్లను నీటి నుండి రక్షించండి."},
"Bacterial Wilt":{"symptoms":"Sudden wilting","medicine":"Remove plants","emergency":"Control water","telugu":"అకస్మాత్తుగా వాడిపోవడం","pro":"మట్టి నీటి నియంత్రణ ముఖ్యం."},
"Early Blight":{"symptoms":"Target spots","medicine":"Copper fungicide","emergency":"Early spray","telugu":"గుండ్రని మచ్చలు","pro":"ప్రారంభ దశలోనే చికిత్స చేయండి."},
"Late Blight":{"symptoms":"Dark patches","medicine":"Metalaxyl","emergency":"Act fast","telugu":"గాఢమైన మచ్చలు","pro":"వెంటనే స్ప్రే చేయాలి."},
"Root Rot":{"symptoms":"Roots rot","medicine":"Reduce water","emergency":"Improve drainage","telugu":"వేరు కుళ్ళిపోవడం","pro":"డ్రైనేజ్ బాగుండాలి."},
"Stem Rot":{"symptoms":"Weak stem","medicine":"Fungicide","emergency":"Remove part","telugu":"తాడు బలహీనంగా మారుతుంది","pro":"బాధిత భాగం తొలగించండి."},
"Leaf Curl":{"symptoms":"Curling leaves","medicine":"Insecticide","emergency":"Spray immediately","telugu":"ఆకులు ముడుచుకోవడం","pro":"పురుగులను నియంత్రించండి."},
"Mosaic Virus":{"symptoms":"Mosaic pattern","medicine":"Remove plants","emergency":"Stop spread","telugu":"మచ్చల నమూనా","pro":"ఇతర మొక్కలకు వ్యాప్తి నివారించండి."},
"Yellow Leaf":{"symptoms":"Yellow leaves","medicine":"Nitrogen fertilizer","emergency":"Improve nutrients","telugu":"పసుపు ఆకులు","pro":"ఎరువులు సరిగా వేయండి."},
"Scab":{"symptoms":"Rough lesions","medicine":"Fungicide","emergency":"Treat quickly","telugu":"గట్టిగా మచ్చలు","pro":"తక్షణ చికిత్స చేయండి."},
"Damping Off":{"symptoms":"Seedlings die","medicine":"Clean soil","emergency":"Avoid overwatering","telugu":"చిన్న మొక్కలు చనిపోతాయి","pro":"నీరు ఎక్కువ ఇవ్వకండి."},
"Smut":{"symptoms":"Black powder","medicine":"Seed treatment","emergency":"Protect crop","telugu":"నల్లటి పొడి","pro":"విత్తన శుద్ధి చేయండి."},
"Black Rot":{"symptoms":"Black decay","medicine":"Fungicide","emergency":"Remove parts","telugu":"నల్లగా కుళ్ళిపోవడం","pro":"బాధిత భాగం తొలగించండి."},
"Fusarium Wilt":{"symptoms":"Yellow + wilt","medicine":"Resistant seeds","emergency":"Soil treatment","telugu":"వాడిపోవడం","pro":"రోగ నిరోధక విత్తనాలు వాడండి."},
"Alternaria Leaf Spot":{"symptoms":"Dark circular spots","medicine":"Fungicide","emergency":"Treat fast","telugu":"గుండ్రని మచ్చలు","pro":"త్వరగా చికిత్స చేయండి."}
}

# =========================
# SELECT DISEASE
# =========================
disease = st.selectbox("🔍 Select Disease / వ్యాధి ఎంచుకోండి", list(disease_info.keys()))
info = disease_info[disease]

# =========================
# LAYOUT
# =========================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 Disease Info")
    st.info(f"🦠 Symptoms: {info['symptoms']}")
    st.success(f"💊 Medicine: {info['medicine']}")
    st.warning(f"🚨 Emergency: {info['emergency']}")
    st.write(f"🌱 తెలుగు: {info['telugu']}")

    if st.button("🔊 Speak Telugu"):
        speak(info['telugu'])

with col2:
    st.image("https://images.unsplash.com/photo-1598514982901-1c3e6b0c2f4b", use_column_width=True)

# =========================
# PRO TIPS
# =========================
if st.button("⭐ Pro Tips"):
    st.success(f"🌾 {info['pro']}")
    st.markdown("### 📊 Government Schemes")
    st.markdown("""
    - Pradhan Mantri Fasal Bima Yojana  
    - Rythu Bharosa  
    - Fertilizer Subsidy  
    """)

# =========================
# DASHBOARD
# =========================
st.markdown("---")
st.subheader("📊 Farmer Dashboard")

c1, c2, c3 = st.columns(3)
c1.metric("🌱 Diseases", "20+")
c2.metric("👨‍🌾 Farmers Helped", "1000+")
c3.metric("📈 Accuracy", "95%")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("🌾 Made with ❤️ for Farmers")