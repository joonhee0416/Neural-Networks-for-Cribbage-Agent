TestNNCribbage:
	echo "#!/bin/bash" > TestNNCribbage
	echo "python3 test_nn_cribbage.py \"\$$@\"" >> TestNNCribbage
	chmod u+x TestNNCribbage
