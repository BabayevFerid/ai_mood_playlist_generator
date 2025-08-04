import streamlit as st
from emotion_model import get_emotion
from spotify_recommender import get_playlist_by_emotion

st.set_page_config(page_title="AI Mood Playlist Generator", page_icon="🎵")
st.title("🎵 AI Mood Playlist Generator")

st.write("İstədiyin əhvalı yaz və AI sənə uyğun Spotify playlist təklif etsin.")

user_input = st.text_area("Bugünkü əhval-ruhiyyəni bir-iki cümlə ilə təsvir et:")

if user_input:
    with st.spinner("Emosiyan analiz olunur..."):
        emotion = get_emotion(user_input)
        playlist = get_playlist_by_emotion(emotion)

    st.success(f"Təyin olunan emosiyan: **{emotion.capitalize()}**")

    if playlist:
        st.markdown(f"### 🎧 [{playlist['name']}]({playlist['url']})")
        st.image(playlist['image'], width=300)
    else:
        st.warning("Təəssüf ki, uyğun playlist tapılmadı.")
