import os


print 'TESTS start'
os.system('nosetests -v ./test_main.py --with-allure --logdir="./report/pew"')
os.system('allure generate "./report/pew" -o "./report/chrome"')
os.system('rm -r ./report/pew')
print 'TESTS end'
