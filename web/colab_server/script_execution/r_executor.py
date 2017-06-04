from .script_executor import ScriptExecutor


class RExecutor(ScriptExecutor):
    def execute(self, script):
        return self.do_execute(script=script, kernel='ir')

