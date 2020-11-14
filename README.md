# internet_speedtest
Log my internet providers speed

While I use poetry for environment and dependency management, the only package I install is `speedtest-cli`.

The script write 3 csv files locally.

I set up a cron job using `crontab -e`.

The cron file just runs the `./runner.sh` every hour:
`30 9-23 * * * cd {(LOCATION TO FILE} && ./runner.sh`
