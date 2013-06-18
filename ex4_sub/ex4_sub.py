from osv import osv, fields

class obj1(osv.osv):
    _name = 'ex4.sub.obj1'
    _columns = {
        'name': fields.char('Name', size=50),
        'obj3_ids': fields.many2many('ex4.sub.obj3', 'obj1_3_rel', 'obj1_id', 'obj3_id', 'Obj3 & obj1'),
        'obj2_ids': fields.many2one('ex4.sub.obj2', 'Obj2'), 
    }

obj1()

class obj2(osv.osv):
    _name = 'ex4.sub.obj2'
    _columns = {
        'name': fields.char('Name', size=50),
        'obj2_lines': fields.one2many('ex4.sub.obj2.line', 'obj2_id', 'Obj2 Lines'),
    }

obj2()

class obj2_line(osv.osv):
    _name = 'ex4.sub.obj2.line'
    _columns = {
        'name': fields.char('Description', size=50),
        'obj2_id': fields.many2one('ex4.sub.obj2', 'Obj2'),
        'qty': fields.integer('Qty'),
    }

obj2_line()

class obj3(osv.osv):
    _name = 'ex4.sub.obj3'
    _columns = {
        'name': fields.char('Name', size=60),
    }

obj3()
