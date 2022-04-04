list_tables = ["Appointments", "OpenSlots","Workers"]
nav_bar_items = [{"title":"Afspraak maken", "url":"booking"},
                 {"title": "Inloopspreekuur", "url": "inloopspreekuur"},
                 {"title":"Mijnkeuringsverslag", "url": "mijnverslag"},
                 {"title": "Inhoud keuring", "url": "inhoudkeuring"},
                 {"title": "Over ons", "url": "aboutus"},
                 {"title": "Contact", "url": "contact"},
                 ]
                 # {"title":"Zoek keuring", "url":"zoekkeuring"},

list_time_duration_choices = ["10 min", "15 min", "20 min", "25 min", "30 min"]

list_services = [("medisch","Medische keuring €35,00"),
                 ('75+', '75+ rijbewijs A/B/BE €35,00'),
                 ('groot', 'Rijbewijskeuring groot €35,00'),
                 ('taxipas', 'Rijbewijskeuring taxipas €35,00'),
                 ('touring', 'Rijbewijskeuring touringscarchauffeurs €35,00'),
                 ('multiplekeuring', 'Meerdere keuringen €50,00'),
                 ('thuiskeuring', 'Thuiskeuring €75,00'),
                 ]

landingpage_items = [{"item":"BIG geregistreerde artsen"},
                    {"item":"Inzage in uw keuringsrapport"},
                    {"item":"Verbonden met Zorgdomein"},
                    {"item":"Prijzen vanaf 35 euro"},
                     ]

dict_payments_links = {
                "medisch":"https://tikkie.me/pay/RijRdam/ucsqSFszXivucPSqxJgXKE",
                '75+':'https://tikkie.me/pay/RijRdam/eVJuiK65iGQbP3NxSvb6Jb',
                'groot': 'https://tikkie.me/pay/RijRdam/7RrXrKdTKC7ckUjAzM5NRX',
                'taxipas': 'https://tikkie.me/pay/RijRdam/3MWN3ATsyiXjU3FTShEwXr',
                'touring': 'https://tikkie.me/pay/RijRdam/a72TP7RzzMSrNaQazgcoAY',
                'multiplekeuring': 'https://tikkie.me/pay/RijRdam/bAFvY84bg74J6XioYMnKk',
                'thuiskeuring':'https://tikkie.me/pay/RijRdam/wwVEAfN8pkXKCzKXmokd2h'
                }

address_list = ['<h3>Rotterdam Overschie </h3> Corkstraat 46, 3047AC <br> <a href="https://goo.gl/maps/Juy8PXtUY1uZf5UK8" target=_blank>Klik hier voor de lokatie op de kaart</a> ',
                '<h3>Capelle aan den IJssel </h3> Kanaalweg 33, 2903LR <br> <a href="https://goo.gl/maps/ae7f51xgw2xyry3W9" target=_blank>Klik hier voor de lokatie op de kaart</a> ',
                '<h3>Rotterdam Feyenoord </h3> Olympiaweg 4, 3077 AL <br> <a href="https://goo.gl/maps/FTsMX5u77rL4zvkw5" target=_blank>Klik hier voor de lokatie op de kaart</a> ']
address_list_short = ["ADD Business Point, Corkstraat 46, 3047AC, Rotterdam Overschie", "ADD Business Point, Kanaalweg 33, 2903 LR, Capelle aan den IJssel", "Kantoorgebouw Greenstand, Olympiaweg 4, 3077 AL, Rotterdam Feyenoord"]
# address_list = [i["item"] for i in address_list]