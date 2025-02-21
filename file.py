from vikingsClasses import Soldier, Viking, Saxon, War
import random
import streamlit as st

st.title("⚔️ Welcome to the battle of VIKINGS! ⚔️")
st.write("Battle simulator between Vikings and Saxons. Press the button to see the output of the battle.")

if "great_war" not in st.session_state:
    st.session_state.great_war = War()
    st.session_state.round = 0

    soldier_names = ["Albert", "Andres", "Archie", "Dani", "David", "Gerard", "German", "Graham", "Imanol", "Laura"]

    for _ in range(5):
        st.session_state.great_war.addViking(Viking(random.choice(soldier_names), 100, random.randint(0, 100)))
        st.session_state.great_war.addSaxon(Saxon(100, random.randint(0, 100)))

st.write(f"👥 **Viking Army:** {len(st.session_state.great_war.vikingArmy)} warriors")
st.write(f"🏰 **Saxon Army:** {len(st.session_state.great_war.saxonArmy)} warriors")

st.image("vikings.jpg")

if st.button("🔥 Let the battles begin!"):
    while st.session_state.great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        st.write(st.session_state.great_war.vikingAttack())
        st.write(st.session_state.great_war.saxonAttack())
        st.session_state.round += 1

    st.title( 
        f"The battle has finished in {st.session_state.round} rounds!\n")
    st.header(f"Vikings left: {len(st.session_state.great_war.vikingArmy)} 🛡️ // "
        f"Saxons left: {len(st.session_state.great_war.saxonArmy)} 🏰")
    
    st.success(st.session_state.great_war.showStatus())
    st.audio("victory.wav")