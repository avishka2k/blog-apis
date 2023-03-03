from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, API!'


@app.route('/products', methods=['GET'])
def products():
    products = [
        {'drug_item': 'Acetaminophen'},
        {'drug_item': '    Adderall'},
        {'drug_item': '    Amitriptyline'},
        {'drug_item': '    Amlodipine'},
        {'drug_item': '    Amoxicillin'},
        {'drug_item': '    Ativan'},
        {'drug_item': '    Atorvastatin'},
        {'drug_item': '    Azithromycin'},
        {'drug_item': '    Benzonatate'},
        {'drug_item': '    Brilinta'},
        {'drug_item': '    Bunavail'},
        {'drug_item': '    Buprenorphine'},
        {'drug_item': '    Cephalexin'},
        {'drug_item': '    Ciprofloxacin'},
        {'drug_item': '    Citalopram'},
        {'drug_item': '    Clindamycin'},
        {'drug_item': '    Clonazepam'},
        {'drug_item': '    Cyclobenzaprine'},
        {'drug_item': '    Cymbalta'},
        {'drug_item': '    Doxycycline'},
        {'drug_item': '    Dupixent'},
        {'drug_item': '    Entresto'},
        {'drug_item': '    Entyvio'},
        {'drug_item': '    Farxiga'},
        {'drug_item': '    Fentanyl Patch'},
        {'drug_item': '    Gabapentin'},
        {'drug_item': '    Gilenya'},
        {'drug_item': '    Humira'},
        {'drug_item': '    Hydrochlorothiazide'},
        {'drug_item': '    Hydroxychloroquine'},
        {'drug_item': '    Ibuprofen'},
        {'drug_item': '    Imbruvica'},
        {'drug_item': '    Invokana'},
        {'drug_item': '    Januvia'},
        {'drug_item': '    Jardiance'},
        {'drug_item': '    Kevzara'},
        {'drug_item': '    Lexapro'},
        {'drug_item': '    Lisinopril'},
        {'drug_item': '    Lofexidine'},
        {'drug_item': '    Loratadine'},
        {'drug_item': '    Lyrica'},
        {'drug_item': '    Melatonin'},
        {'drug_item': '    Meloxicam'},
        {'drug_item': '    Metformin'},
        {'drug_item': '    Methadone'},
        {'drug_item': '    Methotrexate'},
        {'drug_item': '    Metoprolol'},
        {'drug_item': '    Naloxone'},
        {'drug_item': '    Naltrexone'},
        {'drug_item': '    Naproxen'},
        {'drug_item': '    Narcan'},
        {'drug_item': '    Nurtec'},
        {'drug_item': '    Omeprazole'},
        {'drug_item': '    Onpattro'},
        {'drug_item': '    Otezla'},
        {'drug_item': '    Ozempic'},
        {'drug_item': '    Pantoprazole'},
        {'drug_item': '    Prednisone'},
        {'drug_item': '    Probuphine'},
        {'drug_item': '    Rybelsus'},
        {'drug_item': '    secukinumab'},
        {'drug_item': '    Sublocade'},
        {'drug_item': '    Tramadol'},
        {'drug_item': '    Trazodone'},
        {'drug_item': '    Viagra'},
        {'drug_item': '    Wegovy'},
        {'drug_item': '    Wellbutrin'},
        {'drug_item': '    Xanax'},
        {'drug_item': '    Zubsolv'},
        ]

    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
