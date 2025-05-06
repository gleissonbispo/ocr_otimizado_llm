
# 📄 OCR Inteligente de PDFs com LLM Local + Markdown

Transforme arquivos PDF em texto limpo e formatado automaticamente, pronto para publicação ou impressão.  
Este projeto utiliza **OCR via Tesseract**, integrado a um **modelo de linguagem local via Ollama**, que reestrutura e melhora o texto retornando em **formato Markdown**.

---

## 🚀 Demonstração

![ocr-llm-demo](/OCR.gif) <!-- Substitua pelo seu GIF ou imagem -->

---

## 🧰 Tecnologias Utilizadas

| Categoria            | Ferramentas & Bibliotecas                                         |
|----------------------|-------------------------------------------------------------------|
| **LLM Local**        | [Ollama](https://ollama.com) · Modelo: `gemma3:12b`               |
| **Orquestração**     | LangChain · PromptTemplate                                        |
| **OCR**              | Tesseract OCR                                                     |
| **Conversão PDF**    | Poppler · `pdf2image`                                             |
| **Interface**        | Streamlit                                                         |
| **Backend**          | Python                                                            |

---

## 🧱 Funcionalidades

### 📥 Upload e Leitura de PDFs
- Upload de arquivos PDF com múltiplas páginas
- Conversão para imagem com **Poppler + pdf2image**
- Extração de texto com **Tesseract OCR (idioma: português)**

### 🤖 Otimização com LLM Local
- Integração com modelo **Gemma3:12b** rodando via **Ollama**
- Prompt otimizado para:
  - Corrigir erros de OCR
  - Melhorar pontuação e fluidez
  - Manter a estrutura de parágrafos original
  - **Formatar como Markdown** com títulos, listas e ênfases

### 🖥️ Exibição e Exportação
- Visualização bonita do conteúdo formatado
- Suporte a **Markdown renderizado**
- Botão para **download como `.md`** (pronto para colar no Notion, GitHub, etc.)

---

## ⚙️ Instalação

### 1. Instale os programas necessários no sistema

#### 🔠 Tesseract OCR

- **Windows**:  
  Baixe o instalador via [repositório da UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)  
  > ⚠️ Durante a instalação, marque a opção para adicionar o `tesseract.exe` ao PATH.

- **Linux (Debian/Ubuntu)**:
  ```bash
  sudo apt install tesseract-ocr
  ```

---

#### 📄 Poppler (obrigatório para ler PDF com `pdf2image`)

- **Windows**:

  1. Baixe o ZIP do Poppler para Windows:  
     👉 https://github.com/oschwartz10612/poppler-windows/releases
  2. Extraia em um diretório, ex: `C:\poppler\`
  3. Adicione o seguinte caminho à variável de ambiente **PATH**:  
     ```
     C:\poppler\Library\bin
     ```
  4. Reinicie o terminal após adicionar ao PATH.

- **Linux (Debian/Ubuntu)**:
  ```bash
  sudo apt install poppler-utils
  ```

---

#### 🤖 Ollama + Modelo LLM

- Instale o Ollama:  
  👉 https://ollama.com

- Baixe e rode o modelo:

  ```bash
  ollama run gemma3:12b
  ```

---

### 2. Clone o projeto e instale as dependências Python

```bash
git clone https://github.com/gleissonbispo/ocr_otimizado_llm.git
cd ocr_otimizado_llm
pip install -r requirements.txt
```

> **Requisitos principais**:
> - streamlit
> - pytesseract
> - pdf2image
> - pillow
> - langchain
> - langchain-community

---

### 3. Execute a aplicação

```bash
streamlit run app_ocr.py
```


## 🔐 Privacidade

Este projeto **não depende de nuvem**.  
Tanto o OCR quanto o modelo LLM rodam **localmente na sua máquina**, garantindo segurança total dos dados.

