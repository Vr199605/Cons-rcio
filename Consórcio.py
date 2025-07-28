import streamlit as st
import plotly.graph_objects as go

# Função para calcular os valores da simulação
def simular_consorcio(valor_carta, parcelas, valor_parcela, percentual_venda, valor_embutido):
    valor_carta_liquido = valor_carta * (1 - valor_embutido / 100)

    valor_total_pago = parcelas * valor_parcela
    valor_venda = valor_carta_liquido * (percentual_venda / 100)
    lucro = valor_venda - valor_total_pago
    rendimento_bruto = (lucro / valor_total_pago) * 100 if valor_total_pago else 0

    # Rendimento mensal simples (rendimento bruto dividido pelo número de parcelas)
    rendimento_mensal = rendimento_bruto / parcelas if parcelas else 0

    return valor_total_pago, valor_venda, lucro, rendimento_bruto, rendimento_mensal, valor_carta_liquido

# Título
st.title("Simulador de Venda de Carta de Crédito")

# Entradas do usuário
valor_carta = st.number_input("Valor da Carta de Crédito (R$)", min_value=1000.0, step=500.0, format="%.2f")
parcelas = st.number_input("Número de Parcelas", min_value=1, step=1)
valor_parcela = st.number_input("Valor da Parcela (R$)", min_value=0.0, step=50.0, format="%.2f")
percentual_venda = st.selectbox("Porcentagem do Valor de Venda da Carta (%)", [20, 25, 30, 40])
valor_embutido = st.selectbox("Valor Embutido (%)", [0, 20, 40])

# Botão de simular
if st.button("Simular"):
    total_pago, valor_venda, lucro, rendimento_bruto, rendimento_mensal, valor_carta_liquido = simular_consorcio(
        valor_carta, parcelas, valor_parcela, percentual_venda, valor_embutido
    )

    # Resultados
    st.subheader("📊 Resultados da Simulação:")
    st.write(f"💳 Valor da Carta Líquido (após {valor_embutido}% embutido): R$ {valor_carta_liquido:,.2f}")
    st.write(f"💰 Valor Total Pago: R$ {total_pago:,.2f}")
    st.write(f"🏷️ Valor de Venda da Carta (com percentual de venda): R$ {valor_venda:,.2f}")
    st.write(f"📈 Lucro Estimado (líquido): R$ {lucro:,.2f}")
    st.write(f"📊 Rendimento Bruto: {rendimento_bruto:.2f}%")
    st.write(f"📅 Rendimento Mensal Aproximado: {rendimento_mensal:.2f}%")

    # Gráfico interativo
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Valor Total Pago', x=['Simulação'], y=[total_pago], marker_color='indianred'))
    fig.add_trace(go.Bar(name='Valor de Venda', x=['Simulação'], y=[valor_venda], marker_color='green'))
    fig.add_trace(go.Bar(name='Lucro', x=['Simulação'], y=[lucro], marker_color='blue'))

    fig.update_layout(barmode='group', title='Comparativo de Valores', xaxis_title='Indicadores', yaxis_title='R$')
    st.plotly_chart(fig)

    st.success("Simulação finalizada com sucesso! 🚀")
