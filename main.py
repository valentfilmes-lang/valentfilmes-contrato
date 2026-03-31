import streamlit as st
from fpdf import FPDF
from datetime import datetime

st.set_page_config(page_title="Contratos ValentFilmes", page_icon="📸")

st.title("📸 Gerador de Contrato - ValentFilmes")

with st.form("dados_contrato"):
    st.subheader("1. Dados do Contratante")
    nome = st.text_input("Nome Completo")
    documento = st.text_input("CPF ou CNPJ")
    contato = st.text_input("WhatsApp")
    
    st.subheader("2. Tipo de Evento")
    # Opção de marcação única para o tipo de evento
    tipo_evento = st.radio(
        "Selecione o tipo de evento:",
        ["Aniversário infantil", "Aniversário 15 anos", "Casamento", "Aniversário adulto"],
        horizontal=True
    )
    homenageado = st.text_input("Nome do Homenageado")
    data_evento = st.date_input("Data do Evento")
    local_evento = st.text_input("Local do Evento")

    st.divider()

    st.subheader("3. Quais serviços você tem interesse?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**📸 Fotografia Casamento:**")
        foto_pre = st.checkbox("Cobertura Pré-wedding")
        foto_pos = st.checkbox("Cobertura Pós-wedding")
        foto_mak = st.checkbox("Cobertura Making-of")
        foto_cer = st.checkbox("Cobertura Cerimônia")
        foto_rec = st.checkbox("Cobertura Recepção")
        
        st.write("**🎥 Filmagem Casamento:**")
        film_pre = st.checkbox("Cobertura Pré-wedding ", key="f1")
        film_pos = st.checkbox("Cobertura Pós-wedding ", key="f2")
        film_mak = st.checkbox("Cobertura Making-of ", key="f3")
        film_cer = st.checkbox("Cobertura Cerimônia ", key="f4")
        film_rec = st.checkbox("Cobertura Recepção ", key="f5")

    with col2:
        st.write("**🚀 Adicionais e Entretenimento:**")
        drone = st.checkbox("Filmagem aérea com drone")
        plat360 = st.checkbox("Plataforma 360")
        totem = st.checkbox("Totem fotográfico")
        cabine = st.checkbox("Cabine fotográfica")
        tunel = st.checkbox("Túnel infinity")

    st.warning("O valor final será ajustado conforme os serviços selecionados acima.")
    gerar = st.form_submit_button("Gerar Contrato com Serviços Selecionados")

if gerar:
    # Lógica para listar apenas o que foi marcado
    servicos_selecionados = []
    if foto_pre: servicos_selecionados.append("Fotografia: Pré-wedding")
    if foto_pos: servicos_selecionados.append("Fotografia: Pós-wedding")
    if foto_mak: servicos_selecionados.append("Fotografia: Making-of")
    if foto_cer: servicos_selecionados.append("Fotografia: Cerimônia")
    if foto_rec: servicos_selecionados.append("Fotografia: Recepção")
    if film_pre: servicos_selecionados.append("Filmagem: Pré-wedding")
    if film_pos: servicos_selecionados.append("Filmagem: Pós-wedding")
    if film_mak: servicos_selecionados.append("Filmagem: Making-of")
    if film_cer: servicos_selecionados.append("Filmagem: Cerimônia")
    if film_rec: servicos_selecionados.append("Filmagem: Recepção")
    if drone: servicos_selecionados.append("Filmagem aérea com drone")
    if plat360: servicos_selecionados.append("Plataforma 360")
    if totem: servicos_selecionados.append("Totem fotográfico")
    if cabine: servicos_selecionados.append("Cabine fotográfica")
    if tunel: servicos_selecionados.append("Túnel infinity")

    # Geração do PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(0, 10, "CONTRATO DE PRESTAÇÃO DE SERVIÇOS - VALENTFILMES", ln=True, align="C")
    pdf.ln(10)
    
    pdf.set_font("helvetica", "", 11)
    pdf.multi_cell(0, 7, f"CONTRATANTE: {nome}\nDOCUMENTO: {documento}\nWHATSAPP: {contato}\n")
    pdf.multi_cell(0, 7, f"EVENTO: {tipo_evento} ({homenageado})\nDATA: {data_evento.strftime('%d/%m/%Y')}\nLOCAL: {local_evento}\n")
    
    pdf.set_font("helvetica", "B", 12)
    pdf.cell(0, 10, "SERVIÇOS CONTRATADOS:", ln=True)
    pdf.set_font("helvetica", "", 11)
    
    if servicos_selecionados:
        for s in servicos_selecionados:
            pdf.cell(0, 7, f"- {s}", ln=True)
    else:
        pdf.cell(0, 7, "- Nenhum serviço específico selecionado.", ln=True)
        
    pdf.ln(5)
    pdf.set_font("helvetica", "B", 11)
    pdf.multi_cell(0, 7, "CLÁUSULAS E CONDIÇÕES:")
    pdf.set_font("helvetica", "", 10)
    pdf.multi_cell(0, 5, "1. PAGAMENTO: Conforme política da ValentFilmes (Entrada + restante na semana do evento).\n"
                         "2. DESISTÊNCIA: Retenção de 40% do valor total conforme Art. 420 do CC.\n"
                         "3. USO DE IMAGEM: Autorizado para fins de portfólio e redes sociais.\n"
                         "4. FORO: Comarca de Contagem/MG.")

    pdf.ln(10)
    pdf.cell(0, 10, f"Assinado digitalmente em {datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=True)
    
    pdf_output = f"Contrato_{nome.replace(' ', '_')}.pdf"
    pdf.output(pdf_output)

    with open(pdf_output, "rb") as f:
        st.success("✅ Contrato com serviços detalhados gerado!")
        st.download_button("📥 Baixar PDF Atualizado", f, file_name=pdf_output)
