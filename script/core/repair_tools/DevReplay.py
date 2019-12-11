import os
import subprocess
import datetime
import json
import shutil
import csv

from config import OUTPUT_PATH
from config import WORKING_DIRECTORY
from core.RepairTool import RepairTool
from core.utils import add_repair_tool
from core.runner.RepairTask import RepairTask

class DevReplay(RepairTool):
    """DevReplay"""

    def __init__(self, name="DevReplay"):
        super(DevReplay, self).__init__(name, "DevReplay")
        self.seed = 0
        # self.iteration = iteration

    def repair(self, repair_task):
        """"
        :type repair_task: RepairTask
        """
        bug = repair_task.bug
        bug_path = os.path.join(WORKING_DIRECTORY,
                                "%s_%s_%s_%s" % (self.name, bug.benchmark.name, bug.project, bug.bug_id))
        repair_task.working_directory = bug_path
        self.init_bug(bug, bug_path)
        projects = ["Chart", "Closure", "Lang", "Math", "Mockito", "Time"]
        try:
            failing_tests =  bug.failing_tests()
            sources = bug.source_folders()
            tests = bug.test_folders()
            bin_folders = bug.bin_folders()
            test_bin_folders = bug.test_bin_folders()
            classpath = bug.classpath()
            compliance_level = bug.compliance_level()
            target_path = ""
            with open("./defects4j_data.csv", "r") as defects4j_data:
                reader = csv.DictReader(defects4j_data)
                target_bug = [x for x in reader if x["project"] == bug.project and x["bugId"] == str(bug.bug_id)][0]
                target_path = bug_path + "/" + sources[0] + target_bug["revision_path"]
            with open("rules/" + bug.project +".json", "r") as rule_file:
                rule_file = json.load(rule_file)
            log_path = os.path.join(repair_task.log_dir(), "repair.log")
            if not os.path.exists(os.path.dirname(log_path)):
                os.makedirs(os.path.dirname(log_path))
            log = file(log_path, 'w')
            log.flush()
            print(sources)
            print(bug_path)
            print(classpath)
            print(target_bug)
            print(target_path)
            print(os.path.exists(target_path))

            # run the repair tool
        finally:
            result = {
                "repair_begin": self.repair_begin,
                "repair_end": datetime.datetime.now().__str__(),
                "patches": []
            }

            path_results = os.path.join(bug_path, "output.json")
            if os.path.exists(path_results):
                repair_task.status = "FINISHED"
                shutil.copy(path_results, os.path.join(repair_task.log_dir(), "detailed-result.json"))
                repair_task.results = result

                if len(result['patches']) > 0:
                    repair_task.status = "PATCHED"
            else:
                repair_task.status = "ERROR"

            # normalize the output in result
            with open(os.path.join(repair_task.log_dir(), "result.json"), "w+") as fd2:
                json.dump(result, fd2, indent=2)
            shutil.rmtree(bug_path)
        pass



def init(args):
    return DevReplay()

def _args(parser):
    # additional argument for the repair tool
    # parser.add_argument("--argument", help="description", default=100)
    pass

parser = add_repair_tool("DevReplay", init, 'Repair the bug with DevReplay')
_args(parser)