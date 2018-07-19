cd /home/pi/motor_tester
git pull origin master
sudo chmod +x /home/pi/motor_tester/launch.sh
export DISPLAY=:0 ; python3 /home/pi/motor_tester/motor_test.py &
