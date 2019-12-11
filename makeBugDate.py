from subprocess import Popen, PIPE
import csv
import json
from datetime import datetime as dt
from dateutil import parser
import pytz

results = []

# with open("defects4j-bugs.json", "r") as json_file:
#     bugs = json.load(json_file)

#     for bug in bugs:
#         out = Popen(['./benchmarks/defects4j/framework/bin/defects4j', 'info', '-p',str(bug["project"]), '-b', str(bug["bugId"])], stdin=PIPE, stdout=PIPE)
#         stdout, _ = out.communicate()
#         output = stdout.decode('utf-8').splitlines()
#         changed_index = output.index("Revision date (fixed version):")
#         revision_date = output[changed_index + 1]
#         parsed_date = parser.parse(revision_date)
#         parsed_date = parsed_date.astimezone(pytz.timezone('Asia/Tokyo'))
#         parsed_date = parsed_date.replace(tzinfo=None)
#         filepath_index = output.index("List of modified sources:")
#         revision_path = output[filepath_index + 1]
#         revision_path = revision_path.replace(".", "/")[3:] + ".java"
#         is_one_revision = not output[filepath_index + 2].startswith(" - ")


#         results.append({
#             "revisionDate": parsed_date,
#             "bugId": bug["bugId"],
#             "project": bug["project"],
#             "revision_path": revision_path,
#             "is_one_revision": is_one_revision
#         })

# with open("defects4j_data.csv", "w") as target:
#     writer = csv.DictWriter(target, ["project", "bugId", "revisionDate", "revision_path", "is_one_revision"])
#     writer.writeheader()
#     writer.writerows(results)


# with open("defects4j_time.csv", "r") as target:
#     reader = csv.DictReader(target)
#     for bug in reader:
#         parsed_date = parser.parse(bug["revisionDate"])
#         parsed_date = parsed_date.replace(tzinfo=None)
#         # date = dt.strptime(bug["revisionDate"],"%Y-%m-%d %H:%M:%S %z")
#         print(parsed_date)


with open("./defects4j_data.csv", "r") as defects4j_data:
    reader = csv.DictReader(defects4j_data)
    target_bug = [x for x in reader if x["project"] == "Chart" and x["bugId"] == "5"][0]
    print(target_bug)