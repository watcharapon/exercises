from osv import osv, fields

class obj2(osv.osv):
    _name = 'ex10.obj2'
    _columns  = {
        'name': fields.char('Description', size=10),
    }

obj2()

class obj1_line(osv.osv):
    _name = 'ex10.obj1.line'
    _columns  = {
        'name': fields.char('Name', size=10),
        'total': fields.float('Total'),
        'tax': fields.char('Tax', size=50),
        'obj1_id': fields.many2one('ex10.obj1', 'Name', size=10),

    }

obj1_line()

class obj3(osv.osv):
    _name = 'ex10.obj3'
    _columns  = {
        'name': fields.char('Name', size=50),
        'surname': fields.char('Sur Name', size=50),
        'expiry_date': fields.date('Exp. Date', size=50),
        'obj3_line_ids': fields.one2many('ex10.obj3.line', 'obj3_id',  'lines'),
    }

obj3()

class obj3_lines(osv.osv):
    _name = 'ex10.obj3.line'
    _columns  = {
        'name': fields.char('Name', size=30),
        'obj3_id': fields.many2one('ex10.obj3', "obj3"),
    }

obj3_lines()

class obj1(osv.osv):
    _name = 'ex10.obj1'
    _columns  = {
        'name': fields.char('Name', size=10),
        'grade': fields.char('Grade', size=2),
        'gender': fields.char('Gender', size=2),
        'prefix': fields.many2one('ex10.obj2', 'Prefix'),
        'obj1_line_ids': fields.one2many('ex10.obj1.line', 'obj1_id',  'lines'),
        'm2mobj1_lines': fields.many2many('ex10.obj3', 'ex10_obj1_3_rel','ex10_obj1_id', 'ex10_obj3_id','lines'),

    }

obj1()
