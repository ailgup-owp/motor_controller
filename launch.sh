cd /home/pi/motor_tester
while ! ping -c 1 -W 1 8.8.8.8; do
    echo "Waiting ..."
    sleep 1
done
git fetch --all
git reset --hard origin/master
sudo chmod +x /home/pi/motor_tester/launch.sh
python3 /home/pi/motor_tester/motor_test.py &
