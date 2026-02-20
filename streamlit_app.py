import os
import sys

# Add the src directory to the path so local modules (financial_math, etc.) can be imported
_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
if _src not in sys.path:
    sys.path.insert(0, _src)

# Execute the Streamlit application from src/app_interface.py.
# Using exec/compile (instead of import) ensures the app code is re-run on every
# Streamlit interaction cycle, which is required for widget state to work correctly.
_app_file = os.path.join(_src, "app_interface.py")
try:
    with open(_app_file, encoding="utf-8") as _f:
        exec(compile(_f.read(), _app_file, "exec"))  # noqa: S102
except FileNotFoundError:
    import streamlit as st
    st.error(f"No se encontró el archivo de la aplicación: {_app_file}")
    st.stop()
