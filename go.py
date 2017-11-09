#!/bin/env python2.7
from pypeflow.simple_pwatcher_bridge import (
    PypeLocalFile, makePypeLocalFile, fn,
    PypeTask,
    PypeProcWatcherWorkflow, MyFakePypeThreadTaskBase)
from falcon_unzip import io
import sys
import tasks

def main(prog):
    print 'hi'
    #io.mkdirs('run')
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
    wf.max_jobs = 2
    i1 = makePypeLocalFile('./in/i1')
    o1 = makePypeLocalFile('./run/dir1/o1.txt')
    parameters = {}
    make_task = PypeTask(
            inputs={
                'i1': i1,
            },
            outputs={
                'o1': o1,
            },
            parameters=parameters,
            )
    a_task = make_task(tasks.taskA)
    wf.addTask(a_task)
    wf.refreshTargets()

if __name__ == '__main__':
    main(*sys.argv)
