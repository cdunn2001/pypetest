from pypeflow.simple_pwatcher_bridge import fn

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
