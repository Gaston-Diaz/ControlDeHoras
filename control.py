import PySimpleGUI as sg
import calendar
from datetime import datetime

def create_calendar_layout(year, month):
    # Obtener el calendario para el mes y año especificados
    cal = calendar.monthcalendar(year, month)
    
    # Crear la cabecera del calendario
    layout = [[sg.Text(calendar.month_name[month] + ' ' + str(year), size=(20,1), justification='center', font=("Helvetica", 25))]]
    layout.append([sg.Text(day, size=(5, 1), justification='center') for day in ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']])
    
    # Crear las filas del calendario
    for week in cal:
        row = []
        for day in week:
            if day == 0:
                row.append(sg.Text('', size=(5, 2)))
            else:
                row.append(sg.Button(str(day), size=(5, 2)))
        layout.append(row)
    
    return layout

def main():
    # Obtener la fecha actual del sistema
    now = datetime.now()
    year, month = now.year, now.month
    
    # Crear el diseño del calendario
    layout = create_calendar_layout(year, month)
    
    # Crear la ventana de PySimpleGUI
    window = sg.Window('Calendario', layout)
    
    while True:
        event, values = window.read()
        
        # Si se cierra la ventana, salir del bucle
        if event == sg.WINDOW_CLOSED:
            break
        
        # Aquí se pueden manejar otros eventos del calendario
        print(f'Botón presionado: {event}')
    
    window.close()

if __name__ == '__main__':
    main()



