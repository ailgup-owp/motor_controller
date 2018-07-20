cd /home/pi/motor_tester
sleep 5
git fetch --all
git reset --hard origin/master
sudo chmod +x /home/pi/motor_tester/launch.sh
python3 /home/pi/motor_tester/motor_test.py &
