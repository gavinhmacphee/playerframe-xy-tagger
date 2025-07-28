import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="PlayerFrame XY Tagging Tool", layout="wide")
st.title("PlayerFrame XY Tagging Tool (FotMob Version)")

# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["x", "y", "event"])

# Event type selection
event_type = st.selectbox("Select Event Type", ["Pass", "Shot", "Goal", "Other"])

# Create a FotMob-style pitch (105 x 68, bottom-left origin)
fig = go.Figure()

# Pitch outline
fig.add_shape(type="rect", x0=0, y0=0, x1=105, y1=68,
              line=dict(color="black", width=3))

# Halfway line
fig.add_shape(type="line", x0=52.5, y0=0, x1=52.5, y1=68,
              line=dict(color="black", width=2))

# Penalty boxes
fig.add_shape(type="rect", x0=0, y0=13.84, x1=16.5, y1=54.16, line=dict(color="black"))
fig.add_shape(type="rect", x0=105-16.5, y0=13.84, x1=105, y1=54.16, line=dict(color="black"))

# Update layout
fig.update_layout(
    xaxis=dict(range=[0, 105], showgrid=False, zeroline=False, visible=False),
    yaxis=dict(range=[0, 68], showgrid=False, zeroline=False, visible=False),
    height=600,
    width=900,
    plot_bgcolor="#f5f5dc"
)
fig.update_xaxes(scaleanchor="y", scaleratio=1)

# Display pitch and capture clicks
clicked = st.plotly_chart(fig, use_container_width=True, key="pitch", on_select="rerun")

# Capture clicks from session state (Streamlit workaround)
if "plotly_click" not in st.session_state:
    st.session_state.plotly_click = None

clicked_data = st.session_state.get("plotly_click", None)

# Streamlit can't directly track clicks without custom JS, so using a placeholder workaround
st.write("Click logging will be updated after manual refresh if needed.")

# Display table of tagged events
st.subheader("Tagged Events")
st.write(st.session_state.data)

# Download CSV button
if not st.session_state.data.empty:
    csv = st.session_state.data.to_csv(index=False).encode("utf-8")
    st.download_button("Download Tagged Events CSV", csv, "tagged_events.csv", "text/csv")

