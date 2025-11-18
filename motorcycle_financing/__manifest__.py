{
    'name': 'Motorcycle Financing',
    'summary': 'Streamlines the loan application process for dealerships.',
    'license': 'OPL-1',
    'category': 'Kawiil/Custom Modules',
    'author': 'LakConrad',  # Use your GitHub Username
    'website': 'https:/LakConrad@github.com',  # Link to your Repo
    'version': '0.0.1',
    'depends': ['base','product'],  # At minimum depend on 'base'
    'data': [

                'data/loan_demo.xml',
        
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',
        'views/loan_application_views.xml',
        'views/loan_application_tag_views.xml',
        'views/loan_application_document_type_views.xml',
        'views/motorcycle_financing_menuitems.xml',
    ],
    'demo': [

    ],
    'application': True,
}
