import flet as ft
import subprocess
import time
import src

counties = src.county_data.counties.get_counties()


def main(page: ft.Page):
    title = ft.Text(value="Tax Matrix")
    version = ft.Text(value=f"Version: {src.config.current_version()}")
    update_date = ft.Text(value=f"Last Updated: {src.config.date_revised()}")

    page.controls.append(title)
    page.controls.append(version)
    page.controls.append(update_date)

    page.update()

    rates_to_be_applied={}
    fees_to_be_applied={}

    def display_rates_and_fees():
        for title,rate in rates_to_be_applied.items():
            page.add(ft.Row(ft.Text(title),ft.Text(": "),ft.Text(rate)))

        for title,fee in fees_to_be_applied.items():
            page.add(ft.Row(ft.Text(title),ft.Text(": "),ft.Text(fee)))

    def submit_value(e):
        # page.add(ft.Text(value=f"Entered Value: ${value.value}"))
        used_value.value = f"Subject Value being used: ${value_text_box.value}"
        page.update()

    def choose_county(e):
        # page.add(ft.Text(value=f"Selected County: {county_dropdown.value}"))
        selected_county.value = f"Selected County: {county_dropdown.value}"
        list_of_cities=generate_city_list(county_dropdown.value)
        city_dropdown.options=list_of_cities
        page.update()
        county_dict=counties[county_dropdown.value]
        county_wide_dict=county_dict["county_wide"]
        title=county_wide_dict["title"]
        rate=county_wide_dict["rate"]
        rates_to_be_applied[title]=rate
        display_rates_and_fees()

    def generate_city_list(county):
        city_list=[]
        county_dict=counties[county]
        for city in county_dict["cities"]:
            city_list.append(ft.dropdown.Option(city))

        return city_list

    def choose_city(e):
        page.add(ft.Text(value=f"Selected City: {city_dropdown.value}"))
        city_dict=counties[county_dropdown.value]["cities"][city_dropdown.value]
        ft.Text(value=f"{city_dict['title']}: {city_dict['rate']}")
        page.update()
        title=city_dict["title"]
        rate=city_dict["rate"]
        rates_to_be_applied[title]=rate
        checkboxes=[]
        if len(city_dict)>2:
            for item in city_dict:
                if item!="title" and item!="rate":
                    inner_item_dict=city_dict[item]
                    title=inner_item_dict["title"]
                    try:
                        rate=inner_item_dict["rate"]
                    except KeyError:
                        rate=None
                    try:
                        fee=inner_item_dict["fee"]
                    except KeyError:
                        fee=None
                    if rate is None:
                        if fee is None:
                            pass
                        else:
                            checkbox_city_fee=ft.Checkbox(label=f"{title}: ${fee:.2f}",on_change=update_city_subfee)
                            page.add(checkbox_city_fee)
                    else:
                        checkbox_city_rate=ft.Checkbox(label=f"{title}: {rate}",on_change=update_city_subrate)
                        page.add(checkbox_city_rate)
        else:
            pass

    def update_city_subfee(e):
        county_dict=counties[county_dropdown.value]
        city_dict=county_dict["cities"][city_dropdown.value]
        for item in city_dict:
            if item!="title" and item!="rate":
                inner_item_dict=city_dict[item]
                title=inner_item_dict["title"]
                try:
                    rate=inner_item_dict["rate"]
                except KeyError:
                    rate=None
                try:
                    fee=inner_item_dict["fee"]
                except KeyError:
                    fee=None
        if checkbox_city_fee.value:
            fees_to_be_applied[title]=fee

        page.update()

    def update_city_subrate(e):
        county_dict=counties[county_dropdown.value]
        city_dict=county_dict["cities"][city_dropdown.value]
        for item in city_dict:
            if item!="title" and item!="rate":
                inner_item_dict=city_dict[item]
                title=inner_item_dict["title"]
                try:
                    rate=inner_item_dict["rate"]
                except KeyError:
                    rate=None
                try:
                    fee=inner_item_dict["fee"]
                except KeyError:
                    fee=None
        if checkbox_city_rate.value:
            rates_to_be_applied[title]=rate

        page.update()

    # declare value field for entering
    value_text_box = ft.TextField(
        hint_text="Enter Subject Value", value="", text_align="right"
    )

    # declare value field for displaying
    used_value = ft.Text(value=f"Subject Value being used: ${value_text_box.value}")
    page.add(used_value)

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

    # declare selected county field
    selected_county = ft.Text(value=f"Selected County: {county_dropdown.value}")
    page.add(selected_county)

    page.add(
        ft.Row(
            [value_text_box, ft.ElevatedButton("Submit Value", on_click=submit_value)]
        )
    )
    page.add(
        ft.Text(value="Please select a county: "),
    )
    page.add(county_dropdown)

    city_dropdown=ft.Dropdown(options=None,on_change=choose_city,width=200)

    page.add(city_dropdown)

    checkbox_city_fee=ft.Checkbox(label="",on_change=update_city_subfee)
    checkbox_city_rate=ft.Checkbox(label="",on_change=update_city_subrate)

ft.app(target=main)
