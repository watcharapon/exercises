#from osv import osv
from jasper_reports import report_jasper
from pprint import pprint

def parse(cr, uid, ids, datas, context=None):
    records = []
    no = 1    
    for rec in range(10):
        record = {}
        record['no'] = rec
        record['id'] = rec
        record['name'] = "name %s" % (rec)
        no += 1
        records.append(record)

    pprint(records)
    return {
        'data_source': 'records',
        'records': records,
    }

report_jasper('report.ex10.obj1_1', 'ex10.obj1', parse)
