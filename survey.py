import streamlit as st 
import streamlit_survey as ss 
from datetime import date
survey = ss.StreamlitSurvey()
# import time
st.set_page_config(page_title="Coca-Cola Uzbekistan bo'yicha so'rovnoma", layout="centered")

st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://1000logos.net/wp-content/uploads/2016/11/Coca-Cola-Logo.png" width="200"/>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
        body {
            background-color: #fff;
        }

        .main {
            padding: 20px;
            font-family: 'Arial', sans-serif;
            color: #222;
        }

        h1, h2, h3 {
            color: #e41c1c;
        }

        .survey-question {
            background-color: #fcebec;
            border: 2px solid #e41c1c;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        }

        .survey-question:hover {
            background-color: #fff0f0;
        }

        .stRadio > div {
            background-color: #fff;
            border-radius: 10px;
            padding: 10px;
        }

        .stButton > button {
            background-color: #e41c1c;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.5em 1.5em;
            border: none;
        }

        .stButton > button:hover {
            background-color: #c81010;
        }
    </style>
    """,
    unsafe_allow_html=True
)


survey.text_input("1.Ismingizni yozing", key = 'name')

st.markdown("<br><br>", unsafe_allow_html=True)

survey.radio(
    "2.Yosh kategoriyangizni belgilang",
    options = ['12-18', '19-24', '25-40', '40+'], 
    horizontal=True
)

st.markdown("<br><br>", unsafe_allow_html=True)
survey.radio(
    "3.Tanlang:",
    options = ['Erkak', 'Ayol'], 
    horizontal=True,
    key="gender"
)


st.markdown("<br><br>", unsafe_allow_html=True)

survey.radio(
    "4.Coca-Colani qanchalik tez-tez sotib olasiz?:",
    options= ['Har kuni', 'Haftada bir necha marta', 'Kamdan kam', 'Faqat bayramlarda', 'Umuman sotib olmayman'], 
    horizontal=False
)

st.markdown("<br><br>", unsafe_allow_html=True)
survey.multiselect(
    "5.Qaysi Coca-Cola mahsulotini ko'proq sotib olasiz?",
    options = ['Coca-Cola classic', 'Zero Sugar', 'Light', 'Fanta', 'Sprite', 'Fuse tea', 'Bonaqua'],
    max_selections=3  # Maksimal 3 ta tanlov
)


st.markdown("<br><br>", unsafe_allow_html=True)
st.select_slider(
    "6.Coca-Cola mahsulotlarini qanday ta'riflaysiz?:", 
    options=["Yomon", "Qoniqarli", "O'rtacha",  "Yaxshi", "A'lo"], 
    key="Q2"
)

st.markdown("<br><br>", unsafe_allow_html=True)
survey.radio(
    "7.Eng ko'p qanday hajmda sotib olasiz?",
    options = ['0.5', '1', '1.5', '2', '2.5'],
    horizontal = True
)

st.markdown("<br><br>", unsafe_allow_html=True)
survey.multiselect(
    "8.Coca-colani ko'proq qayerdan sotib olasiz?",
    options = ['Supermarket', 'Fast food/restoran', "Mahalla do'koni", "Avtomat (vending) apparatlaridan"],
    max_selections=3
)


st.markdown("<br><br>", unsafe_allow_html=True)
st.write("9.Coca-Cola nima bilan ko'proq bog'laysiz?")
options = ["Baxt", "Energiya", "Oila va do'stlar davrasi", "Bayramlar", 'Yozgi salqinlik', 'Reklama roliklari']
selected = []

for option in options:
    if st.checkbox(option):
        selected.append(option)


st.markdown("<br><br>", unsafe_allow_html=True)
survey.multiselect(
    "10.Xarid qaroringizga nima ko'proq ta'sir qiladi?",
    options = ['Narxi', 'Tami', 'Brendga ishonchim', "Mahsulot dizayni", 'Sog\'lik omili', 'Chegirma/aksiyalar'],
    max_selections=3
)

st.markdown("<br><br>", unsafe_allow_html=True)
st.write("11.Coca-Colani qanday taom bilan ichishni afzal ko'rasiz?")
options = [
    "Pizza", 
    "KFC", 
    "Lavash", 
    "Sushi", 
    "Milliy taomlar",
    "Burger",
    "Shirikliklar" 
    "Farqi yo'q"
]
selected_options = []
for option in options:
    if st.checkbox(option):
        selected_options.append(option)

st.markdown("<br><br>", unsafe_allow_html=True)
survey.radio(
    "12.Coca-Colani tavsiya qilish darajangizni baholang:",
    options=list(range(0, 11)), 
    horizontal=True
)

st.markdown("<br><br>", unsafe_allow_html=True)
survey.multiselect(
    "13.eklamalarga qayerda ko'proq duch kelasiz?",
    options = ['Televizor', 'Instagram', 'Tiktok', 'Posterlar', 'Korzinka']
)

st.markdown("<br><br>", unsafe_allow_html=True)
st.select_slider(
    "14.Coca-Colani boshqa ichimliklarga nisbatan qanday baholaysiz?:", 
    options=["Yomon", "Qoniqarli", "O'rtacha", "Yaxshi", "A'lo"], 
    key="Q3"
)
st.markdown("<br><br>", unsafe_allow_html=True)
st.write("15.Coca-Cola va boshqa brendlarning reklamalari orasida qaysi biri sizni ko'proq jalb qiladi?")
options = [
    "Televizion reklama",
    "Internet yoki ijtimoiy tarmoq reklamalari",
    "Tezkor takliflar yoki aksiyalar",
    "Brendning o'ziga xos va esda qoladigan reklamasi",
    "Mahsulotning foydaliligiga doir ma'lumotlar"
]

selected_options = []
for option in options:
    if st.checkbox(option):
        selected_options.append(option)


st.markdown("<br><br>", unsafe_allow_html=True)


survey.multiselect(
    "16.Yana qaysi ichimlik brendini tanlaysiz?",
    options = ['Pepsi mahsulotlari(Pepsi, Mirinda, Mountain dew)',
                'Energetic(Adrinaline, Red Bull, Flash)', 
                'Salqin choylar(Lipton, Ceylon, Ice tea)', 
                'Moxito'],
    max_selections=3
)

st.markdown("<br><br>", unsafe_allow_html=True)

st.write("17.Agar siz Coca-Cola o‘rniga boshqa brendni tanlasangiz, bu qarorga nima ta’sir qilgan?")
options = [
    "Narxi arzonroq", 
    "Yangi mahsulotni sinab ko'rish", 
    "Do‘konda mavjud bo‘ladi", 
    "Qadoqlanishi qulay", 
    "Ko‘proq reklama qilinadi", 
    "Salomatlik uchun foydaliroq ko‘rinadi"
]
selected_options = []
for option in options:
    if st.checkbox(option):
        selected_options.append(option)

# "Boshqa" checkboxini qo'shish
other_checkbox = st.checkbox("Boshqa")

# Agar "Boshqa" tanlansa, fikrni yozish so'raladi
if other_checkbox:
    other_reason = st.text_input("Iltimos, fikringizni yozing:")
    if not other_reason:
        st.warning("Iltimos, 'Boshqa' variantini tanlagan bo'lsangiz, fikrni yozing.")
    else:
        selected_options.append(f"Boshqa: {other_reason}")

st.markdown("<br><br>", unsafe_allow_html=True)

st.write("18.Agar Coca-Cola sizning ehtiyojlaringizga moslashish imkonini bersa, qanday o‘zgarishlarni kutilayotgan edingiz?")

options = [
    'Sog‘lomroq variantlar (kamroq shakar, vitaminlar)', 
    'Maxsus o‘zgartirilgan ta’m variantlari', 
    'Chegirma/aksiyalar', 
    'Mahsulot qadog‘ida o‘zgarishlar',
    'Boshqa'  
]

selected_option = st.radio("Tanlang:", options)

if selected_option == 'Boshqa':
    other_reason = st.text_input("Iltimos, fikringizni yozing:",  key="other_reason")
    if other_reason:
        st.write(f"Sizning fikringiz: {other_reason}")
    else:
        st.warning("Iltimos, 'Boshqa' variantini tanlasangiz, fikrni yozing.")


st.markdown("<br><br>", unsafe_allow_html=True)
survey.text_area("19.Takliflaringiz?", key="open_feedback")



if st.button("So'rovnomani yuborish"):
    st.write("So'rovnoma yuborildi. Rahmat!")
