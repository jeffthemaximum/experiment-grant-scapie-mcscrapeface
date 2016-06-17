from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from grants.scraper.scraper import scrape

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute=0, hour='*/1')),
    name="task_scrape_grants",
    ignore_result=True
)
def task_scrape_grants():
    """
    Saves latest image from Flickr
    """
    scrape()
    logger.info("Scraped")

# ; ==================================
# ;  celery worker supervisor example
# ; ==================================

# ; the name of your supervisord program
# [program:django_backend]

# ; Set full path to celery program if using virtualenv
# command=/home/jeff/experiment-grant-scapie-mcscrapeface/django-backend/env/bin/celery worker -A project --loglevel=INFO

# ; The directory to your Django project
# directory=/home/jeff/experiment-grant-scapie-mcscrapeface/django-backend

# ; If supervisord is run as the root user, switch users to this UNIX user account
# ; before doing any processing.
# user=jeff

# ; Supervisor will start as many instances of this program as named by numprocs
# numprocs=1

# ; Put process stdout output in this file
# stdout_logfile=/var/log/celery/django_backend_worker.log

# ; Put process stderr output in this file
# stderr_logfile=/var/log/celery/django_backend_worker.log

# ; If true, this program will start automatically when supervisord is started
# autostart=true

# ; May be one of false, unexpected, or true. If false, the process will never
# ; be autorestarted. If unexpected, the process will be restart when the program
# ; exits with an exit code that is not one of the exit codes associated with this
# ; process’ configuration (see exitcodes). If true, the process will be
# ; unconditionally restarted when it exits, without regard to its exit code.
# autorestart=true

# ; The total number of seconds which the program needs to stay running after
# ; a startup to consider the start successful.
# startsecs=10

# ; Need to wait for currently executing tasks to finish at shutdown.
# ; Increase this if you have very long running tasks.
# stopwaitsecs = 600

# ; When resorting to send SIGKILL to the program to terminate it
# ; send SIGKILL to its whole process group instead,
# ; taking care of its children as well.
# killasgroup=true

# ; if your broker is supervised, set its priority higher
# ; so it starts first
# priority=998

# ; ================================
# ;  celery beat supervisor example
# ; ================================

# ; the name of your supervisord program
# [program:django_backend_beat]

# ; Set full path to celery program if using virtualenv
# command=/home/jeff/experiment-grant-scapie-mcscrapeface/django-backend/env/bin/celerybeat -A project --loglevel=INFO

# ; The directory to your Django project
# directory=/home/jeff/experiment-grant-scapie-mcscrapeface/django-backend

# ; If supervisord is run as the root user, switch users to this UNIX user account
# ; before doing any processing.
# user=jeff

# ; Supervisor will start as many instances of this program as named by numprocs
# numprocs=1

# ; Put process stdout output in this file
# stdout_logfile=/var/log/celery/django_backend_beat.log

# ; Put process stderr output in this file
# stderr_logfile=/var/log/celery/django_backend_beat.log

# ; If true, this program will start automatically when supervisord is started
# autostart=true

# ; May be one of false, unexpected, or true. If false, the process will never
# ; be autorestarted. If unexpected, the process will be restart when the program
# ; exits with an exit code that is not one of the exit codes associated with this
# ; process’ configuration (see exitcodes). If true, the process will be
# ; unconditionally restarted when it exits, without regard to its exit code.
# autorestart=true

# ; The total number of seconds which the program needs to stay running after
# ; a startup to consider the start successful.
# startsecs=10

# ; if your broker is supervised, set its priority higher
# ; so it starts first
# priority=999
