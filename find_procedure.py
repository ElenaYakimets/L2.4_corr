import os

if __name__ == '__main__':
    migrations = 'Migrations'
    current_dir = os.path.dirname ( os.path.abspath ( __file__ ) )
    path = '\\Users\elena\PycharmProjects\23t\L2.4\Migrations'
    cur_dir = os.getcwd ()
    ext = '.sql'
    while True:
        s = input ( 'Filter:' )
        if not s: break
        files = [ i for i in os.listdir ( cur_dir ) if ext in i ]
        for fname in files:
            with open ( fname, encoding='utf-8' ) as f:
                if s in f.read ():
                    print ( fname )