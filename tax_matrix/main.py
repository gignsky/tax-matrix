import flet as ft
import subprocess
import time
import src

counties = src.county_data.counties.get_counties()
Subject=src.subject.Subject()

def main(page: ft.Page):
    title = ft.Text(value="Tax Matrix")
    version = ft.Text(value=f"Version: {src.config.current_version()}")
    update_date = ft.Text(value=f"Last Updated: {src.config.date_revised()}")

    page.controls.append(title)
    page.controls.append(version)
    page.controls.append(update_date)

    def submit_value(e):
        Subject.update_value(value_text_box.value)
        page.update()

    def choose_county(e):
        Subject.update_county(
            county_dropdown.value,
            counties[county_dropdown.value],
            counties[county_dropdown.value]["county_wide"],
        )
        city_dropdown.options = Subject.get_cities_dropdown()
        page.update()

    def choose_city(e):
        Subject.update_city(
            city_dropdown.value, Subject.county_dict["cities"][city_dropdown.value]
        )
        page.update()

    # declare value field for entering
    value_text_box = ft.TextField(
        hint_text="Enter Subject Value", value="", text_align="right"
    )

    list_of_county_dropdown_options = []
    # county options
    for county in list(counties):
        list_of_county_dropdown_options.append(ft.dropdown.Option(county))

    # declare county selector
    county_dropdown = ft.Dropdown(
        options=list_of_county_dropdown_options,
        on_change=choose_county,
        width=400,
    )

    page.add(ft.Divider())

    city_dropdown = ft.Dropdown(options=None, on_change=choose_city, width=200)

    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        value_text_box,
                        ft.ElevatedButton("Submit Value", on_click=submit_value),
                    ]
                ),
                ft.Row([county_dropdown]),
                ft.Row([city_dropdown]),
            ]
        ),
        ft.Column(
            [
                ft.Text(value=f"Subject Value: ${Subject.value}"),
                ft.Text(value=f"County: {Subject.county}"),
                ft.Text(value=f"City: {Subject.city}"),
            ]
        ),
    )


ft.app(target=main)
