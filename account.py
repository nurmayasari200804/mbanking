# Data rekening lengkap
ACCOUNTS = [
    {
        "id": "bri",
        "name": "Bank BRI",
        "number": "025901087762503",
        "owner": "Nurmayasari Usman",
        "label": "Nomor Rekening",
        "icon": "🏦",
        "icon_class": "icon-bri"
    },
    {
        "id": "seabank",
        "name": "SeaBank",
        "number": "901641785010",
        "owner": "Nurmayasari Usman",
        "label": "Nomor Rekening",
        "icon": "🌊",
        "icon_class": "icon-seabank"
    },
    {
        "id": "dana",
        "name": "DANA",
        "number": "082246038126",
        "owner": "Nurmayasari Usman",
        "label": "Nomor DANA",
        "icon": "🕊️",
        "icon_class": "icon-dana"
    },
    {
        "id": "gopay",
        "name": "GoPay",
        "number": "082246038126",
        "owner": "Nurmayasari Usman",
        "label": "Nomor GoPay",
        "icon": "🍃",
        "icon_class": "icon-gopay"
    },
    {
        "id": "shopeepay",
        "name": "ShopeePay",
        "number": "082246038126",
        "owner": "nmayaaaa",
        "label": "Nomor ShopeePay",
        "icon": "🛍️",
        "icon_class": "icon-shopeepay"
    }
]

# Fungsi untuk mendapatkan account by ID
def get_account_by_id(account_id):
    for account in ACCOUNTS:
        if account['id'] == account_id:
            return account
    return None

# Fungsi untuk mendapatkan semua metode
def get_all_methods():
    return [account['name'] for account in ACCOUNTS]