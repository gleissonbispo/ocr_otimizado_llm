# =============================
# 📄 OCR de PDF com LLM Local
# =============================

# 📦 Bibliotecas
import streamlit as st
from PIL import Image
from pdf2image import convert_from_bytes
import pytesseract
import re
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# =============================
# ⚙️ Inicialização do Modelo LLM (Ollama local)
# =============================
llm = ChatOllama(model="gemma3:4b")

prompt = PromptTemplate(
    template="""
Você receberá um texto extraído por OCR. Ele pode conter palavras desconexas, quebras de linha desnecessárias e erros de pontuação.

Seu trabalho é:

- Corrigir os erros.
- Melhorar a pontuação.
- E formatar como um documento em **Markdown** que seja pronto para o print.
- Não inclua comentários.
- Utilize apenas o texto.
- Faça apenas o que foi pedido.

Use títulos (`##`), subtítulos (`####`), quebras de parágrafo e ênfases quando apropriado. Preserve a estrutura do documento original sempre que possível.

Texto OCR:
{texto_extraido}
""",
    input_variables=["texto_extraido"]
)

# =============================
# 🎨 Configuração da Interface
# =============================
st.set_page_config(page_title="OCR otimizado com Gen AI", page_icon="📄", layout="centered")

with st.container():
    st.title("📄 OCR otimizado com Gen AI")
    st.caption("Extração de texto via OCR e formatação automática com LLM local.")
    st.markdown("---")

# =============================
# 📂 Upload de Arquivo
# =============================
uploaded_file = st.file_uploader("Escolha um arquivo", type=["pdf"])

# =============================
# 🧹 Funções de Pré-processamento
# =============================
def clean_text(text):
    text = text.replace('-\n', '')  # Junta palavras cortadas por hifenização
    text = re.sub(r'[ \t]+\n', '\n', text)  # Remove espaços antes de quebras
    text = re.sub(r'\n{2,}', '\n\n', text)  # Força quebras de parágrafo
    return text.strip()

# =============================
# 🚀 Processamento do OCR + LLM
# =============================
if uploaded_file is not None:
    with st.spinner('📄 Convertendo PDF em imagens...'):
        images = convert_from_bytes(uploaded_file.read(), dpi=300)

    st.success(f"{len(images)} página(s) convertida(s).")

    full_text = ""
    for idx, img in enumerate(images):
        st.image(img, caption=f"Página {idx + 1}", use_container_width=True)
        raw_text = pytesseract.image_to_string(img, lang='por')
        full_text += raw_text + "\n\n"

    cleaned_text = clean_text(full_text)

    with st.status("💡 Formatando com LLM...", expanded=True) as status:
        resposta = llm.invoke(prompt.format(texto_extraido=cleaned_text))
        markdown_text = str(resposta.content.strip()).replace("```markdown", "").strip("```")
        status.update(label="✅ Texto formatado com sucesso!", state="complete")

    # =============================
    # 🖥️ Exibição do Resultado
    # =============================
    st.subheader("📝 Texto Formatado (Markdown)")
    st.markdown("---")
    st.markdown(markdown_text, unsafe_allow_html=True)

    # =============================
    # 💾 Download
    # =============================
    st.download_button(
        label="📥 Baixar Markdown",
        data=markdown_text,
        file_name="texto_formatado.md",
        mime="text/markdown"
    )

    st.markdown("---")
    st.caption("🔐 Todo o processamento ocorre localmente, com segurança e privacidade garantidas.")
