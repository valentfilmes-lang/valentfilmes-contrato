import streamlit as st
from fpdf import FPDF
from datetime import datetime

# Configurações de estilo e marca
st.set_page_config(page_title="Contratos ValentFilmes", page_icon="📸")

st.title("📸 Gerador de Contrato - ValentFilmes")
st.write("Preencha os campos abaixo para gerar seu contrato de Totem Fotográfico.")

# Formulário de entrada de dados
with st.form("dados_contrato"):
    st.subheader("1. Dados do Contratante")
    nome = st.text_input("Nome Completo / Razão Social")
    documento = st.text_input("CPF ou CNPJ")
    endereco_cli = st.text_input("Endereço Residencial")
    contato = st.text_input("Telefone de Contato (WhatsApp)")
    email = st.text_input("E-mail para envio da cópia")
    
    st.divider()
    
    st.subheader("2. Dados do Evento")
    homenageado = st.text_input("Nome do Homenageado")
    tipo_evento = st.text_input("Tipo de Evento (Ex: Casamento, 15 anos)")
    data_evento = st.date_input("Data do Evento")
    local_evento = st.text_input("Endereço/Local do Evento")
    horario = st.text_input("Horário do Totem", value="20:00hs às 00:00hs")

    st.divider()
    
    st.info("Ao clicar em Gerar, você concorda com as cláusulas de retenção de arras (40%) e uso de imagem.")
    gerar = st.form_submit_button("Gerar Contrato e Assinar")

if gerar:
    # Criação do PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    
    # Cabeçalho
    pdf.cell(200, 10, "CONTRATO DE PRESTAÇÃO DE SERVIÇOS - VALENTFILMES", ln=True, align='C')
    pdf.ln(5)
    
    pdf.set_font("Arial", size=10)
    # Dados preenchidos
    pdf.multi_cell(0, 7, f"CONTRATANTE: {nome}\nDOCUMENTO: {documento}\nENDEREÇO: {endereco_cli}\nCONTATO: {contato}")
    pdf.ln(3)
    pdf.multi_cell(0, 7, f"EVENTO: {tipo_evento} de {homenageado}\nDATA: {data_evento.strftime('%d/%m/%Y')}\nLOCAL: {local_evento}\nHORÁRIO: {horario}")
    pdf.ln(5)
    
    # Cláusulas do seu documento original
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 7, "SERVIÇOS E VALORES", ln=True)
    pdf.set_font("Arial", size=9)
    pdf.multi_cell(0, 5, "• Totem fotográfico por 4 horas com fotos impressas na hora e monitor.\n• Valor total: R$ 1.100,00 com entrada no ato e restante na semana do evento.")
    pdf.ln(3)
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 7, "PRINCIPAIS CLÁUSULAS", ln=True)
    pdf.set_font("Arial", size=9)
    pdf.multi_cell(0, 5, "CLÁUSULA SEGUNDA: Em caso de desistência, haverá retenção de 40% do valor total.\n"
                         "CLÁUSULA QUINTA: Após 30 dias do envio do link, a contratada está isenta de responsabilidade sobre os arquivos.\n"
                         "CLÁUSULA DÉCIMA QUINTA: O contratante autoriza o uso de imagem para fins de divulgação.")
    
    pdf.ln(10)
    pdf.cell(0, 10, f"Contagem/MG, {datetime.now().strftime('%d/%m/%Y')}", ln=True)
    pdf.ln(5)
    pdf.cell(0, 10, "________________________________________________", ln=True)
    pdf.cell(0, 5, f"Assinatura Digital: {nome} (IP registrado)", ln=True)

    # Output
    pdf_file = f"Contrato_{nome.replace(' ', '_')}.pdf"
    pdf.output(pdf_file)

    with open(pdf_file, "rb") as f:
        st.success("✅ Contrato Gerado!")
        st.download_button("📥 Baixar Contrato em PDF", f, file_name=pdf_file)
        
        # Link para WhatsApp
        msg = f"Olá, aqui é {nome}. Acabei de preencher o contrato para o evento no dia {data_evento.strftime('%d/%m/%Y')}!"
        link_zap = f"https://wa.me/55319XXXXXXXX?text={msg.replace(' ', '%20')}" # Coloque seu número aqui
        st.link_button("📲 Enviar Aviso pelo WhatsApp", link_zap)
