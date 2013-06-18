from osv import osv, fields

class obj1(osv.osv):
    _name = 'ex4.obj1'
    _columns = {
        'name': fields.char('Name', size=50),
        'score': fields.integer('Score'),
    }

obj1()
