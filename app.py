import streamlit as st
from collections import Counter

st.title("📚 Analisador de Textos")

texto = st.text_area("Digite ou cole seu texto:")

if st.button("🔍 Analisar texto"):

    if texto == "":
        st.warning("Digite algum texto!")

    else:
        palavras = texto.lower().split()
        contagem = Counter(palavras)

        palavra, quantidade = contagem.most_common(1)[0]

        frases = texto.count(".") + texto.count("!") + texto.count("?")

        st.write("📝 Quantidade de palavras:", len(palavras))
        st.write("🔤 Quantidade de caracteres:", len(texto))
        st.write("📄 Quantidade de frases:", frases)
        st.write("⭐ Palavra mais frequente:", palavra)
        st.write("🔢 Apareceu:", quantidade, "vezes")
