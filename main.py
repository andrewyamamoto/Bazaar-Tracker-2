from nicegui import ui
import os

@ui.page('/')
def main_page():
    ui.label('Hello NiceGUI!')

ui.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))