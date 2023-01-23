# ############################################
# 
#          Trakteer Donate Data Types
#          ~~ 2023 (c) by Realzzy ~~
# 
# ############################################

# Data class to process donation data
class TrakteerDonationData:
    """

    Data class to process donation data from Trakteer
    Available properties:
    - name: str
    - unit: str
    - amount: int
    - message: str
    - avatar: str
    - unit_icon: str
    - price: str
    - media: Optional(str)
    - id: str

    2023 (c) by Realzzy
    """
    
    # Initialize data
    def __init__(self, data):
        self.__supporter_name = data["supporter_name"]
        self.__unit = data["unit"]
        self.__quantity = data["quantity"]
        self.__supporter_message = data["supporter_message"]
        self.__supporter_avatar = data["supporter_avatar"]
        self.__unit_icon = data["unit_icon"]
        self.__price = data["price"]
        self.__media = data["media"]
        self.__id = data["id"]

    # Convert to a dict object
    def to_dict(self):
        return {
            "name": self.name,
            "unit": self.unit,
            "amount": self.amount,
            "message": self.message,
            "avatar": self.avatar,
            "unit_icon": self.unit_icon,
            "price": self.price,
            "media": self.media,
            "id": self.id
        }
    
    # Set property
    @property
    def name(self):
        return self.__supporter_name

    @property
    def unit(self):
        return self.__unit

    @property
    def amount(self):
        return self.__quantity

    @property
    def message(self):
        return self.__supporter_message
        
    @property
    def avatar(self):
        return self.__supporter_avatar

    @property
    def unit_icon(self):
        return self.__unit_icon

    @property
    def price(self):
        return self.__price

    @property
    def media(self):
        return self.__media

    @property
    def id(self):
        return self.__id

    # Make it unoverridable
    @name.setter
    def name(self, value):
        pass

    @unit.setter
    def unit(self, value):
        pass

    @amount.setter
    def amount(self, value):
        pass

    @message.setter
    def message(self, value):
        pass

    @avatar.setter
    def avatar(self, value):
        pass

    @unit_icon.setter
    def unit_icon(self, value):
        pass

    @price.setter
    def price(self, value):
        pass

    @media.setter
    def media(self, value):
        pass

    @id.setter
    def id(self, value):
        pass

# Error Classes
class TrakteerMissingUserHash(Exception): pass
class TrakteerMissingStreamKey(Exception): pass
class TrakteerWebsocketError(Exception): pass
class TrakteerMethodUnoverridable(Exception): pass