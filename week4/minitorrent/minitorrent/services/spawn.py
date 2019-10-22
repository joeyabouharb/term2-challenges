"""
module to spawn background processes
ie. socket listeners, and kill
when application is terminated
"""

import subprocess
import os
import signal


def listener():
    """
    run python socket listener in background
    """
    listener = subprocess.Popen(
        './minitorrent/services/listener.py',
        shell=True, preexec_fn=os.setsid, stdout=subprocess.PIPE
    ) # spawn as a seperate process
    return listener

def kill(listener):
    """
    kill all spawned processes
    """
    os.killpg(
        os.getpgid(listener.pid), signal.SIGTERM
    )