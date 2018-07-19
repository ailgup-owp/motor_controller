cd /home/pi/motor_tester
git pull origin master

export DISPLAY=:0 ; python3 /home/pi/motor_tester/motor_test.py &
