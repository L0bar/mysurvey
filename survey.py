import streamlit as st 
import streamlit_survey as ss 
from datetime import date
survey = ss.StreamlitSurvey()
import requests
from datetime import date

st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://1000logos.net/wp-content/uploads/2016/11/Coca-Cola-Logo.png" width="200"/>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<h2 style='text-align: center; color: red;'>🥤 Coca-Cola bo'yicha so'rovnoma</h2>", 
    unsafe_allow_html=True
)


name = survey.text_input("1.Ismingizni yozing", key = 'name')

st.markdown("<br><br>", unsafe_allow_html=True)

age = st.radio(
    "2.Yosh kategoriyangizni belgilang",
    options = ['14-18', '19-24', '25-40', '40+'], 
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
max_selections = 3
for option in options:
    if st.checkbox(option):
        selected.append(option)
if len(selected) > max_selections:
    st.error(f"Faqat {max_selections} ta variantni tanlashingiz mumkin.")
    st.stop()


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
    "Shirikliklar", 
    "Farqi yo'q"
]
food_options = []
max_selection = 3
for option in options:
    if st.checkbox(option):
        food_options.append(option)
if len(food_options) > max_selections:
    st.error(f"Faqat {max_selections} ta variantni tanlashingiz mumkin.")
    st.stop()

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
    key='ads',
    max_selections = 3
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
    "Brendning o'ziga xos va esda qoladigan reklamasi"
]

compare_options = []
max_selections = 3
for option in options:
    if st.checkbox(option):
        compare_options.append(option)
if len(compare_options) > max_selections:
    st.error(f"Faqat {max_selections} ta variantni tanlashingiz mumkin.")
    st.stop()


st.markdown("<br><br>", unsafe_allow_html=True)


choice = survey.multiselect(
    "16.Yana qaysi ichimlik brendini tanlaysiz?",
    options = ['Pepsi mahsulotlari(Pepsi, Mirinda, Mountain dew)',
                'Energetic(Adrinaline, Red Bull, Flash)', 
                'Salqin choylar(Lipton, Ceylon, Ice tea)', 
                'Moxito, Limonadi, Love is',
                'Boshqalar'],
    max_selections=3,
    key='choice'
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
decision_options = []
max_selection = 3
for option in options:
    if st.checkbox(option):
        decision_options.append(option)

other_checkbox = st.checkbox("Boshqa")

if other_checkbox:
    other_reason = st.text_input("Iltimos, fikringizni yozing:")
    if not other_reason:
        st.warning("Iltimos, 'Boshqa' variantini tanlagan bo'lsangiz, fikrni yozing.")
    else:
        decision_options.append(f"Boshqa: {other_reason}")
if len(decision_options) > max_selections:
    st.error(f"Faqat {max_selections} ta variantni tanlashingiz mumkin.")
    st.stop()

st.markdown("<br><br>", unsafe_allow_html=True)

news = st.write("18.Coca-Colada qanday o‘zgarishlarni ko'rishni xohlaysiz?", key='news')

options = [
    'Sog‘lomroq variantlar (kamroq shakar, vitaminlar)', 
    'Maxsus o‘zgartirilgan ta’m variantlari', 
    'Chegirma/aksiyalar', 
    'Mahsulot qadog‘ida o‘zgarishlar',
    'Boshqa'  
]

new_option = st.radio(" ", options)

if new_option == 'Boshqa':
    other_reason = st.text_input("Iltimos, fikringizni yozing:",  key="other_reason")
    if other_reason:
        st.write(f"Sizning fikringiz: {other_reason}")
    else:
        st.warning("Iltimos, 'Boshqa' variantini tanlasangiz, fikrni yozing.")

st.markdown("<br><br>", unsafe_allow_html=True)
open_feedback = survey.text_area("19.Takliflaringiz?", key="open_feedback")

all_required_filled = all([name, product, place, selected, effect, food_options, ads, compare_options, choice, decision_options, open_feedback])


if st.button("So'rovnomani yuborish"):
    if all_required_filled:
        data = {
            'name': name,
            'age': age,
            'gender': gender,
            'frequency': frequency,
            'product': product,
            'rating': rating,
            'size': size,
            'place': place,
            'connect': selected,
            'effect': effect,
            'food': food_options,
            'suggest': suggest,
            'ads': ads,
            'rate': rate,
            'compare': compare_options,
            'choice': choice,
            'decision': decision_options,
            'news': new_option,
            'open_feedback': open_feedback
        }

        try:
            response = requests.post(
                'https://script.google.com/macros/s/AKfycbz2AzQeKoH2UZBunjay0u60sYntNchRD2S-APCI-22WRB3OqOOhpet8ATRW2W2BaTo42A/exec',
                json=data
            )

            if response.status_code == 200:
                st.markdown("<h1 style='text-align: center; color: green;'>✅ So‘rovnoma muvaffaqiyatli yuborildi! Rahmat! 🥤</h1>", unsafe_allow_html=True)
            else:
                st.error("❌ Yuborishda xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")

        except Exception as e:
            st.error(f"Xatolik yuz berdi: {e}")
    else:
        st.error("Iltimos, barcha maydonlarni to'ldiring.")
