import datetime
from mx import DateTime

from osv import osv, fields

def Ymd(date=None):
    if date is None:
        return DateTime.today()
    elif type(date) in (str, unicode):
        return DateTime.strptime(date, '%Y-%m-%d')
    elif type(date) in (type(DateTime.today()), datetime.datetime):
        return date.strftime('%Y-%m-%d')

class wizard_obj1(osv.osv_memory):
    _name = 'wizard.obj1'
    _columns = {
        'operator': fields.selection([
                ('more', '>')
                , ('less', '<')
                , ('equal', '=')], 'Operator', required=True),        
        'date_print': fields.date('Date Print'),
        'score': fields.integer('Score'),
    }
    _defaults = {
        'date_print': lambda *a: Ymd(Ymd()),
        'operator': lambda *a: 'more',
    }

    def button_print(self, cr, uid, ids, context=None):
        wizard = self.browse(cr, uid, ids[0], context)
        score = wizard.score or 0

        if wizard.operator == 'more':
            # select * from ex4_obj1 where score > wizard.score
            obj1_ids = self.pool.get('ex4.obj1').search(cr, uid, [('score', '>', score)]) # return ids
        elif wizard.operator == 'less':
            obj1_ids = self.pool.get('ex4.obj1').search(cr, uid, [('score', '<', score)])
        else:
            obj1_ids = self.pool.get('ex4.obj1').search(cr, uid, [('score', '=', score)])

        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'ex4.wizard.obj1',
            'datas': {
                'model': 'ex4.obj1',
                'data_source': 'model',
                'ids': obj1_ids,
                'parameters': {
                     'date_print': wizard.date_print,
                }
            }
        }

wizard_obj1()
