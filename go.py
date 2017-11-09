#!/bin/env python2.7
import logging
import sys
from pypeflow.simple_pwatcher_bridge import (
    PypeProcWatcherWorkflow, MyFakePypeThreadTaskBase)
from falcon_unzip import io
import tasks

def setup_workflow():
    config = {
        'job_type': 'string',
        'job_queue': 'bash -C ${CMD} >| ${STDOUT_FILE} 2>| ${STDERR_FILE}',
        #'job_queue': 'bash -C ${CMD}',
        #'sge_option': '-pe smp 8 -q bigmem',
        'pwatcher_type': 'blocking',
        #watcher_directory=config.get('pwatcher_directory', 'mypwatcher'),
        #'use_tmpdir': '/scratch',
    }
    wf = PypeProcWatcherWorkflow(
        max_jobs=4,
        job_type=config['job_type'],
        job_queue=config.get('job_queue'),
        sge_option=config.get('sge_option'),
        watcher_type=config.get('pwatcher_type'),
        #watcher_directory=config.get('pwatcher_directory', 'mypwatcher'),
        use_tmpdir=config.get('use_tmpdir'),
    )
    return wf

def main(prog):
    wf = setup_workflow()
    wf.max_jobs = 2

    task = tasks.create_task_old()
    wf.addTask(task)
    wf.refreshTargets()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, formatter=None)
    main(*sys.argv)
