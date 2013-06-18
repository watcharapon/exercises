from osv import osv
from jasper_reports import report_jasper

def parse(cr, uid, ids, datas, context=None):
    if context is None:
        context = {}
    if not ids:
        raise osv.except_osv(('Warining'), ('No data to print'))

    records = []
    date_print = datas.get('parameters')['date_print']

    cr.execute("""
            select id, name, score from ex4_obj1 where id in %s
        """, (tuple(ids),))
    no = 1    
    for rec in cr.dictfetchall():
        record = {}
        record['no'] = no
        record['id'] = rec['id']
        record['name'] = rec['name']
        record['score'] = rec['score']
        no += 1
        records.append(record)

    return {
        'data_source': 'records',
        'records': records,
        'parameters': {
                    'date_print': date_print, 
                    }
    }

#report_jasper('report.<report_name>', '<object_name>', <parser_function>) -> see report.xml
report_jasper('report.ex4.wizard.obj1', 'ex4.obj1', parse)
