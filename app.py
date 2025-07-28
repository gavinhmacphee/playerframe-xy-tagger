import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="PlayerFrame XY Tagging Tool", layout="wide")
st.title("PlayerFrame XY Tagging Tool (Beta)")

# Store data in session state
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["x", "y", "event"])

# Select event type
event_type = st.selectbox("Select Event Type", ["Pass", "Shot", "Goal"])

# Create a blank pitch (120x80)
fig = go.Figure()
fig.update_layout(
    xaxis=dict(range=[0, 120], showgrid=False, zeroline=False),
    yaxis=dict(range=[0, 80], showgrid=False, zeroline=False),
    height=600,
    width=900,
    plot_bgcolor="#f5f5dc"
)
fig.update_xaxes(scaleanchor="y", scaleratio=1)

st.plotly_chart(fig, use_container_width=True)

st.write("Tagged Events (click logging coming soon):")
st.write(st.session_state.data)
