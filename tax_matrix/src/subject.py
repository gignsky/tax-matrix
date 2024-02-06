class Subject:
    def __init__(self):
        self.value=0
        self.rates_to_be_applied={}
        self.fees_to_be_applied={}
        self.county=None
        self.county_dict=None
        self.county_wide_dict=None
        self.city=None
        self.city_dict=None

    def update_value(self,new_value):
        self.value=new_value

    def update_county(self,new_county, new_county_dict, new_county_wide_dict):
        self.county=new_county
        self.county_dict=new_county_dict
        self.county_wide_dict=new_county_wide_dict

    def update_city(self,new_city, new_city_dict):
        self.city=new_city
        self.city_dict=new_city_dict
