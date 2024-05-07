import PySimpleGUI as sg
import src

sg.theme("DarkAmber")

counties = src.county_data.counties.get_counties()

left_pane = [[sg.Button(county, key=f"-{county.upper()}-")] for county in counties]

# right_pane = [[sg.Text("Test")]]

layout = [
    [
        sg.Text(
            f"Tax Matrix, {src.config.current_version()}, updated as of {src.config.date_revised()}"
        )
    ],
    [sg.HorizontalSeparator(color="white")],
    [
        sg.Text("Subject Value/Purchase Price"),
        sg.InputText(key="-PURCHASE_PRICE-", enable_events=True),
        sg.Button("Submit", key="-SUBMIT-"),
    ],
    [sg.HorizontalSeparator(color="white")],
    [
        sg.Column(left_pane),
        # sg.VerticalSeparator(color="white"),
        # sg.Column(right_pane),
    ],
    [sg.HorizontalSeparator(color="white")],
    [sg.Button("Exit")],
]

window = sg.Window("Tax Matrix", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-SUBMIT-":
        try:
            purchase_price = int(values["-PURCHASE_PRICE-"])
            formatted_price = f"${purchase_price:,}"
            window["-PURCHASE_PRICE-"].update(formatted_price)
        except ValueError:
            pass

window.close()
