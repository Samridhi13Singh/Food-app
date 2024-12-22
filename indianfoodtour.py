import streamlit as st
import random

food = [
    {'Name':'double ka mitha','Image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGZWFEIqY1zoDxfDYSn8kEkZpjG1fpJCi0vg&s'},
    {'Name':'khunfa','Image':'https://media-assets.swiggy.com/swiggy/image/upload/f_auto,q_auto,fl_lossy/wmltmg5tz1aygnuo0qas'},
    {'Name':'khunafa cheesecake','Image':'https://flaircakeboutique.com/wp-content/uploads/2023/04/WhatsApp-Image-2023-04-12-at-3.13.14-PM.jpeg'},
    {'Name':'Aloo Tikki','Image':'https://www.indianveggiedelight.com/wp-content/uploads/2023/07/aloo-tikki-featured.jpg'},
    {'Name':'Pani Puri','Image':'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Pani_Puri1.JPG/640px-Pani_Puri1.JPG'}
]
st.title('INDIA STREET FOOD TOUR ')
if st.button('Generate me some food'):
    food= random.choice(food)

    st.subheader(food['Name'])
    st.image(food['Image'],caption=food['Name'])