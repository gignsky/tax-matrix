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
        sg.Button("Submit", key="-SUBMIT PURCHASE PRICE-"),
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
    if event == "-SUBMIT PURCHASE PRICE-":
        try:
            purchase_price = int(values["-PURCHASE_PRICE-"])
            formatted_price = f"${purchase_price:,}"
            window["-PURCHASE_PRICE-"].update(formatted_price)
        except ValueError:
            pass
    if event.startswith("-") and event.endswith("-"):
        county_name = event[1:-1].lower()
        county_data = counties.get(county_name)
        if county_data:
            src.county_data.county_gui.display_county_data(county_data)
window.close()
