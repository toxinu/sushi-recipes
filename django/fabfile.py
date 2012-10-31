import os
import sys
from fabric.api import task, local

@task
def init_dev():
	init_venv()
	update_requirements('dev')

@task
def update_requirements(env):
	virtualenv('pip install -r requirements/%s.txt' % env)

@task
def runserver(env, ip='127.0.0.1', port=8000, workers=2):
	if env == 'prod':
		virtualenv('gunicorn {{ app|lower }}.wsgi:application --workers=%s -b %s:%s' % (workers, ip, port))
	else:
		virtualenv('python manage.py runserver %s:%s --settings=\'{{ app|lower }}.settings.%s\'' % (ip, port, env))

@task
def syncdb(env):
	virtualenv('python manage.py syncdb --settings=\'{{ app|lower }}.settings.%s\'' % env)

def virtualenv(command):
	if not os.path.exists('venv'):
		print(' :: I need a virtualenv (venv). Use init_venv.')
		sys.exit(1) 
        local('source venv/bin/activate && ' + command)

@task
def init_venv():
	local('virtualenv venv')
