from nicegui import ui

ui.label('Hello NiceGUI!')

ui.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))