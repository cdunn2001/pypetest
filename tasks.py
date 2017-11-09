from pypeflow.simple_pwatcher_bridge import (
    PypeLocalFile, makePypeLocalFile, fn,
    PypeTask,
)

def task_generic_bash_script(self):
    """Generic script task.
    The script template should be in
    self.parameters['_bash_'].
    The template will be substituted by
    the content of "self" and of "self.parameters".
    (That is a little messy, but good enough for now.)
    """
    script = self.parameters('_bash_')
    self_dict = dict()
    self_dict.update(self)
    self_dict.update(self.parameters)
    script = script_unsub % self_dict
    script_fn = 'script.sh'
    with open(script_fn, 'w') as ofs:
        ofs.write(script)
    self.generated_script_fn = script_fn


def gen_task(wf, script, inputs, outputs, parameters={}):
    parameters['_bash_'] = script
    make_task = PypeTask(
            inputs={k: makePypeLocalFile(v) for k,v in inputs.iteritems()},
            outputs={k: makePypeLocalFile(v) for k,v in outputs.iteritems()},
            parameters=parameters,
            )
    return make_task(task_generic_bash_script)

def create_task_new():
    i1 = './in/i1'
    o1 = './run/dir1/o1.txt'
    script = """
set -vex
cat %(i1)s > %(o1)s
echo taskA
"""
    return gen_task(
            script=script,
            inputs={
                'i1': i1,
            },
            outputs={
                'o1': o1,
            },
            parameters={},
    )


def taskA(self):
    i1 = fn(self.i1)
    o1 = fn(self.o1)
    script = """
set -vex
cat %(i1)s > %(o1)s
echo taskA
"""%locals()
    script_fn = 'script.sh'
    with open(script_fn, 'w') as ofs:
        ofs.write(script)
    self.generated_script_fn = script_fn

def create_task_old():
    i1 = './in/i1'
    o1 = './run/dir1/o1.txt'
    i1 = makePypeLocalFile(i1)
    o1 = makePypeLocalFile(o1)
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
    return make_task(taskA)
