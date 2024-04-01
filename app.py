import streamlit as st
import tensorflow as tf

nn = tf.keras.models.load_model('nn_model.h5')

def predict_survival(input_data):
    prediction = nn.predict(input_data)

    return prediction

st.title('Breast Cancer Survival Rate Prediction')


age_at_diagnosis = st.number_input('Age at Diagnosis', min_value=0, max_value=150, value=50)
chemotherapy = st.number_input('Chemotherapy 0 or 1')
hormone_therapy = st.number_input('Hormone Therapy 0 or 1')
inferred_menopausal_state = st.number_input('Inferred Menopausal State 0 or 1')
pik3ca = st.number_input('PIK3CA Mutation', value=0.0)
cdh1 = st.number_input('CDH1 Mutation', value=0.0)
gata3 = st.number_input('GATA3 Mutation', value=0.0)
map3k1 = st.number_input('MAP3K1 Mutation', value=0.0)
syne1 = st.number_input('SYNE1 Mutation', value=0.0)
ush2a = st.number_input('USH2A Mutation', value=0.0)
pten = st.number_input('PTEN Mutation', value=0.0)

input_data = [[age_at_diagnosis, chemotherapy, hormone_therapy, inferred_menopausal_state,
               pik3ca, cdh1, gata3, map3k1, syne1, ush2a, pten]]

if st.button('Predict Survival Rate'):

    prediction = predict_survival(input_data)
    st.write(f'Predicted Breast Cancer Survival Rate: {prediction[0][0]*100:.2f}%')