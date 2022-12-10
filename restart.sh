#!|bin|bash
hosts='192.168.11.55 192.168.11.56'
apps_list='httpd nginx'
for ip in $hosts
do 
    for app in $apps_list
    do
        systemctl -H root@$ip restart $app
        if [ $? = 0 ]
        then 
        echo 'Application $app succesfuly restarted on host $ip'>> restart.log
        break
        else
        echo 'Application $app not started on host $ip'>> restart.log
        fi 

    done
done