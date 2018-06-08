# -*- coding: utf-8 -*-
{
    "name": """Chile - Web Services de Documentos Tributarios Electrónicos\
    """,
    'version': '9.0.8.1.4',
    'category': 'Localization/Chile',
    'sequence': 12,
    'author':  'Daniel Santibáñez Polanco, BMyA SA - Blanco Martín & Asociados, Odoo Chile',
    'website': 'https://globalresponse.cl',
    'license': 'AGPL-3',
    'summary': '',
    'description': """
Chile: API and GUI to access Electronic Invoicing webservices.
""",
    'depends': [
        'l10n_cl_counties',
        'l10n_cl_invoice',
        'l10n_cl_dte_caf',
        'user_signature_key',
        'account',
        'report',
        'purchase',
        ],
    'external_dependencies': {
        'python': [
            'xmltodict',
            'dicttoxml',
            'pdf417gen',
            'M2Crypto',
            'base64',
            'hashlib',
            'cchardet',
            'suds',
            'urllib3',
            'SOAPpy',
            'signxml',
            'ast',
            'pysftp',
        ]
    },
    'data': [
        'views/invoice_view.xml',
        'views/partner_view.xml',
        'views/company_view.xml',
        'views/payment_t_view.xml',
        'views/sii_regional_offices_view.xml',
        'views/layout.xml',
        'views/sii_cola_envio.xml',
        'views/mail_dte.xml',
        'views/res_config.xml',
        'wizard/masive_send_dte.xml',
        'wizard/masive_dte_process.xml',
        'wizard/masive_dte_accept.xml',
        'wizard/upload_xml.xml',
        'wizard/validar.xml',
        'data/sii.regional.offices.csv',
        'data/sequence.xml',
        'data/product.xml',
        'data/cron.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
