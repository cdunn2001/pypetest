#!/bin/env python2.7
from pypeflow.simple_pwatcher_bridge import (
    PypeLocalFile, makePypeLocalFile, fn,
    PypeTask,
    PypeProcWatcherWorkflow, MyFakePypeThreadTaskBase)
import sys
from falcon_unzip import io

def taskA(self):
    o1_fn = fn(self.o1)
    script = """
#!/bin/bash
set -vex
touch %(o1_fn)s
echo taskA
"""%locals()
    script_fn = 'script.sh'
    with open(script_fn, 'w') as ofs:
        ofs.write(script)
    self.generated_script_fn = script_fn

def main(prog):
    print 'hi'
    #io.mkdirs('run')
    return
    wf = PypeProcWatcherWorkflow(
        max_jobs=unzip_blasr_concurrent_jobs,
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
    wf.addTask(taskAA)
    wf.refreshTargets()

if __name__ == '__main__':
    main(*sys.argv)
