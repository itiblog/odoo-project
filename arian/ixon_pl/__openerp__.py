# -*- coding: utf-8 -*-
{
    'name': "IXON PL",

    'summary': "IXON PL",

    'description': "IXON PL",

    'author': "Muhammmad Awais",
    'website': "http://www.bcube.com",

    # any module necessary for this one to work correctly
    'depends': ['base', 'report', 'account'],
    # always loaded
    'data': [
        'template.xml',
        'views/module_report.xml',
    ],
    'css': ['static/src/css/report.css'],
}
