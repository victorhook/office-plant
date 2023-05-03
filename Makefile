REMOTE = victor@victorsplant.local
REMOTE_PROJECT = /home/victor/projects/office-plant



deploy:
	rsync -a backend ${REMOTE}:${REMOTE_PROJECT}

sample:
	ssh ${REMOTE} "python ${REMOTE_PROJECT}/backend/sample.py"