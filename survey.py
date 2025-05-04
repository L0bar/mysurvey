import streamlit as st 
import streamlit_survey as ss 
from datetime import date
survey = ss.StreamlitSurvey()

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
    "<h1 style='text-align: center; color: red;'>🥤 Coca-Cola bo'yicha so'rovnoma</h1>", 
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


name = survey.text_input("1.Ismingizni yozing", key = 'name')

st.markdown("<br><br>", unsafe_allow_html=True)

age = survey.radio(
    "2.Yosh kategoriyangizni belgilang",
    options = ['12-18', '19-24', '25-40', '40+'], 
    horizontal=True,
    key = 'age'
)

st.markdown("<br><br>", unsafe_allow_html=True)
gender = survey.radio(
    "3.Tanlang:",
    options = ['Erkak', 'Ayol'], 
    horizontal=True,
    key="gender"
)


st.markdown("<br><br>", unsafe_allow_html=True)

frequency = survey.radio(
    "4.Coca-Colani qanchalik tez-tez sotib olasiz?:",
    options= ['Har kuni', 'Haftada bir necha marta', 'Kamdan kam', 'Faqat bayramlarda', 'Umuman sotib olmayman'], 
    horizontal=False,
    key = 'frequency'
)

st.markdown("<br><br>", unsafe_allow_html=True)
product = survey.multiselect(
    "5.Qaysi Coca-Cola mahsulotini ko'proq sotib olasiz?",
    options = ['Coca-Cola classic', 'Coca-Cola shakarsiz', 'Fanta', 'Sprite', 'Fuse tea', 'Bonaqua'],
    max_selections=3,
    key = 'product'
)


st.markdown("<br><br>", unsafe_allow_html=True)
rating = st.select_slider(
    "6.Coca-Cola mahsulotlarini qanday ta'riflaysiz?:", 
    options=["Yomon", "Qoniqarli", "O'rtacha",  "Yaxshi", "A'lo"], 
    key="rating"
)

st.markdown("<br><br>", unsafe_allow_html=True)
size = survey.radio(
    "7.Eng ko'p qanday hajmda sotib olasiz?",
    options = ['0.5', '1', '1.5', '2', '2.5'],
    horizontal = True,
    key='size'
)

st.markdown("<br><br>", unsafe_allow_html=True)
place = survey.multiselect(
    "8.Coca-colani ko'proq qayerdan sotib olasiz?",
    options = ['Supermarket', 'Fast food/restoran', "Mahalla do'koni", "Avtomat (vending) apparatlaridan"],
    max_selections=3,
    key='place'
)


st.markdown("<br><br>", unsafe_allow_html=True)
connect = st.write("9.Coca-Cola nima bilan ko'proq bog'laysiz?", key='connect')
options = ["Baxt", "Energiya", "Oila va do'stlar davrasi", "Bayramlar", 'Yozgi salqinlik', 'Reklama roliklari']
selected = []

for option in options:
    if st.checkbox(option):
        selected.append(option)


st.markdown("<br><br>", unsafe_allow_html=True)
effect = survey.multiselect(
    "10.Xarid qaroringizga nima ko'proq ta'sir qiladi?",
    options = ['Narxi', 'Tami', 'Brendga ishonchim', "Mahsulot dizayni", 'Sog\'lik omili', 'Chegirma/aksiyalar'],
    max_selections=3,
    key='effect'
)

st.markdown("<br><br>", unsafe_allow_html=True)
food = st.write("11.Coca-Colani qanday taom bilan ichishni afzal ko'rasiz?", key='food')
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
suggest = survey.radio(
    "12.Coca-Colani tavsiya qilish darajangizni baholang:",
    options=list(range(0, 11)), 
    horizontal=True,
    key='suggest'
)

st.markdown("<br><br>", unsafe_allow_html=True)
ads = survey.multiselect(
    "13.Reklamalarga qayerda ko'proq duch kelasiz?",
    options = ['Televizor', 'Instagram', 'Tiktok', 'Posterlar', 'Korzinka'],
    key='ads'
)

st.markdown("<br><br>", unsafe_allow_html=True)
rate = st.select_slider(
    "14.Coca-Colani boshqa ichimliklarga nisbatan qanday baholaysiz?:", 
    options=["Yomon", "Qoniqarli", "O'rtacha", "Yaxshi", "A'lo"], 
    key="rate"
)
st.markdown("<br><br>", unsafe_allow_html=True)
compare = st.write("15.Coca-Cola va boshqa brendlarning reklamalari orasida qaysi biri sizni ko'proq jalb qiladi?", key='compare')
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


select = survey.multiselect(
    "16.Yana qaysi ichimlik brendini tanlaysiz?",
    options = ['Pepsi mahsulotlari(Pepsi, Mirinda, Mountain dew)',
                'Energetic(Adrinaline, Red Bull, Flash)', 
                'Salqin choylar(Lipton, Ceylon, Ice tea)', 
                'Moxito', 'Limonadi', 'Love is'],
    max_selections=3,
    key='select'
)

st.markdown("<br><br>", unsafe_allow_html=True)

decision = st.write("17.Agar siz Coca-Cola o‘rniga boshqa brendni tanlasangiz, bu qarorga nima ta’sir qilgan?", key='decision')
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

new = st.write("18.Coca-Colada qanday o‘zgarishlarni ko'rishni xohlaysiz?", key='new')

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
open_feedback = survey.text_area("19.Takliflaringiz?", key="open_feedback")


all_required_filled = all([name, age, gender, frequency, product, rating, size, place, connect, effect, food, suggest, ads, rate, compare, select, open_feedback])

# Survey submission
if st.button("So'rovnomani yuborish"):
    if all_required_filled:
        st.write("So'rovnoma yuborildi. Rahmat!")
    else:
        st.error("Iltimos, barcha maydonlarni to'ldiring.")

