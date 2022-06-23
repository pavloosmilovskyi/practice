import datetime
import validation
import date_validation
class Product:
    def __init__(self, id='1', title='title', image_url='hhttps://product.com/products/jg', price='23', date_of_creation='11.11.2019', updated_at='12.11.2019',description= 'This_amazing_product_was_made_on_11.11.2019_and_updated_on_12.11.2019'):
        #" ID, title, image_url, price, created_at (date), updated_at (date), description"
        self.id = validation.validate_id(id)
        self.title = validation.validate_title(title)
        self.image_url =  validation.validate_image_url(image_url)
        self.price = validation.validate_numb(price)
        self.date_of_creation = date_validation.is_date(date_of_creation)
        self.updated_at = date_validation.is_date(updated_at)
        self.description = validation.validate_description(self.date_of_creation, self.updated_at, self.image_url, description)

    def get_id(self):
        return self.id
    def get_title(self):
        return self.title
    def get_image_url(self):
        return self.image_url
    def get_material(self):
        return self.material
    def get_type(self):
        return self.date
    def get_date_of_creation(self):
        return self.date_of_creation
    def get_updated_at(self):
        return self.updated_at
    def get_price(self):
        return self.price
    def get_description(self):
        return self.description


    def __str__(self):
        return f"{self.id} {self.title} {self.image_url} {self.price} {self.date_of_creation} " + \
               f"{self.updated_at} {self.description}"
#return f"{self.id} {self.title} {self.image_url} {self.price} {self.date_of_creation} {self.updated_at} {self.description}"

    def input(self):
        print("ID:")
        self.id = validation.validate_id()
        print("title:")
        self.title = validation.name_validation()
        print("image_url:")
        self.image_url = validation.validate_image_url()
        print("price:")
        self.price = validation.validate_numb()
        print("created_at:")
        self.date_of_creation = date_validation.is_date()
        print("updated_at")
        self.updated_at = date_validation.updated_at(self.date_of_creation)                 # jhrtttttttttttttttttttttttttttttttttttttttttttttttthuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
        print("description:")
        self.description = validation.validate_description(self.date_of_creation, self.updated_at, self.image_url)


    def is_found(self, search_object):
        all_parameters = (str(self)).split()
        for i in all_parameters:
            if str(search_object) in i:
                return True
        return False