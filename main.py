import streamlit as st
from fpdf import FPDF
from datetime import datetime

st.set_page_config(page_title="Contratos ValentFilmes", page_icon="📸")

st.title("📸 Gerador de Contrato - ValentFilmes")

with st.form("dados_contrato"):
    st.subheader("📝 Preencha os campos abaixo")
    
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Contratante")
        documento = st.text_input("CPF/CNPJ")
        endereco_cli = st.text_input("Endereço (Rua/Nº)")
        bairro = st.text_input("Bairro")
    with col2:
        homenageado = st.text_input("Homenageado")
        contato = st.text_input("Contato (Tel/Zap)")
        cidade = st.text_input("Cidade", value="Contagem")
        tipo_evento = st.selectbox("Tipo de Evento", ["Aniversário infantil", "Aniversário 15 anos", "Casamento", "Aniversário adulto"])

    st.divider()
    
    col3, col4 = st.columns(2)
    with col3:
        data_evento = st.date_input("Data do Evento")
        local_evento = st.text_input("Endereço do Evento")
    with col4:
        horario = st.text_input("Horário do Totem", value="20:00hs às 00:00hs")

    st.subheader("💡 Quais serviços você tem interesse?")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**Fotografia/Filmagem:**")
        s_foto = st.multiselect("Fotografia", ["Pré-wedding", "Pós-wedding", "Making-of", "Cerimônia", "Recepção"])
        s_film = st.multiselect("Filmagem", ["Pré-wedding ", "Pós-wedding ", "Making-of ", "Cerimônia ", "Recepção "])
    with c2:
        st.write("**Estrutura:**")
        drone = st.checkbox("Filmagem aérea com drone")
        plat360 = st.checkbox("Plataforma 360")
        totem = st.checkbox("Totem fotográfico")
        cabine = st.checkbox("Cabine fotográfica")
        tunel = st.checkbox("Túnel infinity")

    gerar = st.form_submit_button("Gerar Contrato Idêntico")

if gerar:
    pdf = FPDF()
    pdf.add_page()
    
    # Cabeçalho Identidade Visual
    pdf.set_font("helvetica", "B", 10)
    pdf.cell(0, 5, "VALENTI www.valentfilmes.com.br I @valentfilmes", ln=True, align="R")
    pdf.ln(5)

    # SEÇÃO: DADOS PESSOAIS
    pdf.set_fill_color(240, 240, 240)
    pdf.set_font("helvetica", "B", 11)
    pdf.cell(0, 8, " Dados Pessoais:", ln=True, fill=True)
    pdf.set_font("helvetica", "", 10)
    
    y_pessoais = pdf.get_y()
    pdf.multi_cell(95, 7, f"Contratante: {nome}\nHomenageado: {homenageado}\nEndereço: {endereco_cli}\nBairro: {bairro}")
    pdf.set_y(y_pessoais)
    pdf.set_x(105)
    pdf.multi_cell(95, 7, f"CPF/CNPJ: {documento}\nContato: {contato}\nCidade: {cidade}")
    pdf.ln(5)

    # SEÇÃO: DADOS DO EVENTO
    pdf.set_font("helvetica", "B", 11)
    pdf.cell(0, 8, " Dados do Evento:", ln=True, fill=True)
    pdf.set_font("helvetica", "", 10)
    
    y_evento = pdf.get_y()
    pdf.multi_cell(95, 7, f"Tipo de Evento: {tipo_evento}\nEndereço do Evento: {local_evento}")
    pdf.set_y(y_evento)
    pdf.set_x(105)
    pdf.multi_cell(95, 7, f"Data do Evento: {data_evento.strftime('%d/%m/%Y')}\nHorário do Evento: {horario}")
    pdf.ln(5)

    # SEÇÃO: SERVIÇOS SELECIONADOS
    pdf.set_font("helvetica", "B", 11)
    pdf.cell(0, 8, " Serviços Contratados:", ln=True, fill=True)
    pdf.set_font("helvetica", "", 9)
    
    servicos_txt = ""
    if s_foto: servicos_txt += f"• Fotografia: {', '.join(s_foto)}\n"
    if s_film: servicos_txt += f"• Filmagem: {', '.join(s_film)}\n"
    if drone: servicos_txt += "• Filmagem aérea com drone\n"
    if plat360: servicos_txt += "• Plataforma 360\n"
    if totem: servicos_txt += "• Totem fotográfico por 4 horas (Fotos ilimitadas, monitor, arte personalizada, adereços)\n"
    if cabine: servicos_txt += "• Cabine fotográfica\n"
    if tunel: servicos_txt += "• Túnel infinity\n"
    
    pdf.multi_cell(0, 6, servicos_txt if servicos_txt else "Nenhum serviço selecionado.")
    pdf.ln(5)

    # VALOR E PAGAMENTO
    pdf.set_font("helvetica", "B", 10)
    pdf.multi_cell(0, 6, "Valor total: R$ 1100,00 com entrada à vista no ato do fechamento e restante na semana do evento.")
    pdf.set_font("helvetica", "", 9)
    pdf.cell(0, 6, "Pagamento via chave pix email (valentselfie@gmail.com) - banco nubank.", ln=True)
    pdf.ln(5)

    # CLÁUSULAS (Resumo das principais conforme seu PDF)
    pdf.set_font("helvetica", "B", 11)
    pdf.cell(0, 8, " Cláusulas:", ln=True, fill=True)
    pdf.set_font("helvetica", "", 8)
    clausulas = (
        "Cláusula Segunda: Em caso de desistência, fica estipulada a retenção das arras penitenciais (40% do valor).\n"
        "Cláusula Décima Quarta: Os arquivos ficam arquivados pelo prazo máximo de 05 meses.\n"
        "Parágrafo Único: O CONTRATANTE autoriza o uso de sua imagem para portfólio e Redes Sociais.\n"
        "Cláusula Décima Sexta: Elegem o foro da comarca de CONTAGEM MG para medidas legais."
    )
    pdf.multi_cell(0, 5, clausulas)
    
    pdf.ln(10)
    pdf.cell(95, 10, "__________________________", ln=0, align="C")
    pdf.cell(95, 10, "__________________________", ln=1, align="C")
    pdf.cell(95, 5, "Contratante", ln=0, align="C")
    pdf.cell(95, 5, "ValentFilmes", ln=1, align="C")

    # Salvar
    pdf_output = f"Contrato_{nome.replace(' ', '_')}.pdf"
    pdf.output(pdf_output)

    with open(pdf_output, "rb") as f:
        st.success("✅ Layout gerado com sucesso!")
        st.download_button("📥 Baixar Contrato Identico", f, file_name=pdf_output)
