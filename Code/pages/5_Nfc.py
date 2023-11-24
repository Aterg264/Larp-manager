import nfc
import ndef
import streamlit as st

if ndef is not None:
    for record in ndef.records:
        print(record)


st.write(ndef is not None)
st.write(ndef.is_writeable)