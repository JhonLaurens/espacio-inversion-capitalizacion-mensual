import base64

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Importar lógica de negocio
from financial_math import FinancialMath

# Configuración de la página
st.set_page_config(
    page_title="Inversión Capitalización Mensual",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --- FUNCIONES AUXILIARES ---
def get_image_base64(path):
    """Convierte una imagen a base64 para embeberla en HTML"""
    try:
        with open(path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
        return f"data:image/png;base64,{encoded}"
    except Exception:
        return ""


def generar_proyeccion(p0, r, n_meses):
    """Genera dataframe con la proyección completa"""
    datos = []
    for mes in range(n_meses + 1):
        geom = FinancialMath.calcular_interes_compuesto(p0, r, mes)
        arit = FinancialMath.calcular_interes_simple(p0, r, mes)
        datos.append(
            {
                "Mes": mes,
                "Geométrico": geom,
                "Aritmético": arit,
                "Diferencia": geom - arit,
            }
        )
    return pd.DataFrame(datos)


# --- CARGAR LOGOS ---
logo_dark = get_image_base64("assets/logo_dark_theme.png")  # Para tema CLARO
logo_light = get_image_base64("assets/logo_light_theme.png")  # Para tema OSCURO

# --- ESTILOS CSS PERSONALIZADOS Y LOGO AUTOMÁTICO ---
st.markdown(
    """
<style>
    /* Estilos Generales */
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1E3A8A;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .stButton>button {
        width: 100%;
        background-color: #1E3A8A;
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1e40af;
    }

    /* LOGO AUTOMÁTICO (CSS) */
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .logo-img {
        width: 100%;
        max-width: 250px;
        height: auto;
    }
    
    /* Por defecto (Tema Claro): Mostrar logo oscuro, ocultar claro */
    .logo-for-light-theme { display: block; }
    .logo-for-dark-theme { display: none; }
    
    /* En Tema Oscuro (media query): Ocultar oscuro, mostrar claro */
    @media (prefers-color-scheme: dark) {
        .logo-for-light-theme { display: none; }
        .logo-for-dark-theme { display: block; }
    }
    
    /* Soporte adicional para atributo data-theme de Streamlit si está presente */
    [data-theme="dark"] .logo-for-light-theme { display: none; }
    [data-theme="dark"] .logo-for-dark-theme { display: block; }
</style>
""",
    unsafe_allow_html=True,
)

# --- SIDEBAR: CONFIGURACIÓN ---
with st.sidebar:
    # Renderizar Logo HTML con ambas imágenes
    st.markdown(
        f"""
    <div class="logo-container">
        <img src="{logo_dark}" class="logo-img logo-for-light-theme" alt="Logo ITM">
        <img src="{logo_light}" class="logo-img logo-for-dark-theme" alt="Logo ITM">
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.header("Parámetros de Inversión")
    st.markdown("---")

    # Entradas
    p0 = st.number_input(
        "Capital Inicial ($)",
        min_value=100000.0,
        value=8000000.0,
        step=100000.0,
        format="%f",
    )

    r_percent = st.number_input(
        "Tasa Mensual (%)", min_value=0.1, value=1.2, step=0.1, format="%.2f"
    )
    r = r_percent / 100.0

    n = st.slider("Plazo (Meses)", min_value=6, max_value=120, value=36)

    st.markdown("---")
    st.info(f"**Tasa Efectiva Anual aprox:** {((1+r)**12 - 1)*100:.2f}%")
    st.markdown("---")
    st.caption("v1.0.0 - Modelo Académico")

# --- CUERPO PRINCIPAL ---
st.markdown(
    '<div class="main-header">Espacio para Inversión con Capitalización Mensual</div>',
    unsafe_allow_html=True,
)

# 1. Cálculos
df = generar_proyeccion(p0, r, n)
capital_final = df.iloc[-1]["Geométrico"]
ganancia = capital_final - p0
meses_duplicacion = FinancialMath.calcular_meses_duplicacion(r)

# 2. KPIs (Tarjetas Superiores)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
    <div class="metric-card">
        <h3 style="margin:0; font-size:1rem; color:#6B7280;">Capital Final</h3>
        <h2 style="margin:0; color:#1E3A8A;">${capital_final:,.0f}</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
    <div class="metric-card">
        <h3 style="margin:0; font-size:1rem; color:#6B7280;">Ganancia Total</h3>
        <h2 style="margin:0; color:#10B981;">+${ganancia:,.0f}</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        f"""
    <div class="metric-card">
        <h3 style="margin:0; font-size:1rem; color:#6B7280;">Rendimiento Total</h3>
        <h2 style="margin:0; color:#F59E0B;">{(ganancia/p0)*100:.1f}%</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        f"""
    <div class="metric-card">
        <h3 style="margin:0; font-size:1rem; color:#6B7280;">Tiempo Duplicación</h3>
        <h2 style="margin:0; color:#6366F1;">{meses_duplicacion:.1f} m</h2>
    </div>
    """,
        unsafe_allow_html=True,
    )

# 3. Gráficos y Tablas
st.markdown("### 📊 Análisis de Crecimiento")

tab1, tab2, tab3 = st.tabs(
    ["Gráfico Comparativo", "Tabla Detallada", "Análisis Matemático"]
)

with tab1:
    # Gráfico interactivo con Plotly
    fig = go.Figure()

    # Línea Geométrica (Interés Compuesto)
    fig.add_trace(
        go.Scatter(
            x=df["Mes"],
            y=df["Geométrico"],
            mode="lines+markers",
            name="Interés Compuesto (Geométrico)",
            line=dict(color="#1E3A8A", width=3),
            hovertemplate="Mes %{x}<br>Capital: $%{y:,.0f}",
        )
    )

    # Línea Aritmética (Interés Simple)
    fig.add_trace(
        go.Scatter(
            x=df["Mes"],
            y=df["Aritmético"],
            mode="lines",
            name="Interés Simple (Aritmético)",
            line=dict(color="#EF4444", width=2, dash="dash"),
            hovertemplate="Mes %{x}<br>Capital: $%{y:,.0f}",
        )
    )

    fig.update_layout(
        title="Comparación de Modelos de Crecimiento",
        xaxis_title="Meses",
        yaxis_title="Capital ($)",
        hovermode="x unified",
        template="plotly_white",
        height=500,
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        f"💡 **Insight**: Al mes {n}, el interés compuesto ha generado **${(df.iloc[-1]['Diferencia']):,.0f}** más que el interés simple."
    )

with tab2:
    st.markdown("#### Desglose Mensual")

    # Formatear columnas para visualización
    df_display = df.copy()
    for col in ["Geométrico", "Aritmético", "Diferencia"]:
        df_display[col] = df_display[col].apply(lambda x: f"${x:,.2f}")

    st.dataframe(
        df_display,
        use_container_width=True,
        height=400,
        column_config={"Mes": st.column_config.NumberColumn("Mes", format="%d")},
    )

    # Botón de descarga CSV
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Descargar Reporte CSV",
        data=csv,
        file_name=f"inversion_p{p0:.0f}_n{n}.csv",
        mime="text/csv",
    )

with tab3:
    st.markdown(
        """
    ### Fundamentos Matemáticos
    
    Este simulador se basa en **Progresiones Geométricas**, una técnica de conteo donde cada término se obtiene multiplicando el anterior por una razón constante.
    
    #### 1. Fórmula de Interés Compuesto
    $$P_n = P_0 (1 + r)^n$$
    Donde:
    - $P_n$: Capital final
    - $P_0$: Capital inicial
    - $r$: Tasa de interés
    - $n$: Número de períodos (meses)
    
    #### 2. Tiempo de Duplicación
    Para saber cuándo se duplica el dinero ($P_n = 2P_0$):
    $$n = \\frac{\ln(2)}{\ln(1+r)}$$
    
    #### 3. Diferencia con Modelo Aritmético
    El modelo aritmético (Interés Simple) crece linealmente:
    $$A_n = P_0 + (n \\cdot P_0 \\cdot r)$$
    """
    )
