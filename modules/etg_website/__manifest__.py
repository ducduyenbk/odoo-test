{
    'name': 'ETG Website',
    'version': '1.0',
    'summary': '',
    'description': 'ETG Website',
    'category': 'Website',
    'author': 'e-Leisure: AT',
    'maintainer': 'e-Leisure: AT',
    'website': 'https://erpsimplity.com',
    'license': 'AGPL-3',
    'depends': ['website_sale', 'crm'],
    'data': [
        'views/register_template.xml',
        'views/lead_view.xml',
        'data/product_category.xml',
        'data/product_template.xml',
    ],
    'demo': [''],
    'installable': True,
    'application': True,
    'auto_install': False,
}
