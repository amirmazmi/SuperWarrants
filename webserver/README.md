## Serve it


Serve superwarrant plots. 

Rsync with superwarrants plots output on server

<br><br><br> 

Command to run
> gunicorn main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:9000 --name=warrWeb --capture-output --log-level 'info' --access-logfile logs/gunicorn_$(date '+%Y-%m-%d_%H-%M').logs --error-logfile logs/gunicorn_$(date '+%Y-%m-%d_%H-%M').logs

<br> 

This option not working
>  --access-logformat ='%a %l %u %t "%r" %s %b "%{Referrer}i" "%{User-Agent}i"' 
