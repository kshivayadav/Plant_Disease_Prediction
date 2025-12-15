import streamlit as st
from PIL import Image
from main import predict_image_class, model, class_indices
from llm import get_llm_report
import tempfile
# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI Plant Health Advisor",
    page_icon="🌿",
    layout="centered"
)

# ------------------ UI HEADER ------------------
st.title("🌿 AI Plant Health Advisor")
st.caption("CNN-based prediction with Open-Source LLM (LLaMA-3)")

st.markdown("---")

uploaded_image = st.file_uploader("📤 Upload a plant leaf image",
                                    type=["jpg", "jpeg", "png"]
                                )

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    
    Analyze = st.button("🔍 Analyze Plant", use_container_width=True)
    col1, col2 = st.columns(2)
    with col1:
        resized_img = image.resize((300, 300))
        st.image(resized_img,caption="Uploaded Image")

    if Analyze:
        with col2:
            # -------- TEMP FILE SAVE --------
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                tmp.write(uploaded_image.getbuffer())
                image_path = tmp.name

            # -------- CNN PREDICTION --------
            with st.spinner("Analyzing image..."):
                prediction, confidence = predict_image_class(
                    model,
                    image_path,
                    class_indices
                )
            plant_name, disease = prediction.split("___")
            plant_name = plant_name.replace("_", " ")

            st.success(f"🌱 Plant: {plant_name}")
            st.info(f"🩺 Condition")

            st.markdown(f"### **{disease}**")

            st.progress(int(confidence))
            st.metric("Prediction Confidence", f"{confidence:.2f}%")

        if confidence >= 85:
            st.success("✅ Highly confident prediction")
        elif confidence >= 70:
            st.warning("⚠️ Moderate confidence — consider a clearer image")
        else:
            st.error("❗ Low confidence — please upload a clearer leaf image")

        # -------- LLM ADVISORY --------
        with st.spinner("Generating plant care advisory..."):
            report = get_llm_report(plant_name, disease, round(confidence, 2))
            if report is None:
                st.error("❗ Failed to generate advisory. Please try again later.")
                st.stop()
            else:
                print(report)
                st.markdown("---")
                st.markdown("📋 Expert Recommendation")
                st.write(f"**Summary:** {report.summary}")
                if disease.lower() == "healthy":
                    st.subheader("✅ Benefits")
                    for b in report.benefits:
                        st.write(f"- {b}")

                    st.subheader("🍽 Uses")
                    for u in report.uses:
                        st.write(f"- {u}")
                else:
                    st.subheader("🦠 Causes")
                    for c in report.causes:
                        st.write(f"- {c}")

                    st.subheader("💊 Treatment Steps")
                    for t in report.treatment_steps:
                        st.write(f"- {t}")

                    st.subheader("🛡 Prevention Tips")
                    for p in report.prevention_tips:
                        st.write(f"- {p}")

                st.info(report.confidence_message)