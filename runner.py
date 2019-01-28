import os, click


@click.command()
@click.option('--osb', default='macos', help='OS environment: windows, macos, unix. Default is unix')
@click.option('--browser', default='chrome', help='Browsers: chrome, firefox. Default is chrome')
def run_test(osb, browser):
    try:
        print 'RUNNING TESTS ON {} ON {}'.format(osb, browser)
        # os.system('nosetests -v -s ./test_main.py --tc=osb:{osb} --tc=browser:{bro} '
        #           '--with-allure --logdir="./report/pew"'.format(osb=osb, bro=browser))
        # os.system('allure generate "./report/pew" -o "./report/{}" --clean'.format(browser))
        os.system('nosetests -v -s ./test_main.py '
                  '--tc=osb:{osb} --tc=browser:{bro}'.format(osb=osb, bro=browser))
        if osb in ['windows', 'Windows']:
            os.system('rmdir .\\report\\pew')
        else:
            os.system('rm -r ./report/pew')
        print 'TESTING ACCOMPLISHED'
    except Exception as err:
        print 'TESTING WAS UNSUCCESSFUL:\n{}'.format(err)


run_test()
