import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/user/AAE4202_src/wk3/teacher_student_pkg/install/teacher_student_pkg'
