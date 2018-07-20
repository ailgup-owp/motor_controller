COUNT=1
while ! ping -c 1 -W 1 8.8.8.8; do
    if [ "$COUNT" -gt 5 ]
    then
      break
    fi
    echo "Waiting ..."
    sleep 1
    COUNT=$(($COUNT+1))
    done
git -C /home/pi/motor_tester fetch --all
git -C /home/pi/motor_tester reset --hard origin/master
python3 /home/pi/motor_tester/motor_test.py &

